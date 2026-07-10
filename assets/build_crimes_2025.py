# -*- coding: utf-8 -*-
"""2025批次：赣高法〔2025〕20号《量刑指导意见（二）》实施细则 七种犯罪。
从通用基座 base.html 生成 非法经营罪/猥亵儿童罪/侵犯公民个人信息罪/
帮助信息网络犯罪活动罪/开设赌场罪/拒不执行判决、裁定罪/组织卖淫罪 七张表。
引擎已支持每罪封顶覆盖（window.SENTENCE_CAPS）。
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "base.html")
OUT  = os.path.join(HERE, "..", "crimes")

def region(html, start, end, inner):
    i = html.index(start) + len(start)
    j = html.index(end, i)
    return html[:i] + inner + html[j:]

def inject_caps(html, caps):
    """将 caps 覆盖注入 <script> 内部，作为可执行 JS（window.SENTENCE_CAPS = {...}）。"""
    if not caps:
        return html
    marker = '<script>\n'
    i = html.index(marker) + len(marker)
    stmt = 'window.SENTENCE_CAPS = %s;\n' % caps
    return html[:i] + stmt + html[i:]

# ---------------- 七种犯罪内容 ----------------
CRIMES = []

# ===== 非法经营罪（刑法225条 / 第三章第八节 扰乱市场秩序罪）=====
CRIMES.append(dict(
key="illegal_business_notes_v1",
title='非法经营罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。本罪以"情节严重/情节特别严重"两档为量刑幅度；不同非法经营对象有专门数额标准。本表估算器以最常见的"非法经营烟草专卖品"为主要驱动，并在"五、基准刑增量"下列全部对象标准。',
caps='{1:60,2:180}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>情节严重（第一幅度）</h3>
      <div class="range">拘役 – 5年</div>
      <div class="desc">基本档：非法经营烟草专卖品/证券期货保险/外汇/POS套现/出版物/电信/黑广播/赌博机/食品/非法放贷/其他，达"情节严重"标准，量刑起点 三个月拘役至一年。</div>
    </div>
    <div class="card second">
      <h3>情节特别严重（第二幅度）</h3>
      <div class="range">5年 – 15年</div>
      <div class="desc">达"情节特别严重"标准，量刑起点 5年至6年；最高至15年，并处违法所得1–5倍罚金或没收财产。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>非法经营罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款（条文以官方发布文本为准，可点击编辑、补充批注）。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百二十五条【非法经营罪】</h3>
    <ul>
      <li>违反国家规定，有下列非法经营行为之一，扰乱市场秩序，<b>情节严重的，处五年以下有期徒刑或者拘役，并处或者单处违法所得一倍以上五倍以下罚金</b>：……（一）未经许可经营专营、专卖物品或其他限制买卖物品；（二）买卖进出口许可证、原产地证明等经营许可证或批准文件；（三）未经批准经营证券、期货、保险业务或非法从事资金支付结算；（四）其他严重扰乱市场秩序的非法经营行为。</li>
      <li><b>情节特别严重的，处五年以上有期徒刑，并处违法所得一倍以上五倍以下罚金或者没收财产。</b></li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">量刑规范</span>赣高法〔2025〕20号 ·《关于常见犯罪的量刑指导意见（二）（试行）》实施细则</h3>
    <ul>
      <li>本细则"一、七种常见犯罪的量刑"第（一）项专章规定本罪，细分<b>烟草专卖品、证券期货保险、资金支付结算/买卖外汇、POS套现、非法出版物、国际港澳台电信、网络删帖/发帖、黑广播伪基站、赌博机、危害食品安全、非法放贷、其他非法经营活动</b>等对象的标准与增量。</li>
      <li>同一案件中数额/违法所得分别构成情节轻重档的，按处罚较重的数额定罪；相关数额均明确的，以确定基准刑较重的标准计算，不得同时用于增加刑罚量。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>出罪/界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>非法经营罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>市场准入秩序</b>（国家对专营专卖、金融业务等的管制）。</li>
      <li><b>客观方面</b>：违反国家规定，实施刑法第225条列明的非法经营行为，<b>达到"情节严重"</b>。</li>
      <li><b>主体</b>：一般主体（自然人与单位均可构成本罪）。</li>
      <li><b>主观方面</b>：<b>故意</b>，且一般以营利为目的。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">出罪</span>罪与非罪的界限 · 界分点</h3>
    <ul>
      <li><b>① 是否"违反国家规定"</b>：仅违反部门规章/地方法规的不构成本罪，须是违反全国人大及其常委会/国务院的规定。</li>
      <li><b>② 数额/情节是否达标</b>：未达"情节严重"标准的一般按行政违法处理（如无证经营烟草未达5万元数额等）。</li>
      <li><b>③ 与买卖国家机关证件/印章罪、伪造/变造/买卖国家机关公文证件印章罪区分</b>：买卖的是经营许可证/批准文件定非法经营；买卖的是证件/印章本身可能定他罪。</li>
      <li><b>④ 与非法吸收公众存款罪、集资诈骗罪区分</b>：非法放贷中兼具吸存/集资性质的，注意特别法优先与竞合。</li>
      <li><b>⑤ 与走私罪、生产销售伪劣产品罪区分</b>：对象与行为性质不同，注意想象竞合从一重。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">非法经营罪为"口袋罪"，常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">生产、销售伪劣产品罪</td><td class="cedit" data-key="d1b">非法经营侧重<b>无资质/违禁经营</b>；生产销售伪劣产品侧重<b>产品本身不合格</b>。</td><td class="cedit" data-key="d1c">竞合从一重；伪劣烟草常定非法经营（专卖属性）。</td></tr>
      <tr><td class="cedit" data-key="d2">非法吸收公众存款罪</td><td class="cedit" data-key="d2b">非法放贷若具"吸存"性质，可能同时触犯；非法经营（非法放贷）侧重<b>高利放贷经营</b>。</td><td class="cedit" data-key="d2c">区分行为性质；竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d3">买卖国家机关公文、证件、印章罪</td><td class="cedit" data-key="d3b">买卖的是<b>经营许可证/批准文件</b>定非法经营；买卖证件印章本身定他罪。</td><td class="cedit" data-key="d3c">区分对象。</td></tr>
      <tr><td class="cedit" data-key="d4">走私罪</td><td class="cedit" data-key="d4b">走私是<b>逃避海关监管</b>进出口；非法经营是<b>境内无资质经营</b>。</td><td class="cedit" data-key="d4c">区分行为场域；同时走私定走私。</td></tr>
      <tr><td class="cedit" data-key="d5">擅自设立金融机构罪</td><td class="cedit" data-key="d5b">未经批准<b>设立</b>金融机构；非法经营（证券期货保险）是未经批准<b>经营</b>该业务。</td><td class="cedit" data-key="d5c">区分"设机构"与"营业务"。</td></tr>
      <tr><td class="cedit" data-key="d6">帮助信息网络犯罪活动罪</td><td class="cedit" data-key="d6b">为网络犯罪<b>提供支付结算/技术支持</b>可能竞合非法经营（资金支付结算）。</td><td class="cedit" data-key="d6c">想象竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d7">串通投标罪</td><td class="cedit" data-key="d7b">围标串标是<b>招投标领域</b>特别规定；非法经营者可能兼具。</td><td class="cedit" data-key="d7c">特别法优先。</td></tr>
      <tr><td class="cedit" data-key="d8">虚假广告罪</td><td class="cedit" data-key="d8b">网络有偿发帖/删帖若虚假宣传性质不同；纯经营性定非法经营。</td><td class="cedit" data-key="d8c">区分目的与手段。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪（双罚制）。</li>
      <li><b>立案追诉门槛</b>：依各对象专门标准——如烟草（数额5万/违法所得2万/卷烟20万支）、证券期货保险（数额100万/违法所得10万）、买卖外汇（数额500万/违法所得10万）、POS套现（数额100万）、出版物（个人8万/单位25万）、电信（去话/来话100万）、网络删帖（个人5万/单位15万）、黑广播（设备3套/数额5万）、赌博机（个人5万）、食品（数额10万/违法所得5万）、非法放贷（个人200万/单位1000万）等。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审；情节特别严重可能由中级法院一审。</li>
      <li><b>追诉时效</b>：情节严重（5年以下）→ <b>5年或10年</b>；情节特别严重（5–15年）→ <b>15年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽；退缴违法所得、配合调查可从宽（部分对象可减基准刑40%以下，甚至不起诉/免罚）。</li>
      <li><b>认罪认罚从宽</b>：可减基准刑30%以下（总则），叠加本罪专门从宽规则。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（情节严重，最高 5 年）；红色块＝<b>第二量刑幅度</b>（情节特别严重，5 年–15 年）。
    本罪对象众多，下表以"非法经营烟草专卖品"为代表列基本档/升档起点，全部对象的详细标准与增量见"五"。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–5年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（5年–15年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形（情节严重 / 特别严重）</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>非法经营（情节严重）</td><td>各对象达"情节严重"标准（如烟草：数额5万/违法所得2万/卷烟20万支；POS套现：数额100万）</td><td class="start s1">拘役 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>非法经营（情节特别严重）</td><td>各对象达"情节特别严重"标准（如烟草：数额25万/违法所得10万/卷烟100万支；POS套现：数额500万）</td><td class="start s2">5年 – 6年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <p class="note-tip" style="margin:2px 0 8px;">估算器以"<b>非法经营烟草专卖品</b>"为主要驱动（下表①–④）。其余对象的专门增量如下，供办案直接引用（完整文本见赣高法〔2025〕20号原文）：</p>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项（烟草为代表）</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">非法经营数额（情节档）每 +4000元</td><td class="c2">+1个月 / 4000元</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">违法所得数额（情节档）每 +1600元</td><td class="c2">+1个月 / 1600元</td></tr>
      <tr data-tier="2" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">非法经营数额（特别严重档 25万–250万）每 +4.5万元</td><td class="c2">+1个月 / 4.5万元</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">非法经营数额（特别严重档 &gt;250万）每 +40万元</td><td class="c2">+1个月 / 40万元</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px">
    <h3>其他对象"情节严重/特别严重"增量速查（节选）</h3>
    <ul>
      <li><b>证券、期货、保险业务</b>：情节档 数额+8万/月、违法所得+8000元/月；特别严重档 数额(500万–5000万)+85万/月、(&gt;5亿)+750万/月。</li>
      <li><b>资金支付结算/买卖外汇</b>：情节档 数额+40万/月、违法所得+8000元/月；特别严重档 数额(2500万–2.5亿)+420万/月、(&gt;2.5亿)+3750万/月。</li>
      <li><b>POS信用卡套现</b>：情节档 数额+8万/月；特别严重档 数额(500万–5000万)+85万/月。</li>
      <li><b>非法出版物</b>：个人 数额(8万–25万)+3500元/月、(&gt;250万)+40万/月；单位标准更高（详见原文）。</li>
      <li><b>国际港澳台电信</b>：去话/来话 情节档+8万/月；特别严重档(500万–5000万)+85万/月。</li>
      <li><b>网络有偿删帖/发帖</b>：个人 数额(5万–25万)+4000元/月；特别严重档(25万–250万)+4.5万/月。</li>
      <li><b>黑广播/伪基站</b>：设备 情节档+1套(每套+4月)、特别严重档(15–150套)+3套/月。</li>
      <li><b>赌博机</b>：个人 数额(5万–25万)+4000元/月；特别严重档(25万–250万)+4.5万/月。</li>
      <li><b>危害食品安全</b>：数额(10万–50万)+8000元/月；特别严重档(50万–500万)+8.5万/月。</li>
      <li><b>非法放贷</b>：个人 数额(200万–1000万)+15万/月、(&gt;1亿)+1500万/月；违法所得、对象人数同步增量。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节</h3>
    <ul>
      <li><b>增加基准刑 20% 以下</b>（已作为犯罪构成事实的除外；同时具有两种以上情形的，累计不得超过基准刑的 100%）：
        <ul>
          <li>（1）曾因非法经营行为受过刑事追究，或二年内因非法经营受过行政处罚；</li>
          <li>（2）拒不交代赃款去向或拒不配合追缴，致使赃款无法追缴；</li>
          <li>（3）造成恶劣社会影响或其他严重后果；</li>
          <li>（4）烟草类：曾因非法经营烟草三年内受二次以上处罚、经营假冒伪劣/假冒注册商标烟草；</li>
          <li>（5）外汇类：曾因买卖外汇受刑事追究/二年内受行政处罚、拒不交代资金去向、造成其他严重后果；</li>
          <li>（6）食品类：持续时间6个月以上、私设屠宰厂宰售来源不明生猪；</li>
          <li>（7）非法放贷类：二年内受行政处罚2次以上、以超72%年利率放贷10次以上、黑恶势力、纠集他人暴力讨债等。</li>
        </ul>
      </li>
      <li>从宽：积极退赃退赔可减基准刑30%以下；未参与分赃/获利少可减20%以下（部分对象如实供述+退缴可减40%以下，情节轻微可不诉/免罚）。</li>
      <li>具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</li>
    </ul>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>判处5年以下（情节档）：<b>并处或者单处违法所得一倍以上五倍以下罚金</b>；违法所得难以确定的，罚金最低<b>不少于一千元</b>。</li>
      <li>判处5年以上（特别严重档）：并处违法所得一倍以上五倍以下罚金<b>或者没收财产</b>。</li>
      <li>单位犯罪：对单位判处罚金，数额一般<b>不得低于</b>对直接责任人员判处的罚金数额。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①犯罪数额不大、系初犯/从犯，已退缴违法所得，宣告刑≤3年且符合刑法第72条；</li>
        <li>②认罪认罚、积极配合调查、退缴全部违法所得；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①曾因非法经营受刑事处罚或二年内受行政处罚；</li>
        <li>②拒不交代赃款去向或拒不配合追缴，致使赃款无法追缴；</li>
        <li>③造成恶劣社会影响或其他严重后果；</li>
        <li>④食品类非法经营（严格适用缓刑、可宣告禁止令）；</li>
        <li>⑤黑恶势力非法放贷等情节恶劣。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>非法经营数额(情节档·烟草) 每+4000元</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="0.25"><span>月</span></div>
          <div class="prow"><span>违法所得数额(情节档·烟草) 每+1600元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="0.625"><span>月</span></div>
          <div class="prow"><span>非法经营数额(特别严重档25–250万) 每+4.5万元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="0.222"><span>月</span></div>
          <div class="prow"><span>非法经营数额(特别严重档&gt;250万) 每+40万元</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="0.025"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>非法经营罪·特定从重(屡犯/拒退赃/严重后果/食品类持久)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="3" data-max="12" data-tier="1">拘役–1年（情节严重）</button>
        <button type="button" class="chip-btn" data-min="60" data-max="72" data-tier="2">5年–6年（情节特别严重）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(屡犯/拒退赃/严重后果/食品类持久) +20%</label>',
default_tier=1,
))

# ===== 猥亵儿童罪（刑法237条 / 第四章 侵犯公民人身权利、民主权利罪）=====
CRIMES.append(dict(
key="child_molest_notes_v1",
title='猥亵儿童罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第237条；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。一般情形 1–3年；加重情形 5–7年。',
caps='{1:36,2:84}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>一般情形（第一幅度）</h3>
      <div class="range">1年 – 3年</div>
      <div class="desc">犯罪情节一般：在 1年至3年有期徒刑幅度内确定量刑起点；按人数/次数/伤害后果累加。</div>
    </div>
    <div class="card second">
      <h3>加重情形（第二幅度）</h3>
      <div class="range">5年 – 7年</div>
      <div class="desc">猥亵儿童3人/3次、聚众/当众、造成儿童伤害等严重后果、手段恶劣等：5年至7年；最高至15年。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>猥亵儿童罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百三十七条【猥亵儿童罪】</h3>
    <ul>
      <li>以暴力、胁迫或者其他方法<b>猥亵儿童</b>的，处<b>五年以下有期徒刑</b>。</li>
      <li>有下列情形之一的，处<b>五年以上有期徒刑</b>：（一）猥亵儿童多人或者多次的；（二）聚众猥亵儿童，或者在公共场所当众猥亵儿童，情节恶劣的；（三）造成儿童伤害或者其他严重后果的；（四）猥亵手段恶劣或者有其他恶劣情节的。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2023〕3号 · 关于办理强奸、猥亵未成年人刑事案件适用法律若干问题的解释</h3>
    <ul>
      <li>明确"猥亵手段恶劣或者有其他恶劣情节"的具体情形；对负有特殊职责人员、利用职业便利等作案依法从严。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>猥亵儿童罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>儿童身心健康与性自主权</b>（对象为不满14周岁的儿童）。</li>
      <li><b>客观方面</b>：以暴力、胁迫或其他方法对儿童实施<b>猥亵行为</b>（不要求暴力，抠摸、搂抱等均可）。</li>
      <li><b>主体</b>：一般主体，已满<b>16周岁</b>具有刑事责任能力的自然人。</li>
      <li><b>主观方面</b>：<b>直接故意</b>，明知是儿童而实施猥亵。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 与强奸罪的界限</b>：有性器官插入等性交行为的定强奸（幼女）；猥亵为性交以外的下流行为。</li>
      <li><b>② 与猥亵儿童（治安违法）的界限</b>：情节显著轻微、未达刑事追诉标准的按治安处罚。</li>
      <li><b>③ 年龄认定</b>：对象是否"不满14周岁"是构成要件，须有证据证明。</li>
      <li><b>④ 负有特殊职责人员</b>：对未成年人负有监护、收养、看护、教育、医疗等特殊职责的人员实施猥亵，依法从重。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">猥亵儿童罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">强奸罪（奸淫幼女）</td><td class="cedit" data-key="d1b">猥亵是<b>性交以外的下流行为</b>；与幼女性交定强奸。</td><td class="cedit" data-key="d1c">区分行为性质；兼具的从一重。</td></tr>
      <tr><td class="cedit" data-key="d2">强制猥亵、侮辱罪</td><td class="cedit" data-key="d2b">对象为<b>儿童</b>定猥亵儿童罪；对象为已满14周岁他人定强制猥亵。</td><td class="cedit" data-key="d2c">区分对象年龄。</td></tr>
      <tr><td class="cedit" data-key="d3">寻衅滋事罪</td><td class="cedit" data-key="d3b">随意猥亵不特定人、流氓动机可能竞合寻衅滋事；针对儿童定本罪。</td><td class="cedit" data-key="d3c">区分动机与对象。</td></tr>
      <tr><td class="cedit" data-key="d4">引诱、容留、介绍卖淫罪</td><td class="cedit" data-key="d4b">组织/强迫儿童卖淫另定组织卖淫等；单纯对儿童猥亵定本罪。</td><td class="cedit" data-key="d4c">区分行为目的。</td></tr>
      <tr><td class="cedit" data-key="d5">故意伤害罪</td><td class="cedit" data-key="d5b">猥亵中造成儿童轻伤以上，按本罪加重情节（造成伤害后果）评价。</td><td class="cedit" data-key="d5c">不另定故意伤害，吸收评价。</td></tr>
      <tr><td class="cedit" data-key="d6">传播淫秽物品牟利罪</td><td class="cedit" data-key="d6b">制作儿童淫秽影像另定他罪；对儿童的猥亵行为定本罪。</td><td class="cedit" data-key="d6c">区分行为。</td></tr>
      <tr><td class="cedit" data-key="d7">拐卖儿童罪</td><td class="cedit" data-key="d7b">以出卖为目的拐带有别于猥亵；猥亵后出卖的竞合。</td><td class="cedit" data-key="d7c">区分目的。</td></tr>
      <tr><td class="cedit" data-key="d8">治安管理处罚中的猥亵</td><td class="cedit" data-key="d8b">对象非儿童、情节显著轻微按治安违法。</td><td class="cedit" data-key="d8c">区分对象与情节。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；侵害未成年人，一般不适用刑事和解，从严把握从宽。</li>
      <li><b>立案追诉门槛</b>：实施猥亵儿童行为即应追诉（无单独数额标准）；造成轻伤以上依伤情鉴定。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审；可能判无期/死刑由中院一审。</li>
      <li><b>追诉时效</b>：一般情形（5年以下）→ <b>5年/10年</b>；加重情形（5年以上）→ <b>15年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽但应从严把握；成年被告人一般不适用缓刑。</li>
      <li><b>从业禁止</b>：利用职业便利实施的，应当依法适用从业禁止。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（一般情形，最高 3 年）；红色块＝<b>第二量刑幅度</b>（加重情形，5 年–15 年）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（1年–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（5年–15年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>犯罪情节一般</td><td>猥亵儿童，无其他加重情节</td><td class="start s1">1年 – 3年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>猥亵儿童3人/3次</td><td>猥亵儿童三人或者三次</td><td class="start s2">5年 – 7年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>聚众/当众/造成严重后果/手段恶劣</td><td>聚众猥亵、公共场所当众情节恶劣、造成儿童伤害等严重后果、手段恶劣</td><td class="start s2">6年 – 7年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">猥亵儿童每增加 1人 或 1次</td><td class="c2">+12个月 / 人·次</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">每增加 1名轻微伤</td><td class="c2">+6个月 / 人</td></tr>
      <tr data-tier="2" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">每增加 1名轻伤</td><td class="c2">+12个月 / 人</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">每增加 1名重伤</td><td class="c2">+24个月 / 人</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px"><h3>加重情形其他增量（节选）</h3>
    <ul>
      <li>致使儿童自残/自杀、感染艾滋病/梅毒/淋病等严重性病的，每增加1人 +24–36个月。</li>
      <li>每增加《刑法》第237条第3款第一至四项情形之一 +24–36个月。</li>
      <li>多人多次的，以确定基准刑较重的标准计算，不重复累加。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（增加基准刑 30% 以下，两种以上累计不超过 100%）</h3>
    <ul>
      <li>（1）负有特殊职责人员、与儿童有共同家庭生活关系人员、国家工作人员或冒充国家工作人员猥亵；</li>
      <li>（2）采取暴力、胁迫、麻醉、非法拘禁等手段；</li>
      <li>（3）侵入住宅或学生集体宿舍；</li>
      <li>（4）有摧残、凌辱行为；</li>
      <li>（5）对猥亵过程或隐私部位制作视频/照片等影像资料；</li>
      <li>（6）同时符合两种以上"手段恶劣/其他恶劣情节"；</li>
      <li>（7）对不满十周岁儿童、留守儿童、严重残疾或精神发育迟滞儿童实施；</li>
      <li>（8）利用其他未成年人诱骗、介绍、胁迫；</li>
      <li>（9）二人以上轮流实施；</li>
      <li>（10）造成被害人亲属自杀、死亡或精神失常等严重后果；</li>
      <li>（11）曾因性侵犯罪被判处刑罚；其他可从重。</li>
    </ul>
    <p class="note-tip">具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。成年被告人一般不适用缓刑；认罪认罚/赔偿谅解从宽应从严把握。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>猥亵儿童罪以<b>自由刑为主</b>，可并处罚金；造成经济损失的通过附带民事诉讼赔偿。</li>
      <li class="note-tip">（赔偿谅解虽不体现为罚金，但影响量刑与缓刑，应重点争取；成年被告人缓刑从严。）</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 极少数可适用缓刑</h3>
      <ul>
        <li>①犯罪情节极轻、系初犯、真诚悔罪，宣告刑≤3年且符合刑法第72条；</li>
        <li>②其他可以适用缓刑的情形（从严审查）。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①<b>猥亵儿童的成年被告人，一般不适用缓刑</b>；</li>
        <li>②具有聚众/当众/造成伤害后果/手段恶劣等加重情节；</li>
        <li>③曾因性侵犯罪受刑罚；</li>
        <li>④利用特殊职责/职业便利实施；</li>
        <li>⑤造成被害人严重后果或恶劣社会影响。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>猥亵儿童 每+1人/1次</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="12" value="12"><span>月</span></div>
          <div class="prow"><span>每增加1名轻微伤</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="6" value="6"><span>月</span></div>
          <div class="prow"><span>每增加1名轻伤</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="12" value="12"><span>月</span></div>
          <div class="prow"><span>每增加1名重伤</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="24" value="24"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>猥亵儿童罪·特定从重(特殊职责/暴力/侵入住宅/制作影像/不满十周岁/轮流)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="12" data-max="36" data-tier="1">1年–3年（一般情形）</button>
        <button type="button" class="chip-btn" data-min="60" data-max="84" data-tier="2">5年–7年（加重情形）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(特殊职责/暴力/侵入住宅/制作影像/不满十周岁/轮流) +20%</label>',
default_tier=1,
))

# ===== 侵犯公民个人信息罪（刑法253条之一 / 第四章）=====
CRIMES.append(dict(
key="citizen_info_notes_v1",
title='侵犯公民个人信息罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第253条之一；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。基本档 拘役–1年；加重档 3–4年。',
caps='{1:36,2:84}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>基本犯（第一幅度）</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">达入罪标准（如行踪/通信/征信/财产信息50条、其他信息5000条、违法所得5000元等）：拘役至1年（部分情形至9个月/6个月）。</div>
    </div>
    <div class="card second">
      <h3>加重情形（第二幅度）</h3>
      <div class="range">3年 – 7年</div>
      <div class="desc">造成被害人死亡/重伤/精神失常/被绑架等严重后果，或数量达基本标准10倍以上：3年至4年。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>侵犯公民个人信息罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百五十三条之一【侵犯公民个人信息罪】</h3>
    <ul>
      <li>违反国家有关规定，向他人<b>出售或者提供公民个人信息，情节严重</b>的，处<b>三年以下有期徒刑或者拘役，并处或者单处罚金</b>。</li>
      <li><b>情节特别严重</b>的，处<b>三年以上七年以下有期徒刑，并处罚金</b>。</li>
      <li>在履行职责或提供服务过程中获得的公民个人信息，<b>出售或者提供给他人的，从重处罚</b>。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2017〕10号 · 关于办理侵犯公民个人信息刑事案件适用法律若干问题的解释</h3>
    <ul>
      <li>明确"公民个人信息"范围、入罪数量标准（行踪轨迹/通信内容/征信/财产信息50条；住宿/通信记录/健康生理/交易信息等500条；其余5000条）及"情节特别严重"为10倍以上。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>侵犯公民个人信息罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>公民个人信息权</b>（个人信息自决与安全管理秩序）。</li>
      <li><b>客观方面</b>：违反国家规定，<b>出售、提供或非法获取</b>公民个人信息，达到"情节严重"。</li>
      <li><b>主体</b>：一般主体（自然人与单位）；特殊主体（履职/服务中获取后出售提供）从重。</li>
      <li><b>主观方面</b>：<b>故意</b>。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 是否"公民个人信息"</b>：须可识别特定自然人（含行踪轨迹、通信内容、征信、财产、住宿、健康、交易等）。</li>
      <li><b>② 是否"违反国家有关规定"</b>：经被收集者同意的合法提供一般出罪。</li>
      <li><b>③ 与非法获取计算机信息系统数据罪区分</b>：侵入系统窃取信息的竞合从一重。</li>
      <li><b>④ 与诈骗罪/敲诈勒索罪区分</b>：购买信息后用于诈骗等，数罪并罚或从一重。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">侵犯公民个人信息罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">非法获取计算机信息系统数据罪</td><td class="cedit" data-key="d1b">侵入系统窃取信息；本罪侧重<b>出售/提供/非法获取</b>公民个人信息。</td><td class="cedit" data-key="d1c">竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d2">诈骗罪</td><td class="cedit" data-key="d2b">购信息后用于诈骗；本罪是信息犯罪。</td><td class="cedit" data-key="d2c">数罪并罚或从一重。</td></tr>
      <tr><td class="cedit" data-key="d3">侵犯商业秘密罪</td><td class="cedit" data-key="d3b">对象为<b>商业秘密</b>（经营信息）而非公民个人信息。</td><td class="cedit" data-key="d3c">区分信息性质。</td></tr>
      <tr><td class="cedit" data-key="d4">寻衅滋事罪（网络）</td><td class="cedit" data-key="d4b">网上散布他人信息起哄；本罪是非法出售/提供。</td><td class="cedit" data-key="d4c">区分行为目的。</td></tr>
      <tr><td class="cedit" data-key="d5">敲诈勒索罪</td><td class="cedit" data-key="d5b">获取信息后敲诈；本罪是信息犯罪。</td><td class="cedit" data-key="d5c">数罪并罚或从一重。</td></tr>
      <tr><td class="cedit" data-key="d6">帮信罪</td><td class="cedit" data-key="d6b">提供信息用于网络犯罪可能竞合帮信。</td><td class="cedit" data-key="d6c">竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d7">滥用职权/玩忽职守罪</td><td class="cedit" data-key="d7b">公职人员在履职中泄露信息可能竞合。</td><td class="cedit" data-key="d7c">依主体与行为定性。</td></tr>
      <tr><td class="cedit" data-key="d8">绑架罪</td><td class="cedit" data-key="d8b">非法提供行踪信息致被绑架；本罪是信息犯罪。</td><td class="cedit" data-key="d8c">数罪并罚或从一重。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪。</li>
      <li><b>立案追诉门槛</b>：依法释〔2017〕10号数量标准——行踪轨迹/通信内容/征信/财产信息<b>50条</b>；住宿/通信记录/健康生理/交易信息等<b>500条</b>；其余信息<b>5000条</b>；违法所得<b>5000元</b>；履职/服务中获取后出售提供按标准一半；为合法经营购买收受获利5万元等。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审。</li>
      <li><b>追诉时效</b>：基本犯（3年以下）→ <b>5年</b>；加重（3–7年）→ <b>10年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽；退赃退赔影响量刑与缓刑。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（情节严重，最高 3 年）；红色块＝<b>第二量刑幅度</b>（情节特别严重，3 年–7 年）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（3年–7年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>情节严重（一般）</td><td>达入罪数量/数额标准（如行踪等信息50条、其他5000条、违法所得5000元）</td><td class="start s1">拘役 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>履职中出售/提供（减半标准）</td><td>将在履职/服务中获取得出售提供，达标准一半</td><td class="start s1">拘役 – 9个月</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>情节特别严重</td><td>造成被害人死亡/重伤/精神失常/被绑架等严重后果，或数量达基本标准10倍以上</td><td class="start s2">3年 – 4年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">行踪/通信/征信/财产信息 每 +50条</td><td class="c2">+3个月 / 50条</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">其他敏感信息(住宿/交易等) 每 +500条</td><td class="c2">+3个月 / 500条</td></tr>
      <tr data-tier="2" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">违法所得 每 +5000元</td><td class="c2">+1个月 / 5000元</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">造成被害人重伤/精神失常 每 +1人</td><td class="c2">+6个月 / 人</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px"><h3>加重情形其他增量（节选）</h3>
    <ul>
      <li>行踪/通信/征信/财产信息 每增加100条 +1–3个月；其他敏感信息 每增加1000条 +1–3个月；其余信息 每增加1万条 +1–3个月。</li>
      <li>条数与违法所得数额不得同时用以增加刑罚量，以确定基准刑较重的标准计算。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（上限 30% 以下，两种以上累计不超过 100%）</h3>
    <ul>
      <li>（1）违反国家规定，将在履行职责或提供服务过程中获得的公民个人信息出售或提供给他人的，增加基准刑 <b>10%–30%</b>；</li>
      <li>（2）非法获取、出售或提供未成年人或老年人个人信息，损害其合法权益的，增加基准刑 <b>20%以下</b>；</li>
      <li>（3）设立专门用于实施非法获取、出售或提供公民个人信息违法犯罪活动的网站、通讯群组的，增加基准刑 <b>20%以下</b>；</li>
      <li>（4）其他可以从重处罚的情形，增加基准刑 <b>20%以下</b>。</li>
    </ul>
    <p class="note-tip">具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>一般在<b>违法所得一倍以上五倍以下</b>决定罚金。</li>
      <li>无违法所得或无法查实：单处罚金一般 <b>2000元–3万元</b>；判3年以下拘役一般并处 <b>2000元–5万元</b>；判3年以上罚金一般<b>不低于1万元</b>。</li>
      <li>单位犯罪：无违法所得/无法查实，情节严重一般 <b>5万–100万元</b>；情节特别严重罚金一般<b>不低于20万元</b>。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①犯罪数量刚达标、系初犯、已退赃退赔，宣告刑≤3年且符合刑法第72条；</li>
        <li>②为合法经营而购买收受且获利较小；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①造成被害人死亡、重伤、精神失常或被绑架等严重后果；</li>
        <li>②曾因本罪受刑事处罚或二年内受行政处罚；</li>
        <li>③出售/提供行踪轨迹信息多次被他人用于犯罪；</li>
        <li>④非法获取/出售通信内容、征信、财产信息500条以上；</li>
        <li>⑤利用职业便利获取或将在履职/服务中获取的信息出售提供；</li>
        <li>⑥其他不适用缓刑的情形。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>行踪/通信/征信/财产信息 每+50条</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>其他敏感信息(住宿/交易等) 每+500条</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>违法所得 每+5000元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>造成重伤/精神失常 每+1人</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="6" value="6"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>侵犯公民个人信息罪·特定从重(履职中出售/未成年老年/专设网站群组)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="6" data-max="12" data-tier="1">拘役–1年（情节严重）</button>
        <button type="button" class="chip-btn" data-min="36" data-max="48" data-tier="2">3年–4年（情节特别严重）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(履职中出售/未成年老年/专设网站群组) +20%</label>',
default_tier=1,
))

# ===== 帮助信息网络犯罪活动罪（刑法287条之二 / 第六章第一节）=====
CRIMES.append(dict(
key="help_info_notes_v1",
title='帮助信息网络犯罪活动罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第287条之二；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。本罪最高 3年以下。',
caps='{1:36}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>基本幅度</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">为3个对象提供帮助/支付结算20万/提供资金5万/违法所得1万等达入罪标准：三个月拘役至六个月（部分情形六个月至一年）。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>帮助信息网络犯罪活动罪</b>（帮信罪）。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第二百八十七条之二【帮助信息网络犯罪活动罪】</h3>
    <ul>
      <li>明知他人利用信息网络实施犯罪，为其犯罪提供<b>互联网接入、服务器托管、网络存储、通讯传输等技术支持，或者提供广告推广、支付结算等帮助，情节严重</b>的，处<b>三年以下有期徒刑或者拘役，并处或者单处罚金</b>。</li>
      <li>单位犯前款罪的，对单位判处罚金，并对其直接负责的主管人员和其他直接责任人员依规定处罚。</li>
      <li>有前两款行为，同时构成其他犯罪的，依照<b>处罚较重的规定定罪处罚</b>。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2019〕15号 · 关于办理非法利用信息网络、帮助信息网络犯罪活动等刑事案件适用法律若干问题的解释</h3>
    <ul>
      <li>明确"情节严重"标准（对象数、支付结算金额、提供资金、违法所得等）及确因客观条件无法查证被帮助对象但数额达5倍以上的处理。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>帮信罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>信息网络安全管理秩序</b>。</li>
      <li><b>客观方面</b>：为信息网络犯罪提供<b>技术支持或广告推广、支付结算等帮助</b>，达到"情节严重"。</li>
      <li><b>主体</b>：一般主体（自然人与单位）。</li>
      <li><b>主观方面</b>：<b>明知</b>他人利用信息网络实施犯罪而提供帮助。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 是否"明知"</b>：须明知他人利用信息网络犯罪；仅提供正常技术服务无明知的不构罪。</li>
      <li><b>② 与上游犯罪共犯区分</b>：与上游犯罪通谋的定共犯；无通谋仅提供帮助定本罪（从一重）。</li>
      <li><b>③ 与掩饰、隐瞒犯罪所得罪区分</b>：帮信是"帮助"；事后转移赃物定掩饰隐瞒犯罪所得。</li>
      <li><b>④ 与非法经营罪区分</b>：提供支付结算若同时符合非法经营（资金支付结算）竞合从一重。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">帮信罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">上游犯罪共犯</td><td class="cedit" data-key="d1b">与上游犯罪<b>通谋</b>定共犯；无通谋仅帮助定本罪。</td><td class="cedit" data-key="d1c">区分通谋与否；从一重。</td></tr>
      <tr><td class="cedit" data-key="d2">掩饰、隐瞒犯罪所得罪</td><td class="cedit" data-key="d2b">帮信是犯罪<b>过程中</b>帮助；掩饰隐瞒是<b>事后</b>转移赃物。</td><td class="cedit" data-key="d2c">区分阶段；竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d3">非法经营罪</td><td class="cedit" data-key="d3b">提供支付结算若符合非法经营（资金支付结算）竞合。</td><td class="cedit" data-key="d3c">想象竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d4">非法利用信息网络罪</td><td class="cedit" data-key="d4b">设立违法网站/通讯群组；帮信是为其提供技术支持/结算。</td><td class="cedit" data-key="d4c">区分行为。</td></tr>
      <tr><td class="cedit" data-key="d5">侵犯公民个人信息罪</td><td class="cedit" data-key="d5b">提供个人信息用于网络犯罪可能竞合。</td><td class="cedit" data-key="d5c">竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d6">诈骗罪共犯</td><td class="cedit" data-key="d6b">为诈骗提供技术支持/结算且通谋。</td><td class="cedit" data-key="d6c">通谋定共犯。</td></tr>
      <tr><td class="cedit" data-key="d7">洗钱罪</td><td class="cedit" data-key="d7b">帮信与洗钱对象/阶段不同。</td><td class="cedit" data-key="d7c">区分行为性质。</td></tr>
      <tr><td class="cedit" data-key="d8">拒不履行信息网络安全管理义务罪</td><td class="cedit" data-key="d8b">网络服务提供者不履责；本罪是主动提供帮助。</td><td class="cedit" data-key="d8c">区分主体与行为。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪。</li>
      <li><b>立案追诉门槛</b>：为3个对象提供帮助；支付结算金额20万；提供资金5万；违法所得1万；二年内曾因非法利用信息网络等受行政处罚又实施；被帮助对象犯罪致被害人自杀/死亡/精神失常；出租出售信用卡单向流入30万且至少3000元涉诈；收购出售信用卡5张；手机卡20张；相关数额达第(2)–(4)项标准5倍以上等。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审。</li>
      <li><b>追诉时效</b>：最高3年以下 → <b>5年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽；配合追赃挽损可从宽。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>基本幅度</b>（本罪法定最高 3 年，单档）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>基本幅度（拘役–3年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">基本幅度</span></td><td>一般入罪情形</td><td>为3对象帮助/支付结算20万/提供资金5万/违法所得1万等</td><td class="start s1">拘役 – 6个月</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">基本幅度</span></td><td>较重入罪情形</td><td>被帮助对象犯罪致自杀/死亡/精神失常；二年内曾受行政处罚又实施；单向流入30万涉诈</td><td class="start s1">6个月 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">被帮助对象 每 +1个</td><td class="c2">+1个月 / 个</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">支付结算金额 每 +100万元</td><td class="c2">+1个月 / 100万</td></tr>
      <tr data-tier="1" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">提供资金 每 +2万元</td><td class="c2">+1个月 / 2万</td></tr>
      <tr data-tier="1" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">违法所得 每 +5000元</td><td class="c2">+1个月 / 5000元</td></tr>
    </tbody>
  </table>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（增加基准刑 20% 以下，两种以上累计不超过 100%）</h3>
    <ul>
      <li>（1）跨境非法提供技术支持或帮助；</li>
      <li>（2）提供专门或主要用于信息网络犯罪的技术、软件、设备或服务；</li>
      <li>（3）从事"卡头""卡商"等非法活动；</li>
      <li>（4）行业内部人员利用职业或提供服务便利实施犯罪；</li>
      <li>（5）组织、利用未成年人、在校学生、老年人、残疾人等特殊群体实施；</li>
      <li>（6）非法利用区块链、人工智能等技术手段实施；</li>
      <li>（7）曾因网络犯罪、帮信、洗钱、掩饰隐瞒犯罪所得等违法犯罪受过处罚；</li>
      <li>（8）提供对公账户；</li>
      <li>（9）被帮助对象涉及国家安全、公共安全或重大公共利益；</li>
      <li>（10）被帮助对象犯罪造成被害人自杀/死亡/精神失常等严重后果；其他可从重。</li>
    </ul>
    <p class="note-tip">具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。从宽：系在校学生/残疾人等特殊群体、积极配合追赃挽损所起作用较大的，可减少基准刑20%以下。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>单处罚金：一般在<b>违法所得一倍以上二倍以下</b>，罚金数额一般<b>不低于2000元</b>。</li>
      <li>判1年以下有期徒刑或拘役：一般并处 <b>1000元–3万元</b>；判1年以上有期徒刑：罚金一般<b>不低于5000元</b>。</li>
      <li>单位犯罪：罚金一般<b>不低于5万元</b>且不低于对直接责任人员判处的罚金。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①系初犯、数量/数额刚达标、已退缴违法所得，宣告刑≤3年且符合刑法第72条；</li>
        <li>②在校学生/残疾人等特殊群体、积极配合追赃挽损；</li>
        <li>③其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①提供专门或主要用于犯罪的工具/技术/服务；</li>
        <li>②从事"卡头""卡商"；</li>
        <li>③行业内部人员利用便利实施；</li>
        <li>④组织、利用特殊群体实施；</li>
        <li>⑤非法利用区块链/AI等技术；曾因网络犯罪等受刑事处罚；</li>
        <li>⑥涉及国家安全/公共安全、造成被害人自杀死亡等严重后果、将违法所得用于其他犯罪、拒不退出违法所得。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>被帮助对象 每+1个</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>支付结算金额 每+100万元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>提供资金 每+2万元</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>违法所得 每+5000元</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>帮信罪·特定从重(跨境/专门工具/卡头/行业内部/特殊群体/AI/对公账户)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="3" data-max="6" data-tier="1">拘役–6个月（一般入罪）</button>
        <button type="button" class="chip-btn" data-min="6" data-max="12" data-tier="1">6个月–1年（较重入罪）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(跨境/专门工具/卡头/行业内部/特殊群体/AI/对公账户) +20%</label>',
default_tier=1,
))

# ===== 开设赌场罪（刑法303条 / 第六章第一节）=====
CRIMES.append(dict(
key="open_gambling_notes_v1",
title='开设赌场罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第303条第2款；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。基本档 6月–2年；情节严重 5–6年。',
caps='{1:60,2:120}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>基本犯（第一幅度）</h3>
      <div class="range">6个月 – 5年</div>
      <div class="desc">线下/网络/为赌博网站服务/设置赌博机：6月–1年6月（网络/设机可至2年）；情节严重 5–6年。</div>
    </div>
    <div class="card second">
      <h3>情节严重（第二幅度）</h3>
      <div class="range">5年 – 10年</div>
      <div class="desc">抽头/违法所得10万、赌资100万、参赌120人以上等：5年至6年；最高至10年。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>开设赌场罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第三百零三条【开设赌场罪】</h3>
    <ul>
      <li>开设赌场的，处<b>五年以下有期徒刑、拘役或者管制，并处罚金</b>。</li>
      <li><b>情节严重的，处五年以上十年以下有期徒刑，并处罚金</b>。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2005〕3号 · 关于办理赌博刑事案件具体应用法律若干问题的解释；法释〔2010〕40号网络赌博解释</h3>
    <ul>
      <li>明确"情节严重"标准（抽头渔利/赌资/参赌人数/利润分成/为网站服务数额等）及设置赌博机组织赌博的认定。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>开设赌场罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>社会管理秩序（社会风尚与经济秩序）</b>。</li>
      <li><b>客观方面</b>：<b>开设赌场</b>——建立赌博网站/实体场所、为网站担任代理接受投注、提供技术支持/资金结算、设置赌博机等。</li>
      <li><b>主体</b>：一般主体（自然人与单位）。</li>
      <li><b>主观方面</b>：<b>故意</b>，且一般以营利为目的。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 与聚众赌博（赌博罪）区分</b>：开设赌场具有"经营性/持续性/开放性"；临时凑局聚众赌博定赌博罪。</li>
      <li><b>② 与娱乐活动区分</b>：亲友间少量财物输赢的娱乐不构罪。</li>
      <li><b>③ 与非法经营罪区分</b>：为赌博网站提供资金结算可能竞合非法经营。</li>
      <li><b>④ 设置赌博机</b>：达数量标准即构罪，容留未成年人/中小学附近从重。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">开设赌场罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">赌博罪（聚众赌博）</td><td class="cedit" data-key="d1b">开设赌场具<b>经营性/持续性</b>；聚众赌博是临时凑局。</td><td class="cedit" data-key="d1c">区分经营性与临时。</td></tr>
      <tr><td class="cedit" data-key="d2">非法经营罪</td><td class="cedit" data-key="d2b">为赌博网站提供资金结算可能竞合非法经营。</td><td class="cedit" data-key="d2c">想象竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d3">帮助信息网络犯罪活动罪</td><td class="cedit" data-key="d3b">为赌博网站提供技术支持可能竞合帮信。</td><td class="cedit" data-key="d3c">竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d4">抢劫罪/敲诈勒索罪</td><td class="cedit" data-key="d4b">在赌场内暴力讨债另定他罪。</td><td class="cedit" data-key="d4c">数罪并罚。</td></tr>
      <tr><td class="cedit" data-key="d5">组织参与国（境）外赌博罪</td><td class="cedit" data-key="d5b">组织境内人员出境赌博另定他罪。</td><td class="cedit" data-key="d5c">区分行为。</td></tr>
      <tr><td class="cedit" data-key="d6">容留他人吸毒罪</td><td class="cedit" data-key="d6b">赌场内容留吸毒可能竞合。</td><td class="cedit" data-key="d6c">数罪并罚或竞合。</td></tr>
      <tr><td class="cedit" data-key="d7">窝藏、包庇罪</td><td class="cedit" data-key="d7b">为赌徒提供隐藏处所可能竞合。</td><td class="cedit" data-key="d7c">区分行为。</td></tr>
      <tr><td class="cedit" data-key="d8">故意毁坏财物罪</td><td class="cedit" data-key="d8b">赌博中毁损财物按相应规定。</td><td class="cedit" data-key="d8c">区分行为。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪。</li>
      <li><b>立案追诉门槛</b>：实施开设赌场行为即应追诉；"情节严重"标准——抽头/违法所得10万、赌资100万、参赌120人以上、网站利润分成/代理、为10个以上网站投广告或累计100条、赌博机60台等。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审；情节严重可能由中院一审。</li>
      <li><b>追诉时效</b>：基本犯（5年以下）→ <b>5年/10年</b>；情节严重（5–10年）→ <b>15年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽；退缴违法所得影响量刑与缓刑。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（基本犯，最高 5 年）；红色块＝<b>第二量刑幅度</b>（情节严重，5 年–10 年）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（6月–5年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（5年–10年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>线下/网络/为网站服务/设机</td><td>抽头5000元、赌资5万、参赌20人；建网站/代理/分成；为网站服务；设机10台</td><td class="start s1">6月 – 1年6月</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>网络/设机（可至2年）</td><td>利用网络组织赌博、设置赌博机组织赌博</td><td class="start s1">6月 – 2年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>情节严重</td><td>抽头/违法所得10万、赌资100万、参赌120人以上等</td><td class="start s2">5年 – 6年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">抽头渔利/违法所得 每 +2000元</td><td class="c2">+1个月 / 2000元</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">赌资数额 每 +2万元</td><td class="c2">+1个月 / 2万</td></tr>
      <tr data-tier="1" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">参赌人数 每 +2人</td><td class="c2">+1个月 / 2人</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">情节严重档：抽头渔利/违法所得 每 +1万元</td><td class="c2">+1个月 / 1万</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px"><h3>情节严重档其他增量（节选）</h3>
    <ul>
      <li>赌资每+10万 +1个月；参赌每+10人 +1–3个月（情节严重档）。</li>
      <li>网络利润分成/代理 违法所得每+1万 +1个月；为网站服务 服务费每+3万 +1个月；设机60台以上 每+3台 +1个月。</li>
      <li>抽头/赌资/参赌人数等不得同时用以增加刑罚量，以确定基准刑较重的标准计算。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（增加基准刑 20% 以下，两种以上累计不超过 100%）</h3>
    <ul>
      <li>（1）具有国家机关工作人员身份，或组织国家机关工作人员参赌；</li>
      <li>（2）组织、招揽、雇佣未成年人实施，或组织、胁迫、引诱、教唆、容留未成年人参与赌博；</li>
      <li>（3）采用限制人身自由等手段强迫他人赌博或结算赌资；</li>
      <li>（4）因开设赌场致1人以上死亡、重伤或3人以上轻伤，或引发其他严重后果；</li>
      <li>（5）曾因涉赌受刑事处罚或二年内受行政处罚（累犯/同一行为除外）；</li>
      <li>（6）黑恶势力实施的开设赌场；其他可从重。</li>
    </ul>
    <p class="note-tip">具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>判5年以下：一般并处 <b>2000元–20万元</b>罚金。</li>
      <li>判5年以上：并处罚金一般<b>不低于5万元</b>。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①规模小、系从犯/初犯、已退缴违法所得，宣告刑≤3年且符合刑法第72条；</li>
        <li>②其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①具有国家工作人员身份或组织国家工作人员参赌；</li>
        <li>②组织、招揽、雇佣未成年人参与；</li>
        <li>③采用限制人身自由等手段强迫赌博/结算；</li>
        <li>④致1人以上死亡/重伤或3人以上轻伤等严重后果；</li>
        <li>⑤曾因涉赌受刑事处罚或二年内受行政处罚；拒不退缴违法所得；黑恶势力。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>抽头渔利/违法所得 每+2000元</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>赌资数额 每+2万元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>参赌人数 每+2人</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>情节严重档 抽头渔利 每+1万元</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>开设赌场罪·特定从重(国家工作人员/未成年人/强迫/致死伤/累犯/黑恶)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="6" data-max="18" data-tier="1">6月–1年6月（基本犯）</button>
        <button type="button" class="chip-btn" data-min="60" data-max="72" data-tier="2">5年–6年（情节严重）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(国家工作人员/未成年人/强迫/致死伤/累犯/黑恶) +20%</label>',
default_tier=1,
))

# ===== 拒不执行判决、裁定罪（刑法313条 / 第六章第二节 妨害司法罪）=====
CRIMES.append(dict(
key="refuse_judgment_notes_v1",
title='拒不执行判决、裁定罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第313条；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。基本档 拘役–1年；情节特别严重 3–4年。',
caps='{1:36,2:84}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>情节严重（第一幅度）</h3>
      <div class="range">拘役 – 3年</div>
      <div class="desc">隐藏/转移财产、拒报财产、拒不交付财物/迁出、虚假诉讼妨害等致判决无法执行：拘役至9个月（部分至1年）。</div>
    </div>
    <div class="card second">
      <h3>情节特别严重（第二幅度）</h3>
      <div class="range">3年 – 7年</div>
      <div class="desc">暴力抗拒致1人重伤/3人轻伤、财产损失5万、无法执行财产100万、致债权人重大损失、自杀自残等：3年至4年。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>拒不执行判决、裁定罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第三百一十三条【拒不执行判决、裁定罪】</h3>
    <ul>
      <li>对人民法院的<b>判决、裁定有能力执行而拒不执行，情节严重</b>的，处<b>三年以下有期徒刑、拘役或者罚金</b>。</li>
      <li><b>情节特别严重的，处三年以上七年以下有期徒刑，并处罚金</b>。</li>
      <li>单位犯前款罪的，对单位判处罚金，并对其直接负责的主管人员和其他直接责任人员依规定处罚。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2015〕16号 · 关于审理拒不执行判决、裁定刑事案件适用法律若干问题的解释</h3>
    <ul>
      <li>明确"有能力执行而拒不执行，情节严重"的具体情形及"情节特别严重"标准。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>拒执罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>人民法院裁判的权威与执行秩序</b>。</li>
      <li><b>客观方面</b>：对<b>人民法院判决、裁定</b>有能力执行而<b>拒不执行，情节严重</b>（含隐藏转移财产、拒报、拒不交付、暴力阻碍、虚假诉讼妨害等）。</li>
      <li><b>主体</b>：被执行人、担保人、协助执行义务人等（自然人与单位）。</li>
      <li><b>主观方面</b>：<b>故意</b>（有能力执行而拒不执行）。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 是否"有能力执行"</b>：确无履行能力的不构罪（ execution impossibility）。</li>
      <li><b>② 与妨害公务罪区分</b>：暴力阻碍执行人员可能竞合；本罪是拒不执行生效裁判。</li>
      <li><b>③ 与非法处置查封/扣押/冻结财产罪区分</b>：对象与行为不同，注意竞合。</li>
      <li><b>④ 与虚假诉讼罪区分</b>：以虚假诉讼妨害执行定本罪（解释明确为情形之一）。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">拒不执行判决、裁定罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">妨害公务罪</td><td class="cedit" data-key="d1b">暴力阻碍执行人员；本罪是拒不执行生效裁判。</td><td class="cedit" data-key="d1c">竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d2">非法处置查封、扣押、冻结财产罪</td><td class="cedit" data-key="d2b">对象为被查封扣押冻结财产；本罪是拒不执行裁判。</td><td class="cedit" data-key="d2c">区分对象与行为。</td></tr>
      <tr><td class="cedit" data-key="d3">虚假诉讼罪</td><td class="cedit" data-key="d3b">以虚假诉讼妨害执行定本罪（解释情形之一）。</td><td class="cedit" data-key="d3c">依本罪评价。</td></tr>
      <tr><td class="cedit" data-key="d4">故意伤害罪/故意杀人罪</td><td class="cedit" data-key="d4b">暴力抗拒致执行人员轻伤以上。</td><td class="cedit" data-key="d4c">数罪并罚或从一重。</td></tr>
      <tr><td class="cedit" data-key="d5">故意毁坏财物罪</td><td class="cedit" data-key="d5b">毁损执行器械/材料可能竞合。</td><td class="cedit" data-key="d5c">数罪并罚。</td></tr>
      <tr><td class="cedit" data-key="d6">窝藏、包庇罪</td><td class="cedit" data-key="d6b">协助被执行人隐藏财产/逃匿可能竞合。</td><td class="cedit" data-key="d6c">区分主体与行为。</td></tr>
      <tr><td class="cedit" data-key="d7">滥用职权罪</td><td class="cedit" data-key="d7b">国家机关工作人员通谋妨害执行可能竞合。</td><td class="cedit" data-key="d7c">依主体与行为定性。</td></tr>
      <tr><td class="cedit" data-key="d8">拒不支付劳动报酬罪</td><td class="cedit" data-key="d8b">拒不支付劳动报酬另定他罪；本罪是拒不执行生效裁判。</td><td class="cedit" data-key="d8c">区分对象。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪。</li>
      <li><b>立案追诉门槛</b>：有能力执行而拒不执行，具有司法解释列明的"情节严重"情形（隐藏转移财产、拒报财产、拒不交付财物/迁出、违反限高令经罚款拘留仍拒执、虚假诉讼/仲裁/和解妨害、暴力阻碍执行、致债权人重大损失等）。</li>
      <li><b>管辖法院</b>：犯罪地（通常执行法院所在地）基层人民法院一审。</li>
      <li><b>追诉时效</b>：情节严重（3年以下）→ <b>5年/10年</b>；情节特别严重（3–7年）→ <b>15年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：一审宣告判决前履行全部执行义务可减基准刑40%以下；履行部分可参照比例减。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（情节严重，最高 3 年）；红色块＝<b>第二量刑幅度</b>（情节特别严重，3 年–7 年）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（拘役–3年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（3年–7年）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>情节严重（一般）</td><td>隐藏转移财产/拒报财产/拒不交付财物/违反限高令仍拒执等致无法执行</td><td class="start s1">拘役 – 9个月</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-first2"><td><span class="tier t1">第一幅度</span></td><td>情节严重（较重）</td><td>与国家机关工作人员通谋、暴力威胁阻碍、虚假诉讼/仲裁/和解妨害、致执行工作无法进行</td><td class="start s1">6个月 – 1年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r2"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>情节特别严重</td><td>暴力致1人重伤/3人轻伤、财产损失5万、无法执行财产100万、致债权人重大损失/自杀自残</td><td class="start s2">3年 – 4年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">每增加 1种拒执情形</td><td class="c2">+3个月 / 种</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">暴力抗拒 每增加 1名轻微伤</td><td class="c2">+1个月 / 人</td></tr>
      <tr data-tier="2" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">情节特别严重 每增加 1种情形</td><td class="c2">+6个月 / 种</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">致债权人损失 每 +10万元</td><td class="c2">+1个月 / 10万</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px"><h3>情节特别严重档其他增量（节选）</h3>
    <ul>
      <li>每增加轻微伤1人 +1–3个月；轻伤二级1人 +3–6个月；轻伤一级1人 +6–9个月。</li>
      <li>直接财产损失每+5000元 +1–2个月；无法执行财产/债权人损失每+30万 +1–2个月。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（增加基准刑 20% 以下，两种以上累计不超过 100%）</h3>
    <ul>
      <li>（1）曾因妨害司法受刑事处罚或一年内因妨害司法受罚款/拘留（累犯/同一判决除外）；</li>
      <li>（2）拒不执行支付赡养费、扶养费、抚育费、抚恤金、医疗费用、劳动报酬等判决裁定；</li>
      <li>（3）煽动群众阻碍执行；</li>
      <li>（4）采取持械、聚众围攻等暴力、威胁手段；</li>
      <li>（5）造成恶劣社会影响；其他可从重。</li>
    </ul>
    <p class="note-tip">从宽：一审宣告判决前履行全部执行义务，可减少基准刑40%以下；履行部分的参照比例减少。具体比例见估算器「本罪特定从重」（默认 20%，可调；上限 30%以下）。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>单处罚金：一般 <b>2000元–10万元</b>。</li>
      <li>判3年以上7年以下：并处罚金一般<b>不低于1万元</b>。</li>
      <li>单位犯罪：情节严重一般 <b>5万–200万元</b>；情节特别严重罚金一般<b>不低于20万元</b>。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 一般可以适用缓刑</h3>
      <ul>
        <li>①情节较轻、系初犯、一审前已全部履行执行义务，宣告刑≤3年且符合刑法第72条；</li>
        <li>②其他可以适用缓刑的情形。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①一审宣告判决前仍拒不执行或未赔偿经济损失（二审前履行除外）；</li>
        <li>②煽动群众以暴力、威胁方法阻碍执行；</li>
        <li>③采用持械、聚众围攻等暴力、威胁手段；</li>
        <li>④与他人串通虚假诉讼/仲裁/和解、与国家机关工作人员通谋妨害执行；</li>
        <li>⑤造成1人以上轻伤或多人轻微伤；曾因妨害司法受刑事处罚；造成严重后果或恶劣影响。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>每增加1种拒执情形</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="3" value="3"><span>月</span></div>
          <div class="prow"><span>暴力抗拒 每+1名轻微伤</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>情节特别严重 每+1种情形</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="6" value="6"><span>月</span></div>
          <div class="prow"><span>致债权人损失 每+10万元</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>拒执罪·特定从重(屡犯/赡养医疗劳动报酬/煽动/持械暴力/串通虚假诉讼)<i class="rng">30%以下</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="3" data-max="9" data-tier="1">拘役–9个月（情节严重）</button>
        <button type="button" class="chip-btn" data-min="36" data-max="48" data-tier="2">3年–4年（情节特别严重）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(屡犯/赡养医疗劳动报酬/煽动/持械暴力/串通虚假诉讼) +20%</label>',
default_tier=1,
))

# ===== 组织卖淫罪（刑法358条 / 第六章第八节）=====
CRIMES.append(dict(
key="organize_prostitution_notes_v1",
title='组织卖淫罪量刑指引（江西·赣高法〔2025〕20号《量刑指导意见（二）》实施细则）',
sub='依据：刑法第358条；最高人民法院、最高人民检察院《关于常见犯罪的量刑指导意见（二）（试行）》；江西省实施细则（赣高法〔2025〕20号）。一般情形 5–7年；情节严重 10–13年。',
caps='{1:120,2:180}',
overview='''    <div class="overview">
    <div class="card first">
      <h3>一般情形（第一幅度）</h3>
      <div class="range">5年 – 10年</div>
      <div class="desc">犯罪情节一般：5年至7年有期徒刑；按卖淫人数/非法获利/伤害后果累加。</div>
    </div>
    <div class="card second">
      <h3>情节严重（第二幅度）</h3>
      <div class="range">10年 – 无期</div>
      <div class="desc">卖淫10人/非法获利100万以上、组织境外/境内出境、造成自残自杀等严重后果：10年至12年/13年；依法可至无期。</div>
    </div>
  </div>''',
law='''  <h2 class="section" style="border-left-color:var(--teal)">〇、刑法与司法解释规定（定罪依据）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本表量刑的前提是行为已构成<b>组织卖淫罪</b>。以下列明定罪所依据的刑法条文与司法解释关键条款。</p>
  <div class="block law">
    <h3><span class="law-src">刑法</span>第三百五十八条【组织卖淫罪】</h3>
    <ul>
      <li>组织他人卖淫或者<b>强迫他人卖淫</b>的，处<b>五年以上十年以下有期徒刑，并处罚金</b>。</li>
      <li>有下列情形之一的，处<b>十年以上有期徒刑或者无期徒刑，并处罚金或者没收财产</b>：（一）组织他人卖淫，情节严重的；（二）强迫不满十四周岁幼女卖淫；（三）强迫多人卖淫或者多次强迫他人卖淫；（四）强奸后迫使卖淫；（五）造成被强迫卖淫的人重伤、死亡或者其他严重后果的。</li>
    </ul>
  </div>
  <div class="block law">
    <h3><span class="law-src">司法解释</span>法释〔2017〕13号 · 关于办理组织、强迫、引诱、容留、介绍卖淫刑事案件适用法律若干问题的解释</h3>
    <ul>
      <li>明确"情节严重"标准（卖淫人数、非法获利、组织境外/境内出境、造成严重后果等）。</li>
    </ul>
  </div>''',
const='''  <h2 class="section" style="border-left-color:var(--green)">一、构成要件与罪与非罪界限（定罪分析）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">量刑的前提是行为已构成本罪。本节先拆解<b>构成要件</b>，再列出实务中最常用的<b>界分点</b>。</p>
  <div class="block const">
    <h3><span class="tag-const">四要件</span>组织卖淫罪的犯罪构成</h3>
    <ul>
      <li><b>客体</b>：<b>社会管理秩序与良好风尚</b>（含被组织者的身心健康）。</li>
      <li><b>客观方面</b>：<b>组织、策划、指挥他人卖淫</b>（建立、控制卖淫团伙，安排卖淫活动等）。</li>
      <li><b>主体</b>：一般主体（组织者；协助组织卖淫另定他罪）。</li>
      <li><b>主观方面</b>：<b>故意</b>，一般以营利为目的。</li>
    </ul>
  </div>
  <div class="block const">
    <h3><span class="tag-const">界分</span>罪与非罪 · 界分点</h3>
    <ul>
      <li><b>① 与协助组织卖淫罪区分</b>：起组织/策划/指挥作用的定本罪；仅起帮助作用的定协助组织卖淫罪。</li>
      <li><b>② 与容留、介绍卖淫罪区分</b>：本罪是"组织"（控制性）；容留/介绍是放任/撮合。</li>
      <li><b>③ 与强迫卖淫罪区分</b>：以暴力/胁迫强迫他人卖淫定强迫卖淫（升档）；组织含非强迫情形。</li>
      <li><b>④ 人数与获利认定</b>：卖淫人数、非法获利数额是"情节严重"的核心指标。</li>
    </ul>
  </div>''',
dist='''  <h2 class="section" style="border-left-color:#6a5acd">二、此罪与彼罪的界限（竞合 / 区分）</h2>
  <p class="note-tip" style="margin:2px 0 12px;">组织卖淫罪常与下列犯罪混淆。下表列明<b>关键区分点</b>与<b>处理规则</b>。</p>
  <table class="distTbl" id="distTbl">
    <thead><tr><th class="c1">易混淆罪名</th><th class="c2">关键区分点</th><th class="c3">处理规则（竞合 / 定性）</th></tr></thead>
    <tbody>
      <tr><td class="cedit" data-key="d1">协助组织卖淫罪</td><td class="cedit" data-key="d1b">起<b>帮助</b>作用；本罪起组织/策划/指挥作用。</td><td class="cedit" data-key="d1c">区分地位作用。</td></tr>
      <tr><td class="cedit" data-key="d2">容留、介绍卖淫罪</td><td class="cedit" data-key="d2b">本罪具<b>组织/控制性</b>；容留介绍是放任/撮合。</td><td class="cedit" data-key="d2c">区分行为性质。</td></tr>
      <tr><td class="cedit" data-key="d3">强迫卖淫罪</td><td class="cedit" data-key="d3b">以暴力胁迫<b>强迫</b>他人卖淫升档；本罪含非强迫情形。</td><td class="cedit" data-key="d3c">区分手段；竞合从一重。</td></tr>
      <tr><td class="cedit" data-key="d4">强奸罪</td><td class="cedit" data-key="d4b">强奸后迫使卖淫（解释升档情形）。</td><td class="cedit" data-key="d4c">依本罪升档评价。</td></tr>
      <tr><td class="cedit" data-key="d5">拐卖妇女、儿童罪</td><td class="cedit" data-key="d5b">以出卖为目的拐带；组织卖淫是控制卖淫活动。</td><td class="cedit" data-key="d5c">区分目的。</td></tr>
      <tr><td class="cedit" data-key="d6">故意伤害罪</td><td class="cedit" data-key="d6b">造成卖淫人员轻伤以上按本罪加重情节评价。</td><td class="cedit" data-key="d6c">吸收评价。</td></tr>
      <tr><td class="cedit" data-key="d7">传播性病罪</td><td class="cedit" data-key="d7b">卖淫人员患性病卖淫另定他罪；组织者明知的可能竞合。</td><td class="cedit" data-key="d7c">区分主体。</td></tr>
      <tr><td class="cedit" data-key="d8">聚众淫乱罪</td><td class="cedit" data-key="d8b">自愿聚众淫乱；本罪是组织他人卖淫营利。</td><td class="cedit" data-key="d8c">区分行为目的。</td></tr>
    </tbody>
  </table>''',
info='''  <h2 class="section" style="border-left-color:var(--teal)">三、立案追诉标准、管辖与时效</h2>
  <p class="note-tip" style="margin:2px 0 12px;">本节速查本罪作为公诉案件的立案门槛、管辖与追诉时效等程序性要点。</p>
  <div class="block info">
    <ul>
      <li><b>案件性质</b>：<b>公诉案件</b>；单位亦可构成本罪（双罚制）。</li>
      <li><b>立案追诉门槛</b>：实施组织他人卖淫行为即应追诉（无单独数额标准）；"情节严重"依法释〔2017〕13号（卖淫10人/非法获利100万/组织境外或境内出境/造成自残自杀等严重后果）。</li>
      <li><b>管辖法院</b>：犯罪地基层人民法院一审；可能判无期由中院一审。</li>
      <li><b>追诉时效</b>：一般（10年以下）→ <b>10年/15年</b>；情节严重（10年以上/无期）→ <b>15年/20年</b>（刑法第87条）。</li>
      <li><b>程序适用</b>：认罪认罚可从宽；退缴赃款影响量刑；具有减轻处罚情节判3年以下的从严把握缓刑。</li>
    </ul>
  </div>''',
start='''  <h2 class="section">四、量刑起点一览（符合什么情形 → 起点多少刑）</h2>
  <p class="note-tip" style="margin:2px 0 10px;">
    <b>结构说明：</b>蓝色块＝<b>第一量刑幅度</b>（一般情形，5 年–10 年）；红色块＝<b>第二量刑幅度</b>（情节严重，10 年–无期）。
  </p>
  <div class="legend">
    <span><i class="chip" style="background:var(--blue)"></i>第一量刑幅度（5年–10年）</span>
    <span><i class="chip" style="background:var(--red)"></i>第二量刑幅度（10年–无期）</span>
    <span><i class="chip" style="background:#b9b09a"></i>批注（可编辑）</span>
  </div>
  <table id="startTbl">
    <thead><tr><th style="width:72px">起点档</th><th style="width:120px">行为类型</th><th>具体情形</th><th style="width:150px">量刑起点幅度</th><th style="width:200px">✎ 我的批注</th></tr></thead>
    <tbody>
      <tr class="grp-first1"><td><span class="tier t1d">第一幅度</span></td><td>犯罪情节一般</td><td>组织卖淫，卖淫人员达3人</td><td class="start s1">5年 – 7年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r1"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>情节严重（人数/获利）</td><td>卖淫10人、非法获利100万，或其他情节严重</td><td class="start s2">10年 – 12年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r4"></td></tr>
      <tr class="grp-second"><td><span class="tier t2">第二幅度</span></td><td>情节严重（境外/后果）</td><td>组织境外/境内出境卖淫、造成自残自杀等严重后果</td><td class="start s2">10年 – 13年</td><td class="editable" data-ph="点击添加批注" contenteditable="true" data-key="r5"></td></tr>
    </tbody>
  </table>''',
cmp='''  <h2 class="section">五、基准刑增加刑罚量（起点之上，按犯罪事实累加）</h2>
  <table class="cmp">
    <thead><tr><th style="width:40px">项</th><th class="c1">基准刑增量项</th><th class="c2">增率（月 / 单位）</th></tr></thead>
    <tbody>
      <tr data-tier="1" data-f="f_amt1" data-pmin="p_amt1" data-pmax="p_amt1"><td>①</td><td class="c1">卖淫人员 每 +1人</td><td class="c2">+6个月 / 人</td></tr>
      <tr data-tier="1" data-f="f_amt2" data-pmin="p_amt2" data-pmax="p_amt2"><td>②</td><td class="c1">非法获利 每 +2万元</td><td class="c2">+1个月 / 2万</td></tr>
      <tr data-tier="2" data-f="f_amt3" data-pmin="p_amt3" data-pmax="p_amt3"><td>③</td><td class="c1">卖淫人员(情节严重,10人以上) 每 +1人</td><td class="c2">+2个月 / 人</td></tr>
      <tr data-tier="2" data-f="f_times" data-pmin="p_times" data-pmax="p_times"><td>④</td><td class="c1">非法获利(情节严重,100万以上) 每 +5万元</td><td class="c2">+1个月 / 5万</td></tr>
    </tbody>
  </table>
  <div class="block info" style="margin-top:12px"><h3>情节严重档其他增量（节选）</h3>
    <ul>
      <li>卖淫人员中未成年/孕妇/智障/严重性病患者每+1人 +4个月；组织境外/境内出境每人 +6–12个月。</li>
      <li>造成卖淫人员轻伤二级每人 +3–6个月、轻伤一级 +6–9个月；自残/自杀/重伤等每人 +18–24个月。</li>
      <li>人数与非法获利不得同时用以增加刑罚量；卖淫人员超3人且含特殊群体人员的，分别情形计算不叠加。</li>
    </ul>
  </div>''',
heavy='''  <h2 class="section">六、从重处罚情节（调节基准刑）</h2>
  <div class="block heavy">
    <h3>⚠ 从重调节（上限 100% 以内，依情形 5%–20%）</h3>
    <ul>
      <li>（1）组织未成年人卖淫，增加基准刑 <b>10%–20%</b>；</li>
      <li>（2）旅馆业、饮食服务业、文化娱乐业、出租汽车业等单位主要负责人利用本单位条件组织的，增加基准刑 <b>10%–20%</b>；其他人员利用本单位条件组织的，增加 <b>10%以下</b>；</li>
      <li>（3）公共场所公然招嫖、网络/短信发布招嫖信息等方式公开招募，增加基准刑 <b>20%以下</b>；</li>
      <li>（4）曾因组织/强迫/引诱/容留/介绍卖淫受行政处罚的，增加 5%以下；受刑事追究但不构成累犯的，增加 5%–10%以下；</li>
      <li>（5）对被组织卖淫人员同时具有引诱卖淫行为的，增加 20%以下；</li>
      <li>（6）其他可以从重处罚的情形，增加 20%以下。</li>
    </ul>
    <p class="note-tip">具体比例见上方估算器「本罪特定从重」（默认 20%，可调；上限依情形）。</p>
  </div>''',
fine='''  <h2 class="section">八、罚金</h2>
  <div class="block fine">
    <h3>罚金幅度</h3>
    <ul>
      <li>依法判处<b>犯罪所得二倍以上的罚金</b>；共同犯罪合计判处罚金应在犯罪所得二倍以上。</li>
      <li>犯罪所得无法查实：判5–10年一般并处 <b>2万–200万元</b>；判10年以上罚金一般<b>不低于30万元</b>。</li>
    </ul>
  </div>''',
pro='''  <h2 class="section">九、缓刑适用</h2>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
    <div class="block pro-yes">
      <h3>✓ 极少数可适用缓刑</h3>
      <ul>
        <li>①具有减轻处罚情节、判3年以下、系从犯/初犯，符合刑法第72条；</li>
        <li>②其他可以适用缓刑的情形（从严把握）。</li>
      </ul>
    </div>
    <div class="block pro-no">
      <h3>✕ 一般不适用缓刑</h3>
      <ul>
        <li>①组织未成年人卖淫；</li>
        <li>②利用单位条件（负责人/从业人员）组织；</li>
        <li>③公共场所/网络公开招嫖招募；</li>
        <li>④曾因同类行为受行政处罚/刑事追究；</li>
        <li>⑤造成严重后果或恶劣社会影响。</li>
      </ul>
    </div>
  </div>''',
prows='''          <div class="prow"><span>卖淫人员 每+1人</span><input type="number" id="f_amt1" value="0" min="0"><i>×</i><input type="number" id="p_amt1" data-def="6" value="6"><span>月</span></div>
          <div class="prow"><span>非法获利 每+2万元</span><input type="number" id="f_amt2" value="0" min="0"><i>×</i><input type="number" id="p_amt2" data-def="1" value="1"><span>月</span></div>
          <div class="prow"><span>卖淫人员(情节严重) 每+1人</span><input type="number" id="f_amt3" value="0" min="0"><i>×</i><input type="number" id="p_amt3" data-def="2" value="2"><span>月</span></div>
          <div class="prow"><span>非法获利(情节严重) 每+5万元</span><input type="number" id="f_times" value="0" min="0"><i>×</i><input type="number" id="p_times" data-def="1" value="1"><span>月</span></div>''',
spec_prow='          <div class="prow"><span>组织卖淫罪·特定从重(组织未成年人/单位负责人/公开招嫖/屡犯/引诱)<i class="rng">依情形</i></span><input type="number" id="p_d_spec" data-def="20" value="20"></div>',
chips='''      <span class="chips" id="startChips">
        <button type="button" class="chip-btn" data-min="60" data-max="84" data-tier="1">5年–7年（一般情形）</button>
        <button type="button" class="chip-btn" data-min="120" data-max="156" data-tier="2">10年–13年（情节严重）</button>
      </span>''',
spec_label='        <label title="本罪特定从重（比例见参数面板「本罪特定从重」）"><input type="checkbox" data-param="p_d_spec"> 特定情形(组织未成年人/单位负责人/公开招嫖/屡犯/引诱) +20%</label>',
default_tier=1,
))

# ---------------- 生成 ----------------
base = open(BASE, encoding="utf-8").read()

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
        h = region(h, v[0], v[1], c.get(k, ''))
    h = inject_caps(h, c.get('caps', ''))
    name = h1name
    fname = os.path.join(OUT, '%s量刑指引（江西）.html' % name)
    open(fname, 'w', encoding='utf-8').write(h)
    print('written:', fname, '(%d bytes)' % len(h))
print('DONE')
