# -*- coding: utf-8 -*-
"""
part5_discussion_methods.py
Covers:
- Full Discussion: Paradigm shift from LoF to GoF, proximity pharmacology beyond PROTAC,
  targeting undruggable oncogenic transcription factors, and translational horizons.
- STAR Methods: Step-by-step experimental procedures, chemical synthesis, TR-FRET, ITC,
  PRO-seq, ChIP-seq, and mouse in vivo toxicology protocols.
"""

DISCUSSION_AND_METHODS = '''
  <!-- 全文深度讨论与范式革命 -->
  <section class="card-section" id="discussion">
    <h2 class="section-heading"><span class="sec-id">Discussion</span>全文深度讨论：从“消除抑制”走向“功能重构”的药理学革命</h2>

    <p>
      数十年来，人类现代肿瘤靶向药物研发的思维范式几乎完全被<strong>“功能缺失型”（Loss-of-Function, LoF）</strong>所垄断：无论是占据激酶催化活性口袋的小分子抑制剂、利用单抗中和膜表面受体，还是近年炙手可热的 PROTAC / 分子胶靶向蛋白降解（TPD），其底层的药理学目标都是<strong>“消灭一个对肿瘤生存必不可少的蛋白功能”</strong>。
    </p>
    <p>
      然而，这一传统逻辑正面临着日益严峻的生物学天花板：
    </p>

    <table class="custom-table">
      <thead>
        <tr>
          <th style="width: 20%;">干预维度</th>
          <th style="width: 40%;">传统抑制剂 / PROTAC 靶向降解 (LoF)</th>
          <th style="width: 40%;">TCIP 转录化学邻近重构疗法 (GoF)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>靶标占据度要求</strong></td>
          <td>通常需要对靶蛋白达到 <strong>90%–99% 以上的近乎完全占据或彻底清除</strong>，才足以切断其促癌信号通路。</td>
          <td><strong>仅需动用极小比例（约 10%–15%）</strong>的靶标分子即可催化组装三元复合物，发挥显性获得性转录致死效应。</td>
        </tr>
        <tr>
          <td><strong>有效工作浓度</strong></td>
          <td>微摩尔或高纳摩尔级别（如 BI3802 \(EC_{50} > 10\\,\\mu\\text{M}\)，dBET1 \(EC_{50} \\approx 489\\text{ nM}\)）。</td>
          <td><strong>超低纳摩尔级（TCIP1 \(EC_{50} \\approx 1.3\\text{ nM}\)）</strong>，效能高出传统降解剂 1,000 倍以上。</td>
        </tr>
        <tr>
          <td><strong>耐药逃逸机制</strong></td>
          <td>癌细胞极易通过点突变破坏结合口袋，或通过代偿性激活旁路酪氨酸激酶/其他转录因子实现生存逃逸。</td>
          <td><strong>直接反戈一击</strong>：肿瘤细胞对 BCL6 驱动基因的表达依赖越高，其合成促凋亡机器的“底物平台”就越充沛，将致癌依赖反转为致死弱点。</td>
        </tr>
        <tr>
          <td><strong>正常组织在体毒性</strong></td>
          <td>若靶蛋白具有维持正常造血、免疫或神经稳态的生理功能，不可逆的全身清除将诱发严重机制性毒性（如 BCL6 全身敲除小鼠死于多脏器炎症）。</td>
          <td><strong>由于仅借用微量分子且遵循“组合与门”（AND-Gate）特异性</strong>，在缺乏高丰度 BCL6 的正常组织中表现为惰性无毒，小鼠试验未见明显毒副反应。</td>
        </tr>
        <tr>
          <td><strong>生化作用时程</strong></td>
          <td>依赖泛素化级联、多聚泛素链延伸及蛋白酶体转运降解，通常需要数小时至十数小时才能见效。</td>
          <td><strong>光速级转录延伸</strong>：给药 <strong>15 分钟</strong> 内即观察到 RNA Pol II 跨过外显子-内含子暂停点进行转录延伸，2 小时即完成关键靶标表达重构。</td>
        </tr>
      </tbody>
    </table>

    <h3 class="subsection-heading">从“不可成药”到“功能劫持”：转录因子靶向的破局新思路</h3>
    <p>
      在所有人类恶性肿瘤的驱动驱动基因中，超过 70% 是转录因子或表观遗传重塑复合体（如 MYC、BCL6、STAT3、FOXM1、EWS-FLI1 等）。因为转录因子通常缺乏酶类深邃的疏水催化口袋，且依靠广泛而平坦的蛋白质-蛋白质相互作用（PPI）界面发挥作用，它们在过去半个世纪中一直被工业界视为<strong>“不可成药”（Undruggable）的绝壁</strong>。
    </p>
    <p>
      TCIP 技术的诞生彻底打破了这一桎梏：<strong>它不再要求小分子必须具备阻断庞大 PPI 界面的极高结合能，而仅仅需要一个小分子配体能够“搭上一只手”（微弱或非变构结合即可）</strong>。只要能把转录因子作为物理锚定点，TCIP 就能强行拖拽细胞内原本就存在的、极为强大的内源转录激活或表观重塑机器（如 BRD4、P-TEFb、BAF/SWI-SNF、p300/CBP、核受体等），将该位点的染色质景观与转录状态进行颠覆性逆转！
    </p>

    <div class="mechanism-card blue">
      <div class="mechanism-title">🚀 未来拓展地平线：TCIP 在生命科学与医学领域的广泛应用前景</div>
      <p style="font-size: 14.5px; color: #1e3a8a; line-height: 1.75;">
        在讨论部分的尾声，通讯作者 Crabtree 院士与 Gray 教授明确指出，TCIP 所代表的“转录与表观重构”概念绝不仅限于抗击淋巴瘤：<br>
        1. <strong>衰老细胞精准清除 (Senolytics)</strong>：衰老细胞往往依赖特定的抗凋亡网络维持长期存活并释放衰老相关分泌表型 (SASP)，TCIP 可用于精准劫持衰老特征性转录因子诱导衰老细胞自我清除；<br>
        2. <strong>单倍剂量不足 (Haploinsufficiency) 遗传病治疗</strong>：人类有上百种严重的罕见遗传病是由于单个等位基因突变失活导致表达量减半。TCIP 可设计为特异性结合残留完好的等位基因启动子，通过招募强效延伸因子，将其转录量精准提升 2 倍，恢复正常生理表型；<br>
        3. <strong>肿瘤新抗原原位激活与免疫治疗</strong>：通过 TCIP 重新开启在肿瘤中被表观遗传致密沉默的免疫原性逆转录病毒元件（HERVs）或新抗原，将“冷肿瘤”强行转化为“热肿瘤”；<br>
        4. <strong>合成生物学人工基因线路重编程</strong>：无需引入外源基因编辑工具，利用化学小分子在任意时空节点实现内源基因表达的即时开/关切换。
      </p>
    </div>
  </section>

  <!-- 实验方法全流程解析 (STAR Methods) -->
  <section class="card-section" id="methods">
    <h2 class="section-heading"><span class="sec-id">Methods</span>详尽实验方法全流程解析 (STAR Methods)</h2>

    <h3 class="subsection-heading">1. 细胞株培养与化学合成路线</h3>
    <p>
      <strong>细胞培养</strong>：KARPAS422、SUDHL4、OCI-LY1 等人源淋巴瘤细胞系在含 10% 胎牛血清（FBS）及双抗的 RPMI-1640 培养基中于 37°C、5% CO<sub>2</sub> 培养。原代人扁桃体成熟淋巴细胞取自扁桃体切除手术标本，经 Ficoll 密度梯度离心分离获得。<br>
      <strong>TCIP1 合成要点</strong>：以 (+)-JQ1 羧酸衍生物为起始物，经缩合反应偶联特制单 Boc 保护的聚乙二醇/叔胺连接臂，脱保护后与活化的 BI3812 衍生酸进行高效酰胺缩合，所得粗产物经反相制备型高相液相色谱（RP-HPLC，C18 柱）纯化，并通过高分辨质谱（HRMS）和 <sup>1</sup>H/<sup>13</sup>C 核磁共振（NMR）验证结构与纯度（纯度 > 98%）。
    </p>

    <h3 class="subsection-heading">2. 细胞活力、凋亡测定与流式细胞术</h3>
    <p>
      <strong>细胞活力</strong>：采用 CellTiter-Glo 荧光发光法，于 384 孔板中每孔接种 2,000 个细胞，加入梯度稀释化合物，处理 72 小时后加入检测试剂，酶标仪测定化学发光信号，采用 GraphPad Prism 进行非线性回归四参数拟合计算 \(EC_{50}\)。<br>
      <strong>细胞凋亡与周期分析</strong>：细胞经化合物处理特定时间后收集，以冷 PBS 洗涤，使用 FITC-Annexin V 和碘化丙啶（PI）进行双重染色，30 分钟内利用 BD LSRFortessa 流式细胞仪检测；周期分析使用无水乙醇固定后经 RNAase A 消化并进行 PI 染色分析。
    </p>

    <h3 class="subsection-heading">3. 体外生物物理测定：TR-FRET 与等温滴定量热 (ITC)</h3>
    <p>
      <strong>TR-FRET 测定体系</strong>：在 384 孔白色微孔板中构建 20 μL 反应体系，包含 50 nM 纯化 6xHis-BRD4(BD1)、50 nM FITC-BCL6(BTB) 以及 2 nM 铽螯合物标记抗 His 抗体（Tb-anti-His）。加入梯度稀释化合物后室温孵育 1 小时，使用 PerkinElmer EnVision 酶标仪检测供体（337 nm 激发，495 nm 发射）与受体（520 nm 发射）荧光比值（Em520/Em495）。<br>
      <strong>ITC 实验</strong>：使用 MicroCal PEAQ-ITC 量热仪，在 25°C 下将 150 μM BCL6(BTB) 逐步滴定进入含有 15 μM BRD4(BD1) 与 15 μM TCIP1 的样品池中，通过一阶结合模型拟合得出结合焓（\(\Delta H\)）、结合常数（\(K_d\)）及摩尔结合化学计量比（\(n\)）。
    </p>

    <h3 class="subsection-heading">4. 高通量表观组与转录组学：PRO-seq、RNA-seq 与 ChIP-seq</h3>
    <p>
      <strong>PRO-seq (精确核连缀测序)</strong>：按经典方案分离细胞核，在生物素标记的 NTPs 存在下进行极短时间的核连缀反应，利用抗生物素蛋白磁珠（Streptavidin Beads）精准富集处于转录延伸状态的初生新生 RNA，构建高通量文库，以此解析 RNA Pol II 瞬间的转录延伸速率。<br>
      <strong>ChIP-seq (染色质免疫共沉淀测序)</strong>：以 1% 甲醛室温交联 10 分钟，甘氨酸终止，裂解后利用超声破碎仪（Covaris）将染色质断裂至 200–500 bp 片段。分别加入高特异性抗体（抗 BCL6、抗 BRD4、抗 RNA Pol II、抗 Pol II Ser2P、抗 Pol II Ser5P、抗 CDK9、抗 H3K27ac）于 4°C 免疫共沉淀过夜。富集 DNA 经文库构建后于 Illumina NovaSeq 6000 平台进行双端测序；比对至 GRCh38 参考基因组，利用 MACS2 进行峰识别（Peak Calling），Deeptools 生成归一化 Bigwig 轨迹文件。
    </p>

    <h3 class="subsection-heading">5. 模式动物体内耐受性与药效学实验</h3>
    <p>
      8–10 周龄野生型雄性 C57BL/6 小鼠随机分组，每天腹腔注射给予 10 mg/kg TCIP1（溶于含 10% DMSO、40% PEG400、5% Tween-80、45% 生理盐水的给药载体）或对照溶剂，连续给药 5 天。每日监测小鼠体重、活动度和进食状态。末次给药 24 小时后眼眶取血分离血清进行 LC-MS/MS 药物浓度检测，分离主要内脏器官，部分组织用于石蜡包埋、切片与 H&E 染色进行组织毒理学盲检评估，部分脾脏组织提取总 RNA 进行高深度 Illumina 转录组测序分析。
    </p>
  </section>
'''
