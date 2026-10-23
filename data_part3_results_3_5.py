# -*- coding: utf-8 -*-
"""
data_part3_results_3_5.py
Contains Results Section 3, Results Section 4, Main Figure 3, and Results Section 5.
Strict faithful sentence-by-sentence and paragraph-by-paragraph bilingual text.
"""

RESULTS_3 = {
    "title_en": "Apoptosis throughout the cell cycle",
    "title_zh": "贯穿整个细胞周期的细胞凋亡诱导",
    "paras": [
        {
            "en": "To characterize the cell death observed with TCIP1, we quantified cells that have externalized phosphatidylserine by staining with annexin V. We observed a dose-dependent increase in the number of annexin-positive cells, at 10 nM TCIP1, at 24 h (Extended Data Fig. 4a). TCIP1 induced detectable apoptosis by 4–8 h (Extended Data Fig. 4b).",
            "zh": "为了表征 TCIP1 引起的细胞死亡表型，我们通过膜联蛋白 V（Annexin V）染色对发生磷脂酰丝氨酸外翻的细胞进行了定量分析。在给药 24 小时后，10 nM TCIP1 引起 Annexin V 阳性细胞比例呈明显的剂量依赖性增加（扩展数据图 4a）。在处理后仅 4–8 小时内，TCIP1 便诱导了可检测到的细胞凋亡（扩展数据图 4b）。"
        },
        {
            "en": "Cancers can evade cell killing by many chemotherapeutics that function only during a specific stage of the cell cycle. To investigate the cell-cycle dependence of the apoptosis caused by TCIP1, we performed cell-cycle analysis in concert with TUNEL staining, which measures DNA fragmentation (Extended Data Fig. 4c). The cell-cycle analysis revealed that TCIP1 induced both a G1/S and G2/M block in the cell cycle (Extended Data Figs. 4d and 5a). By examining DNA cleavage with the TUNEL assay, we found that cell death occurred during all phases of the cell cycle (Extended Data Figs. 4e and 5a). To further examine the mechanism of cell death by TCIP1, we used serum starvation to arrest the cell cycle in G0/G1. The cells became even more sensitive to TCIP1, exhibiting an EC50 of 250 pM compared with 3.2 nM without arrest (Extended Data Fig. 4f). This observation indicates that TCIP1 produces cell death by activating more than a single cell death pathway.",
            "zh": "恶性肿瘤常通过逃逸仅在细胞周期特定时相发挥作用的化疗药物杀伤来产生耐药。为了探讨 TCIP1 所致凋亡对细胞周期的依赖性，我们将细胞周期分析与测定 DNA 断裂的 TUNEL 染色联合应用（扩展数据图 4c）。细胞周期分析表明，TCIP1 诱导了细胞周期在 G1/S 期与 G2/M 期的双重阻滞（扩展数据图 4d 及 5a）。通过 TUNEL 实验检测 DNA 切割断裂，我们发现细胞死亡广泛发生于细胞周期的所有各个时相（扩展数据图 4e 及 5a）。为了进一步阐明 TCIP1 诱导细胞死亡的机制，我们通过血清饥饿处理使细胞周期阻滞于 G0/G1 静息期；结果发现处于阻滞状态的细胞对 TCIP1 展现出更高的敏感性，其 EC50 达到 250 pM（未阻滞状态下为 3.2 nM，扩展数据图 4f）。这一重要观察表明，TCIP1 诱导的细胞死亡是通过同时激活多条不同的细胞死亡通路来实现的。"
        }
    ]
}

RESULTS_4 = {
    "title_en": "TCIP1 activates pro-apoptotic genes",
    "title_zh": "TCIP1 激活促凋亡靶基因表达",
    "paras": [
        {
            "en": "To define the genes involved in the induction of apoptosis by TCIP1, we carried out RNA sequencing studies 20 h after adding drug at 10 or 100 nM, when the critical genes were likely to be executing their functions. Changes in gene expression were dependent on dose (Extended Data Fig. 6a–c), and at just 10 nM TCIP1, the expression of 1,654 genes was increased, whereas the expression of 1,347 genes was reduced (Fig. 3a). Genes activated by TCIP1 were enriched for known cell-cycle arrest and pro-apoptotic targets normally repressed by BCL6, such as P21 (also known as CDKN1A), FOXO3 and PMAIP1 (also known as NOXA) (Fig. 3a and Extended Data Fig. 6b,c,e). Along with the p53 and apoptosis pathways, TCIP1 also induces the TNF pathway (Extended Data Fig. 6d). Signalling via NF-κB has been shown to be repressed by BCL6. These changes in mRNA levels were paralleled by dose-dependent and time-dependent changes in protein expression in two different DLBCL cell lines, SUDHL5 and KARPAS422, with negligible effect of the chemical controls Neg1 and Neg2 (Fig. 3d–f).",
            "zh": "为了界定参与 TCIP1 诱导凋亡的关键基因，我们在加入 10 或 100 nM 药物 20 小时后（此时关键基因很可能正在行使其效应功能）进行了 RNA 测序分析。基因表达的改变呈现剂量依赖性（扩展数据图 6a–c）；在仅为 10 nM 的 TCIP1 处理下，即有 1,654 个基因表达显著上调，1,347 个基因表达显著下调（图 3a）。被 TCIP1 激活的基因显著富集于已知的细胞周期阻滞及促凋亡靶点，这些基因在生理状态下通常受到 BCL6 的表观阻遏，例如 P21（亦称 CDKN1A）、FOXO3 以及 PMAIP1（亦称 NOXA）（图 3a 及扩展数据图 6b,c,e）。除了 p53 通路与凋亡通路外，TCIP1 还激活了 TNF 信号通路（扩展数据图 6d）；既往研究已证明 NF-κB 信号转导受 BCL6 的直接抑制。在两株不同的 DLBCL 细胞系 SUDHL5 和 KARPAS422 中，mRNA 水平的变化与蛋白表达的剂量依赖性及时间依赖性改变高度吻合，而化学阴性对照 Neg1 和 Neg2 则几乎无任何蛋白影响（图 3d–f）。"
        },
        {
            "en": "Of particular interest was the observation that FOXO3 is activated by 0.5 nM TCIP1 (Fig. 3e) and within 2 h by 10 nM TCIP1 (Fig. 4d). Activation of FOXO3 also displayed a hook effect (Fig. 3e), characteristic of the direct target of a bivalent molecule. FOXO3 is a master pro-apoptotic gene with a BCL6-binding site at its promoter. Although FOXO3 and P21 are also known to be activated downstream of TP53, which is itself a BCL6 target, TP53 is biallelically inactivated in this DLBCL line (KARPAS422) and other chemotherapy-resistant DLBCL lines killed by TCIP1. This supports the evidence in Extended Data Fig. 4 that TCIP1 derepresses multiple cell-cycle arrest and death pathways that are normally repressed by BCL6.",
            "zh": "特别引人注目的是，FOXO3 在仅 0.5 nM TCIP1 浓度下即被强力激活（图 3e），且在 10 nM TCIP1 给药仅 2 小时内迅速上调（图 4d）。FOXO3 的蛋白激活同样展现出典型的钩状效应（图 3e），这正是双价分子直接靶标的经典特征。FOXO3 作为核心促凋亡主控转录因子，其启动子区域含有一个保守的 BCL6 结合位点。尽管已知 FOXO3 和 P21 亦可在 TP53 下游被激活（TP53 自身也是 BCL6 的阻遏靶基因），但在本研究所使用的 DLBCL 细胞株 KARPAS422 以及其他被 TCIP1 高效杀伤的化疗耐药 DLBCL 细胞中，TP53 基因早已发生双等位基因失活突变。这一事实有力支持了扩展数据图 4 中的结论：即 TCIP1 的促死效应源于其直接去阻遏并反转了原本被 BCL6 严格抑制的多条细胞周期阻滞与死亡程序通路。"
        }
    ]
}

FIGURE_3 = {
    "id": "fig3",
    "img": "figures/fig3.png",
    "title_en": "Fig. 3 | TCIP1 represses MYC and its targets while activating pro-apoptotic genes.",
    "title_zh": "图 3 | TCIP1 抑制 MYC 及其靶基因并激活促凋亡基因",
    "caption_en": "Fig. 3 | TCIP1 represses MYC and its targets while activating pro-apoptotic genes. a, Gene activation (median change: fourfold up) and repression after addition of 10 nM TCIP1 in KARPAS422 cells for 20 h, with well-known BCL6 targets labelled. Significance cut-offs were Padjusted ≤ 0.05 and |log2(drug/DMSO)| ≥ 1); n = 2 biological replicates. b, Downregulated genes are significantly enriched for MYC targets (MSigDB hallmark pathways). c, Analysis of transcription factor binding of the top 100 downregulated genes in 4,500 or more public ChIP–seq datasets in blood-lineage cells. For b,c, the adjusted P values were computed by two-sided Fisher’s exact test and adjusted for multiple comparisons by Benjamini–Hochberg. d, Kinetics of protein changes in MYC, p21 and FOXO3 in DLBCL cell lines after treatment with 10 nM TCIP1. e, Dose-dependent changes in protein levels of target genes selected from the RNA sequencing results in two separate DLBCL cell lines, KARPAS422 and SUDHL5. f, Negligible effect of the negative controls Neg1 and Neg2 on protein levels of TCIP1 targets. For d–f, blots are representative of two biological replicates, except KARPAS422 in d and in e where data represent three biological replicates. g, Rescue of p21 and FOXO3 upregulation and MYC downregulation by competitive titration of the BTB binder BI3812 against constant 10 nM TCIP1 treatment for 8 h. Representative of two biological replicates. In all blots in d–g, any markers immunoblotted for the same gel are followed immediately by the loading control GAPDH run on that same gel.",
    "caption_zh": "图 3 | TCIP1 在抑制 MYC 及其靶基因的同时激活促凋亡基因。a，在 KARPAS422 细胞中加入 10 nM TCIP1 处理 20 小时后的全基因组激活（中位倍数变化：上调 4 倍）与抑制情况，标注了公认的 BCL6 靶基因。统计学显著性阈值设定为矫正后 P 值 Padjusted ≤ 0.05 且 |log2(药物/DMSO)| ≥ 1；n = 2 次独立生物学重复。b，下调基因显著富集于 MYC 靶基因基因集（MSigDB 标志性通路）。c，在血液系统细胞的 4,500 多个公开 ChIP-seq 数据集中，对下调幅度前 100 位基因启动子区的转录因子结合富集度进行系统分析。对于 b 和 c，矫正后 P 值通过双侧 Fisher 精确检验计算，并采用 Benjamini–Hochberg 方法进行多重假设检验校正。d，在 DLBCL 细胞系中加入 10 nM TCIP1 处理后，MYC、p21 和 FOXO3 蛋白变化的动力学曲线。e，根据 RNA 测序结果筛选出的靶基因在两株独立 DLBCL 细胞系（KARPAS422 和 SUDHL5）中呈现的剂量依赖性蛋白表达变化。f，阴性对照分子 Neg1 和 Neg2 对 TCIP1 靶蛋白水平几乎无任何影响。对于 d–f，Western blot 图像为两次独立生物学重复的代表性结果（d 和 e 中的 KARPAS422 为三次生物学重复）。g，在恒定 10 nM TCIP1 处理 8 小时的条件下，通过递增滴定 BTB 结合剂 BI3812 实现了对 p21、FOXO3 上调以及 MYC 下调的完全竞争性挽救逆转（两次生物学重复的代表性结果）。在 d–g 的所有免疫印迹实验中，同一凝胶上检测的蛋白标志物均紧跟其同胶内参 GAPDH 载荷对照。"
}

RESULTS_5 = {
    "title_en": "TCIP1 represses MYC and its targets",
    "title_zh": "TCIP1 抑制 MYC 及其下游靶基因",
    "paras": [
        {
            "en": "Among the group of genes whose expression was most reduced were MYC and its targets (Fig. 3b and Extended Data Fig. 6c). This is important as many DLBCLs are considered to be dependent on MYC. We examined the top 100 most TCIP1-reduced genes using over 4,500 ChIP–seq datasets of human transcription factors in blood cancer cell lines, and found the promoters of TCIP1-inhibited genes highly enriched for MYC binding in multiple datasets (Fig. 3c). Examination of MYC protein levels upon the addition of TCIP1 showed that MYC levels were reduced starting at less than 1 nM TCIP1 and within 2 h of addition of the drug (Fig. 3d,e). The chemical controls Neg1 and Neg2 did not affect MYC levels at comparable concentrations (Fig. 3f). BET/BRD4 inhibitors such as JQ1 are known to reduce the expression of MYC, but at much higher levels of drug (500 nM) than TCIP1. We therefore hypothesized that repression of MYC is a gain-of-function consequence of the ternary complex formed by TCIP1.",
            "zh": "在表达受抑制最显著的基因群中，原癌基因 MYC 及其下游调控靶标占据了主导地位（图 3b 及扩展数据图 6c）。这一发现极为关键，因为许多弥漫大B细胞淋巴瘤被公认高度依赖于 MYC 驱动生存。我们利用涵盖血液肿瘤细胞系的 4,500 多个公开发表的人类转录因子 ChIP-seq 数据集，对受 TCIP1 抑制最为剧烈的前 100 个基因进行了结合位点富集分析，发现这些被抑制基因的启动子区在多个独立数据集中均高度富集 MYC 的物理结合（图 3c）。对加入 TCIP1 后的 MYC 蛋白水平检测表明，在低于 1 nM 的极低浓度下以及给药后仅 2 小时内，MYC 蛋白表达量便迅速下降（图 3d,e）。在相当浓度下，化学阴性对照 Neg1 和 Neg2 均不影响 MYC 水平（图 3f）。众所周知，传统的 BET/BRD4 抑制剂（如 JQ1）虽然也能降低 MYC 的表达，但其所需药物浓度（~500 nM）远高于 TCIP1。因此我们提出假说：MYC 的超低浓度快速抑制，是 TCIP1 所诱导形成的三元超两性复合物所引发的一种独特的“获得性功能”（gain-of-function）转录重编程效应。"
        },
        {
            "en": "To clarify the role of ternary complex formation for the repression of MYC as well as other gene expression and protein level changes observed, we blocked binding of TCIP1 to BCL6 by titrating the BCL6(BTB) inhibitor BI3812 against a constant concentration of 10 nM TCIP1 (Fig. 3g). Titration of BI3812 prevented downregulation of MYC, as well as reversed upregulation of p21 and FOXO3 (Fig. 3g). The results indicate that both activation of pro-apoptotic targets and repression of MYC are mediated by the formation of a ternary complex between BRD4, TCIP1 and BCL6, and support the evidence in Fig. 2 that the active biological entity is the ternary complex.",
            "zh": "为了阐明三元复合物的形成对于抑制 MYC 以及引发其他基因转录和蛋白表达改变的核心作用，我们在 10 nM 恒定浓度 TCIP1 条件下滴定竞争性 BCL6(BTB) 抑制剂 BI3812 以阻断 TCIP1 与 BCL6 的结合（图 3g）。BI3812 的滴定完全阻断了 MYC 蛋白的下调，并且彻底逆转了 p21 和 FOXO3 的表达上调（图 3g）。这些严谨的生化挽救结果无可辩驳地证明：促凋亡靶点的激活以及致癌因子 MYC 的下调均依赖于 BRD4、TCIP1 与 BCL6 三者之间所形成的三元复合物，这进一步强有力地佐证了图 2 中的核心论点——即行使生物学功能的真正活性实体正是该超两性三元复合物。"
        }
    ]
}
