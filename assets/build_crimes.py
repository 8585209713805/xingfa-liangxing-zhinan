# -*- coding: utf-8 -*-
"""从通用基座 base.html 生成各罪名量刑表（数据驱动，引擎复用）。
用法：python3 build_crimes.py  -> 在 ../crimes/ 生成 诈骗/故意伤害/交通肇事/抢劫 四个 HTML。
每个罪名只需提供「罪专用内容」，通用情节表与估算器引擎保持不变。
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "base.html")
OUT  = os.path.join(HERE, "..", "crimes")

def region(html, start, end, inner):
    """替换 start 标记之后、end 标记之前的内容（保留两个标记本身）。"""
    i = html.index(start) + len(start)
    j = html.index(end, i)
    return html[:i] + inner + html[j:]

# ---------------- 各罪名内容 ----------------
CRIMES = []

# ===== 诈骗罪 =====
CRIMES.append(dict(
key="fraud_notes_v1",
title='诈骗罪量刑指引（江西·法发〔2021〕21号 / 赣高法〔2022〕115号）',
sub='依据：最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（试行）》（法发〔2021〕21号）"诈骗罪"专章；江西省实施细则（赣高法〔2022〕115号）据此细化；江西数额标准见赣高法〔2011〕140号，均可直接修改。',
overview='''    <div class="overview">
    <div class="card first">
      <h3>第一量刑幅度</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">基本犯：诈骗数额较大（江西 5000元），量刑起点在拘役至1年以下有期徒刑之间确定。</div>
    </div>
    <div class="card second">
      <h3>第二量刑幅度</h3>
      <div class="range">3年 – 10年</div>
      <div class="desc">数额巨大（5万元）或有其他严重情节：量刑起点 3–4年；最高至10年。</div>
    </div>
    <div class="card" style="border-color:var(--amber); background:var(--amber-lighter);">
      <h3>第三量刑幅度</h3>
      <div class="range" style="color:var(--amber);">10年 – 无期</div>
      <div class="desc">数额特别巨大（50万元）或有其他特别严重情节：量刑起点 10–12年；可至无期徒刑。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本表量刑的前提是行为已构成<b>诈骗罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款（条文以官方发布文本为准，可点击编辑、补充批注）。
  </p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百六十六条【诈骗罪】</h3>
    <ul>
      <li>诈骗公私财物，<b>数额较大的</b>，处<b>三年以下有期徒刑、拘役或者管制，并处或者单处罚金</b>。</li>
      <li>数额巨大或者有其他严重情节的，处<b>三年以上十年以下有期徒刑，并处罚金</b>。</li>
      <li>数额特别巨大或者有其他特别严重情节的，处<b>十年以上有期徒刑或者无期徒刑，并处罚金或者没收财产</b>。</li>
      <li>本法另有规定的，依照规定（如合同诈骗、集资诈骗、贷款诈骗、保险诈骗等特别法条）。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2011〕7号 · 关于办理诈骗刑事案件具体应用法律若干问题的解释</h3>
    <ul>
      <li><b>第1条（数额）</b> 诈骗公私财物价值 3000元–1万元＝数额较大；3万–10万元＝数额巨大；50万元以上＝数额特别巨大（各省高院在此幅度内确定）。<b>江西标准：数额较大 5000元、数额巨大 5万元、数额特别巨大 50万元</b>（赣高法〔2011〕140号）。</li>
      <li><b>第2条（特殊入罪）</b> 通过多种渠道发布虚假信息对不特定多数人实施诈骗，或诈骗残疾人/老年人/丧失劳动能力人财物等，数额较大标准按第1条的80%掌握；诈骗近亲属谅解的一般可不按犯罪处理。</li>
      <li><b>第5条（未遂）</b> 诈骗未遂，以数额巨大（5万元以上）财物为目标的，应定罪处罚。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">量刑规范</span>法发〔2021〕21号 · 关于常见犯罪的量刑指导意见（试行）</h3>
    <ul>
      <li>总则：规定自首、立功、坦白、认罪认罚、赔偿谅解等通用量刑情节的调节比例，适用于本罪（见本表估算器"通用情节"）。</li>
      <li>分则「诈骗罪」专章：即本表量刑起点、基准刑增量、从重与缓刑规则的来源（赣高法〔2022〕115号据此细化）。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>出罪抗辩点</b>——拿到案子先过这一关。
  </p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>诈骗罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：公私财产所有权（主要客体）；同时可能侵犯社会管理秩序等复杂客体。</li>
      <li><b>客观方面</b>：以<b>虚构事实 / 隐瞒真相</b>的方法，使被害人<b>陷入错误认识并基于错误认识"自愿"处分</b>财物，行为人取得财物、被害人遭受损失。</li>
      <li><b>主体</b>：一般主体，已满<b>16周岁</b>具有刑事责任能力的自然人。</li>
      <li><b>主观方面</b>：<b>直接故意</b>，并具有<b>非法占有目的</b>。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">出罪</span>罪与非罪的界限 · 出罪抗辩点</h3>
    <ul>
      <li><b>① 民事欺诈 vs 刑事诈骗</b>：无非法占有目的、有真实交易/履约意愿与能力的，属民事纠纷，不构成本罪。</li>
      <li><b>② 数额未达较大</b>：江西 5000元以下一般不构成；但电信诈骗、多种渠道发布虚假信息等特殊情形按80%或相应标准入罪。</li>
      <li><b>③ 近亲属间诈骗且获谅解</b>：一般<b>不按犯罪处理</b>（法释7号第4条）。</li>
      <li><b>④ 情节显著轻微（刑法第13条但书）</b>：数额刚达标、初犯、退赃退赔取得谅解，可作无罪处理或相对不起诉。</li>
      <li><b>⑤ 对象错误 / 未发生处分</b>：被害人未陷入错误认识、未实际处分财物（未遂），未达巨大目标且情节轻的，可不诉/免罚。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    诈骗罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>；核心在于被害人是否"自愿处分"、行为人是否"虚构事实"。
  </p>
  <table class="distTbl" id="distTbl">
    <thead>
      <tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr>
    </thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">盗窃罪</td><td class="cedit" data-key="d1b">诈骗是<b>虚构事实使被害人自愿处分</b>；盗窃是<b>秘密窃取</b>违背被害人意志取得。</td><td class="cedit" data-key="d1c">区分：被害人是否基于错误认识<b>自愿交付</b>。</td></tr>
      <tr><td class="cedit" data-key="d2">敲诈勒索罪</td><td class="cedit" data-key="d2b">诈骗是<b>错误认识下自愿交付</b>；敲诈是<b>以威胁/要挟使人恐惧</b>而交付。</td><td class="cedit" data-key="d2c">区分：交付是否基于<b>恐惧</b>而非错误认识。</td></tr>
      <tr><td class="cedit" data-key="d3">合同诈骗罪</td><td class="cedit" data-key="d3b">普通诈骗是一般欺骗；合同诈骗在<b>合同签订、履行过程中</b>骗取对方财物。</td><td class="cedit" data-key="d3c">特别法优先（第224条），一般不并罚。</td></tr>
      <tr><td class="cedit" data-key="d4">集资诈骗罪</td><td class="cedit" data-key="d4b">以<b>非法占有为目的，使用诈骗方法非法集资</b>（涉众、面向不特定人）。</td><td class="cedit" data-key="d4c">金融诈骗特别法，从一重或特别法条论处。</td></tr>
      <tr><td class="cedit" data-key="d5">贷款诈骗罪</td><td class="cedit" data-key="d5b">以非法占有为目的骗取<b>银行/金融机构</b>贷款；与骗取贷款罪区分在有无非法占有目的。</td><td class="cedit" data-key="d5c">特别法优先（第193条）。</td></tr>
      <tr><td class="cedit" data-key="d6">招摇撞骗罪</td><td class="cedit" data-key="d6b">冒充国家机关工作人员招摇撞骗，主要损害国家机关威信；诈骗以骗取财物为目的。</td><td class="cedit" data-key="d6c">竞合从一重；骗取财物重的可定诈骗。</td></tr>
      <tr><td class="cedit" data-key="d7">保险诈骗罪</td><td class="cedit" data-key="d7b">投保人/被保险人/受益人<b>虚构保险标的或事故</b>骗取保险金。</td><td class="cedit" data-key="d7c">特别法优先（第198条）。</td></tr>
      <tr><td class="cedit" data-key="d8">虚假广告罪</td><td class="cedit" data-key="d8b">广告主/经营者/发布者虚假宣传；与诈骗区分在是否有真实交易基础、是否非法占有全部货款。</td><td class="cedit" data-key="d8c">区分目的与手段；竞合从一重。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点（地方标准以江西省"两院"最新规定为准）。
  </p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；符合刑诉法第288条的<b>当事人和解的公诉案件</b>（侵财/因民间纠纷引起、可能判3年以下，或7年以下过失），可和解并从宽。</li>
      <li><b>立案追诉门槛</b>：依法释〔2011〕7号 + 江西 赣高法〔2011〕140号——<b>数额较大 5000元</b>、<b>数额巨大 5万元</b>、<b>数额特别巨大 50万元</b>；特殊情形（多种渠道发虚假信息、诈骗弱势群体等）按80%或相应标准入罪。</li>
      <li><b>财物价值认定</b>：依价格认定规则；电信网络诈骗按查实数额累计计算。</li>
      <li><b>管辖法院</b>：犯罪地（行为地 / 结果地）基层人民法院一审；法定最高刑为无期徒刑。</li>
      <li><b>追诉时效</b>：数额较大（3年以下）→ <b>5年</b>；数额巨大（3–10年）→ <b>10年</b>；数额特别巨大（10年–无期）→ <b>15年 / 20年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚且可能判3年以下可适用速裁 / 简易程序；退赃退赔、赔偿谅解可达成刑事和解，显著从宽。</li>
      <li><b>认罪认罚从宽</b>：可减基准刑30%以下（总则），直接影响量刑起点与缓刑判断。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（基本犯，最高 3 年）；
    红色块＝<b>第二量刑幅度</b>（数额巨大 / 其他严重情节，3–10 年）；
    黄色块＝<b>第三量刑幅度</b>（数额特别巨大 / 其他特别严重情节，10 年–无期）。
    同一幅度内按情节轻重在起点幅度内确定具体起点。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（3年–10年）</span>
    <span><i class="chip" style="background:var(--amber)"></i>第三量刑幅度（10年–无期）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead>
      <tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形（数额 / 情节）</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr>
    </thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>诈骗数额较大</td><td>诈骗公私财物价值 <b>5000元</b>（江西标准；国家幅度 3000–1万元）</td><td class="start s1">拘役 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>其他较大档情形</td><td>电信网络诈骗 / 多次诈骗 / 造成较重后果等（数额较大档次内从重）</td><td class="start s1">拘役 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>数额巨大</td><td>诈骗价值 <b>5万元</b>（江西标准；国家幅度 3万–10万）或其他严重情节</td><td class="start s2">3年 – 4年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>其他严重情节</td><td>诈骗残疾人/老年人/弱势群体、冒充机关/救灾募捐名义、造成被害人自杀等严重后果</td><td class="start s2">3年 – 4年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
      <tr class="grp-first3"><td><span class="tier t3">第三幅度</span></td><td>数额特别巨大</td><td>诈骗价值 <b>50万元</b>（江西标准；国家幅度 50万元以上）或其他特别严重情节</td><td class="start s3">10年 – 12年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r6"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead>
      <tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr>
    </thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">诈骗数额（较大档）每 +1500元</td><td class="c2">+1个月 / 1500元</td></tr>
      <tr data-tier="1" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>②</td><td class="c1">多次 / 团伙诈骗 每 +1次</td><td class="c2">+1个月 / 次</td></tr>
      <tr data-tier="2" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>③</td><td class="c1">诈骗数额（巨大档）每 +5000元</td><td class="c2">+1个月 / 5000元</td></tr>
      <tr data-tier="3" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>④</td><td class="c1">诈骗数额（特别巨大档）每 +5万元</td><td class="c2">+1个月 / 5万元</td></tr>
    </tbody>
  </table>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节</h3>
    <ul>
      <li><b>增加基准刑 30% 以下：</b>诈骗具有以下情形之一的（已作为犯罪构成事实的除外）：
        <ul>
          <li>（1）通过发送短信、拨打电话或利用互联网、广播电视、报刊杂志等发布虚假信息，对不特定多数人实施诈骗的；</li>
          <li>（2）诈骗救灾、抢险、防汛、优抚、扶贫、移民、救济、医疗款物的；</li>
          <li>（3）以赈灾募捐名义实施诈骗的；</li>
          <li>（4）诈骗残疾人、老年人或者丧失劳动能力人的财物的；</li>
          <li>（5）造成被害人自杀、精神失常或者其他严重后果的。</li>
        </ul>
      </li>
      <li>具体比例见上方估算器「本罪特定从重」（默认 20%，可调；21号上限 30%以下）。</li>
    </ul>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>诈骗罪应当在<b>1000元 以上、诈骗数额 2倍以下</b> 判处罚金，但最低不得少于 1000元（参考法发〔2021〕21号财产犯罪罚金原则）。</li>
      <li>数额特别巨大、情节特别严重的，可并处<b>没收财产</b>；单处罚金适用于犯罪较轻、具备免刑条件且主动缴纳罚金的情形。</li>
      <li class="note-tip">（综合犯罪数额、情节、退赃退赔及被告人缴纳能力确定；江西实践一般并处。）</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①诈骗数额较大，系初犯、偶犯，已退赃退赔并取得谅解，宣告刑≤3年且符合刑法第72条；</li>
        <li>②近亲属之间诈骗、取得谅解；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①通过多种渠道发布虚假信息对不特定多数人实施诈骗（电信诈骗）；</li>
        <li>②诈骗救灾/抢险/优抚/扶贫/医疗款物，或残疾人/老年人/丧失劳动能力人财物；</li>
        <li>③造成被害人自杀、精神失常或者其他严重后果；</li>
        <li>④曾因诈骗受过刑事处罚；</li>
        <li>⑤其他不适用缓刑的情形。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>诈骗数额(较大档) 每+1500元</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>诈骗数额(巨大档) 每+5000元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>诈骗数额(特别巨大档) 每+5万元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>多次/团伙诈骗 每+1次</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>诈骗罪·特定情形(多种渠道虚假信息/救灾/弱势群体/医疗/严重后果)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="1" data-max="12" data-tier="1">拘役–1年（数额较大/多次）</button>
        <button type="button" class="chip-btn" data-min="36" data-max="48" data-tier="2">3年–4年（数额巨大）</button>
        <button type="button" class="chip-btn" data-min="120" data-max="144" data-tier="3">10年–12年（数额特别巨大）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(多种渠道虚假信息/救灾/弱势群体/医疗/严重后果) +20%</label>',
default_tier=1,
))

# ===== 故意伤害罪 =====
CRIMES.append(dict(
key="injury_notes_v1",
title='故意伤害罪量刑指引（江西·法发〔2021〕21号 / 赣高法〔2022〕115号）',
sub='依据：法发〔2021〕21号「故意伤害罪」专章；赣高法〔2022〕115号据此细化；伤情以《人体损伤程度鉴定标准》（两院三部 2013）认定，均可直接修改。',
overview='''    <div class="overview">
    <div class="card first">
      <h3>第一量刑幅度</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">基本犯：致1人轻伤（二级/一级），量刑起点在拘役至1年6个月以下有期徒刑之间确定。</div>
    </div>
    <div class="card second">
      <h3>第二量刑幅度</h3>
      <div class="range">3年 – 10年</div>
      <div class="desc">致1人重伤（二级/一级）：量刑起点 3–4年（手段特别残忍 3–5年）；最高至10年。</div>
    </div>
    <div class="card" style="border-color:var(--amber); background:var(--amber-lighter);">
      <h3>第三量刑幅度</h3>
      <div class="range" style="color:var(--amber);">10年 – 死刑</div>
      <div class="desc">致人死亡或以特别残忍手段致人重伤造成严重残疾：起点 10–12年；可至无期徒刑、死刑。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本表量刑的前提是行为已构成<b>故意伤害罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款（条文以官方发布文本为准，可点击编辑、补充批注）。
  </p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百三十四条【故意伤害罪】</h3>
    <ul>
      <li>故意伤害他人身体的，处<b>三年以下有期徒刑、拘役或者管制</b>。</li>
      <li>致人<b>重伤</b>的，处<b>三年以上十年以下有期徒刑</b>。</li>
      <li>致人<b>死亡</b>或者以<b>特别残忍手段致人重伤造成严重残疾</b>的，处<b>十年以上有期徒刑、无期徒刑或者死刑</b>。</li>
      <li>本法另有规定的，依照规定（如刑讯逼供、非法拘禁、聚众斗殴中致人伤残的，依本条定罪并从重）。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>人体损伤程度鉴定标准（两院三部 2013）</h3>
    <ul>
      <li><b>轻伤</b>：使人肢体或者容貌损害，听觉、视觉或者其他器官功能部分障碍或者其他对于人身健康有中度伤害的损伤（分一级、二级）。轻伤以上即构罪。</li>
      <li><b>重伤</b>：使人肢体残废、毁人容貌、丧失听觉/视觉/其他器官功能或者其他对于人身健康有重大伤害的损伤（分一级、二级）。</li>
      <li>伤情须由法定鉴定机构依标准出具意见，是定罪量刑的基础事实。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">量刑规范</span>法发〔2021〕21号 · 关于常见犯罪的量刑指导意见（试行）</h3>
    <ul>
      <li>总则：规定自首、立功、坦白、认罪认罚、赔偿谅解等通用量刑情节的调节比例，适用于本罪（见本表估算器"通用情节"）。</li>
      <li>分则「故意伤害罪」专章：即本表量刑起点、基准刑增量、从重与缓刑规则的来源（赣高法〔2022〕115号据此细化）。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>出罪抗辩点</b>——拿到案子先过这一关。
  </p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>故意伤害罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：他人的<b>身体健康权</b>。</li>
      <li><b>客观方面</b>：非法损害他人身体健康（作为或不作为），造成<b>轻伤以上</b>后果（有伤无情不构成犯罪，按治安处罚）。</li>
      <li><b>主体</b>：一般主体。已满<b>14周岁</b>对致人重伤/死亡负刑责，已满<b>16周岁</b>对致人轻伤负刑责。</li>
      <li><b>主观方面</b>：<b>伤害故意</b>（认识并希望/放任伤害结果）；有杀人故意的定故意杀人罪。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">出罪</span>罪与非罪的界限 · 出罪抗辩点</h3>
    <ul>
      <li><b>① 正当防卫</b>：为使本人/他人人身权利免受正在进行的不法侵害而采取制止行为，未明显超过必要限度造成重大损害的，<b>不负刑责</b>（第20条）；过当应减轻/免除。</li>
      <li><b>② 伤情未达轻伤</b>：轻微伤按治安处罚，不构成本罪。</li>
      <li><b>③ 随意殴打 vs 伤害</b>：出于流氓动机随意殴打不特定人定寻衅滋事；针对特定矛盾对象、具有伤害故意定故意伤害。</li>
      <li><b>④ 故意杀人未遂 vs 故意伤害</b>：主观是杀人还是伤害存疑时，按存疑有利于被告定故意伤害（致死）。</li>
      <li><b>⑤ 被害人承诺 / 自伤</b>：一般不构成伤害罪（除涉聚众、涉毒等法定情形）。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    故意伤害罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>；核心在于主观（伤害 vs 杀人/过失）与行为场域。
  </p>
  <table class="distTbl" id="distTbl">
    <thead>
      <tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr>
    </thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">故意杀人罪</td><td class="cedit" data-key="d1b">主观是<b>杀人故意</b>还是<b>伤害故意</b>；故意伤害致死与故意杀人既遂区分在主观。</td><td class="cedit" data-key="d1c">证据存疑按故意伤害（致死）定性，有利被告。</td></tr>
      <tr><td class="cedit" data-key="d2">寻衅滋事罪</td><td class="cedit" data-key="d2b">随意殴打<b>不特定/随意对象</b>、流氓动机；故意伤害针对特定矛盾对象。</td><td class="cedit" data-key="d2c">区分动机与对象；竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d3">过失致人死亡/重伤罪</td><td class="cedit" data-key="d3b">主观<b>无伤害故意</b>，因过失致伤/死；故意伤害是故意。</td><td class="cedit" data-key="d3c">区分故意与过失。</td></tr>
      <tr><td class="cedit" data-key="d4">刑讯逼供/暴力取证/虐待被监管人罪</td><td class="cedit" data-key="d4b">司法工作人员在履职中暴力致人伤残。</td><td class="cedit" data-key="d4c">依第234条定罪并<b>从重</b>处罚。</td></tr>
      <tr><td class="cedit" data-key="d5">非法拘禁罪</td><td class="cedit" data-key="d5b">拘禁过程中<b>使用暴力致人伤残</b>。</td><td class="cedit" data-key="d5c">依第234条定罪并从重。</td></tr>
      <tr><td class="cedit" data-key="d6">抢劫罪/强奸罪等</td><td class="cedit" data-key="d6b">实施抢劫/强奸中使用暴力致人重伤。</td><td class="cedit" data-key="d6c">按相应重罪（抢劫/强奸）论处，不另定故意伤害。</td></tr>
      <tr><td class="cedit" data-key="d7">聚众斗殴罪</td><td class="cedit" data-key="d7b">聚众斗殴<b>致人重伤/死亡</b>。</td><td class="cedit" data-key="d7c">转化依第234/232条定罪。</td></tr>
      <tr><td class="cedit" data-key="d8">组织出卖人体器官罪</td><td class="cedit" data-key="d8b">不经同意摘取器官，或强迫/欺骗他人捐献器官。</td><td class="cedit" data-key="d8c">定第234条之一，不按故意伤害。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。
  </p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；但民间纠纷引起、可能判3年以下的，符合刑诉法第288条可<b>当事人和解</b>并从宽（故意伤害和解率高）。</li>
      <li><b>立案追诉门槛</b>：依《人体损伤程度鉴定标准》——<b>轻伤二级以上</b>即构罪；轻微伤按治安处罚。</li>
      <li><b>伤情认定</b>：须由法定鉴定机构出具《法医学人体损伤程度鉴定书》。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审；致人死亡/手段特别残忍可能由中级法院一审。</li>
      <li><b>追诉时效</b>：轻伤（3年以下）→ <b>5年</b>；重伤（3–10年）→ <b>10年</b>；致死/特别残忍（10年以上）→ <b>15年 / 20年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可速裁；赔偿谅解达成和解显著从宽，直接影响缓刑判断。</li>
      <li><b>认罪认罚从宽</b>：可减基准刑30%以下（总则）。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（轻伤，最高 3 年）；
    红色块＝<b>第二量刑幅度</b>（重伤，3–10 年）；
    黄色块＝<b>第三量刑幅度</b>（致死 / 特别残忍致严重残疾，10 年–死刑）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（3年–10年）</span>
    <span><i class="chip" style="background:var(--amber)"></i>第三量刑幅度（10年–死刑）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead>
      <tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形（伤情 / 手段）</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr>
    </thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>致1人轻伤（二级）</td><td>故意伤害致1人轻伤二级</td><td class="start s1">拘役 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>致1人轻伤（一级）</td><td>故意伤害致1人轻伤一级</td><td class="start s1">拘役 – 1年6个月</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>致1人重伤（二级）</td><td>故意伤害致1人重伤二级</td><td class="start s2">3年 – 4年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>致1人重伤（一级）/手段特别残忍</td><td>重伤一级，或以特别残忍手段致人重伤</td><td class="start s2">3年 – 5年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
      <tr class="grp-first3"><td><span class="tier t3">第三幅度</span></td><td>致人死亡 / 特别残忍致严重残疾</td><td>致人死亡，或以特别残忍手段致人重伤造成严重残疾</td><td class="start s3">10年 – 12年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r6"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead>
      <tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr>
    </thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">每增加1名轻伤被害人</td><td class="c2">+3个月 / 人</td></tr>
      <tr data-tier="1" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>②</td><td class="c1">持械 / 多次殴打 每 +1次</td><td class="c2">+2个月 / 次</td></tr>
      <tr data-tier="2" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>③</td><td class="c1">每增加1名重伤被害人</td><td class="c2">+12个月 / 人</td></tr>
      <tr data-tier="3" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>④</td><td class="c1">残疾等级每加重1级（1–10级）</td><td class="c2">+3个月 / 级</td></tr>
    </tbody>
  </table>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节</h3>
    <ul>
      <li><b>增加基准刑 20%–30% 以下：</b>故意伤害具有以下情形之一的（已作为犯罪构成事实的除外）：
        <ul>
          <li>（1）持管制刀具、凶器等伤害他人的；</li>
          <li>（2）因邻里、婚姻、债务等民间矛盾激化伤害，且手段残忍的；</li>
          <li>（3）伤害老年人、未成年人、残疾人、孕妇、哺乳期妇女等弱势群体的；</li>
          <li>（4）雇佣、纠集他人伤害或出于报复伤害的；</li>
          <li>（5）造成被害人自杀、精神失常或者其他严重后果的。</li>
        </ul>
      </li>
      <li>具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</li>
    </ul>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>故意伤害罪以<b>自由刑为主</b>，一般不并处罚金；造成被害人经济损失的，通过<b>附带民事诉讼</b>判赔。</li>
      <li>情节特别严重、并处罚金/没收财产的情形，由法院依案情决定；江西实务对单纯伤害一般不单处罚金。</li>
      <li class="note-tip">（赔偿谅解虽不直接体现为罚金，但显著影响缓刑与宣告刑，应重点争取。）</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①致1人轻伤，初犯、偶犯，已赔偿谅解，宣告刑≤3年且符合刑法第72条；</li>
        <li>②民间纠纷引发、达成刑事和解；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①致人重伤 / 死亡的；</li>
        <li>②持凶器伤害、手段残忍；</li>
        <li>③雇凶、报复伤害；</li>
        <li>④累犯；</li>
        <li>⑤未赔偿谅解、社会影响恶劣的。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>每增加1名轻伤被害人</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>持械/多次殴打 每+1次</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="2" value="2"><span>月</span></div>
          <div class="prow"><span>每增加1名重伤被害人</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="12" value="12"><span>月</span></div>
          <div class="prow"><span>残疾等级每加重1级</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="3" value="3"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>故意伤害罪·特定从重(持凶器/弱势群体/报复/严重后果)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="1" data-max="18" data-tier="1">拘役–1年6个月（轻伤）</button>
        <button type="button" class="chip-btn" data-min="36" data-max="60" data-tier="2">3年–4年（重伤）</button>
        <button type="button" class="chip-btn" data-min="120" data-max="144" data-tier="3">10年–12年（致死/特残）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(持凶器/弱势群体/报复/严重后果) +20%</label>',
default_tier=1,
))

# ===== 交通肇事罪 =====
CRIMES.append(dict(
key="traffic_notes_v1",
title='交通肇事罪量刑指引（江西·法发〔2021〕21号 / 赣高法〔2022〕115号）',
sub='依据：法发〔2021〕21号「交通肇事罪」专章；赣高法〔2022〕115号据此细化；责任划分与伤亡/财产损失依法释〔2000〕33号，均可直接修改。',
overview='''    <div class="overview">
    <div class="card first">
      <h3>第一量刑幅度</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">基本犯：负全部/主要责+死1人或重伤3人等；或同等责死3人；或无力赔偿30万元以上：起点 拘役至2年。</div>
    </div>
    <div class="card second">
      <h3>第二量刑幅度</h3>
      <div class="range">3年 – 7年</div>
      <div class="desc">肇事后逃逸 或 其他特别恶劣情节：起点 3–5年；最高至7年。</div>
    </div>
    <div class="card" style="border-color:var(--amber); background:var(--amber-lighter);">
      <h3>第三量刑幅度</h3>
      <div class="range" style="color:var(--amber);">7年 – 15年</div>
      <div class="desc">因逃逸致人死亡：起点 7–10年（法定最高15年）。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本表量刑的前提是行为已构成<b>交通肇事罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款（条文以官方发布文本为准，可点击编辑、补充批注）。
  </p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第一百三十三条【交通肇事罪】</h3>
    <ul>
      <li>违反交通运输管理法规，因而发生重大事故，致人重伤、死亡或者使公私财产遭受重大损失的，处<b>三年以下有期徒刑或者拘役</b>。</li>
      <li>交通肇事后<b>逃逸</b>或者有其他特别恶劣情节的，处<b>三年以上七年以下有期徒刑</b>。</li>
      <li>因<b>逃逸致人死亡</b>的，处<b>七年以上有期徒刑</b>。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2000〕33号 · 关于审理交通肇事刑事案件具体应用法律若干问题的解释</h3>
    <ul>
      <li><b>第2条（基本犯）</b> 负事故全部/主要责任，死亡1人或重伤3人，或重伤1人+酒驾/毒驾/无照/明知无牌证报废/严重超载/逃逸前科等6情形；或负同等责任死亡3人；或无能力赔偿数额30万元以上（全/主责）。</li>
      <li><b>第3条</b> "交通肇事后逃逸"＝为逃避法律追究而逃跑。</li>
      <li><b>第4条（特别恶劣情节）</b> 死亡2人以上或重伤5人以上（全/主责）；死亡6人以上（同等责）；无力赔偿60万元以上。</li>
      <li><b>第5条</b> "因逃逸致人死亡"＝行为人在交通肇事后为逃避法律追究而逃跑，致使被害人因得不到救助而死亡。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">量刑规范</span>法发〔2021〕21号 · 关于常见犯罪的量刑指导意见（试行）</h3>
    <ul>
      <li>分则「交通肇事罪」专章：即本表量刑起点、基准刑增量、从重与缓刑规则的来源（赣高法〔2022〕115号据此细化）。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>出罪抗辩点</b>——拿到案子先过这一关。
  </p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>交通肇事罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>交通运输安全</b>（公共安全）。</li>
      <li><b>客观方面</b>：违反交规，发生<b>重大事故</b>，致人重伤/死亡/重大财产损失；逃逸/特别恶劣/逃逸致死为法定升档。</li>
      <li><b>主体</b>：一般主体（机动车/非机动车驾驶人均可；单位主管人员、车主、承包人指使肇事的，以共犯论）。</li>
      <li><b>主观方面</b>：对事故结果出于<b>过失</b>（对违规可能故意，对结果过失）。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">出罪</span>罪与非罪的界限 · 出罪抗辩点</h3>
    <ul>
      <li><b>① 行政违法 vs 犯罪</b>：未达死/重伤/30万财产损失标准的不构罪（按治安/民事处理）。</li>
      <li><b>② 意外事件 / 不可抗力</b>：无违规或结果非违规所致，不构罪。</li>
      <li><b>③ 责任比例抗辩</b>：交警责任认定是量刑基础；若证据能推翻"全/主责"认定，可能不构成基本犯。</li>
      <li><b>④ 与危险驾驶罪区分</b>：醉驾/追逐竞驶是危险犯，未造成事故定危险驾驶；造成重伤以上且负主责+醉驾等，依重罪（交通肇事）或数罪并罚。</li>
      <li><b>⑤ 与以危险方法危害公共安全罪区分</b>：故意冲撞人群等定以危险方法危害公共安全，而非过失的交通肇事。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    交通肇事罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>；核心在于主观（过失 vs 故意）与行为场域。
  </p>
  <table class="distTbl" id="distTbl">
    <thead>
      <tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr>
    </thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">危险驾驶罪</td><td class="cedit" data-key="d1b">醉驾/追逐竞驶是<b>抽象危险犯</b>，未造成事故即构罪；交通肇事需造成重伤以上事故。</td><td class="cedit" data-key="d1c">造成事故致人重伤且负主责+醉驾等，依重罪（交通肇事）或数罪并罚。</td></tr>
      <tr><td class="cedit" data-key="d2">以危险方法危害公共安全罪</td><td class="cedit" data-key="d2b">主观是<b>故意</b>驾车冲撞不特定人；交通肇事是<b>过失</b>。</td><td class="cedit" data-key="d2c">区分故意与过失；故意冲撞定以危险方法危害公共安全。</td></tr>
      <tr><td class="cedit" data-key="d3">故意杀人/故意伤害罪</td><td class="cedit" data-key="d3b">肇事后为灭口<b>故意碾压/拖行</b>致死伤。</td><td class="cedit" data-key="d3c">转化定故意杀人/伤害，不按交通肇事。</td></tr>
      <tr><td class="cedit" data-key="d4">重大责任事故罪</td><td class="cedit" data-key="d4b">生产、作业中违反安全管理发生事故；交通肇事在公共交通领域。</td><td class="cedit" data-key="d4c">区分是否"公共交通领域"。</td></tr>
      <tr><td class="cedit" data-key="d5">过失致人死亡/重伤罪</td><td class="cedit" data-key="d5b">非交通运输中过失致人死伤；交通肇事是交通过失特别规定。</td><td class="cedit" data-key="d5c">特别规定优先。</td></tr>
      <tr><td class="cedit" data-key="d6">破坏交通设施罪</td><td class="cedit" data-key="d6b">破坏道路/交通设施致事故；交通肇事是使用交通工具肇事。</td><td class="cedit" data-key="d6c">区分行为方式。</td></tr>
      <tr><td class="cedit" data-key="d7">故意毁坏财物罪</td><td class="cedit" data-key="d7b">肇事主要为毁财、无人员伤亡，一般不定交通肇事。</td><td class="cedit" data-key="d7c">区分损害对象与后果。</td></tr>
      <tr><td class="cedit" data-key="d8">交通肇事逃逸 vs 逃逸致死</td><td class="cedit" data-key="d8b">"肇事后逃逸"是升档情节（3–7年）；"因逃逸致人死亡"是更高档（7年以上）。</td><td class="cedit" data-key="d8c">关键看被害人的生命危险是否由逃逸（不救助）导致。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。
  </p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>（过失犯罪），一般不适用刑事和解，但赔偿谅解可从宽。</li>
      <li><b>立案追诉门槛</b>：依法释〔2000〕33号第2条（死/重伤/财产损失标准）；重伤依《人体损伤程度鉴定标准》。</li>
      <li><b>责任认定</b>：以交警《道路交通事故认定书》的责任划分（全/主/同/次责）为量刑基础。</li>
      <li><b>管辖法院</b>：事故发生地基层人民法院一审。</li>
      <li><b>追诉时效</b>：基本犯（3年以下）→ <b>5年</b>；肇事后逃逸（3–7年）→ <b>10年</b>；逃逸致死（7年以上）→ <b>15年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可速裁；积极抢救、赔偿获谅解显著从宽（影响缓刑）。</li>
      <li><b>认罪认罚从宽</b>：可减基准刑30%以下（总则）。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（基本犯，最高 3 年）；
    红色块＝<b>第二量刑幅度</b>（逃逸 / 特别恶劣情节，3–7 年）；
    黄色块＝<b>第三量刑幅度</b>（逃逸致人死亡，7 年–15 年）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（3年–7年）</span>
    <span><i class="chip" style="background:var(--amber)"></i>第三量刑幅度（7年–15年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead>
      <tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形（责任 / 后果）</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr>
    </thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>基本犯</td><td>负全/主责 死1人或重伤3人；或同等责死3人；或无力赔偿30万元以上</td><td class="start s1">拘役 – 2年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>基本犯（重伤1人+6情形）</td><td>负全/主责 重伤1人 + 酒驾/毒驾/无照/超载/失灵车/逃逸前科等</td><td class="start s1">拘役 – 2年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>肇事后逃逸 / 特别恶劣情节</td><td>交通肇事后逃逸；或死2人/重伤5人负全主责等特别恶劣情节</td><td class="start s2">3年 – 5年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>特别恶劣情节（更重）</td><td>死2人以上或重伤5人以上负全主责；死6人以上同等责；无力赔偿60万元以上</td><td class="start s2">3年 – 7年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
      <tr class="grp-first3"><td><span class="tier t3">第三幅度</span></td><td>因逃逸致人死亡</td><td>肇事后逃逸致被害人因得不到救助而死亡</td><td class="start s3">7年 – 10年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r6"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead>
      <tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr>
    </thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">每增加1名死亡被害人</td><td class="c2">+6个月 / 人</td></tr>
      <tr data-tier="1" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>②</td><td class="c1">酒后/无照/超载等恶劣情节 每 +1项</td><td class="c2">+2个月 / 项</td></tr>
      <tr data-tier="2" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>③</td><td class="c1">每增加1名重伤被害人</td><td class="c2">+3个月 / 人</td></tr>
      <tr data-tier="3" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>④</td><td class="c1">无能力赔偿数额 每 +10万元</td><td class="c2">+1个月 / 10万元</td></tr>
    </tbody>
  </table>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（比例从重，区别于法定升档）</h3>
    <ul>
      <li><b>增加基准刑 20% 以下：</b>交通肇事具有下列情形之一的（已作为犯罪构成/升档事实的除外）：
        <ul>
          <li>（1）酒后、吸食毒品后驾驶机动车的；</li>
          <li>（2）无驾驶资格驾驶机动车的；</li>
          <li>（3）明知是安全装置不全或者安全机件失灵的机动车而驾驶的；</li>
          <li>（4）明知是无牌证或者已报废的机动车而驾驶的；</li>
          <li>（5）严重超载驾驶的；</li>
          <li>（6）为逃避法律追究逃离事故现场（尚未构成"交通肇事后逃逸"升档情节的）。</li>
        </ul>
      </li>
      <li>具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。<b>注意：</b>法定"交通肇事后逃逸""逃逸致死"为<b>法定刑升档</b>，已体现在第四项起点，不在此比例从重内重复评价。</li>
    </ul>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>交通肇事罪以<b>自由刑为主</b>，造成财产损失的通过<b>附带民事诉讼</b>赔偿；一般可并处罚金，单处情形少。</li>
      <li class="note-tip">（赔偿谅解虽不体现为罚金，但显著从宽并影响缓刑，应重点争取。）</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①基本犯、初犯、积极抢救/报警、已赔偿谅解，宣告刑≤3年且符合刑法第72条；</li>
        <li>②肇事後主动报案、救助被害人；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①交通肇事后逃逸（法定升档）；</li>
        <li>②因逃逸致人死亡；</li>
        <li>③醉驾/毒驾且后果严重；</li>
        <li>④无赔偿能力且未取得谅解、社会影响恶劣；</li>
        <li>⑤其他不适用缓刑的情形。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>每增加1名死亡被害人</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="6" value="6"><span>月</span></div>
          <div class="prow"><span>酒后/无照/超载等恶劣情节 每+1项</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="2" value="2"><span>月</span></div>
          <div class="prow"><span>每增加1名重伤被害人</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>无能力赔偿数额 每+10万元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>交通肇事罪·特定从重(酒驾/无照/失灵车/超载/逃离现场)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="1" data-max="24" data-tier="1">拘役–2年（基本犯）</button>
        <button type="button" class="chip-btn" data-min="36" data-max="60" data-tier="2">3年–5年（逃逸/特别恶劣）</button>
        <button type="button" class="chip-btn" data-min="84" data-max="120" data-tier="3">7年–10年（逃逸致死）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(酒驾/无照/失灵车/超载/逃离现场) +20%</label>',
default_tier=1,
))

# ===== 抢劫罪 =====
CRIMES.append(dict(
key="robbery_notes_v1",
title='抢劫罪量刑指引（江西·法发〔2021〕21号 / 赣高法〔2022〕115号）',
sub='依据：法发〔2021〕21号「抢劫罪」专章；赣高法〔2022〕115号据此细化；入户/公交等8种加重情形依刑法第263条，均可直接修改。',
overview='''    <div class="overview">
    <div class="card first">
      <h3>基本犯幅度</h3>
      <div class="range">3年 – 10年</div>
      <div class="desc">基本犯：以暴力/胁迫当场取财（无8种加重情形），量刑起点 3–6年，并处罚金。</div>
    </div>
    <div class="card second">
      <h3>加重幅度</h3>
      <div class="range">10年 – 无期/死刑</div>
      <div class="desc">入户/公交/银行/多次/数额巨大/致人重伤死亡等8种加重情形：起点 10–13年（可至无期/死刑）。</div>
    </div>
    <div class="card" style="border-color:var(--amber); background:var(--amber-lighter);">
      <h3>致死/特别严重</h3>
      <div class="range" style="color:var(--amber);">10年 – 死刑</div>
      <div class="desc">抢劫致人重伤、死亡：起点 10年以上；情节极重可判处死刑。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本表量刑的前提是行为已构成<b>抢劫罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款（条文以官方发布文本为准，可点击编辑、补充批注）。
  </p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百六十三条【抢劫罪】</h3>
    <ul>
      <li>以暴力、胁迫或者其他方法<b>抢劫公私财物</b>的，处<b>三年以上十年以下有期徒刑，并处罚金</b>。</li>
      <li>有下列情形之一的，处<b>十年以上有期徒刑、无期徒刑或者死刑，并处罚金或者没收财产</b>：（一）入户抢劫；（二）在公共交通工具上抢劫；（三）抢劫银行或者其他金融机构；（四）<b>多次抢劫或者抢劫数额巨大</b>；（五）<b>抢劫致人重伤、死亡</b>；（六）冒充军警人员抢劫；（七）持枪抢劫；（八）抢劫军用物资或者抢险、救灾、救济物资。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">刑法</span>转化抢劫 / 携带凶器抢夺</h3>
    <ul>
      <li><b>第269条（转化抢劫）</b>：犯盗窃、诈骗、抢夺罪，为窝藏赃物、抗拒抓捕或者毁灭罪证而<b>当场</b>使用暴力或者以暴力相威胁的，依抢劫罪论处。</li>
      <li><b>第267条第2款</b>：携带凶器抢夺的，以抢劫罪论处。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">量刑规范</span>法发〔2021〕21号 · 关于常见犯罪的量刑指导意见（试行）</h3>
    <ul>
      <li>分则「抢劫罪」专章：即本表量刑起点、基准刑增量、从重与缓刑规则的来源（赣高法〔2022〕115号据此细化）。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>出罪抗辩点</b>——拿到案子先过这一关。
  </p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>抢劫罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>复杂客体</b>（财产权 + 人身权利）。</li>
      <li><b>客观方面</b>：以<b>暴力、胁迫或者其他方法</b>（如灌醉、催眠）当场强行取财，或迫使被害人当场交出财物。</li>
      <li><b>主体</b>：一般主体，已满<b>14周岁</b>具有刑事责任能力（抢劫系8种严重犯罪之一，14周岁起担责）。</li>
      <li><b>主观方面</b>：<b>直接故意</b>，具有<b>非法占有目的</b>（且使用暴力/胁迫）。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">出罪</span>罪与非罪的界限 · 出罪抗辩点</h3>
    <ul>
      <li><b>① 与抢夺区分</b>：抢劫对人使用暴力/胁迫；抢夺对物暴力（公然夺取）。携带凶器抢夺→抢劫。</li>
      <li><b>② 与敲诈勒索区分</b>：抢劫是"当场"暴力取财；敲诈是威胁日后加害索取。</li>
      <li><b>③ 转化抢劫（第269条）</b>：盗窃/诈骗/抢夺后"当场"使用暴力→抢劫；非当场则数罪并罚。</li>
      <li><b>④ 与绑架区分</b>：抢劫当场取财；绑架以人质要挟第三人交付。</li>
      <li><b>⑤ 情节显著轻微</b>：强拿硬要少量财物、未使用实质暴力且无轻伤，可能定寻衅滋事而非抢劫。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    抢劫罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>；核心在于是否"对人使用暴力/胁迫当场取财"。
  </p>
  <table class="distTbl" id="distTbl">
    <thead>
      <tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr>
    </thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">抢夺罪</td><td class="cedit" data-key="d1b">抢劫<b>对人使用暴力/胁迫</b>；抢夺对物暴力（公然夺取）。</td><td class="cedit" data-key="d1c">携带凶器抢夺→抢劫；竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d2">敲诈勒索罪</td><td class="cedit" data-key="d2b">抢劫是<b>当场</b>暴力取财；敲诈是威胁<b>日后</b>加害索取。</td><td class="cedit" data-key="d2c">区分是否"当场"暴力。</td></tr>
      <tr><td class="cedit" data-key="d3">绑架罪</td><td class="cedit" data-key="d3b">抢劫<b>当场</b>取财；绑架以人质要挟<b>第三人</b>交付。</td><td class="cedit" data-key="d3c">区分取财对象与场合。</td></tr>
      <tr><td class="cedit" data-key="d4">故意杀人罪</td><td class="cedit" data-key="d4b">抢劫中故意杀人取财定抢劫（致死档）；图财先杀后取定故意杀人+盗窃/抢劫。</td><td class="cedit" data-key="d4c">依主观与行为顺序定性。</td></tr>
      <tr><td class="cedit" data-key="d5">寻衅滋事罪（强拿硬要）</td><td class="cedit" data-key="d5b">随意、流氓动机、情节较轻；抢劫暴力明显、以非法占有为目的。</td><td class="cedit" data-key="d5c">区分动机与暴力程度。</td></tr>
      <tr><td class="cedit" data-key="d6">转化抢劫（第269条）</td><td class="cedit" data-key="d6b">盗窃/诈骗/抢夺后<b>当场</b>暴力→抢劫。</td><td class="cedit" data-key="d6c">依第269条定性为抢劫。</td></tr>
      <tr><td class="cedit" data-key="d7">招摇撞骗/诈骗罪</td><td class="cedit" data-key="d7b">非暴力取财；与抢劫区分在是否使用暴力/胁迫。</td><td class="cedit" data-key="d7c">区分取财手段。</td></tr>
      <tr><td class="cedit" data-key="d8">聚众哄抢罪</td><td class="cedit" data-key="d8b">聚众公然哄抢财物；与抢劫区分暴力程度与主体。</td><td class="cedit" data-key="d8c">区分暴力程度与主体。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">
    本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。
  </p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>（严重暴力犯罪）；一般不适用刑事和解，但赔偿谅解可从宽（暴力犯罪从宽应从严掌握）。</li>
      <li><b>立案追诉门槛</b>：实施抢劫行为即构罪（<b>无数额要求</b>）；转化抢劫以前行为（盗窃/诈骗/抢夺）为前置。</li>
      <li><b>伤情认定</b>：致人重伤/死亡依《人体损伤程度鉴定标准》。</li>
      <li><b>管辖法院</b>：犯罪地基层/中级法院（可能无期、死刑由中院一审）。</li>
      <li><b>追诉时效</b>：基本犯（10年以下）→ <b>15年</b>；加重情形（无期/死刑）→ <b>20年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽（暴力犯罪从严掌握）；赔偿谅解影响量刑与死缓/无期适用。</li>
      <li><b>认罪认罚从宽</b>：可减基准刑30%以下（总则），但暴力犯罪应从严掌握幅度。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>基本犯幅度</b>（无8种加重，3–10 年）；
    红色块＝<b>加重幅度</b>（入户/公交/银行/多次/数额巨大等，10 年–无期）；
    黄色块＝<b>致死 / 特别严重</b>（抢劫致人重伤、死亡，10 年–死刑）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>基本犯幅度（3年–10年）</span>
    <span><i class="chip" style="background:var(--red)"></i>加重幅度（10年–无期）</span>
    <span><i class="chip" style="background:var(--amber)"></i>致死/特别严重（10年–死刑）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead>
      <tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形（基本犯 / 8种加重）</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr>
    </thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">基本犯</span></td><td>基本犯</td><td>以暴力/胁迫/其他方法当场取财，无8种加重情形</td><td class="start s1">3年 – 6年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">加重幅度</span></td><td>入户 / 公交 / 银行金融机构抢劫</td><td>第263条第（一）（二）（三）项</td><td class="start s2">10年 – 13年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">加重幅度</span></td><td>多次抢劫 / 抢劫数额巨大</td><td>第263条第（四）项</td><td class="start s2">10年 – 13年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
      <tr class="grp-first3"><td><span class="tier t3">致死/特重</span></td><td>抢劫致人重伤、死亡</td><td>第263条第（五）项；或冒充军警/持枪/军用救灾物资</td><td class="start s3">10年以上</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r6"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead>
      <tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr>
    </thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">抢劫数额 每 +2000元</td><td class="c2">+1个月 / 2000元</td></tr>
      <tr data-tier="1" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>②</td><td class="c1">多次抢劫 每 +1次</td><td class="c2">+12个月 / 次</td></tr>
      <tr data-tier="2" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>③</td><td class="c1">每增加1人轻伤</td><td class="c2">+3个月 / 人</td></tr>
      <tr data-tier="3" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>④</td><td class="c1">每增加1人重伤</td><td class="c2">+12个月 / 人</td></tr>
    </tbody>
  </table>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 法定升档 vs 比例从重</h3>
    <ul>
      <li><b>法定刑升档（非比例从重，已体现在第四项起点）</b>：入户、公交上、银行金融机构、多次、数额巨大、致人重伤死亡、冒充军警、持枪、军用/抢险救灾救济物资——直接升格至10年以上/无期/死刑。</li>
      <li><b>比例从重（增加基准刑 20% 以下，在相应幅度内从重）</b>：具有下列情形之一的：
        <ul>
          <li>（1）抢劫弱势群体（老弱病残孕、未成年人）；</li>
          <li>（2）在公共场所当众抢劫；</li>
          <li>（3）持械（非枪）抢劫；</li>
          <li>（4）造成被害人轻伤以下后果 / 财产损失较重；</li>
          <li>（5）流窜作案 / 合伙抢劫。</li>
        </ul>
      </li>
      <li>具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</li>
    </ul>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>抢劫罪<b>必并处罚金</b>（基本犯）；加重情形并处罚金或者<b>没收财产</b>。</li>
      <li>数额巨大、致人伤亡的，江西实践一般并处罚金，情节特别严重的可并处没收财产。</li>
      <li class="note-tip">（综合抢劫数额、情节、缴纳能力确定。）</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①基本犯、情节较轻、初犯、已退赃赔偿谅解，宣告刑≤3年（基本犯起点3年起，缓刑空间小但存在）；</li>
        <li>②其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①8种加重情形（入户/公交/致人重伤死亡等）；</li>
        <li>②持枪 / 冒充军警；</li>
        <li>③多次抢劫 / 抢劫数额巨大；</li>
        <li>④累犯；</li>
        <li>⑤造成严重后果的。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>抢劫数额 每+2000元</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>多次抢劫 每+1次</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="12" value="12"><span>月</span></div>
          <div class="prow"><span>每增加1人轻伤</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>每增加1人重伤</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="12" value="12"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>抢劫罪·特定从重(弱势群体/公共场所/持械/流窜)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="36" data-max="72" data-tier="2">3年–6年（基本犯）</button>
        <button type="button" class="chip-btn" data-min="120" data-max="156" data-tier="3">10年–13年（入户/公交等加重）</button>
        <button type="button" class="chip-btn" data-min="120" data-max="180" data-tier="3">10年以上（致人重伤死亡，可至无期/死刑）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(弱势群体/公共场所/持械/流窜) +20%</label>',
default_tier=2,
))

# ---------------- 生成 ----------------
base = open(BASE, encoding="utf-8").read()

# 精确锚点
MARK = dict(
  overview=('  <!-- 速览 -->', '  <!-- 法条依据 -->'),
  law=('  <!-- 法条依据 -->', '  <!-- 一、构成要件与罪与非罪 -->'),
  const=('  <!-- 一、构成要件与罪与非罪 -->', '  <!-- 二、此罪与彼罪 -->'),
  dist=('  <!-- 二、此罪与彼罪 -->', '  <!-- 三、立案追诉标准 / 管辖 / 时效 -->'),
  info=('  <!-- 三、立案追诉标准 / 管辖 / 时效 -->', '  <!-- 量刑起点一览 -->'),
  start=('  <!-- 量刑起点一览 -->', '  <!-- 基准刑增量 -->'),
  cmp=('  <!-- 基准刑增量 -->', '  <!-- 从重情节 -->'),
  heavy=('  <!-- 从重情节 -->', '  <!-- 常见量刑情节 -->'),
  fine=('  <!-- 罚金 -->', '  <!-- 缓刑 -->'),
  pro=('  <!-- 缓刑 -->', '  <!-- 估算器 -->'),
  chips=('      <span class="chips" id="startChips">', '      </span>\n      <span class="note-tip">或手动输入'),
)

TITLE_OLD = '<title>盗窃罪量刑指引（江西·法发〔2021〕21号 / 赣高法〔2022〕115号）</title>'
H1_OLD = '    <h1>盗窃罪 · 量刑指引表（可编辑）</h1>'
SUB_OLD = '    <div class="sub">依据：最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（试行）》（法发〔2021〕21号）盗窃罪专章；江西省实施细则（赣高法〔2022〕115号）据此细化。部分条款以国家基准为准，江西细则可能更细，表中数值均可直接修改。</div>'
KEY_OLD = 'const KEY = "sentencing_notes_v1";'
PROWS_OLD = '''          <div class="prow"><span>盗窃数额(较大档) 每+1000元</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>盗窃数额(巨大档) 每+3000元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>盗窃数额(特别巨大档) 每+2000元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>多次盗窃 每+1次</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>'''
SPEC_PROW_OLD = '          <div class="prow"><span>盗窃罪·特定情形(救灾/弱势群体/医院/生产急需/严重后果)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>'
SPEC_LABEL_OLD = '        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(救灾/弱势群体/医院/生产急需/严重后果) +20%</label>'
RADIO_OLD = '''      <label><input type="radio" name="tier" value="1" checked> 基本幅度（法定上限 3年）</label>
      <label><input type="radio" name="tier" value="2"> 升档幅度（法定上限 10年）</label>
      <label><input type="radio" name="tier" value="3"> 特别加重（法定上限 15年）</label>'''

def set_default_tier(html, t):
    if t == 1:
        repl = RADIO_OLD
    elif t == 2:
        repl = '''      <label><input type="radio" name="tier" value="1"> 基本幅度（法定上限 3年）</label>
      <label><input type="radio" name="tier" value="2" checked> 升档幅度（法定上限 10年）</label>
      <label><input type="radio" name="tier" value="3"> 特别加重（法定上限 15年）</label>'''
    else:
        repl = '''      <label><input type="radio" name="tier" value="1"> 基本幅度（法定上限 3年）</label>
      <label><input type="radio" name="tier" value="2"> 升档幅度（法定上限 10年）</label>
      <label><input type="radio" name="tier" value="3" checked> 特别加重（法定上限 15年）</label>'''
    return html.replace(RADIO_OLD, repl)

for c in CRIMES:
    h = base
    h1name = c['title'].split('量刑指引')[0]
    h = h.replace(TITLE_OLD, '<title>%s</title>' % c['title'])
    h = h.replace(H1_OLD, '    <h1>%s · 量刑指引表（可编辑）</h1>' % h1name)
    h = h.replace(SUB_OLD, '    <div class="sub">%s</div>' % c['sub'])
    h = h.replace(KEY_OLD, 'const KEY = "%s";' % c['key'])
    h = h.replace(PROWS_OLD, c['prows'])
    h = h.replace(SPEC_PROW_OLD, c['spec_prow'])
    h = h.replace(SPEC_LABEL_OLD, c['spec_label'])
    h = set_default_tier(h, c['default_tier'])
    for k, v in MARK.items():
        h = region(h, v[0], v[1], c[k])
    # 文件命名
    name = h1name  # 诈骗/故意伤害/交通肇事/抢劫（已含"罪"）
    fname = os.path.join(OUT, '%s量刑指引（江西）.html' % name)
    open(fname, 'w', encoding='utf-8').write(h)
    print('written:', fname, '(%d bytes)' % len(h))
print('DONE')
