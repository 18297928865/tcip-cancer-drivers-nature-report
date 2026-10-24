# -*- coding: utf-8 -*-
"""
Part 3: Results Section 2 & Figure 2
Cell killing requires a ternary complex
Verbatim translation, figure insertion, and academic terminology notes.
"""

PART3_DATA = {
    "section_title_en": "Cell killing requires a ternary complex",
    "section_title_zh": "细胞杀伤效应依赖于三元复合物 (Ternary Complex) 的形成",
    "paragraphs": [
        {
            "en": "The 1,000-fold increase in potency of TCIP1 over BRD4 or BCL6 degradation suggested the formation of a gain-of-function ternary complex between BRD4, BCL6 and TCIP1. We carried out chemical rescue experiments in which we titrated increasing concentrations of either JQ1 or BI3812 to multiple DLBCL cell lines, against constant concentrations of TCIP1 that kill 50–95% of cells within 72 h. JQ1 or BI3812 prevented death by TCIP1, indicating that both the BRD4-binding and the BCL6-binding side of TCIP1 are essential for effective killing (Fig. 2a,b). Examination of other DLBCL lines indicated that death of cell lines with little or no BCL6 could not be rescued (Extended Data Fig. 2a–c), and that in cell lines with low levels of BCL6, the potency of TCIP1 was comparable with Neg2, suggesting that the effects of TCIP1 in lines without BCL6 are due to simple BRD4 inhibition (Extended Data Fig. 2d,e).",
            "zh": "相较于单纯降解BRD4或BCL6，TCIP1展现出高达1000倍的杀伤效力提升，这强烈提示在BRD4、BCL6与TCIP1之间形成了一种具有功能获得性 (gain-of-function) 的三元复合物 (ternary complex)。我们开展了化学救援实验 (chemical rescue experiments)：在多个DLBCL细胞系中，我们维持能够在72小时内杀灭50–95%细胞的恒定浓度TCIP1，同时滴加浓度梯度的游离单体JQ1或BI3812。结果显示，过量的JQ1或BI3812均能有效阻止TCIP1诱导的细胞死亡，这表明TCIP1的BRD4结合端与BCL6结合端对于实现高效细胞杀伤都是必不可少的 (Fig. 2a,b)。对其他DLBCL细胞系的检测表明，在几乎不表达或完全缺失BCL6的细胞系中，细胞死亡无法被竞争性单体所救援 (Extended Data Fig. 2a–c)；而在BCL6低表达的细胞系中，TCIP1的杀伤效力与阴性对照分子Neg2相当，这提示TCIP1在缺失BCL6的细胞系中所表现出的微弱效应仅仅源于对BRD4的基础抑制作用 (Extended Data Fig. 2d,e)。",
            "terms": [
                {"term": "三元复合物 (Ternary Complex)", "desc": "由靶蛋白A（BCL6）、双功能诱导分子（TCIP1）与靶蛋白B（BRD4）按1:1:1化学计量比组装成的异三聚体超分子复合物，是产生近距离诱导生物学效应的核心功能单位。"},
                {"term": "功能获得性 (Gain-of-function)", "desc": "区别于传统小分子抑制剂的阻断活性，TCIP诱导的三元复合物赋予了染色质原抑制位点崭新的转录驱动活性，因而在极低分子浓度下即可触发强大的生物学输出。"}
            ]
        },
        {
            "en": "To quantify the direct interaction between TCIP1, BRD4 and BCL6, we developed a time-resolved fluorescence resonance energy transfer (TR-FRET) assay based on the proximity of the BTB domain of BCL6 labelled with fluorescein isothiocyanate (FITC) to bromodomain 1 (BD1) of BRD4 detected with an anti-histidine tag, terbium-conjugated antibody (Fig. 2c). Formation of a ternary complex in vitro, related to TR-FRET peak height and area under the curve33, was detected using TCIP1 as well as multiple TCIP molecules shown in Fig. 2e.",
            "zh": "为了定量测定TCIP1、BRD4与BCL6之间的直接相互作用，我们建立了一种时间分辨荧光共振能量转移 (time-resolved fluorescence resonance energy transfer, TR-FRET) 分析方法。该方法基于被异硫氰酸荧光素 (FITC) 荧光标记的BCL6 BTB结构域与通过铽 (terbium, Tb) 偶联抗组氨酸标签抗体所检测的BRD4第1溴结构域 (BD1) 之间的空间邻近性 (Fig. 2c)。体外三元复合物的形成量与TR-FRET信号的峰高及曲线下面积 (area under the curve, AUC) 直接相关33；利用该体系，我们成功检测到了TCIP1以及Fig. 2e中展示的多种TCIP衍生物分子所诱导的三元复合物组装。",
            "terms": [
                {"term": "时间分辨荧光共振能量转移 (TR-FRET)", "desc": "结合长寿命镧系元素（如铽Terbium）作为供体的高灵敏度均相生物物理技术，通过时间延迟滤除背景短寿命自发荧光，能够极高信噪比地定量纳米级分子间距离与复合物形成动力学。"}
            ]
        },
        {
            "en": "One reason for the broad hook effect observed in the TR-FRET assay for TCIP1 and other potent TCIPs (Fig. 2c,e and Extended Data Fig. 3a) is the formation of cooperative protein–protein interactions induced by the drug, such as a molecular glue9,34,35. To examine this in detail, we carried out isothermal calorimetry binary and ternary titrations of TCIP1, BRD4(BD1) and BCL6(BTB). Both binary interactions of BCL6–TCIP1 and BRD4–TCIP1 were weak (Kd of BRD4–TCIP1 = 5.08 µM; Kd of BCL6–TCIP1 > 1 mM; Extended Data Fig. 3b), but the ternary complex affinity was Kd of BRD4–TCIP1–BCL6 = 340 ± 108 nM (mean ± s.d., n = 3) (Fig. 2d, left). Using an orthogonal method, biolayer interferometry, we obtained a similar affinity of Kd of BRD4–TCIP1–BCL6 = 293 ± 132 nM (Fig. 2d, right) and confirmed the weak interaction between TCIP1 and BCL6(BTB). We verified the published affinities of JQ1 to BRD4(BD1) and BI3812 to BCL6(BTB), and also that the protein domains do not interact on their own (Extended Data Fig. 3b). Biolayer interferometry measurements also revealed that the ternary complex has a slow off-rate of 26 ms−1 with a half-life of 30 s (Extended Data Fig. 3c–e). Together, the data indicate that TCIP1 induces a stable, cooperative protein–protein interaction between bromodomain 1 of BRD4 and the BTB domain of BCL6.",
            "zh": "在TR-FRET分析中，对于TCIP1和其他高活性TCIP分子所观察到的宽广钩状效应 (broad hook effect) (Fig. 2c,e 以及 Extended Data Fig. 3a)，其重要原因之一在于该化合物诱导了类似于分子胶 (molecular glue) 的协同蛋白质–蛋白质相互作用 (cooperative protein–protein interactions)9,34,35。为了深入剖析这一机制，我们对TCIP1、BRD4(BD1)与BCL6(BTB)进行了等温滴定量热法 (isothermal titration calorimetry, ITC) 的二元与三元滴定测定。BCL6–TCIP1与BRD4–TCIP1两者的二元亲和力均极其微弱（BRD4–TCIP1的Kd = 5.08 µM；BCL6–TCIP1的Kd > 1 mM；Extended Data Fig. 3b），然而三元复合物的解离常数却大幅提高至Kd (BRD4–TCIP1–BCL6) = 340 ± 108 nM (均值 ± s.d., n = 3) (Fig. 2d, 左侧)。利用另一种正交生物物理学方法——生物膜干涉技术 (biolayer interferometry, BLI)，我们测得了高度吻合的三元亲和力：Kd (BRD4–TCIP1–BCL6) = 293 ± 132 nM (Fig. 2d, 右侧)，并再次证实了TCIP1与BCL6(BTB)之间单独二元结合的微弱性。我们同时验证了文献已报道的JQ1对BRD4(BD1)以及BI3812对BCL6(BTB)的亲和力，并且证明了在缺乏药物时这两个蛋白质结构域自身互不发生直接相互作用 (Extended Data Fig. 3b)。生物膜干涉测定还进一步揭示，该三元复合物具有非常缓慢的解离速率 (off-rate koff = 26 ms−1)，其解离半衰期长达30秒 (Extended Data Fig. 3c–e)。综合上述数据表明：TCIP1诱导了BRD4第1溴结构域与BCL6 BTB结构域之间高度稳定且具有协同正效应的蛋白质–蛋白质相互作用。",
            "terms": [
                {"term": "钩状效应 (Hook Effect / 两极效应)", "desc": "双功能分子（如PROTAC或TCIP）在高浓度时，由于游离分子分别独立饱和靶蛋白A和靶蛋白B，形成竞争性的A-Drug和B-Drug二元复合物，导致有效的三元复合物A-Drug-B解离减少，在浓度响应曲线上呈现为先上升后下降的典型钟形（钩状）曲线。"},
                {"term": "协同结合效应 (Cooperativity, α因子)", "desc": "三元复合物形成后，蛋白质A与蛋白质B表面产生新的非共价接触面（类似分子胶），使得三元复合物的亲和力显著超越两端二元结合亲和力的乘积（协同因子 α > 1）。TCIP1的三元Kd (340 nM) 比二元结合弱亲和力强千倍以上。"},
                {"term": "等温滴定量热法 (Isothermal Titration Calorimetry, ITC)", "desc": "生物物理热力学金标准技术，通过测量分子结合过程中释放或吸收的微量热量，直接无标记测定结合常数Kd、反应焓变ΔH和结合化学计量比N。"},
                {"term": "生物膜干涉技术 (Biolayer Interferometry, BLI)", "desc": "光学非标记生物传感技术，基于光波在光纤生物传感器表面的反射干涉图谱位移，实时监测结合解离动力学速率常数（kon, koff）。"}
            ]
        },
        {
            "en": "TCIP1 was the most potent in cell killing among a small library of related TCIPs using different linkers (Fig. 2e). To better understand the relationship between the molecular structure and cellular activity of TCIP, we analysed the relationship between BCL6 reporter transactivation in DLBCL cells and favourable ternary complex formation in vitro and inside the cell (Fig. 2f,g). The most potent TCIPs at cell killing and activating the BCL6 reporter also had high affinities of in vitro and intracellular ternary complex formation (Fig. 2f,g and Extended Data Fig. 3f). The data are consistent with the requirement of an intracellular ternary complex of BRD4, TCIP1 and BCL6 for the activation of cell death.",
            "zh": "在包含不同连接链结构的相关TCIP小分子化合物库中，TCIP1在杀灭肿瘤细胞方面表现出最强的效力 (Fig. 2e)。为了更深入理解TCIP的分子化学结构与其细胞生物学活性之间的构效关系 (structure-activity relationship, SAR)，我们分析了DLBCL细胞中BCL6荧光报告系统的转录反式激活水平与体外及活细胞内优势三元复合物形成之间的相关性 (Fig. 2f,g)。那些在杀伤细胞和激活BCL6报告基因方面效力最强的TCIP分子，同样在体外和细胞内展现出最高的三元复合物形成亲和力 (Fig. 2f,g 以及 Extended Data Fig. 3f)。这些实验数据高度一致地证实：在细胞内形成由BRD4、TCIP1和BCL6组成的三元复合物，是激活下游程序性细胞死亡的绝对必要前提。",
            "terms": [
                {"term": "活细胞nanoBRET技术 (NanoBRET)", "desc": "基于纳米荧光素酶 (NanoLuc) 与荧光受体配体之间的生物发光共振能量转移技术，可无损、实时地在活细胞内直接原位检测蛋白质间相互作用与三元复合物组装。"}
            ]
        }
    ],
    "figure": {
        "id": "fig2",
        "image": "figures/fig2.png",
        "title_en": "Fig. 2 | TCIP1 functions by inducing ternary complex formation.",
        "title_zh": "图 2 | TCIP1 通过诱导形成三元复合物发挥功能。",
        "caption_en": "a, Competitive titration of BI3812 against TCIP1. TCIP1 was added at concentrations from 2 to 64 nM that killed 90% of SUDHL5 DLBCL cells at the same time as addition of the indicated concentrations of BI3812. n = 3 biological replicates, mean ± s.d., 72 h of drug treatment. b, Competitive titration of JQ1 against TCIP1. n = 3 biological replicates, mean ± s.d, 72 h of drug treatment. c, TR-FRET assay to measure molecule-dependent ternary complex formation between BRD4(BD1) and BCL6(BTB). Plotted are a representative set of TCIPs that were the most potent (in cell viability assays) within each category of linker structure. TCIP1 had the highest potency of all designed molecules. Each point represents an independent replicate, which is the mean of three technical repeats; the mean value line is drawn. d, Analysis of cooperative binding induced by TCIP1 and the BRD4(BD1) and BCL6(BTB) domains. A representative ternary complex Kd measurement by isothermal calorimetry is shown. For binary measurements see Extended Data Fig. 3b. n = 3 independent replicates, mean ± s.d. Isothermal calorimetry parameters shown are 20:1 BRD4(BD1):TCIP1 titrated into BCL6(BTB). Right, biolayer interferometry ternary binding measurement using immobilized BCL6(BTB) and BRD4(BD1) in solution. e, Linker structure optimization for TCIP molecules. Linker category and chain length are indicated. f, Correlation between the EC50 for activation of the BCL6 reporter gene in KARPAS422 cells and the in vitro TR-FRET ternary complex formation EC50 for each indicated TCIP. g, Detection of in-cell ternary complex formation between full-length BCL6 and BRD4 by nanoBRET assay in HEK293T cells. n = 3 independent replicates, mean ± s.d.",
        "caption_zh": "a, 单体BI3812针对TCIP1的竞争性滴定救援实验。在SUDHL5 DLBCL细胞系中，以2至64 nM能够杀灭90%细胞的TCIP1浓度为基准，同时加入所示浓度梯度的游离BI3812。n = 3次独立生物学重复，数据表示为均值 ± s.d.，加药培养72小时后测定。b, 单体JQ1针对TCIP1的竞争性滴定救援实验。n = 3次独立生物学重复，均值 ± s.d.，加药处理72小时。c, 测定小分子依赖性BRD4(BD1)与BCL6(BTB)三元复合物形成的TR-FRET实验。图中绘制了在不同连接链结构分类中（在细胞活力测定中）效力最强的一组代表性TCIP化合物。在所有设计的分子中，TCIP1展现出最高的三元复合物诱导效力。每个数据点代表一次独立重复（为3次技术重复的平均值）；图中绘制了平均值折线。d, 由TCIP1、BRD4(BD1)与BCL6(BTB)结构域诱导的协同结合效应分析。左图展示了等温滴定量热法 (ITC) 测定三元复合物解离常数Kd的代表性曲线；二元亲和力测定见Extended Data Fig. 3b；n = 3次独立重复，均值 ± s.d.。所示ITC参数为将20:1的BRD4(BD1):TCIP1混合液滴定至BCL6(BTB)溶液中。右图为生物膜干涉 (BLI) 三元结合测定，采用固相化固定的BCL6(BTB)和溶液相BRD4(BD1)。e, TCIP分子的连接链结构优化。标注了连接链类别与链长碳原子数。f, KARPAS422细胞中BCL6报告基因激活EC50与各所示TCIP化合物体外TR-FRET三元复合物形成EC50之间的相关性散点图。g, 在HEK293T细胞中利用nanoBRET测定法原位检测全长BCL6与BRD4在活细胞内形成三元复合物的剂量反应曲线。n = 3次独立重复，均值 ± s.d.。"
    }
}
