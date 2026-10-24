# -*- coding: utf-8 -*-
"""
Part 1: Paper Title, Metadata, Abstract, and Introduction
Faithful, verbatim sentence-by-sentence translation with terminology annotations.
"""

PART1_DATA = {
    "meta": {
        "title_en": "Rewiring cancer drivers to activate apoptosis",
        "title_zh": "重新布线癌症驱动因子以激活细胞凋亡",
        "journal": "Nature | Vol 620 | 10 August 2023 | 417–427",
        "doi": "https://doi.org/10.1038/s41586-023-06348-2",
        "authors": [
            "Sai Gourisankar (共同一作, Stanford)",
            "Andrey Krokhotin (共同一作, Stanford)",
            "Wenzhi Ji (季文智, 共同一作, Stanford)",
            "Xiaofan Liu",
            "Chiung-Ying Chang",
            "Samuel H. Kim",
            "Zhengnian Li",
            "Wendy Wenderski",
            "Juste M. Simanauskaite",
            "Haopeng Yang",
            "Hannes Vogel",
            "Tinghu Zhang",
            "Michael R. Green",
            "Nathanael S. Gray (通讯作者, Stanford)",
            "Gerald R. Crabtree (通讯作者, Stanford / HHMI)"
        ],
        "affiliations": "Stanford University School of Medicine, Stanford Cancer Institute, MD Anderson Cancer Center, Howard Hughes Medical Institute (HHMI)"
    },
    "abstract": {
        "en": "Genes that drive the proliferation, survival, invasion and metastasis of malignant cells have been identified for many human cancers1–4. Independent studies have identified cell death pathways that eliminate cells for the good of the organism5,6. The coexistence of cell death pathways with driver mutations suggests that the cancer driver could be rewired to activate cell death using chemical inducers of proximity (CIPs). Here we describe a new class of molecules called transcriptional/epigenetic CIPs (TCIPs) that recruit the endogenous cancer driver, or a downstream transcription factor, to the promoters of cell death genes, thereby activating their expression. We focused on diffuse large B cell lymphoma, in which the transcription factor B cell lymphoma 6 (BCL6) is deregulated7. BCL6 binds to the promoters of cell death genes and epigenetically suppresses their expression8. We produced TCIPs by covalently linking small molecules that bind BCL6 to those that bind to transcriptional activators that contribute to the oncogenic program, such as BRD4. The most potent molecule, TCIP1, increases binding of BRD4 by 50% over genomic BCL6-binding sites to produce transcriptional elongation at pro-apoptotic target genes within 15 min, while reducing binding of BRD4 over enhancers by only 10%, reflecting a gain-of-function mechanism. TCIP1 kills diffuse large B cell lymphoma cell lines, including chemotherapy-resistant, TP53-mutant lines, at EC50 of 1–10 nM in 72 h and exhibits cell-specific and tissue-specific effects, capturing the combinatorial specificity inherent to transcription. The TCIP concept also has therapeutic applications in regulating the expression of genes for regenerative medicine and developmental disorders.",
        "zh": "驱动恶性细胞增殖 (proliferation)、存活 (survival)、侵袭 (invasion) 和转移 (metastasis) 的基因已在多种人类癌症中被鉴定出来1–4。与此同时，独立的诸多研究也明确了为了机体利益而清除异常细胞的细胞死亡通路 (cell death pathways)5,6。细胞死亡通路与驱动突变 (driver mutations) 的共存提示：我们可以利用化学近距离诱导剂 (chemical inducers of proximity, CIPs)，将癌症驱动因子重新布线 (rewire)，使其转而激活细胞死亡。在本研究中，我们描述了一类被称为转录/表观遗传近距离诱导剂 (transcriptional/epigenetic CIPs, TCIPs) 的新型分子，它们能够将内源性癌症驱动因子或其下游转录因子招募至细胞死亡基因的启动子 (promoters) 区，从而激活这些促死基因的表达。我们重点聚焦于弥漫性大B细胞淋巴瘤 (diffuse large B cell lymphoma, DLBCL)，在这类肿瘤中转录因子B细胞淋巴瘤6 (B cell lymphoma 6, BCL6) 发生表达失调7。BCL6会结合在细胞死亡基因的启动子上，并在表观遗传层面上抑制其表达8。我们通过将结合BCL6的小分子与结合促进致癌程序的转录激活因子（例如BRD4）的小分子进行共价偶联，制造出了TCIPs。其中最强效的分子TCIP1能够使BRD4在全基因组BCL6结合位点上的结合量增加50%，并在15分钟内诱导促凋亡靶基因发生转录延伸 (transcriptional elongation)，而BRD4在增强子 (enhancers) 上的结合仅减少10%，这充分反映出一种功能获得性 (gain-of-function) 机制。TCIP1在72小时内以1–10 nM的半数有效浓度 (EC50) 杀灭弥漫性大B细胞淋巴瘤细胞系（包括化疗耐药且TP53突变的细胞株），并表现出细胞特异性与组织特异性效应，成功捕捉了转录所固有的组合特异性 (combinatorial specificity)。TCIP这一概念在调控基因表达方面，同样具有应用于再生医学 (regenerative medicine) 和发育障碍疾病 (developmental disorders) 的治疗潜力。",
        "terms": [
            {"term": "化学近距离诱导剂 (Chemical Inducers of Proximity, CIPs)", "desc": "一种双功能小分子，通过两端分别结合两种不同的蛋白质分子，诱导它们在空间上相互靠近，从而在不借助基因工程的情况下人为控制蛋白质相互作用与信号转导。由Gerald Crabtree和Stuart Schreiber于1993年开创。"},
            {"term": "转录/表观遗传近距离诱导剂 (TCIPs)", "desc": "Transcriptional Chemical Inducers of Proximity。本研究提出的新型双功能分子，一端结合致癌转录因子/阻遏蛋白（如BCL6），另一端结合转录延伸激活复合物（如BRD4），将转录阻遏位点瞬间改造为高活性转录激活复合体。"},
            {"term": "弥漫性大B细胞淋巴瘤 (DLBCL)", "desc": "Diffuse Large B Cell Lymphoma，最常见的恶性非霍奇金淋巴瘤类型，临床异质性高，约30-40%患者出现原发耐药或复发。BCL6基因易位或启动子突变在其发病中起关键驱动作用。"},
            {"term": "功能获得性机制 (Gain-of-function mechanism)", "desc": "与传统抑制剂或降解剂（PROTAC）通过消除蛋白功能不同，TCIP让致癌蛋白结合并激活本不被激活的下游通路，表现为主动赋予新功能的显性表型。"}
        ]
    },
    "intro": [
        {
            "en": "Induced proximity is fundamental to many forms of biological regulation, including receptor function9, post-translational modifications10,11, regulation of transcription12,13, epigenetic regulation14–16 and allosteric processes that generate scaffolds to facilitate protein–protein interactions. The underlying physical principle is based on the fact that an effective collision between two molecules is inversely proportional to the cube of the distance between them15. The biological roles of induced proximity have been probed with dimeric small molecules, CIPs, that have been used to recapitulate many steps in signal transduction, protein localization and transcription15. Recently, dimeric small molecules that use CIP to target proteins to the proteasome, PROTACS17, or to inhibit protein–protein interactions18 have been developed. More broadly, the observation that even an event as carefully regulated as programmed cell death can be activated by CIPs19–21 suggests that distinct cellular circuitries might be linked, or rewired, using CIPs, to cause cancer cells to activate processes leading to apoptosis.",
            "zh": "诱导邻近 (induced proximity) 是许多生物调控形式的基础，包括受体功能9、翻译后修饰 (post-translational modifications)10,11、转录调控12,13、表观遗传调控14–16以及通过生成脚手架 (scaffolds) 促进蛋白质–蛋白质相互作用的变构过程 (allosteric processes)。其底层的物理学原理在于：两个分子之间的有效碰撞概率与它们之间距离的立方成反比15。诱导邻近的生物学功能已通过二聚小分子——即化学近距离诱导剂 (CIPs) 进行了广泛探索，这类分子已被用于重现信号转导、蛋白质亚细胞定位和转录过程中的诸多步骤15。最近，利用CIP将目标蛋白靶向递送至蛋白酶体 (proteasome) 的二聚小分子（即蛋白降解靶向嵌合体，PROTACs）17，或用于抑制蛋白质–蛋白质相互作用的小分子18已被相继开发。更广泛地讲，即便是像程序性细胞死亡 (programmed cell death) 这样受到极其精密调控的事件也能被CIPs激活的实验观察19–21表明：我们可以利用CIPs将彼此截然不同的细胞内回路连接起来或重新布线 (rewired)，促使癌细胞主动激活走向凋亡 (apoptosis) 的级联反应。",
            "terms": [
                {"term": "有效碰撞与距离三次方反比定律", "desc": "物理化学原理：当两个分子被共价连接的小分子强行约束在同一微环境纳米尺度内时，局部有效浓度 (effective local concentration) 会暴增数千至数万倍，使得原本极弱甚至不存在的分子间反应能够以极高反应速率自发发生。"},
                {"term": "PROTACs (Proteolysis Targeting Chimeras)", "desc": "靶向蛋白降解嵌合体，一端结合靶蛋白，另一端结合E3泛素连接酶（如CRBN或VHL），通过泛素-蛋白酶体途径彻底降解靶蛋白，属于功能缺失型 (loss-of-function) 策略。"}
            ]
        },
        {
            "en": "To rewire transcriptional circuits within a genetically unmodified cell or organism, we developed small molecules that allow the recruitment of cancer-driving transcriptional or epigenetic regulators to the regulatory regions of target therapeutic genes. The general features of the concept and design of a TCIP is illustrated in Fig. 1a and involves synthesis of small molecules that bind to a specific transcriptional or epigenetic regulator on one side; on the other side, a transcription factor binds to a target therapeutic gene. We applied these molecules to activate apoptosis in cancer cells.",
            "zh": "为了在未经过基因工程修饰的细胞或完整生物体内重构转录回路，我们开发了能够将致癌转录调控因子或表观遗传调控因子招募至治疗性靶基因调控区的小分子化合物。TCIP的概念与设计总体特征如图1a (Fig. 1a) 所示：其核心在于合成一类双功能小分子，一端结合特异性的转录或表观遗传调控因子；另一端结合定位在治疗性靶基因上的转录因子。我们进一步将这些分子应用于激活癌细胞中的细胞凋亡过程。",
            "terms": [
                {"term": "重新布线 (Rewiring)", "desc": "指改变细胞内部固有的调控逻辑：肿瘤细胞原本依赖转录因子（如BCL6）持续抑制促凋亡基因以维持不死性；TCIP通过引入BRD4转录激活复合物，将该转录抑制位点强行翻转为强效转录激活开关，变“肿瘤存活驱动源”为“自杀触发源”。"}
            ]
        }
    ]
}
