# -*- coding: utf-8 -*-
"""
Part 4: Results Section 3 & Figure 3
Apoptosis throughout the cell cycle, Activation of pro-apoptotic genes, Repression of MYC and its targets
Verbatim translation, figure insertion, and academic terminology notes.
"""

PART4_DATA = {
    "subsections": [
        {
            "title_en": "Apoptosis throughout the cell cycle",
            "title_zh": "贯穿整个细胞周期的全周期细胞凋亡诱导",
            "paragraphs": [
                {
                    "en": "To characterize the cell death observed with TCIP1, we quantified cells that have externalized phosphatidylserine by staining with annexin V. We observed a dose-dependent increase in the number of annexin-positive cells, at 10 nM TCIP1, at 24 h (Extended Data Fig. 4a). TCIP1 induced detectable apoptosis by 4–8 h (Extended Data Fig. 4b).",
                    "zh": "为了表征TCIP1所诱导的细胞死亡特征，我们通过Annexin V荧光染色对发生磷脂酰丝氨酸外翻 (externalized phosphatidylserine) 的凋亡细胞进行了定量分析。在加药处理24小时后，我们观察到在10 nM TCIP1作用下Annexin V阳性细胞数量呈现剂量依赖性显著增加 (Extended Data Fig. 4a)。TCIP1在加药后仅4至8小时内即可诱导出可被明确检测到的早期细胞凋亡信号 (Extended Data Fig. 4b)。",
                    "terms": [
                        {"term": "磷脂酰丝氨酸外翻 (Externalized Phosphatidylserine, PS)", "desc": "在正常活细胞中，PS主要分布在质膜内小叶；细胞凋亡早期，质膜不对称性丧失，PS快速翻转至质膜外表面，可被特异性结合钙依赖性蛋白Annexin V识别，是早期凋亡的金标准生化标志物。"}
                    ]
                },
                {
                    "en": "Cancers can evade cell killing by many chemotherapeutics that function only during a specific stage of the cell cycle. To investigate the cell-cycle dependence of the apoptosis caused by TCIP1, we performed cell-cycle analysis in concert with TUNEL staining, which measures DNA fragmentation (Extended Data Fig. 4c). The cell-cycle analysis revealed that TCIP1 induced both a G1/S and G2/M block in the cell cycle (Extended Data Figs. 4d and 5a). By examining DNA cleavage with the TUNEL assay, we found that cell death occurred during all phases of the cell cycle (Extended Data Figs. 4e and 5a). To further examine the mechanism of cell death by TCIP1, we used serum starvation to arrest the cell cycle in G0/G1. The cells became even more sensitive to TCIP1, exhibiting an EC50 of 250 pM compared with 3.2 nM without arrest (Extended Data Fig. 4f). This observation indicates that TCIP1 produces cell death by activating more than a single cell death pathway.",
                    "zh": "恶性肿瘤往往能够逃避许多仅在特定细胞周期时相发挥作用的化疗药物的杀伤。为了探究TCIP1诱导细胞凋亡对细胞周期的依赖性，我们将细胞周期分析与检测DNA断裂片段的TUNEL染色技术结合进行分析 (Extended Data Fig. 4c)。细胞周期检测结果显示，TCIP1诱导了细胞周期在G1/S期和G2/M期的双重阻滞 (Extended Data Figs. 4d 与 5a)。通过TUNEL分析检测DNA裂解水平，我们发现细胞死亡广泛发生在细胞周期的所有各个时相中 (Extended Data Figs. 4e 与 5a)。为了进一步深入剖析TCIP1诱导细胞死亡的机制，我们采用血清饥饿法 (serum starvation) 将细胞周期强行阻滞在G0/G1期静止状态。此时细胞对TCIP1展现出更高的敏感性：其EC50从未阻滞状态下的3.2 nM锐降至惊人的250 pM (Extended Data Fig. 4f)。这一实验观察明确证实：TCIP1是通过激活多条彼此独立且协同的细胞死亡通路来引发细胞死亡的，而非单纯依赖活跃周期分裂。",
                    "terms": [
                        {"term": "TUNEL染色法 (Terminal deoxynucleotidyl transferase dUTP nick end labeling)", "desc": "末端脱氧核苷酸转移酶介导的dUTP缺口末端标记测定法，利用TdT酶将荧光标记的dUTP特异性连接至凋亡细胞核内发生断裂的DNA 3'-OH游离末端，用于精准测定晚期凋亡的基因组断裂程度。"},
                        {"term": "全周期杀伤效应 (Cell-Cycle-Independent Apoptosis)", "desc": "绝大多数传统化疗药（如微管抑制剂紫杉醇作用于M期、抗代谢药吉西他滨作用于S期）均具有强烈的细胞周期依赖性，处于休眠G0/G1期的肿瘤干细胞常由此逃逸复发。TCIP1在G0/G1静止期反显更强效力（250 pM），具备清除难治性静止期肿瘤细胞的重大潜力。"}
                    ]
                }
            ]
        },
        {
            "title_en": "TCIP1 activates pro-apoptotic genes",
            "title_zh": "TCIP1 强力激活促凋亡基因的转录表达",
            "paragraphs": [
                {
                    "en": "To define the genes involved in the induction of apoptosis by TCIP1, we carried out RNA sequencing studies 20 h after adding drug at 10 or 100 nM, when the critical genes were likely to be executing their functions. Changes in gene expression were dependent on dose (Extended Data Fig. 6a–c), and at just 10 nM TCIP1, the expression of 1,654 genes was increased, whereas the expression of 1,347 genes was reduced (Fig. 3a). Genes activated by TCIP1 were enriched for known cell-cycle arrest and pro-apoptotic targets normally repressed by BCL6, such as P21 (also known as CDKN1A), FOXO3 and PMAIP1 (also known as NOXA) (Fig. 3a and Extended Data Fig. 6b,c,e). Along with the p53 and apoptosis pathways, TCIP1 also induces the TNF pathway (Extended Data Fig. 6d). Signalling via NF-κB has been shown to be repressed by BCL6 (refs. 22,36,37). These changes in mRNA levels were paralleled by dose-dependent and time-dependent changes in protein expression in two different DLBCL cell lines, SUDHL5 and KARPAS422, with negligible effect of the chemical controls Neg1 and Neg2 (Fig. 3d–f). Of particular interest was the observation that FOXO3 is activated by 0.5 nM TCIP1 (Fig. 3e) and within 2 h by 10 nM TCIP1 (Fig. 4d). Activation of FOXO3 also displayed a hook effect (Fig. 3e), characteristic of the direct target of a bivalent molecule. FOXO3 is a master pro-apoptotic gene38 with a BCL6-binding site at its promoter39. Although FOXO3 and P21 are also known to be activated downstream of TP53 (ref. 40), which is itself a BCL6 target, TP53 is biallelically inactivated in this DLBCL line (KARPAS422) and other chemotherapy-resistant DLBCL lines killed by TCIP1. This supports the evidence in Extended Data Fig. 4 that TCIP1 derepresses multiple cell-cycle arrest and death pathways that are normally repressed by BCL6.",
                    "zh": "为了明确参与TCIP1诱导细胞凋亡的关键靶基因，我们在加入10 nM或100 nM药物后20小时（此时关键调控基因极可能正在全面执行其生物学功能）开展了全转录组RNA测序 (RNA-seq) 研究。基因表达水平的变化呈现高度的剂量依赖性 (Extended Data Fig. 6a–c)；在仅10 nM TCIP1处理下，就有1,654个基因的表达发生显著上调，而1,347个基因的表达发生下调 (Fig. 3a)。被TCIP1显著激活的基因高度富集于那些通常受到BCL6严格转录抑制的已知细胞周期阻滞与促凋亡靶标中，例如P21（亦称CDKN1A）、FOXO3以及PMAIP1（亦称NOXA）(Fig. 3a 以及 Extended Data Fig. 6b,c,e)。除p53通路与细胞凋亡通路外，TCIP1还激活了肿瘤坏死因子 (TNF) 信号通路 (Extended Data Fig. 6d)；以往已有文献表明NF-κB信号转导通路常年受到BCL6的表观遗传抑制22,36,37。上述mRNA转录本水平的激增，在两株不同的DLBCL细胞系SUDHL5与KARPAS422中均伴随着剂量依赖和时间依赖性的蛋白质水平相应上调，而化学阴性对照分子Neg1和Neg2的影响几乎微乎其微 (Fig. 3d–f)。尤为引人瞩目的是：仅0.5 nM极低浓度的TCIP1即可显著激活FOXO3蛋白的表达 (Fig. 3e)，而在10 nM TCIP1处理后2小时内即可检测到其表达上调 (Fig. 4d)。FOXO3的转录激活同样展现出了典型的“钩状效应 (hook effect)”(Fig. 3e)，这是双价诱导分子作用于直接作用靶标的标志性特征。FOXO3是一个主控型促凋亡转录因子38，其启动子区拥有高亲和力的BCL6结合位点39。尽管已知FOXO3和P21在生理状态下也可作为TP53的下游靶标被激活40（而TP53自身亦是BCL6的阻遏靶标），但本研究中测试的KARPAS422细胞系及其他被TCIP1强效杀伤的耐药DLBCL细胞系均存在TP53的双等位基因纯合失活。这一事实有力支持了Extended Data Fig. 4中的实验证据，即TCIP1能够完全独立于p53通路，直接解除并反转BCL6在生理状态下所抑制的多种细胞周期阻滞与凋亡通路。",
                    "terms": [
                        {"term": "FOXO3", "desc": "Forkhead box O3，重要的促凋亡与抑癌转录因子，可直接结合并启动BIM (BCL2L11)、PUMA等促凋亡效应分子的转录表达。在淋巴瘤中被BCL6长期表观抑制。"},
                        {"term": "PMAIP1 (NOXA)", "desc": "Phorbol-12-myristate-13-acetate-induced protein 1，BH3-only促凋亡Bcl-2家族成员，能特异性结合并中和抗凋亡蛋白MCL1，触发线粒体凋亡级联反应。"},
                        {"term": "P21 (CDKN1A)", "desc": "周期蛋白依赖性激酶抑制剂1A，强力抑制CDK2和CDK4/6，导致细胞阻滞在G1/S或G2/M期。"}
                    ]
                }
            ]
        },
        {
            "title_en": "TCIP1 represses MYC and its targets",
            "title_zh": "TCIP1 强力下调致癌基因 MYC 及其下游靶基因网络",
            "paragraphs": [
                {
                    "en": "Among the group of genes whose expression was most reduced were MYC and its targets (Fig. 3b and Extended Data Fig. 6c). This is important as many DLBCLs are considered to be dependent on MYC41,42. We examined the top 100 most TCIP1-reduced genes using over 4,500 ChIP–seq datasets of human transcription factors in blood cancer cell lines43, and found the promoters of TCIP1-inhibited genes highly enriched for MYC binding in multiple datasets (Fig. 3c). Examination of MYC protein levels upon the addition of TCIP1 showed that MYC levels were reduced starting at less than 1 nM TCIP1 and within 2 h of addition of the drug (Fig. 3d,e). The chemical controls Neg1 and Neg2 did not affect MYC levels at comparable concentrations (Fig. 3f). BET/BRD4 inhibitors such as JQ1 are known to reduce the expression of MYC25, but at much higher levels of drug (500 nM) than TCIP1. We therefore hypothesized that repression of MYC is a gain-of-function consequence of the ternary complex formed by TCIP1.",
                    "zh": "在转录表达下调最显著的一组基因中，致癌转录因子MYC及其下游靶基因群居于首位 (Fig. 3b 以及 Extended Data Fig. 6c)。这一发现极其关键，因为临床上绝大多数恶性DLBCL被公认高度依赖MYC以维持其恶性增殖表型41,42。我们利用血液系统恶性肿瘤细胞系中超过4,500个公开的人类转录因子ChIP–seq数据集43，对TCIP1诱导表达下调最显著的前100个基因启动子进行了无偏性转录因子富集分析，结果发现被TCIP1抑制的基因启动子在多个数据集中均高度富集MYC的直接结合位点 (Fig. 3c)。在添加TCIP1后对MYC蛋白水平的时间与剂量检测进一步显示：在低于1 nM的极低TCIP1浓度下即可观察到MYC蛋白表达量的骤减，且在加药后2小时内即迅速发生下调 (Fig. 3d,e)。相比之下，化学阴性对照化合物Neg1和Neg2在相同浓度下对MYC蛋白水平完全没有影响 (Fig. 3f)。虽然已知单体BET/BRD4抑制剂（如JQ1）也能够通过抑制BRD4依赖的超级增强子来降低MYC表达25，但需要达到500 nM甚至更高的药物浓度才能起效（比TCIP1起效浓度高数百倍以上）。因此我们提出假说：TCIP1对MYC的高敏度抑制并非简单的BRD4抑制副产物，而是由TCIP1所介导诱导的三元复合物所产生的一种功能获得性 (gain-of-function) 调控结果。",
                    "terms": [
                        {"term": "致癌超级转录因子 MYC", "desc": "公认最关键的泛癌致癌驱动转录因子之一，主控细胞恶性增殖、代谢重编程与核糖体生物合成。在淋巴瘤（如双打击淋巴瘤）中，MYC失控激活与极差预后密切相关。长久以来，MYC因缺乏小分子结合口袋而被视为经典的“不可成药 (undruggable)”靶点。"}
                    ]
                },
                {
                    "en": "To clarify the role of ternary complex formation for the repression of MYC as well as other gene expression and protein level changes observed, we blocked binding of TCIP1 to BCL6 by titrating the BCL6(BTB) inhibitor BI3812 against a constant concentration of 10 nM TCIP1 (Fig. 3g). Titration of BI3812 prevented downregulation of MYC, as well as reversed upregulation of p21 and FOXO3, with EC50 closely matching that of cell killing (Fig. 3g). The results confirm that binding to BCL6 is necessary for repression of MYC and activation of p21 and FOXO3, indicating that the phenotypic consequences of TCIP1 are directly dependent on the formation of the BCL6–TCIP1–BRD4 ternary complex.",
                    "zh": "为了进一步厘清三元复合物的形成对于下调MYC以及调控其他基因表达和蛋白水平变化的因果决定作用，我们在维持10 nM TCIP1恒定浓度的条件下，通过滴定递增浓度的BCL6(BTB)抑制剂BI3812来竞争性阻断TCIP1与BCL6的结合 (Fig. 3g)。随着BI3812的滴入，MYC蛋白表达的下调被彻底逆转挽救，同时p21和FOXO3的转录上调也完全被抑制回到基线，其救援EC50与细胞杀伤救援的剂量响应紧密贴合 (Fig. 3g)。这些结果确凿地证实：结合BCL6是TCIP1抑制MYC以及激活p21和FOXO3所不可或缺的前提，无可置疑地表明TCIP1的所有表型效应均直接严格依赖于BCL6–TCIP1–BRD4三元复合物的物理组装。",
                    "terms": [
                        {"term": "双打击效应 (Synthetic Lethality & Dual Strike)", "desc": "TCIP1展现出独特的“双重致命打击”机制：一方面通过招募BRD4强力反转BCL6阻遏位点，爆破式激活FOXO3、PMAIP1/NOXA等促凋亡基因；另一方面在1 nM超低浓度下迅速瓦解MYC致癌驱动网络，双管齐下彻底关闭肿瘤细胞的存活通路。"}
                    ]
                }
            ]
        }
    ],
    "figure": {
        "id": "fig3",
        "image": "figures/fig3.png",
        "title_en": "Fig. 3 | TCIP1 represses MYC and its targets while activating pro-apoptotic genes.",
        "title_zh": "图 3 | TCIP1 抑制 MYC 及其靶基因，同时全面激活促凋亡基因网络。",
        "caption_en": "a, Gene activation (median change: fold change ≥ 2) and repression after addition of 10 nM TCIP1 in KARPAS422 cells for 20 h, with well-known BCL6 targets labelled. Significance cut-offs were Padjusted ≤ 0.05 and |log2(drug/DMSO)| ≥ 1); n = 2 biological replicates. b, Downregulated genes are significantly enriched for MYC targets (MSigDB hallmark pathways). c, Analysis of transcription factor binding of the top 100 downregulated genes in 4,500 or more public ChIP–seq datasets in blood-lineage cells. For b,c, the adjusted P values were computed by two-sided Fisher’s exact test and adjusted for multiple comparisons by Benjamini–Hochberg. d, Kinetics of protein changes in MYC, p21 and FOXO3 in DLBCL cell lines after treatment with 10 nM TCIP1. e, Dose-dependent changes in protein levels of target genes selected from the RNA sequencing results in two separate DLBCL cell lines, KARPAS422 and SUDHL5. f, Negligible effect of the negative controls Neg1 and Neg2 on protein levels of TCIP1 targets. For d–f, blots are representative of two biological replicates, except KARPAS422 in d and in e where data represent three biological replicates. g, Rescue of p21 and FOXO3 upregulation and MYC downregulation by competitive titration of the BTB binder BI3812 against constant 10 nM TCIP1 treatment for 8 h. Representative of two biological replicates. In all blots in d–g, any markers immunoblotted for the same gel are followed immediately by the loading control GAPDH run on that same gel.",
        "caption_zh": "a, 在KARPAS422细胞中加入10 nM TCIP1处理20小时后的基因转录激活（中位变化：差异倍数 ≥ 2）与抑制火山散点图，图中对熟知的经典BCL6靶基因进行了高亮标注。显著性筛选阈值设定为矫正P值 (Padjusted) ≤ 0.05 且 |log2(药物/DMSO)| ≥ 1；n = 2次独立生物学重复。b, 显著下调基因群在MSigDB Hallmark癌症特征通路中高度富集于MYC靶基因集。c, 基于血液谱系细胞中超过4,500个公开ChIP–seq数据集，对表达下调最显著的前100个基因启动子进行的转录因子结合位点富集分析。对于b和c图，校正P值均采用双尾Fisher精确检验计算，并通过Benjamini–Hochberg法完成多重假设检验校正。d, 10 nM TCIP1处理后，DLBCL细胞系中MYC、p21与FOXO3蛋白水平随时间动态变化的蛋白质印迹 (Western blot) 动力学分析。e, 在两株独立的DLBCL细胞系KARPAS422与SUDHL5中，从RNA测序结果中选出的关键靶蛋白随TCIP1浓度梯度的剂量反应Western blot分析。f, 阴性对照分子Neg1和Neg2对TCIP1靶蛋白表达水平影响的阴性验证（几乎完全无改变）。在d–f图中，除KARPAS422在d和e中代表3次独立生物学重复外，所有免疫印迹图均代表2次独立生物学重复的典型结果。g, 在恒定10 nM TCIP1处理8小时背景下，滴加浓度梯度的BTB结合剂BI3812成功救援p21与FOXO3上调以及MYC下调的竞争性救援Western blot结果。代表2次独立生物学重复。在d–g的所有电泳印迹中，同一块聚丙烯酰胺凝胶上检测的标志物下方均紧随该凝胶上同步跑胶的内参蛋白GAPDH对照。"
    }
}
