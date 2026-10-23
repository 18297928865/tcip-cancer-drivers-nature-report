# -*- coding: utf-8 -*-
"""
data_part1_intro.py
Contains Article Header, Authors, Affiliations, Verbatim Abstract, and Verbatim Introduction.
Every single sentence is faithful to the original Nature paper (Nature 620, 417-427, 2023).
"""

ARTICLE_HEADER = {
    "journal": "Nature | Vol 620 | 10 August 2023 | 417–427",
    "article_type": "Article",
    "doi": "10.1038/s41586-023-06348-2",
    "doi_url": "https://doi.org/10.1038/s41586-023-06348-2",
    "received": "15 August 2022",
    "accepted": "20 June 2023",
    "published": "26 July 2023",
    "title_en": "Rewiring cancer drivers to activate apoptosis",
    "title_zh": "重连癌症驱动因子以激活细胞凋亡",
    "authors": [
        {"name": "Sai Gourisankar", "affil": "1,2,6", "zh": "Sai Gourisankar（共同第一作者）"},
        {"name": "Andrey Krokhotin", "affil": "1,6", "zh": "Andrey Krokhotin（共同第一作者）"},
        {"name": "Wenzhi Ji", "affil": "3,6", "zh": "季文智（共同第一作者）"},
        {"name": "Xiaofan Liu", "affil": "3", "zh": "刘晓凡"},
        {"name": "Chiung-Ying Chang", "affil": "1", "zh": "Chiung-Ying Chang"},
        {"name": "Samuel H. Kim", "affil": "1", "zh": "Samuel H. Kim"},
        {"name": "Zhengnian Li", "affil": "3", "zh": "李正念"},
        {"name": "Wendy Wenderski", "affil": "1,4", "zh": "Wendy Wenderski"},
        {"name": "Juste M. Simanauskaite", "affil": "1", "zh": "Juste M. Simanauskaite"},
        {"name": "Haopeng Yang", "affil": "5", "zh": "杨浩鹏"},
        {"name": "Hannes Vogel", "affil": "1", "zh": "Hannes Vogel"},
        {"name": "Tinghu Zhang", "affil": "3", "zh": "张廷琥"},
        {"name": "Michael R. Green", "affil": "5", "zh": "Michael R. Green"},
        {"name": "Nathanael S. Gray", "affil": "3*", "email": "nsgray01@stanford.edu", "zh": "Nathanael S. Gray（共同通讯作者）"},
        {"name": "Gerald R. Crabtree", "affil": "1,4*", "email": "crabtree@stanford.edu", "zh": "Gerald R. Crabtree（共同通讯作者）"}
    ],
    "affiliations": [
        {"id": "1", "en": "Department of Pathology, Stanford University, Stanford, CA, USA.", "zh": "美国斯坦福大学医学院病理学系"},
        {"id": "2", "en": "Department of Chemical Engineering, Stanford University, Stanford, CA, USA.", "zh": "美国斯坦福大学化学工程系"},
        {"id": "3", "en": "Department of Chemical and Systems Biology, Stanford Cancer Institute, ChEM-H, Stanford University, Stanford, CA, USA.", "zh": "美国斯坦福大学化学与系统生物学系、斯坦福癌症研究所、ChEM-H 交叉科学研究所"},
        {"id": "4", "en": "Department of Developmental Biology, Stanford University, Stanford, CA, USA.", "zh": "美国斯坦福大学发育生物学系"},
        {"id": "5", "en": "Department of Lymphoma & Myeloma, The University of Texas MD Anderson Cancer Center, Houston, TX, USA.", "zh": "美国德克萨斯大学 MD 安德森癌症中心淋巴瘤与骨髓瘤系"},
        {"id": "6", "en": "These authors contributed equally: Sai Gourisankar, Andrey Krokhotin, Wenzhi Ji.", "zh": "这些作者对本工作做出了同等贡献：Sai Gourisankar、Andrey Krokhotin、季文智。"}
    ]
}

ABSTRACT_PARAS = [
    {
        "en": "Genes that drive the proliferation, survival, invasion and metastasis of malignant cells have been identified for many human cancers. Independent studies have identified cell death pathways that eliminate cells for the good of the organism. The coexistence of cell death pathways with driver mutations suggests that the cancer driver could be rewired to activate cell death using chemical inducers of proximity (CIPs).",
        "zh": "在多种人类癌症中，驱动恶性细胞增殖、存活、侵袭和转移的基因已被广泛鉴定。独立的研究也揭示了有机体为了自身生存与稳态而清除细胞的程序性细胞死亡途径。细胞死亡通路与癌基因驱动突变的共存表明：通过利用化学邻近诱导剂（CIPs），可以将癌症驱动因子重新连接（rewire），使其转而激活细胞死亡程序。"
    },
    {
        "en": "Here we describe a new class of molecules called transcriptional/epigenetic CIPs (TCIPs) that recruit the endogenous cancer driver, or a downstream transcription factor, to the promoters of cell death genes, thereby activating their expression. We focused on diffuse large B cell lymphoma, in which the transcription factor B cell lymphoma 6 (BCL6) is deregulated. BCL6 binds to the promoters of cell death genes and epigenetically suppresses their expression. We produced TCIPs by covalently linking small molecules that bind BCL6 to those that bind to transcriptional activators that contribute to the oncogenic program, such as BRD4.",
        "zh": "在此，我们报道了一类新型分子，称之为“转录/表观遗传邻近诱导剂”（transcriptional/epigenetic CIPs, TCIPs）。该类分子能将内源性癌症驱动因子（或其下游转录因子）招募至细胞死亡基因的启动子区域，从而强效激活其转录表达。我们聚焦于弥漫大B细胞淋巴瘤（DLBCL），该恶性肿瘤中转录因子 B 细胞淋巴瘤 6（BCL6）发生失调。BCL6 结合在细胞死亡基因的启动子上，并通过表观遗传机制抑制其表达。我们通过共价连接结合 BCL6 的小分子与结合参与促癌程序的转录激活因子（如 BRD4）的小分子，设计并合成了 TCIP 分子。"
    },
    {
        "en": "The most potent molecule, TCIP1, increases binding of BRD4 by 50% over genomic BCL6-binding sites to produce transcriptional elongation at pro-apoptotic target genes within 15 min, while reducing binding of BRD4 over enhancers by only 10%, reflecting a gain-of-function mechanism. TCIP1 kills diffuse large B cell lymphoma cell lines, including chemotherapy-resistant, TP53-mutant lines, at EC50 of 1–10 nM in 72 h and exhibits cell-specific and tissue-specific effects, capturing the combinatorial specificity inherent to transcription. The TCIP concept also has therapeutic applications in regulating the expression of genes for regenerative medicine and developmental disorders.",
        "zh": "其中活性最强的分子 TCIP1 能够使全基因组 BCL6 结合位点处的 BRD4 结合量增加 50%，在给药 15 分钟内即在促凋亡靶基因处诱发转录延伸；与此同时，其仅使增强子区域的 BRD4 结合减少约 10%，这一现象反映出独特的“获得性功能增效”（gain-of-function）机制。TCIP1 在 72 小时内以 1–10 nM 的半数有效浓度（EC50）高效杀伤弥漫大B细胞淋巴瘤细胞株（包括化疗耐药、TP53 突变的细胞株），并展现出细胞与组织特异性效应，精准捕获了转录调控固有的组合特异性。TCIP 这一科学构想在再生医学与发育障碍疾病的基因表达调控中同样具备广泛的治疗应用潜力。"
    }
]

INTRO_PARAS = [
    {
        "en": "Induced proximity is fundamental to many forms of biological regulation, including receptor function, post-translational modifications, regulation of transcription, epigenetic regulation and allosteric processes that generate scaffolds to facilitate protein–protein interactions. The underlying physical principle is based on the fact that an effective collision between two molecules is inversely proportional to the cube of the distance between them. The biological roles of induced proximity have been probed with dimeric small molecules, CIPs, that have been used to recapitulate many steps in signal transduction, protein localization and transcription. Recently, dimeric small molecules that use CIP to target proteins to the proteasome, PROTACS, or to inhibit protein–protein interactions have been developed. More broadly, the observation that even an event as carefully regulated as programmed cell death can be activated by CIPs suggests that distinct cellular circuitries might be linked, or rewired, using CIPs, to cause cancer cells to activate processes leading to apoptosis.",
        "zh": "诱导邻近（induced proximity）是生命体系中诸多生物学调控的核心基础，包括受体功能活化、翻译后修饰、转录调控、表观遗传调控以及促进蛋白质-蛋白质相互作用的支架变构过程。其底层的物理学机制基于这样一个基本事实：两个分子之间的有效碰撞频率与其空间距离的立方成反比。以往的研究已利用二聚化小分子——即化学邻近诱导剂（CIPs）——系统探索了诱导邻近的生物学功能，并成功重现了信号转导、蛋白质亚细胞定位和转录调控中的多个关键步骤。近年来，利用 CIP 机制将靶标蛋白招募至蛋白酶体进行降解的双功能小分子（PROTACs），或是用于破坏蛋白-蛋白相互作用的分子相继问世。更广泛地讲，即便是像程序性细胞死亡这样受到严密精细调控的过程亦可通过 CIP 加以激活，这一重大发现启示我们：可以通过 CIP 将互不相同的细胞调控回路偶联或“重连”（rewired），驱动癌细胞自主激活走向凋亡的程序。"
    },
    {
        "en": "To rewire transcriptional circuits within a genetically unmodified cell or organism, we developed small molecules that allow the recruitment of cancer-driving transcriptional or epigenetic regulators to the regulatory regions of target therapeutic genes. The general features of the concept and design of a TCIP is illustrated in Fig. 1a and involves synthesis of small molecules that bind to a specific transcriptional or epigenetic regulator on one side; on the other side, a transcription factor binds to a target therapeutic gene. We applied these molecules to activate apoptosis in cancer cells.",
        "zh": "为了在未经基因工程改造的天然细胞或活体生物中重连转录调控回路，我们开发了一类能够将促癌转录或表观遗传调控因子招募至治疗性靶基因调控区的小分子。TCIP 的总体概念与分子设计原理如图 1a 所示：其分子结构一端结合特定的转录或表观遗传激活调控因子，另一端结合与治疗性靶基因结合的转录因子。在本文中，我们将这一创新分子体系应用于肿瘤细胞，以特异性激活其凋亡程序。"
    }
]
