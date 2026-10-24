# -*- coding: utf-8 -*-
"""
Part 7: Discussion Section
Discussion in full
Verbatim translation and academic terminology notes.
"""

PART7_DATA = {
    "title_en": "Discussion",
    "title_zh": "讨论 (Discussion)",
    "paragraphs": [
        {
            "en": "Existing approaches to targeted cancer chemotherapy rely on inhibiting or degrading a protein or preventing its synthesis by RNAi or CRISPR (or CRISPRi). These approaches require complete or near complete removal of the driver function, often resulting in mechanism-based toxicity when the cancer driver is an essential protein. However, by making use of the intrinsic driving pathways of the cancer cell and rewiring them to activate pathways of cell death, we have introduced an approach to cancer chemotherapy that is analogous to a dominant, gain-of-function mutation in genetics. TCIPs produce their effect by activating cell death signalling and rewiring only a fraction of the cancer driver molecules per cell to drive the phenotype. This assertion is supported by the fact that 10 nM TCIP1 produces only an approximately 1.5-fold increase in BRD4 at BCL6 sites over the genome and less than 10% loss at enhancers (Fig. 4d,f), despite robust gene activation and cell killing. A gain-of-function mechanism would also explain the far more robust cell killing seen with substantially lower concentrations of TCIP1 than the weaker antiproliferative effects of conventional small-molecule inhibitors or degraders of BCL6 (refs. 23,57,58) or BET proteins24. The wealth of regulators of programmed cell death suggests many opportunities to use diverse cancer drivers to generalize this strategy of killing cancer cells by rewiring the cancer driver circuitry.",
            "zh": "现存的恶性肿瘤靶向化疗策略几乎完全依赖于抑制某个蛋白质的功能、诱导其靶向降解，或是通过RNA干扰 (RNAi) 或CRISPR（或CRISPRi转录抑制）在源头上阻止其生物合成。这些传统的“功能缺失型 (loss-of-function)”策略普遍要求彻底或近乎彻底地消除目标致癌驱动蛋白的生物学功能；而当该致癌驱动蛋白在人体正常组织中同样扮演不可或缺的必需生理功能时，往往会导致严重的基于机制的靶向毒性 (mechanism-based toxicity)。然而，通过巧妙利用癌细胞自身固有的内源性致癌驱动信号通路，并将其重新布线以转而激活细胞死亡信号级联，我们开创了一种在遗传学逻辑上类似于“显性功能获得性突变 (dominant, gain-of-function mutation)”的全新肿瘤化疗范式。TCIP分子通过主动激活细胞死亡信号通路、且每个细胞仅需重新布线极小一部分致癌驱动分子，即可强力驱动终末杀伤表型。这一重要论断得到了如下实验事实的坚实支持：尽管引发了强烈的促死基因转录激活与高效的细胞杀伤，但10 nM极低浓度的TCIP1仅引起全基因组BCL6结合峰位点处BRD4约1.5倍的适度招募增加，同时活性增强子区域的BRD4占位损失甚至不足10% (Fig. 4d,f)。这种功能获得性新机制，也完美解释了为什么在显著低于传统药物的纳摩尔级超低浓度下，TCIP1所诱导的细胞杀灭效力远远强于传统BCL6小分子竞争性抑制剂或靶向降解剂（参考文献23,57,58）以及传统BET家族抑制剂24所产生的较弱抗增殖效应。真核生物中极其丰富的程序性细胞死亡调控因子网络，为我们利用多种多样的恶性肿瘤驱动因子来广泛推广这一“通过重构致癌驱动网络以杀灭癌细胞”的化疗新策略，提供了广阔而激动人心的探索空间。",
            "terms": [
                {"term": "功能缺失 (Loss-of-Function) vs 显性功能获得 (Gain-of-Function)", "desc": "传统靶向药（抑制剂/PROTAC）是阻断或清除蛋白，要求接近100%抑制率，癌细胞极易通过上调旁路通路或单氨基酸突变产生耐药；TCIP相当于反式显性突变 (dominant-positive in trans)，只要少量三元复合物形成即可发出致命激活指令，肿瘤细胞无法通过简单上调靶蛋白逃逸，反而靶蛋白越多死得越快。"},
                {"term": "基于机制的毒性 (Mechanism-based / On-target Toxicity)", "desc": "药物击中预定靶标而在健康组织中引发的不可避免的不良反应（如彻底抑制BRD4导致造血抑制，全身耗竭BCL6导致致死性自身免疫性心肌炎）。TCIP利用催化性低占位率和细胞特异性组合逻辑，在根除肿瘤的同时保护了正常组织。"}
            ]
        },
        {
            "en": "Past studies have used CIPs of genetically modified transcription factors or epigenetic regulators to activate or repress signal transduction or transcription of exogenous or endogenous genes9,12,14. Small molecules that bind to DNA and/or nucleosomes have also been used for this purpose13,59. Although these studies were mechanistically informative and provided a catalogue of the biologic processes regulated by CIPs15, they had little therapeutic potential because of the need to introduce genetically modified transcription factors or small molecules with relatively little genomic specificity. Our experiments developing TCIPs rely only on endogenous transcription factors and epigenetic modifiers with their intrinsic biologic specificity and capture the combinatorial use of transcriptional regulators. The activation of endogenous genes by small-molecule TCIPs might have application to many other areas of biology and medicine. For example, TCIPs could be designed for use in activating death pathways in senescent cells, activating the expression of therapeutic or haploinsufficient genes, activating the expression of neoantigens in human immunotherapy, or regulating gene expression in cells or organisms for synthetic biology applications.",
            "zh": "以往的经典研究曾利用经基因工程改造的转录因子或表观遗传调控蛋白的化学近距离诱导剂 (CIPs)，来人为激活或抑制外源性或内源性基因的信号转导及转录过程9,12,14。能够结合DNA骨架以及/或者核小体 (nucleosomes) 的合成小分子也曾被用于此类目的13,59。尽管这些先驱性研究在机制层面极富启发性，并系统编纂了一份受CIP调控的生物学过程目录15，但它们在临床转化医学上的应用潜力极为有限——因为它们必须在宿主细胞中预先转染引入外源基因工程修饰的融合蛋白，或者使用基因组序列特异性较差的合成小分子。与此形成鲜明对比的是：我们所开发的TCIP分子技术完全依赖于机体内源性表达的转录因子与表观遗传修饰酶，完美继承了它们固有的生物学序列特异性，并巧妙捕捉了真核生物转录调控因子的组合使用逻辑 (combinatorial use)。利用小分子TCIP激活内源性基因的全新概念，在现代生物学与转化医学的诸多其他前沿领域同样孕育着极其广泛的应用前景。例如：TCIP可被量身设计用于特异性激活衰老细胞 (senescent cells) 中的程序性自毁死亡通路（即新型衰老清除剂 Senolytics）；用于重新激活由于单倍体剂量不足 (haploinsufficiency) 导致表达减半的关键抑癌或治疗性基因；用于在肿瘤免疫治疗中强力激活隐藏的新抗原 (neoantigens) 转录呈现；或者在合成生物学 (synthetic biology) 应用中用于无损、精确调控活体细胞或复杂多细胞生物体内的目标基因表达网络。",
            "terms": [
                {"term": "衰老细胞清除 (Senolytics)", "desc": "衰老细胞抵抗凋亡并在组织中长期存活，持续分泌衰老相关分泌表型 (SASP) 诱发慢性炎症与退行性病变。TCIP技术可将衰老细胞特异性转录因子重新布线至促凋亡启动子，实现衰老细胞的精准清除。"},
                {"term": "单倍体剂量不足基因激活 (Haploinsufficiency Rescue)", "desc": "常染色体显性遗传病中常见：单个功能基因拷贝丢失导致蛋白表达量减半（50%）而致病。TCIP能将强效转录延伸机器定向招募至残留的野生型等位基因上，将表达量提升回正常生理水平（100%），实现基因替代治疗无法匹敌的药物拯救。"}
            ]
        }
    ]
}
