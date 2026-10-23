# -*- coding: utf-8 -*-
"""
part3_results_1_2.py
Covers:
- Section 1: TCIP1 selectively kills DLBCL cells (Figure 1, Extended Data Figs 1, 3)
- Section 2: Cell killing requires a ternary complex (Figure 2, Extended Data Figs 2, 4, 5)
Includes complete translated text, rigorous biochemical interpretation,
embedded high-res figures with captions, and mechanistic breakdown callouts.
"""

RESULTS_1_2 = '''
  <!-- 第一部分：TCIP1 选择性杀伤 DLBCL 细胞 -->
  <section class="card-section" id="sec1">
    <h2 class="section-heading"><span class="sec-id">Results 1</span>TCIP1 的理性设计与对弥漫大 B 细胞淋巴瘤 (DLBCL) 的高效选择性杀伤</h2>

    <p>
      为了验证“重构致癌驱动转录因子以诱导肿瘤细胞凋亡”的假说，研究团队将首个攻坚目标锁定在弥漫性大 B 细胞淋巴瘤（DLBCL）。在 DLBCL 中，癌细胞普遍依赖原癌蛋白 <strong>BCL6</strong> 的异常过度表达来逃避死亡。BCL6 利用其 N 端的 <strong>BTB/POZ 结构域</strong>，形成一个专一的侧向疏水沟槽，强力招募核受体辅阻遏蛋白 <strong>NCOR1/2 (SMRT) 和 BCOR</strong> 等多亚基共抑制复合体，从而在表观遗传水平上致密沉默包括促凋亡基因、细胞周期阻滞基因（如 <em>TP53</em>、<em>CDKN1A</em>/p21、<em>PMAIP1</em>/NOXA）在内的关键靶点。
    </p>

    <div class="mechanism-card blue">
      <div class="mechanism-title">🧪 TCIP1 的分子构效拼装逻辑 (Molecular Engineering Rationale)</div>
      <p style="font-size: 14.5px; color: #1e3a8a; line-height: 1.75;">
        单纯利用小分子占据 BCL6(BTB) 沟槽（如 BI3812）仅能“松开刹车”（Derepression），并不能为启动子提供强效的主动转录激活力。为了克服这一瓶颈，研究团队利用化学生物学“双功能拼装”策略：<br>
        1. <strong>靶向锚定端</strong>：选用针对 BCL6 BTB 结构域的高亲和力配体 <strong>BI3812</strong>（\(K_d \approx 19\\text{ nM}\)），占据辅抑制物结合沟槽，排斥 NCOR/BCOR/SMRT；<br>
        2. <strong>转录激活招募端</strong>：选用经典的 BET 家族溴结构域（Bromodomain）抑制剂 <strong>(+)-JQ1</strong>，其以纳摩尔级亲和力等同结合 <strong>BRD4</strong> 的两个溴结构域（BD1/BD2），并能同时招募 BRD2 与 BRD3；<br>
        3. <strong>化学连接臂 (Linker) 优化</strong>：经过对聚乙二醇（PEG）链与叔胺（Tertiary Amine）连接臂在碳原子长度（\(n = 5 \\sim 11\)）与空间刚柔度的系统性阵列化筛选（详见 Extended Data Fig. 3，JWZ 系列与 XFL 系列），最终确立了具备最佳空间几何匹配与构象互补性的冠军分子——<strong>TCIP1</strong>！
      </p>
    </div>

    <!-- 图 1 嵌入展示 -->
    <div class="figure-wrapper" id="fig1">
      <div class="figure-img-container" onclick="openLightbox('figures/fig1.png')">
        <img src="figures/fig1.png" alt="Figure 1: Production of TCIPs and selective killing of DLBCL cells" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看原始图版</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">图 1 | TCIP 的分子设计理念、化学结构及对 DLBCL 细胞的高效选择性杀伤</strong>
        <p>
          <strong>a</strong>, TCIP 的通用重构模式示意图：内源性靶基因在基态下处于抑制或静默状态，通过异双功能小分子将靶向转录因子 A（如致癌抑制因子）与转录因子 B（如转录延伸机器）物理拉近，使表观遗传沉默转变为主动转录诱导。<br>
          <strong>b</strong>, 针对淋巴瘤设计的特异性 BCL6–BRD4 TCIP 工作假说：利用双功能小分子将转录激活因子/致癌驱动蛋白 BRD4 招募至结合在死亡基因启动子上的 BCL6 阻遏蛋白旁，从而解除表观遗传抑制并强制诱导由 BCL6 锚定位点驱动的死亡基因转录。<br>
          <strong>c</strong>, 活性最强的 BCL6–BRD4 异双功能分子 <strong>TCIP1</strong> 及其阴性对照分子 <strong>Neg1</strong>（BRD4 结合缺陷）与 <strong>Neg2</strong>（BCL6 结合缺陷）的精确化学结构。<br>
          <strong>d</strong>, TCIP1 对化疗多药耐药且伴随 <em>TP53</em> 双等位基因失活的 DLBCL 细胞系 KARPAS422 的杀伤曲线，给药 72 小时后检测细胞活力，其 <strong>\(EC_{50} \\approx 1.3\\text{ nM}\)</strong>；相比之下，阴性对照分子 Neg1 与 Neg2 或单一靶头抑制剂组合即使浓度高出 100–1,000 倍亦无法产生等效杀伤。<br>
          <strong>e</strong>, 利用含有 8 个高亲和力 BCL6 结合基序与侧翼 10 bp 序列驱动 minP-eGFP 的慢病毒报告系统在 KARPAS422 中检测 TCIP1 的原位转录激活能力。TCIP1 在给药 8 小时即呈现出鲜明的剂量依赖性 eGFP 荧光诱导（\(EC_{50} \\approx 5\\text{ nM}\)），且在高浓度下出现经典的双功能分子“钩状效应”（Hook effect）；Neg1 和 Neg2 均无激活效果。<br>
          <strong>f</strong>, TCIP1 与传统靶向蛋白降解剂（PROTAC）对细胞活力的对比：BRD4 降解剂 <strong>dBET1</strong>（\(EC_{50} \\approx 489\\text{ nM}\)）与 BCL6 降解剂 <strong>BI3802</strong>（\(EC_{50} > 10\\,\\mu\\text{M}\)）的杀伤效能较 TCIP1 弱 <strong>200 至 10,000 倍</strong>，表明单纯消耗降解上述蛋白绝非 TCIP1 强效杀伤的主导机制。
        </p>
      </div>
    </div>

    <h3 class="subsection-heading">深度实验数据剖析：1.3 nM 杀伤效能背后的“非对称优势”</h3>
    <p>
      为了验证 TCIP1 是否具备对致癌靶点的专一杀伤，研究团队首先选择了极具临床代表性的 DLBCL 细胞系 <strong>KARPAS422</strong>。该细胞系不仅内源性 BCL6 表达量极高，而且存在 <em>TP53</em> 双等位失活突变，临床上对常规 CHOP 化疗极其耐药。
    </p>
    <p>
      实验结果显示，TCIP1 杀伤 KARPAS422 的 <strong>\(EC_{50}\) 达到惊人的 1.3 nM</strong>！而当研究人员将未连接的 JQ1（BRD4 抑制剂）与 BI3812（BCL6 抑制剂）进行等摩尔物理混合共同加入细胞培养基时，细胞杀伤效率较 TCIP1 下降了整整 <strong>100 到 1,000 倍</strong>（详见 Extended Data Fig. 1a）。这从根本上排除了“TCIP1 仅仅是作为前药在胞内释放两种抑制剂产生协同作用”的可能！
    </p>

    <!-- 扩展数据图 1 & 3 嵌入展示 -->
    <div class="figure-wrapper" id="ed-fig1">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig1.png')">
        <img src="figures/ed_fig1.png" alt="Extended Data Figure 1: PRISM cancer cell screen and specificity" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 1</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 1 (Extended Data Fig. 1) | 906 株人源肿瘤细胞系 PRISM 大规模无偏筛查与 BCL6 表达依赖性</strong>
        <p>
          <strong>a</strong>, JQ1 与 BI3812 游离单药联合处理与 TCIP1 的细胞杀伤曲线对比，证实物理共价连接引起的分子邻近是纳摩尔杀伤的前提。<br>
          <strong>b</strong>, 在包含 14 株血液恶性肿瘤细胞系（DLBCL、伯基特淋巴瘤、白血病等）的测试板中，TCIP1 的敏感性（\(EC_{50}\)）与细胞内 BCL6 的基础表达量呈高度正相关；缺乏 BCL6 表达的细胞株（如 OCILY19）对 TCIP1 表现为耐受。<br>
          <strong>c</strong>, 杀伤效果完全独立于 TP53 状态及内源抗凋亡蛋白 BCL2 的表达丰度。<br>
          <strong>d</strong>, Broad 研究所 PRISM 平台 906 株肿瘤细胞系的大规模活性扫描：只有来源于造血/淋巴系统且高表达 BCL6 的恶性细胞系对 TCIP1 展现出极高敏感性，实体瘤细胞系普遍不敏感，凸显极高组织特异性。
        </p>
      </div>
    </div>

    <div class="figure-wrapper" id="ed-fig3">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig3.png')">
        <img src="figures/ed_fig3.png" alt="Extended Data Figure 3: Linker optimization and chemical structure library" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 3</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 3 (Extended Data Fig. 3) | TCIP 化合物库合成路线与连接臂结构-活性关系 (SAR)</strong>
        <p>
          系统评估了聚乙二醇（PEG）链长（n=5 到 11）、刚性烷基链、哌嗪与叔胺修饰对二元蛋白间距和三元复合物稳定性的影响。实验证实，过短或过长的连接臂均会导致三元复合物空间张力过大或旋转熵损增加，唯有 TCIP1 的特定构象能实现最理想的热力学校正与促凋亡延伸启动。
        </p>
      </div>
    </div>
  </section>

  <!-- 第二部分：三元复合物的形成是细胞致死的绝对必需条件 -->
  <section class="card-section" id="sec2">
    <h2 class="section-heading"><span class="sec-id">Results 2</span>三元复合物 (BRD4–TCIP1–BCL6) 是介导细胞致死的生物活性功能实体</h2>

    <p>
      TCIP1 之所以能展现出超越传统降解剂 1,000 倍以上的杀伤效能，其核心科学机制在于它催化了 <strong>BRD4–TCIP1–BCL6</strong> 异源三元复合物的形成。为了在活细胞及分子生物物理水平严谨证实三元复合物的决定性地位，研究团队开展了经典的<strong>“化学竞争挽救实验”（Chemical Rescue）</strong>与<strong>“时间分辨荧光共振能量转移”（TR-FRET）</strong>测定。
    </p>

    <!-- 图 2 嵌入展示 -->
    <div class="figure-wrapper" id="fig2">
      <div class="figure-img-container" onclick="openLightbox('figures/fig2.png')">
        <img src="figures/fig2.png" alt="Figure 2: Ternary complex formation is required for cell killing" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看原始图版 Figure 2</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">图 2 | 化学挽救实验与体外生物物理表征证实三元复合物的形成是细胞死亡的前提</strong>
        <p>
          <strong>a, b</strong>, 化学竞争挽救实验设计与实测结果：在恒定致死剂量 TCIP1（使 50%–95% 细胞致死）存在下，逐渐滴定过量的游离 <strong>JQ1</strong>（竞争 BRD4 结合端，图 a）或游离 <strong>BI3812</strong>（竞争 BCL6 结合端，图 b）。结果表明，任何一端的游离单配体均能完全阻断 TCIP1 对 KARPAS422 细胞的致死效应，直接证实致死表型绝非单靶点抑制引起，而是依赖两端同时结合形成的功能性三元复合物。<br>
          <strong>c</strong>, 基于 TR-FRET 的三元复合物溶液结合测定原理：将 FITC 荧光基团共价标记于 BCL6 的 BTB 结构域，将 Terbium (Tb) 螯合物标记于抗 His 抗体并结合至带有 6xHis 标签的 BRD4(BD1) 结构域。当 TCIP1 介导两蛋白分子紧密结合时，发生高效 FRET 能量转移。<br>
          <strong>d</strong>, 库中不同连接臂 TCIP 衍生物在 TR-FRET 中的三元复合物信号强度与浓度曲线，TCIP1 呈现极高亲和力与最强能量转移效率。<br>
          <strong>e</strong>, 等温滴定量热法 (ITC) 结合常数热力学测定：在饱和 BRD4–TCIP1 二元复合物中滴定 BCL6(BTB)，测得三元复合物的表观结合常数 <strong>\(K_d = 340 \\pm 108\\text{ nM}\)</strong>，且呈现显著放热峰（\(\\Delta H = -5,304\\text{ kcal/mol}\)）；而游离 TCIP1 与 BCL6 之间的单纯二元结合弱于 1 mM，凸显出三元组装过程中的<strong>协同诱导契合效应（Cooperativity）</strong>。
        </p>
      </div>
    </div>

    <div class="mechanism-card green">
      <div class="mechanism-title">📐 双相药理学特征：双向化学挽救与经典的“钩状效应”</div>
      <p style="font-size: 14.5px; color: #22543d; line-height: 1.75;">
        在化学生物学中，由异双功能小分子诱导的三元复合物普遍遵循质量作用定律所决定的<strong>双相剂量-反应关系（Biphasic Dose-Response）</strong>：<br>
        1. <strong>在纳摩尔最佳浓度区间（1–100 nM）</strong>：单个 TCIP1 分子能够同时捕获一个 BCL6 分子和一个 BRD4 分子，形成催化活性最强的三元复合物，强力启动转录延伸；<br>
        2. <strong>在微摩尔过饱和浓度下（> 1 μM）</strong>：游离的 TCIP1 会分别过度饱和 BCL6 和 BRD4 的结合口袋，形成各自独立的二元非活性复合物（TCIP1–BCL6 和 TCIP1–BRD4），由于二者相互竞争，三元复合物数量反向骤降，导致报告基因激活信号减弱——这就是实验中观察到的<strong>“钩状效应”（Hook Effect）</strong>！这一经典的生物物理学现象完美佐证了 TCIP 并非毒性小分子，其活性严格受控于物理邻近规律。
      </p>
    </div>

    <!-- 扩展数据图 2, 4, 5 嵌入展示 -->
    <div class="figure-wrapper" id="ed-fig2">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig2.png')">
        <img src="figures/ed_fig2.png" alt="Extended Data Figure 2: Chemical rescue across DLBCL panel" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 2</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 2 (Extended Data Fig. 2) | 多株 DLBCL 细胞中的化学挽救及阴性对照特异性验证</strong>
        <p>
          在 SUDHL4、HBL1 等多株高表达 BCL6 的 DLBCL 系中，过量 JQ1 或 BI3812 均能以剂量依赖方式拯救细胞存活；但在原本缺乏 BCL6 的阴性对照细胞系中，TCIP1 仅表现出与游离 JQ1 等同的微弱抑制，且无法被 BI3812 挽救，证实 TCIP1 的细胞杀伤具有绝对的靶向特异性。
        </p>
      </div>
    </div>

    <div class="figure-wrapper" id="ed-fig4">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig4.png')">
        <img src="figures/ed_fig4.png" alt="Extended Data Figure 4: In vitro TR-FRET and ITC kinetics" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 4</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 4 (Extended Data Fig. 4) | 体外 TR-FRET 与 ITC 热力学结合动力学全面解析</strong>
        <p>
          详细展示了 TCIP1 与阴性对照分子在不同浓度梯度下的荧光能量转移曲线、等温滴定量热曲线及结合动力学拟合参数，证实 TCIP1 促成了高亲和力、长停留时间的稳定异源三元超分子复合物。
        </p>
      </div>
    </div>

    <div class="figure-wrapper" id="ed-fig5">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig5.png')">
        <img src="figures/ed_fig5.png" alt="Extended Data Figure 5: Apoptosis kinetics and cell cycle arrest" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 5</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 5 (Extended Data Fig. 5) | 细胞周期阻滞与快速程序性细胞凋亡 (Apoptosis) 发生时程</strong>
        <p>
          流式细胞术 Annexin V / PI 双染分析显示，TCIP1 处理 24–48 小时后，KARPAS422 细胞中早期与晚期凋亡细胞比例出现爆发式递增（凋亡率超 80%），伴随显著的 G0/G1 期周期停滞；Western Blot 显示 PARP 剪切体与活化 Caspase-3 剧烈上调，证实其引发的是典型的线粒体途径程序性细胞自杀。
        </p>
      </div>
    </div>
  </section>
'''
