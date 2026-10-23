# -*- coding: utf-8 -*-
"""
part2_header_intro.py
Contains paper hero, metadata, author affiliations, PhD guide banner,
bilingual abstract, and comprehensive introduction/background rationale.
"""

HEADER_AND_INTRO = '''
  <!-- 论文信息卡片 Hero -->
  <header class="paper-hero" id="overview">
    <div class="journal-badge">Nature · Vol 620 · Article · 顶刊精读</div>
    <h1>重构肿瘤驱动基因以激活细胞凋亡：转录/表观遗传化学邻近诱导剂 (TCIP) 开启癌症合成致死新范式</h1>
    <div class="title-en">Rewiring cancer drivers to activate apoptosis (Transcriptional/Epigenetic Chemical Inducers of Proximity, TCIPs)</div>
    <div class="paper-meta">
      <div class="meta-authors">
        <strong>第一作者</strong>：Sai Gourisankar<sup>1,2,6</sup>, Andrey Krokhotin<sup>1,6</sup>, Wenzhi Ji (季文智)<sup>3,6</sup> 等<br>
        <strong>通讯作者</strong>：<strong>Nathanael S. Gray</strong> (nsgray01@stanford.edu)<sup>3*</sup>，<strong>Gerald R. Crabtree</strong> (crabtree@stanford.edu)<sup>1,4*</sup><br>
        <strong>主要作者</strong>：Xiaofan Liu (刘晓凡)<sup>3</sup>, Chiung-Ying Chang (张琼莹)<sup>1</sup>, Samuel H. Kim<sup>1</sup>, Zhengnian Li (李正念)<sup>3</sup>, Wendy Wenderski<sup>1,4</sup>, Juste M. Simanauskaite<sup>1</sup>, Haopeng Yang (杨浩鹏)<sup>5</sup>, Hannes Vogel<sup>1</sup>, Tinghu Zhang (张廷虎)<sup>3</sup>, Michael R. Green<sup>5</sup><br>
        <strong>研究机构</strong>：斯坦福大学病理学系 (Stanford Pathology)、化学工程系、化学生物学与系统生物学系、ChEM-H 研究所、斯坦福癌症研究所、发育生物学系；德克萨斯大学 MD 安德森癌症中心 (MD Anderson) 淋巴瘤与骨髓瘤系
      </div>
      <div class="meta-links">
        <span>出版信息：Nature 620, 417–427 (2023)</span> |
        <span>DOI：<a href="https://doi.org/10.1038/s41586-023-06348-2" target="_blank" rel="noopener">10.1038/s41586-023-06348-2</a></span> |
        <span>上线日期：2023年7月26日</span> |
        <span>收稿日期：2022年8月15日 · 接收日期：2023年6月20日</span>
      </div>
    </div>
  </header>

  <!-- 博士生文献汇报核心导读横幅 -->
  <div class="phd-guide-banner">
    <h3>🎓 博士文献汇报（Journal Club）核心备战导读</h3>
    <p>
      <strong>核心科学问题与范式危机</strong>：当前所有经典的肿瘤靶向疗法——无论是激酶抑制剂、PROTAC 靶向蛋白降解（TPD）、分子胶，还是 CRISPRi / RNAi 基因沉默，本质上都属于<strong>“功能缺失型”（Loss-of-Function, LoF）</strong>干预手段。它们要求对癌基因进行 100% 彻底的酶活抑制或蛋白清除，这往往会带来两大不可避免的临床困境：① <strong>机制性在体毒性</strong>（当靶点蛋白在正常组织中行使生理必需功能时，彻底清除会摧毁正常稳态）；② <strong>极易快速突变与旁路旁代偿耐药</strong>。<br><br>
      <strong>本研究的颠覆性创见</strong>：化学生物学邻近效应奠基人、斯坦福大学 <strong>Gerald R. Crabtree 院士</strong>与著名激酶/小分子靶向专家 <strong>Nathanael S. Gray 教授</strong>联手，在 <em>Nature</em> 提出了开创性的<strong>“功能获得型”（Gain-of-Function, GoF）药理学概念——转录/表观遗传化学邻近诱导剂（TCIPs）</strong>。通过合成一种异双功能小分子，一端锚定肿瘤高表达的致癌转录抑制因子（如淋巴瘤中的 <strong>BCL6</strong>），另一端招募转录激活延伸因子（如 <strong>BRD4</strong> 或雌激素受体 <strong>ER</strong>）。这种“分子搭桥”不仅解除了 BCL6 对促凋亡基因的表观遗传沉默，更借刀杀人，<strong>将肿瘤细胞赖以生存的致癌驱动蛋白强制改造成驱动细胞自杀的“死亡诱导转录因子”</strong>！只需动用细胞内极小比例（约 10%）的分子即可在 15 分钟内引发爆发式促凋亡转录延伸（<strong>BIM、PMAIP1/NOXA、FOXO3</strong>），在 1–10 nM 极低浓度下彻底歼灭包括耐药和 TP53 突变在内的淋巴瘤细胞（效能高出传统降解剂 1,000 倍以上），并在小鼠体内表现出极高的组织耐受性，为整个人类抗癌药物研发开辟了由“抑制消除”走向“功能重构”的崭新纪元。
    </p>
  </div>

  <!-- 摘要部分 (中英双语对照) -->
  <section class="card-section" id="abstract">
    <h2 class="section-heading"><span class="sec-id">Abstract</span>中英文双语论文摘要逐句精译</h2>

    <div class="mechanism-card blue">
      <div class="mechanism-title">📌 摘要核心要点提炼 (Executive Abstract Takeaways)</div>
      <ul style="margin-left: 20px; line-height: 1.8; font-size: 14.5px; color: #1e3a8a;">
        <li><strong>概念创立</strong>：首次提出 TCIP（Transcriptional/Epigenetic Chemical Inducer of Proximity），无需基因工程改造即可在内源水平重构转录回路。</li>
        <li><strong>首发代表分子 TCIP1</strong>：分子量由 BCL6(BTB) 结合剂 BI3812 与 BET(BRD4) 结合剂 JQ1 经化学 Linker 共价拼装而成。</li>
        <li><strong>作用机制</strong>：在基因组 BCL6 结合位点将 BRD4 丰度提升 50%，15 分钟内诱发 RNA Pol II 在促凋亡靶基因启动子及外显子-内含子接头处发生Ser2磷酸化延伸，同时仅消耗超级增强子处 10% 的 BRD4。</li>
        <li><strong>颠覆性杀伤效能</strong>：在弥漫大 B 细胞淋巴瘤（DLBCL，含 TP53 双等位缺失耐药株）中展现出 1.3 nM 的极低 EC50，比 BCL6 降解剂（BI3802）或 BRD4 降解剂（dBET1）高出 200–10,000 倍。</li>
        <li><strong>正反馈回路重构</strong>：破坏了 BCL6 基因内部原本的负自反馈抑制，将 BCL6 自身诱导为高表达正反馈，放大自杀效应。</li>
        <li><strong>平台普适性验证</strong>：通过设计 TCIP2（招募雌激素受体 ER），成功在 ER+ BCL6+ 淋巴瘤中复现定向杀伤，证明该模块化策略可拓展至更广阔的转录调控靶点。</li>
      </ul>
    </div>

    <table class="custom-table" style="margin-top: 24px;">
      <thead>
        <tr>
          <th style="width: 50%;">英文原文 (Nature Original)</th>
          <th style="width: 50%;">学术规范中文逐句精译与科学评注</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Genes that drive the proliferation, survival, invasion and metastasis of malignant cells have been identified for many human cancers.</td>
          <td>在人类多种恶性肿瘤中，驱动恶性细胞增殖、存活、侵袭与转移的关键基因已被广泛鉴定。</td>
        </tr>
        <tr>
          <td>Independent studies have identified cell death pathways that eliminate cells for the good of the organism.</td>
          <td>与此同时，独立的生物学研究也阐明了机体为了维持整体稳态、清除异常细胞而设立的程序性细胞死亡途径。</td>
        </tr>
        <tr>
          <td>The coexistence of cell death pathways with driver mutations suggests that the cancer driver could be rewired to activate cell death using chemical inducers of proximity (CIPs).</td>
          <td><strong>细胞死亡通路与致癌驱动突变在肿瘤细胞内的共存现象提示我们</strong>：是否可以利用<strong>化学诱导邻近剂 (CIPs)</strong>，将肿瘤驱动因子的促癌功能“重新布线”（Rewiring），反转为主动激活细胞死亡程序的执行者？</td>
        </tr>
        <tr>
          <td>Here we describe a new class of molecules called transcriptional/epigenetic CIPs (TCIPs) that recruit the endogenous cancer driver, or a downstream transcription factor, to the promoters of cell death genes, thereby activating their expression.</td>
          <td>在本研究中，我们报道了一类新型小分子化合物——<strong>转录/表观遗传化学邻近诱导剂 (TCIPs)</strong>。该类分子能够将细胞内源表达的肿瘤驱动蛋白（或其下游转录因子）精准招募至细胞死亡基因的启动子区域，从而强效激活其转录表达。</td>
        </tr>
        <tr>
          <td>We focused on diffuse large B cell lymphoma, in which the transcription factor B cell lymphoma 6 (BCL6) is deregulated. BCL6 binds to the promoters of cell death genes and epigenetically suppresses their expression.</td>
          <td>我们将研究聚焦于<strong>弥漫性大 B 细胞淋巴瘤 (DLBCL)</strong>——在该恶性血液肿瘤中，关键转录因子 <strong>BCL6</strong> 发生持续性失控高表达。BCL6 通过直接结合细胞死亡基因的启动子，在表观遗传学层面深度抑制这些促凋亡基因的转录。</td>
        </tr>
        <tr>
          <td>We produced TCIPs by covalently linking small molecules that bind BCL6 to those that bind to transcriptional activators that contribute to the oncogenic program, such as BRD4.</td>
          <td>我们通过共价连接 BCL6 结合小分子与促进致癌转录程序的转录激活因子结合剂（如 BET 家族蛋白 <strong>BRD4</strong> 结合剂），成功合成了系列 TCIP 分子。</td>
        </tr>
        <tr>
          <td>The most potent molecule, TCIP1, increases binding of BRD4 by 50% over genomic BCL6-binding sites to produce transcriptional elongation at pro-apoptotic target genes within 15 min, while reducing binding of BRD4 over enhancers by only 10%, reflecting a gain-of-function mechanism.</td>
          <td>其中活性最强的代表性分子 <strong>TCIP1</strong>，能够使基因组上 BCL6 结合位点处的 BRD4 招募量提升 50%，在仅仅 <strong>15 分钟内</strong>即在促凋亡靶基因上诱发剧烈的转录延伸反应；与此同时，增强子区域的 BRD4 结合仅轻微减少约 10%，这一鲜明对比极其有力地反映了其独特的<strong>“功能获得型”（Gain-of-Function）</strong>作用机制。</td>
        </tr>
        <tr>
          <td>TCIP1 kills diffuse large B cell lymphoma cell lines, including chemotherapy-resistant, TP53-mutant lines, at EC50 of 1–10 nM in 72 h and exhibits cell-specific and tissue-specific effects, capturing the combinatorial specificity inherent to transcription.</td>
          <td>在 72 小时内，TCIP1 能以 <strong>1–10 nM 的半数有效浓度 (EC<sub>50</sub>)</strong> 高效杀伤多株 DLBCL 细胞系（包括对常规化疗耐药、伴随 <em>TP53</em> 双等位失活突变的高危细胞系），并展现出高度依赖细胞特异性与组织特异性的杀伤谱系，完美契合了真核生物转录调控内在固有的“组合特异性”特征。</td>
        </tr>
        <tr>
          <td>The TCIP concept also has therapeutic applications in regulating the expression of genes for regenerative medicine and developmental disorders.</td>
          <td>TCIP 这一基于化学诱导邻近重构内源基因表达的通用概念，在再生医学修复基因重编程、单倍剂量不足（Haploinsufficiency）遗传发育障碍等诸多领域亦具有极其广阔的转化应用前景。</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- 立项背景与科学假说 -->
  <section class="card-section" id="intro">
    <h2 class="section-heading"><span class="sec-id">Introduction</span>立项背景、生物物理原理与科学假说</h2>

    <h3 class="subsection-heading">1. 邻近诱导效应 (Induced Proximity) 的生物物理物理学基础</h3>
    <p>
      在生物体内，诱导分子相互接近是生命调控的最基本形式之一，涵盖受体二聚化激活、翻译后修饰级联（磷酸化、泛素化）、转录起始复合物装配、表观遗传异染色质浓缩以及各类变构分子骨架的组装。
    </p>
    <p>
      诱导邻近效应的底层物理原理极其直观且深刻：在三维溶液体系中，两个独立分子的有效碰撞与相互作用频率，<strong>与其分子间平均距离的三次方（\(1/r^3\)）成反比</strong>。当一个异双功能小分子将两个通常不发生相互作用的蛋白质强行束缚在数个纳米的微观尺度内时，这两个蛋白质局部的**有效浓度（Effective Concentration）会骤增数千至数万倍**，从而跨越天然热力学与动力学能垒，催化下游反应。
    </p>

    <div class="mechanism-card green">
      <div class="mechanism-title">💡 范式跃迁：从 PROTAC 蛋白质降解到 TCIP 转录机器重构</div>
      <p style="font-size: 14.5px; color: #22543d; line-height: 1.75;">
        过去十年间，基于邻近化学最著名的应用是 <strong>PROTAC（靶向蛋白降解嵌合体）</strong>——利用双功能分子一端结合靶蛋白，另一端招募 E3 泛素连接酶（如 CRBN、VHL），将靶蛋白送入 26S 蛋白酶体粉碎。然而，PROTAC 本质上仍属于<strong>“减法”（Loss-of-Function）</strong>逻辑：<br>
        1. 它必须持续消耗靶蛋白；当靶蛋白耗尽后，细胞仍可能通过激活并联旁路信号产生耐药；<br>
        2. 如果被降解的蛋白在造血、免疫或神经系统中行使正常生理功能，不可逆的全身性降解将引起不可耐受的靶向毒性；<br>
        3. 很多致癌转录因子（如 BCL6、MYC）缺乏深口袋，且往往在肿瘤中呈复合体存在，单一降解难度极大。<br>
        <strong>TCIP 的哲学是“加法”（Gain-of-Function）</strong>：它不消灭致癌蛋白，反而<strong>“挟天子以令诸侯”</strong>——利用癌细胞内 BCL6 的高丰度与超高亲和力，强行把 BRD4 转录延伸机器拉到促凋亡基因上，把肿瘤赖以生存的防线瞬间变成致死的“核弹发射器”！
      </p>
    </div>

    <h3 class="subsection-heading">2. BCL6 在弥漫大 B 细胞淋巴瘤 (DLBCL) 中的病理角色与成药困境</h3>
    <p>
      <strong>BCL6 (B-cell lymphoma 6)</strong> 是一种含有 N 端 BTB/POZ 结构域和 C 端 6 个 Kruppel 型锌指结构域的转录抑制因子，是生发中心（Germinal Center, GC）B 细胞形成的“主控开关”（Master Regulator）。在正常生发中心反应中，B 细胞需要进行剧烈的体细胞高频突变（SHM）和类别转换重组（CSR），BCL6 的生理功能是在此期间强行压制 <em>TP53</em>、<em>CDKN1A</em> (p21)、<em>ATR</em>、<em>CHEK1</em> 等 DNA 损伤检查点和 <em>BCL2L11</em> (BIM)、<em>PMAIP1</em> (NOXA) 等促凋亡基因，防止正在编辑抗体的 B 细胞提前凋亡。
    </p>
    <p>
      然而在 DLBCL 中，染色体易位（如 t(3;14)(q27;q32)）或启动子突变导致 BCL6 持续性、不受控地高表达，使得肿瘤细胞获得源源不断的抗凋亡保护。
    </p>

    <div class="mechanism-card purple">
      <div class="mechanism-title">🔬 BCL6 结合的分子结构机制与成药靶点</div>
      <p style="font-size: 14.5px; color: #44337a; line-height: 1.75;">
        BCL6 依赖其 N 端的 <strong>BTB 二聚体结构域</strong>，形成一个专一的侧向结合沟槽（Lateral Groove），高亲和力招募 <strong>NCOR1、NCOR2 (SMRT) 和 BCOR</strong> 等转录共抑制蛋白，进而招募组蛋白去乙酰化酶（HDAC3 等），维持染色质致密沉默状态。<br>
        过去药企针对该沟槽开发了高亲和力抑制剂（如 Boehringer Ingelheim 开发的 <strong>BI3812</strong>，\(K_d \approx 19\\text{ nM}\)）或降解剂（<strong>BI3802</strong>）。然而，单纯使用抑制剂解除压抑（Derepression）并不能有效诱导细胞凋亡，因为促凋亡基因不仅处于被压制状态，其启动子上还缺乏强效的转录激活与延伸驱动；且 DLBCL 细胞对 BI3812 单药极易产生残留耐药细胞。<strong>这正是 TCIP 诞生的核心驱动力：单纯松开刹车（Derepression）不够，必须踩下致死油门（Active Elongation）！</strong>
      </p>
    </div>
  </section>
'''
