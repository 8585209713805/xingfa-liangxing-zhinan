#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
合并所有罪名数据源 → assets/crimes_data.js
数据源：
  - crimes_full.FULL            (第1–5章，含 penalty/elements/standard/interp)
  - _dir_ch6a.ENTRIES           (第6章 1–4 节)
  - _dir_ch6b.ENTRIES           (第6章 5–9 节)
  - _dir_ch7..ch10.ENTRIES      (第7–10章)
输出：window.ALL_CRIMES = [...]，供 index.html 离线加载。
"""
import sys, os, json, re, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import crimes_full
FRAGMENTS = ["_dir_ch6a", "_dir_ch6b", "_dir_ch7", "_dir_ch8", "_dir_ch9", "_dir_ch10"]

# 13 个已生成量刑指引富页面的 文件 + 摘要
GUIDE = {
    "寻衅滋事罪": ("crimes/寻衅滋事罪量刑指引（江西）.html",
               "基本犯最高3年；纠集他人/多次/造成严重后果等升档至5年、10年。"),
    "盗窃罪": ("crimes/盗窃罪量刑指引（江西）.html",
               "数额较大/多次/入户/携带凶器/扒窃→3年以下；巨大→3–10年；特别巨大→10年以上。"),
    "诈骗罪": ("crimes/诈骗罪量刑指引（江西）.html",
               "数额较大→3年以下；巨大→3–10年；特别巨大→10年以上或无期。"),
    "故意伤害罪": ("crimes/故意伤害罪量刑指引（江西）.html",
               "轻伤→3年以下；致人重伤→3–10年；致人死亡/特别残忍手段致残→10年以上/无期/死刑。"),
    "交通肇事罪": ("crimes/交通肇事罪量刑指引（江西）.html",
               "基本犯→3年以下；肇事后逃逸/其他恶劣情节→3–7年；因逃逸致人死亡→7年以上。"),
    "抢劫罪": ("crimes/抢劫罪量刑指引（江西）.html",
               "基本犯→3–10年；入户/公交/银行/多次/数额巨大/致人重伤死亡等→10年以上/无期/死刑。"),
    "非法经营罪": ("crimes/非法经营罪量刑指引（江西）.html",
               "情节严重→5年以下；情节特别严重→5–15年。不同非法经营对象（烟草、证券、成品油等）有专门数额标准。"),
    "猥亵儿童罪": ("crimes/猥亵儿童罪量刑指引（江西）.html",
               "基本犯→5年以下；猥亵多人/多次、聚众或在公共场所当众、造成儿童伤害或其他严重后果、手段恶劣等→5–15年。"),
    "侵犯公民个人信息罪": ("crimes/侵犯公民个人信息罪量刑指引（江西）.html",
               "情节严重→3年以下；情节特别严重→3–7年。按信息类型与数量（行踪轨迹/通信内容/财产信息 vs 其他信息）及违法所得区分档次。"),
    "帮助信息网络犯罪活动罪": ("crimes/帮助信息网络犯罪活动罪量刑指引（江西）.html",
               "基本犯→3年以下，并处或单处罚金。明知他人利用信息网络实施犯罪，提供互联网接入、服务器托管、通讯传输、广告推广、支付结算等帮助，情节严重。"),
    "开设赌场罪": ("crimes/开设赌场罪量刑指引（江西）.html",
               "基本犯→5年以下；情节严重→5–10年。含线下赌场与利用互联网、移动通讯终端等开设的网上赌场。"),
    "拒不执行判决、裁定罪": ("crimes/拒不执行判决、裁定罪量刑指引（江西）.html",
               "基本犯→3年以下；情节特别严重→3–7年。对人民法院判决、裁定有能力执行而拒不执行，情节严重；单位犯罪双罚。"),
    "组织卖淫罪": ("crimes/组织卖淫罪量刑指引（江西）.html",
               "基本犯→5–10年；情节严重→10年以上或无期。协助组织卖淫单独成罪（5年以下，情节严重5–10年）。"),
    "骗取出口退税罪": ("crimes/骗取出口退税罪量刑指引（江西）.html",
               "数额较大（10万以上）→5年以下；数额巨大（50万以上）/其他严重情节→5–10年；数额特别巨大（500万以上）/其他特别严重情节→10年以上或无期。均处骗取税款1–5倍罚金或没收财产（法释〔2024〕4号）。"),
    "虚开增值税专用发票、用于骗取出口退税、抵扣税款发票罪": ("crimes/虚开增值税专用发票、用于骗取出口退税、抵扣税款发票罪量刑指引（江西）.html",
               "基本犯（虚开税款10万以上）→3年以下或拘役，并处2–20万罚金；数额较大（50万以上）/其他严重情节→3–10年，并处5–50万罚金；数额巨大（500万以上）/其他特别严重情节→10年–无期，并处5–50万罚金或没收财产（刑法第205条、法释〔2024〕4号）。"),
}

def build_record(d, existing=None):
    name = d["name"]
    f, note = GUIDE.get(name, (None, None))
    guideline = bool(d.get("guideline")) or (name in GUIDE)
    rec = {
        "name": name,
        "chap": d["chap"],
        "sec": d.get("sec") or None,
        "art": d.get("art", ""),
        "guideline": guideline,
        "file": f,
    }
    if note:
        rec["note"] = note
    elif d.get("penalty"):
        rec["note"] = d["penalty"]
    elif d.get("art"):
        rec["note"] = "法条依据：" + d["art"]
    else:
        rec["note"] = "（释义待生成）"
    # 保留手工登记的信息，避免重跑脚本时丢失已生成的量刑指引页
    ex = (existing or {}).get(name)
    if ex:
        if ex.get("file"):
            rec["file"] = ex["file"]
        if ex.get("note"):
            rec["note"] = ex["note"]
        if ex.get("guideline"):
            rec["guideline"] = True
    return rec


def load_existing(path):
    """读取现有 crimes_data.js，保留手工登记的 file / note / guideline，
    避免重跑本脚本时丢失已生成的量刑指引页信息。"""
    d = {}
    if not os.path.exists(path):
        return d
    try:
        txt = open(path, encoding="utf-8").read()
        m = re.search(r'window\.ALL_CRIMES\s*=\s*(.*?);\s*$', txt, re.S)
        if not m:
            return d
        arr = json.loads(m.group(1))
        for r in arr:
            if r.get("file") or r.get("guideline"):
                d[r["name"]] = {"file": r.get("file"), "note": r.get("note"),
                                "guideline": r.get("guideline")}
    except Exception as e:
        print("警告：读取现有 crimes_data.js 失败：", e)
    return d


def update_index_html(today, nfile):
    """同步首页页脚的「最后更新」日期与已生成罪名数（自动注入，免手动维护）。"""
    idx = os.path.abspath(os.path.join(HERE, "..", "index.html"))
    if not os.path.exists(idx):
        print("index.html 未找到，跳过日期注入")
        return
    txt = open(idx, encoding="utf-8").read()
    new = re.sub(r'最后更新：\d{4}-\d{2}-\d{2}', '最后更新：' + today, txt)
    new = re.sub(r'<b>\d+\s*个罪名</b>', '<b>%d 个罪名</b>' % nfile, new)
    if new != txt:
        open(idx, "w", encoding="utf-8").write(new)
        print("已更新 index.html 页脚：最后更新=%s，罪名数=%d" % (today, nfile))
    else:
        print("index.html 页脚无需变更（日期 %s / 罪名数 %d）" % (today, nfile))

# 中文数字（之一/之二…）
_CN_NUM = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10}

def parse_art(art):
    """解析「刑法第N条（之一）（第X款）」为可排序的 (art_no, sub, para) 元组。
    用于在每章/每节内按法条真实顺序排序，而非按罪名汉字。"""
    if not art:
        return (99999, 0, 0)
    m = re.search(r'第(\d+)条', art)
    art_no = int(m.group(1)) if m else 99999
    sub = 0
    ms = re.search(r'条之([一二三四五六七八九十]+)', art)
    if ms:
        sub = _CN_NUM.get(ms.group(1), 0)
    para = 0
    mp = re.search(r'第(\d+)(?:[–、,-]\d+)?款', art)
    if mp:
        para = int(mp.group(1))
    return (art_no, sub, para)

def main():
    out = os.path.join(HERE, "crimes_data.js")
    existing = load_existing(out)
    all_recs = []
    # 第1–5章
    for d in crimes_full.FULL:
        all_recs.append(build_record(d, existing))
    # 第6–10章 片段
    for mod in FRAGMENTS:
        m = __import__(mod)
        for d in m.ENTRIES:
            all_recs.append(build_record(d, existing))

    # 去重（按 name，保留 guideline=True 优先）
    seen = {}
    for r in all_recs:
        k = r["name"]
        if k not in seen or (r["guideline"] and not seen[k]["guideline"]):
            seen[k] = r
    recs = list(seen.values())

    # 排序：章 → 节 → 法条序号（第N条 / 之一 / 第X款）→ 罪名（兜底稳定）
    recs.sort(key=lambda r: (r["chap"], r["sec"] or 0, *parse_art(r.get("art","")), r["name"]))

    with open(out, "w", encoding="utf-8") as f:
        f.write("/* 自动生成：罪名全目录（详见 assets/build_index.py）。双击 index.html 离线可用。 */\n")
        f.write("window.ALL_CRIMES = ")
        f.write(json.dumps(recs, ensure_ascii=False, separators=(",", ":")))
        f.write(";\n")

    ng = sum(1 for r in recs if r["guideline"])
    nfile = sum(1 for r in recs if r["file"])
    print("总罪名:", len(recs), "| guideline=True:", ng, "| 有 file:", nfile)
    # 自动同步首页页脚日期与已生成罪名数
    today = datetime.date.today().strftime('%Y-%m-%d')
    update_index_html(today, nfile)
    # 章节分布
    from collections import Counter
    cc = Counter(r["chap"] for r in recs)
    print("各章:", dict(sorted(cc.items())))

if __name__ == "__main__":
    main()
