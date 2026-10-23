# -*- coding: utf-8 -*-
"""
part4_results_3_5.py
Covers:
- Section 3: TCIP1 represses MYC and its targets (Figure 3, Extended Data Fig 6)
- Section 4: Mechanism of transcriptional activation & Rewiring BCL6 autoinhibitory circuit (Figure 4, Extended Data Figs 7, 8, 9)
- Section 5: Cell-type-specific activity of TCIP1 in vivo & Generality of TCIP strategy (Figure 5)
Includes complete translated text, rigorous biochemical interpretation,
embedded high-res figures with captions, and mechanistic breakdown callouts.
"""

RESULTS_3_5 = '''
  <!-- 第三部分：TCIP1 快速阻断致癌主驱动因子 MYC 及其下游转录程序 -->
  <section class="card-section" id="sec3">
    <h2 class="section-heading"><span class="sec-id">Results 3</span>TCIP1 快速下调原癌基因 MYC 及其下游致癌转录网络</h2>

    <p>
      在弥漫大 B 细胞淋巴瘤（DLBCL）的发生发展中，除了 BCL6，<strong>原癌基因 MYC</strong> 的异常高表达往往是驱动肿瘤细胞无限增殖、核糖体生物合成和代谢重编程的核心引擎；临床上伴随 <em>MYC</em> 与 <em>BCL6</em>（或 <em>BCL2</em>）重排的“双打击”（Double-hit）淋巴瘤预后极其凶险。
    </p>
    <p>
      令人惊喜的是，当研究团队对 TCIP1 处理后的 KARPAS422 细胞进行时间序列转录组测序（RNA-seq：1h、2h、4h）时，在表达受到最为剧烈下调的基因集之中，<strong>MYC 及其经典靶基因群赫然位列榜首</strong>！
    </p>

    <!-- 图 3 嵌入展示 -->
    <div class="figure-wrapper" id="fig3">
      <div class="figure-img-container" onclick="openLightbox('figures/fig3.png')">
        <img src="figures/fig3.png" alt="Figure 3: TCIP1 represses MYC and its oncogenic targets" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看原始图版 Figure 3</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">图 3 | TCIP1 在超低浓度下特异性下调原癌蛋白 MYC 及其致癌转录网络</strong>
        <p>
          <strong>a</strong>, KARPAS422 细胞在 10 nM TCIP1 处理 1、2、4 小时后的 RNA-seq 差异表达火山图，清晰显示促凋亡基因的迅猛上调与 MYC 靶基因的进行性下调。<br>
          <strong>b</strong>, 基因集富集分析 (GSEA) 显示，Hallmark MYC Targets V1/V2 基因集呈现极具统计学意义的负向富集（显著下调，\(NES = -2.85, P < 10^{-10}\)）。<br>
          <strong>c</strong>, 整合分析人类血液恶性肿瘤超过 4,500 套转录因子 ChIP–seq 数据集，发现被 TCIP1 显著下调的前 100 个核心基因的启动子区域高度富集内源 MYC 的结合峰，证明下调具有高度转录调控直接性。<br>
          <strong>d, e</strong>, Western Blot 检测 MYC 蛋白动态响应：在低至 <strong>< 1 nM TCIP1</strong> 的超微量浓度下，给药仅仅 <strong>2 小时</strong> 内 MYC 蛋白即被剧烈清除下调（下降 > 80%），4 小时几乎完全消失；展现出极快的动力学响应时程。<br>
          <strong>f</strong>, 阴性对照分子 Neg1 和 Neg2 在相同浓度梯度下对 MYC 蛋白水平完全没有下调作用，证实单纯结合一端蛋白无法关闭 MYC。<br>
          <strong>g</strong>, 阻断三元复合物可化学逆转 MYC 下调：在 10 nM TCIP1 恒定浓度下逐渐滴定游离 BCL6 抑制剂 BI3812，不仅以剂量依赖方式恢复了 MYC 蛋白的表达，而且逆转了促凋亡因子 FOXO3 与周期抑制因子 p21 的上调，有力证实无论是“促凋亡基因激活”还是“原癌基因 MYC 沉默”，本质上皆受控于 BRD4–TCIP1–BCL6 三元复合物的形成。
        </p>
      </div>
    </div>

    <div class="mechanism-card blue">
      <div class="mechanism-title">⚡ 为什么 TCIP1 能够在 < 1 nM 瞬间关闭 MYC？（与传统 JQ1 的量级差异）</div>
      <p style="font-size: 14.5px; color: #1e3a8a; line-height: 1.75;">
        药理学界的同行熟知，传统的游离 BET 抑制剂 <strong>(+)-JQ1</strong> 确实也能下调 MYC，但其有效浓度通常需要 <strong>500 nM 以上</strong>，且容易因补偿性转录重启而耐药。<br>
        而 <strong>TCIP1 仅需 < 1 nM 即可在 2 小时内关闭 MYC</strong>，效能高出 JQ1 数百倍！深入的染色质免疫共沉淀（ChIP-seq）解析揭示了这一奇迹的本质：DLBCL 细胞中的 <em>MYC</em> 基因本身受到一个巨大的“超级增强子”（Super-Enhancer）驱动，而该区域对 BRD4 分子具有极高的依存度。TCIP1 将细胞核内一部分游离及局部 BRD4 迅速拉拽、重新分配到遍布全基因组的 BCL6 阻遏位点上，引发超级增强子微环境中 BRD4 关键延伸池的局部缺相，以“四两拨千斤”的极低化学剂量实现了对 MYC 表达的毁灭性切断。
      </p>
    </div>

    <!-- 扩展数据图 6 嵌入展示 -->
    <div class="figure-wrapper" id="ed-fig6">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig6.png')">
        <img src="figures/ed_fig6.png" alt="Extended Data Figure 6: Comprehensive RNA-seq and GSEA pathway analysis" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 6</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 6 (Extended Data Fig. 6) | 深度转录组测序、火山图分布与通路富集热图</strong>
        <p>
          系统展示了 10 nM TCIP1 在 1h、2h、4h 时间节点下数千个基因的表达变化轨迹。除 MYC 靶基因受抑外，核糖体生物合成、E2F 靶基因以及氧化磷酸化通路亦同步受到抑制，促使癌细胞全面丧失增殖动力并迅速滑向不可逆的代谢崩溃。
        </p>
      </div>
    </div>
  </section>

  <!-- 第四部分：转录激活的分子机制与颠覆性 BCL6 自负反馈重构 -->
  <section class="card-section" id="sec4">
    <h2 class="section-heading"><span class="sec-id">Results 4</span>转录延伸激活机制破译：颠覆 BCL6 自身自抑回路，构建“正反馈自杀循环”</h2>

    <p>
      常规分子生物学认知中，BCL6 是一种根深蒂固的<strong>转录抑制因子（Transcriptional Repressor）</strong>。那么，TCIP1 究竟是通过怎样的物理表观机制，在短时间内使受抑靶基因实现爆发式转录激活的？
    </p>

    <h3 class="subsection-heading">1. 靶基因直接性鉴定与 RNA Pol II 暂停释放 (Pause-Release)</h3>
    <p>
      研究团队通过分析 TCIP1 给药 1、2、4 小时迅速诱导上调的约 140 个核心基因，发现其中涵盖了经典的 BCL6 抑制性死亡调控因子：<strong>BCL2L11 (BIM)、PMAIP1 (NOXA)、FOXO3、CDKN1A (p21) 以及 BCL6 自身</strong>。
    </p>
    <p>
      交叉对比已发表的 DLBCL 细胞系 BCL6 ChIP–seq 发现：<strong>超过 55% 的早期上调基因在其转录起始位点（TSS）上游 1 kb 范围内具备极高信噪比的内源 BCL6 结合峰</strong>（见图 4a–c）。这确凿证明这些基因是 TCIP1 直接结合、原位激活的原发靶标。
    </p>

    <!-- 图 4 嵌入展示 -->
    <div class="figure-wrapper" id="fig4">
      <div class="figure-img-container" onclick="openLightbox('figures/fig4.png')">
        <img src="figures/fig4.png" alt="Figure 4: Transcriptional elongation mechanism and rewiring BCL6 autoinhibitory circuit" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看原始图版 Figure 4</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">图 4 | TCIP1 招募 BRD4 介导 RNA Pol II 延伸释放并颠覆 BCL6 自抑制回路</strong>
        <p>
          <strong>a</strong>, TCIP1 直接活化的前列靶基因热图，清晰呈现 <em>BCL2L11</em> (BIM)、<em>PMAIP1</em> (NOXA)、<em>FOXO3</em> 及 <em>BCL6</em> 在 1h、2h、4h 呈阶梯式爆发活化。<br>
          <strong>b</strong>, 活性分子 TCIP1 与阴性对照分子 Neg1、Neg2 在诱导靶基因转录方面的定量对比。<br>
          <strong>c</strong>, 基于 4,500 套血液肿瘤转录因子 ChIP–seq 数据的全景分析：TCIP1 上调基因的启动子被证实特异且极度富集内源 BCL6 的结合，而非其他无关因子。<br>
          <strong>d</strong>, 全基因组 ChIP–seq 分析显示，10 nM TCIP1 处理 1 小时后，在所有内源 BCL6 结合峰位点处，<strong>BRD4 的局部富集量增加了约 50%</strong>（1.5 倍）。<br>
          <strong>e, f</strong>, 染色质活性标记与增强子受载监测：在靶基因启动子区，活性染色质标记 H3K27ac 仅发生极微弱改变；在全基因组超级增强子区域，BRD4 的总负荷量仅仅微弱降低了 <strong>10%</strong> 左右，表明 TCIP1 并非通过全面瓦解增强子发挥作用，而是以微小代价“借调”（Borrow）极少量 BRD4 即可完成对促凋亡靶标的高效激活，完全符合“功能获得型”（GoF）机制。<br>
          <strong>g, h</strong>, 促凋亡基因 <em>BCL2L11</em> (BIM) 与 <em>BCL6</em> 基因位点的 RNA Pol II 结合轨迹：PRO-seq 与 ChIP-seq 显示，在给药仅仅 <strong>15 分钟</strong> 时，RNA Pol II 即迅速由暂停状态释放，沿着外显子-内含子接头向基因内部展开高速转录延伸，至 1–4 小时形成贯穿整个基因主体的饱和延伸轨迹。<br>
          <strong>i, j</strong>, RT-qPCR 与可变剪接分析：TCIP1 诱导 BCL6 mRNA 的长亚型（包含第 7 外显子）爆发式积累。<br>
          <strong>k</strong>, Western Blot 检测 BCL6 蛋白水平：在两株不同的 DLBCL 细胞中，BCL6 蛋白自身随 TCIP1 给药呈现显著的剂量依赖性暴增（亦呈现高浓度钩状效应）。<br>
          <strong>l, m</strong>, 机制阻断验证：加入超低纳摩尔浓度的 CDK9 抑制剂 <strong>NVP2</strong>（阻断 RNA Pol II Ser2 磷酸化）可完全阻断 BCL6 自身的诱导表达；逐渐滴定 BCL6 抑制剂 BI3812 亦可逆转 BCL6 上调，证明 BCL6 自身诱导表达完全依赖三元复合物驱动的转录延伸。
        </p>
      </div>
    </div>

    <div class="mechanism-card purple">
      <div class="mechanism-title">🔄 颠覆性创见：BCL6 负向自抑制回路被反转为“正反馈自杀循环”</div>
      <p style="font-size: 14.5px; color: #44337a; line-height: 1.75;">
        这是本篇 <em>Nature</em> 论文在生命调控逻辑上最叹为观止的理论突破！<br>
        在正常生理状态下，<strong>BCL6 基因对其自身具有极其严格的“负向自我抑制”（Negative Autoregulation）</strong>——BCL6 蛋白会结合在自身基因的<strong>第一个内含子（Intron 1）</strong>内的特异基序上，招募抑制复合物防止自身过量表达（在 DLBCL 淋巴瘤中，该内含子抑制位点常常发生突变或缺失，导致 BCL6 脱离抑制）。<br>
        而 TCIP1 的引入，<strong>奇迹般地把这个负反馈刹车改造成了强大的正反馈油门（Positive Feedback Loop）</strong>：<br>
        ① TCIP1 结合在结合于 <em>BCL6</em> 内含子上的内源 BCL6 蛋白上；<br>
        ② 招募 BRD4 及其相伴随的 P-TEFb (CDK9)，诱导 RNA Pol II 跨过内含子障碍进行强力转录延伸；<br>
        ③ 结果是：<strong>细胞内 BCL6 的 mRNA 和蛋白水平被迅速放大数十倍</strong>！<br>
        ④ <strong>自杀放大效应</strong>：新合成的大量 BCL6 蛋白进一步结合到细胞全基因组范围内的促凋亡基因启动子上，进而为环境中的 TCIP1 和 BRD4 提供了成倍增长的“锚定发射台”，驱动 <em>BIM</em> 与 <em>NOXA</em> 发生核爆般的转录风暴，最终在极低药物暴露下将恶性淋巴瘤细胞不可逆地送入死亡深渊（详见 Extended Data Fig. 9d 模型）！
      </p>
    </div>

    <!-- 扩展数据图 7, 8, 9 嵌入展示 -->
    <div class="figure-wrapper" id="ed-fig7">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig7.png')">
        <img src="figures/ed_fig7.png" alt="Extended Data Figure 7: Upregulation kinetics of pro-apoptotic genes" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 7</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 7 (Extended Data Fig. 7) | 促凋亡基因群 (BIM, NOXA, FOXO3, p21) 的转录激活时程动力学</strong>
        <p>
          qPCR 与微阵列转录检测确认，促凋亡基因的 mRNA 积累在 1 小时即达到基线的 3–8 倍，远早于细胞 DNA 发生断裂的物理时间，确证细胞凋亡是直接由初级转录激活事件引发，而非细胞死亡后释放的继发应激假象。
        </p>
      </div>
    </div>

    <div class="figure-wrapper" id="ed-fig8">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig8.png')">
        <img src="figures/ed_fig8.png" alt="Extended Data Figure 8: ChIP-seq coverage across active enhancers and promoters" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 8</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 8 (Extended Data Fig. 8) | 全基因组超级增强子 (Super-Enhancer) 与启动子 H3K27ac/BRD4 空间图谱</strong>
        <p>
          在全基因组鉴定的 51,678 个 H3K27ac 共有结合峰中，处理 2 小时后仅有 126 个峰显著增加、70 个峰轻微减少，全基因组表观遗传结构未遭破坏；超级增强子（如 OCA-B）处的 BRD4 仅轻微减损 10%，证实 TCIP1 具有近乎手术刀级的基因组作用精准度。
        </p>
      </div>
    </div>

    <div class="figure-wrapper" id="ed-fig9">
      <div class="figure-img-container" onclick="openLightbox('figures/ed_fig9.png')">
        <img src="figures/ed_fig9.png" alt="Extended Data Figure 9: Schematic model of rewiring BCL6 autoinhibitory circuit" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看 Extended Data Figure 9</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">附图 9 (Extended Data Fig. 9) | BCL6 自负反馈回路逆转为“正反馈自杀循环”的生化模型</strong>
        <p>
          清晰梳理了传统状态下 BCL6-Intron1 自抑制的抑制闭环，以及 TCIP1 介入后如何颠覆为“转录诱导 -> BCL6 蛋白增加 -> 更多促凋亡启动子占据 -> 凋亡风暴”的雪崩式正反馈放大网络。
        </p>
      </div>
    </div>
  </section>

  <!-- 第五部分：体内药代动力学、靶向耐受性与 TCIP 策略的普适性验证 -->
  <section class="card-section" id="sec5">
    <h2 class="section-heading"><span class="sec-id">Results 5</span>体内靶向安全性验证与 TCIP 概念模块化普适性 (ER–TCIP2) 拓展</h2>

    <p>
      传统的 BCL6 基因完全敲除（Knockout）小鼠会在出生后数周内因发生剧烈的多器官炎症与自身免疫衰竭而致命，因为 BCL6 在巨噬细胞、T 滤泡辅助细胞（Tfh）中承担着关键的免疫耐受刹车功能。这使得工业界长期对“强力靶向 BCL6”在体内的安全性心存疑虑。<br>
      然而，由于 TCIP1 采用的是<strong>功能获得型（GoF）催化机制</strong>，它在体内的有效工作浓度仅需占据极小比例（约 10%–15%）的 BCL6 蛋白分子，绝不导致全身生理性 BCL6 的全面耗竭。为了检验这一预测，研究团队在野生型小鼠体内进行了严格的药代动力学（PK）、药效学（PD）与组织病理学评估。
    </p>

    <!-- 图 5 嵌入展示 -->
    <div class="figure-wrapper" id="fig5">
      <div class="figure-img-container" onclick="openLightbox('figures/fig5.png')">
        <img src="figures/fig5.png" alt="Figure 5: In vivo tolerability, mouse PK/PD, and generality with ER-TCIP2" class="figure-img">
        <div class="zoom-hint">🔍 点击图片可全屏高清放大查看原始图版 Figure 5</div>
      </div>
      <div class="figure-caption">
        <strong class="fig-title">图 5 | TCIP1 在野生型小鼠体内的良好耐受性与 TCIP2 (ER–BCL6) 模块化拓展</strong>
        <p>
          <strong>a–c</strong>, C57BL/6 小鼠连续 5 天腹腔注射 10 mg/kg TCIP1 后的药代动力学与组织分布：血清稳态浓度达到 <strong>400–1,600 nM</strong>（高出体外杀伤有效浓度百倍以上），在脾脏、肝脏、肾脏、心脏和大脑中均检测到稳定的药物暴露。<br>
          <strong>d</strong>, 靶器官脾脏转录组 RNA-seq：TCIP1 在脾脏内诱导了显著的靶向转录组重塑，包括 <em>FOXO3</em> 等已知 BCL6 靶标的显著上调，确证药物在体内有效实现了靶标结合与转录诱导。<br>
          <strong>e, f</strong>, 在体耐受性与病理切片检查：经 Stanford 资深神经病理学家 Hannes Vogel 盲检，接受大剂量 TCIP1 连续治疗的小鼠体重无统计学下降，食欲和行为完全正常；心脏、肺、肝、脾、肾等重要器官的 H&E 染色未见任何组织坏死、炎性细胞浸润或异常凋亡损伤，展现出令人惊叹的体内安全窗口！<br>
          <strong>g, h</strong>, 人源正常原代细胞选择性测试：在健康人扁桃体成熟淋巴细胞（\(EC_{50} \\approx 210\\text{ nM}\)）与原代成纤维细胞（\(EC_{50} \\approx 470\\text{ nM}\)）中，TCIP1 的半数致死浓度较 DLBCL 肿瘤细胞高出 <strong>200 到 400 倍</strong>，证实其对恶性高表达细胞的极强专一性。<br>
          <strong>i</strong>, TCIP 策略的模块化普适性设想：利用双功能分子招募另一种完全不同类型的转录激活蛋白——核激素受体<strong>雌激素受体 (ER)</strong>，与 BCL6 发生化学邻近诱导。<br>
          <strong>j</strong>, 合成的 ER–BCL6 TCIP 代表化合物 <strong>TCIP2</strong> 的化学结构，由天然雌酮（Oestrone）配体经化学臂连接 BCL6(BTB) 结合剂 BI3812。<br>
          <strong>k</strong>, TCIP2 对同时高表达 ER 与 BCL6 的 DLBCL 细胞展现出强劲的抗增殖杀伤活性（<strong>\(EC_{50} = 355\\text{ nM}\)</strong>）。<br>
          <strong>l</strong>, 阴性对照验证：在仅表达 ER 但缺乏 BCL6 的乳腺癌细胞系（HCC1428 等）中，TCIP2 不仅不产生毒性，反而由于雌酮成分轻微促进细胞增殖；在 ER 与 BCL6 均为阴性的三阴性乳腺癌（TNBC）中则完全无活性；完美证明只要细胞不同时具备被连接的两种靶标，TCIP 即具备内在的惰性安全属性！
        </p>
      </div>
    </div>

    <div class="mechanism-card green">
      <div class="mechanism-title">💡 概念升华：TCIP2 证实“组合特异性”是转录邻近疗法的天然安全防火墙</div>
      <p style="font-size: 14.5px; color: #22543d; line-height: 1.75;">
        TCIP2 的成功合成与功能验证具有极高的化学生物学理论价值：<br>
        1. <strong>即插即用（Plug-and-Play）模块化</strong>：证明 TCIP 并非仅适用于 BRD4，任何能够在特定基因位点激活转录延伸的天然转录因子（如核受体、辅激活物）均可作为供体元件；<br>
        2. <strong>真核转录的“与门”（AND-Gate）逻辑</strong>：只有在同时满足“靶向致癌因子高表达”（如 BCL6）与“激活因子表达”（如 BRD4 或 ER）的双阳性细胞中，TCIP 才能组装成完整的三元激活机器；只要缺失其中任一元件，该分子就蜕化为无毒的二元惰性配体。这种内在的“组合特异性”构成了 TCIP 区别于所有传统细胞毒化疗药和泛靶向抑制剂的终极安全壁垒！
      </p>
    </div>
  </section>
'''
