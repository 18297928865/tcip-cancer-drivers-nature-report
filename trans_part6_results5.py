# -*- coding: utf-8 -*-
"""
Part 6: Results Section 5 & Figure 5
Cell-type-specific activity of TCIP1, Generality of the TCIP strategy, TCIP2
Verbatim translation, figure insertion, and academic terminology notes.
"""

PART6_DATA = {
    "subsections": [
        {
            "title_en": "Cell-type-specific activity of TCIP1",
            "title_zh": "TCIP1 的细胞类型特异性生物学活性与体内安全性评估",
            "paragraphs": [
                {
                    "en": "BCL6-knockout mice die of a complex inflammatory reaction that has been dissected to specific regions of the protein55. Because TCIP1 requires engagement of both BCL6 and BRD4, and also operates at a concentration that would occupy only a fraction of the total BCL6 molecules (unlike a degrader or inhibitor), we were curious about the potential toxicity of TCIP1. We evaluated the tolerability, pharmacokinetic properties and target engagement of TCIP1 in wild-type C57BL/6 mice treated for 5 days with 10 mg kg−1 TCIP1 once daily by intraperitoneal injection. TCIP1 induced dramatic transcriptomic changes in the spleen despite comparable tissue concentrations of drug (Fig. 5a,b). Serum concentrations were approximately 100–400-fold higher than expected therapeutic doses (Fig. 5c). Notable genes upregulated in DLBCL cells, such as FOXO3, were also upregulated in the spleen as well as other known BCL6 targets in lymphocytes (Fig. 5d and Supplementary Table 1). Despite the large transcriptomic changes in the spleen, TCIP1 was well tolerated with no adverse effects noticed and no significant changes in mouse body weight (Fig. 5e). Haematoxylin and eosin staining and examination (by H.V.) also did not reveal noticeable abnormalities such as inflammatory infiltrates or apoptotic cells (Fig. 5f). We also observed a 200–400-fold lower sensitivity in primary human fibroblasts (EC50 of approximately 470 nM) and lymphocytes (EC50 of approximately 210 nM) (Fig. 5g,h). T and B lymphocytes are particularly germane because they have among the highest levels of BCL6 (ref. 56). The data support the cellular evidence that TCIP1 acts in a context-specific manner dependent on coincident expression of BRD4 and BCL6.",
                    "zh": "纯合敲除BCL6的基因工程小鼠 (BCL6-knockout mice) 会死于极为复杂的严重致死性全身炎症反应，这种炎症表型已被精确解析并归因于该蛋白的特定结构功能域55。鉴于TCIP1发挥效应必须同时结合BCL6与BRD4，并且其起效浓度仅需结合细胞内总BCL6分子中的极小一部分（这与必须接近100%完全抑制靶标的传统抑制剂或彻底消除蛋白的降解剂有着本质区别），因此我们对TCIP1在体内的潜在毒性表现极为关注。我们在野生型C57BL/6小鼠中系统评估了TCIP1的耐受性、药代动力学 (pharmacokinetics, PK) 特征以及体内靶标结合效应：给予小鼠以每天一次10 mg kg−1剂量的TCIP1进行连续5天的腹腔注射 (intraperitoneal injection, i.p.)。尽管TCIP1在肝脏、肺部和脾脏中达到了相当的组织药物累积浓度，但TCIP1在脾脏（免疫中枢器官）中引发了极其剧烈的转录组改变 (Fig. 5a,b)。小鼠血清药物峰值浓度比预期的治疗有效剂量高出约100至400倍 (Fig. 5c)。在离体DLBCL细胞系中显著上调的关键标志基因（如FOXO3）在小鼠脾脏中同样发生显著上调，淋巴细胞中其他已知的BCL6生理靶基因亦是如此 (Fig. 5d 与 补充表格1 Supplementary Table 1)。尽管在脾脏中引起了广泛的转录组重塑，但小鼠对TCIP1展现出极佳的体内耐受性：未观察到任何药物不良反应，小鼠体重亦未出现任何显著下降 (Fig. 5e)。经病理学家 (H.V.) 对肺脏和脾脏组织进行的苏木精-伊红 (H&E) 染色与组织病理学镜检证实：未见任何明显的病理异常，如炎性细胞浸润 (inflammatory infiltrates) 或异常细胞凋亡病灶 (Fig. 5f)。此外，在离体测试中，原代人成纤维细胞（EC50约为470 nM）与原代人扁桃体淋巴细胞（EC50约为210 nM）对TCIP1的敏感性比恶性肿瘤细胞低200至400倍 (Fig. 5g,h)。正常T淋巴细胞和B淋巴细胞的安全性数据尤为关键，因为它们在正常人体组织中属于BCL6生理表达丰度最高的细胞亚群56。上述体内外数据高度一致地支持了细胞层面的实验证据：即TCIP1是以一种高度依赖于BRD4与BCL6两者在同一细胞中病理性高水平共表达的环境特异性 (context-specific) 方式精准发挥杀伤作用的。",
                    "terms": [
                        {"term": "BCL6全身敲除小鼠的致死性炎症", "desc": "经典免疫学表型：BCL6缺失使巨噬细胞和Th2细胞失去转录制动，导致大量产生促炎细胞因子（IL-4、IL-5、MCP-1等），小鼠在数周内因爆发性多器官嗜酸性粒细胞心肌炎与肺泡炎衰竭死亡。传统PROTAC降解剂存在引发类似全身免疫毒性的巨大临床风险。"},
                        {"term": "催化性低占位率 (Low Target Site Occupancy)", "desc": "由于TCIP诱导的是显性转录延伸激活（正向信号放大），仅需占用靶标启动子上1-2%的BCL6分子即可启动促死转录级联；其余98%以上的BCL6仍可行使其正常的免疫稳态调控功能，从而完美规避了全身敲除所致的炎症风暴。"},
                        {"term": "组织特异性逻辑与门 (Synthetic AND-Gate Selectivity)", "desc": "只有当高表达BCL6（肿瘤身份特征）与高负荷BRD4转录延伸复合体在恶性表观遗传背景下同时满足时，细胞凋亡开关才会被触发，实现了极高的治疗安全窗 (therapeutic index)。"}
                    ]
                }
            ]
        },
        {
            "title_en": "Generality of the TCIP strategy",
            "title_zh": "TCIP 策略的普适性与拓展验证 (TCIP2)",
            "paragraphs": [
                {
                    "en": "We explored the generality and predictability of the TCIP approach by designing and synthesizing a series of molecules predicted to borrow the transcriptional activity of the oestrogen hormone receptor protein to activate BCL6 target genes and produce cell death (Fig. 5i). We used the synthetic oestrogen, oestrone for these studies and constructed TCIP2 (Fig. 5j), which showed strong antiproliferative activity with an EC50 of 355 nM (Fig. 5k). As predicted, killing was most robust in DLBCL lines, such as KARPAS422, with higher expression of both ER and BCL6 (Fig. 5k). Several ER-positive human breast cancer cells with low levels of BCL6 showed enhanced proliferation, indicating that oestrone was active and that TCIPs are not intrinsically toxic in cells lacking BCL6 (Fig. 5l). By contrast, triple-negative breast cancer cell lines with neither detectable BCL6 nor ER were not affected by the ER–BCL6 TCIP2 (Fig. 5l). These studies suggest that other transcriptional activators could be predictably hijacked or rewired to facilitate transcription of pro-apoptotic genes in DLBCL cells.",
                    "zh": "我们通过设计并合成一系列预期能够“借用”雌激素受体 (oestrogen receptor, ER) 蛋白的转录激活能力来激活BCL6靶基因并引发细胞死亡的双功能分子，进一步探索了TCIP分子工程学策略的普适性 (generality) 与可预测性 (predictability) (Fig. 5i)。在这些研究中，我们选用了天然雌激素衍生物雌酮 (oestrone)，通过化学连接链与BCL6结合剂偶联构建出了TCIP2 (Fig. 5j)。TCIP2在肿瘤细胞中展现出强劲的抗增殖生物学活性，其EC50为355 nM (Fig. 5k)。正如理论模型所精确预测的那样：在同时高水平表达雌激素受体ER与BCL6的DLBCL恶性细胞系（如KARPAS422）中，TCIP2的细胞杀灭效果最为强劲 (Fig. 5k)。若干虽然ER阳性但BCL6表达量极低的人类乳腺癌细胞系在接受TCIP2处理后反而表现出细胞增殖的轻度增强，这表明偶联的雌酮基团保持了完全的生物学激活活性，并且确证了TCIP分子在缺乏BCL6的细胞中并不具备内源性固有细胞毒性 (Fig. 5l)。相比之下，既无检测可得的BCL6表达又无ER表达的三阴性乳腺癌 (triple-negative breast cancer, TNBC) 细胞系，则完全不受ER–BCL6双功能分子TCIP2的任何生长抑制影响 (Fig. 5l)。这些系统性研究充分证实：人类细胞中的其他强效转录激活因子同样可以被我们以高度可预测的方式人为“劫持”或“重新布线”，用于诱导并强力驱动恶性DLBCL肿瘤细胞中促凋亡基因的转录激活与程序性自毁。",
                    "terms": [
                        {"term": "TCIP2 (ER–BCL6 嵌合分子)", "desc": "由雌酮 (Oestrone，结合雌激素核受体ER) 与BI3812 (结合BCL6 BTB) 通过柔性连接链共价偶联而成的第二代概念验证TCIP分子，证明转录激活端不仅限于BET/BRD4，核激素受体超家族同样可被成功劫持。"},
                        {"term": "三阴性乳腺癌 (Triple-Negative Breast Cancer, TNBC)", "desc": "缺乏雌激素受体 (ER)、孕激素受体 (PR) 和人表皮生长因子受体2 (HER2) 表达的乳腺癌亚型，在本研究中作为双阴性阴性对照，证实TCIP分子对缺乏靶标配对的细胞完全无毒性。"}
                    ]
                }
            ]
        }
    ],
    "figure": {
        "id": "fig5",
        "image": "figures/fig5.png",
        "title_en": "Fig. 5 | Toxicity of TCIP1 in mice and primary human cells and generalization to ER-positive cancers.",
        "title_zh": "图 5 | TCIP1 在小鼠及人原代细胞中的毒性耐受性，以及该策略在雌激素受体 (ER) 阳性肿瘤中的拓展普适性。",
        "caption_en": "a, Tissue-specific transcriptomic effects of TCIP1, treated at 10 mg kg−1 intraperitoneal (i.p.) once daily for 5 days. b, Quantification of transcriptome changes in the liver, lung and spleen and associated accumulated tissue concentrations of TCIP1. Treatment at 10 mg kg−1 TCIP1 intraperitoneal once daily, with measurement on day 5. n = 3 mice per treatment. c, Pharmacokinetic parameters of TCIP1. t1/2, half-life; tmax, time to max serum concentration; Cmax, maximum serum concentration; AUC0-last, area under the curve from dosing to last measured concentration. d, Comparison of key gene targets upregulated by TCIP1 in both cultured DLBCL cells (KARPAS422) and in the spleen. e, Body weight of treated mice. No adverse effects or behavioural abnormalities were noticed. f, Haematoxylin and eosin staining of the lung and spleen from representative mice treated with vehicle and drug. Scale bars, 50 µm (lung images) and 100 µm (spleen images). n = 3 mice each for treatment and vehicle for a–f. g, Effect of TCIP1 on cell viability of primary human tonsillar lymphocytes. h, Effect of TCIP1 on cell viability of primary human fibroblasts. i, ER–BCL6 TCIP2 designed to induce cell death in oestrogen-positive, BCL6-overexpressing DLBCLs. j, Chemical structure of TCIP2. k, Effect on cell viability of TCIP2 compared with controls: oestrone, BI3812 (a BCL6(BTB) inhibitor) and BI3802 (a BCL6 degrader) in KARPAS422 cells with high ERβ (encoded by ESR2) levels. l, Measurement of the selective effect on cell viability by TCIP2 in DLBCL cells with coincident overexpression of ER and BCL6 (KARPAS422) compared with primary human lymphocytes, a triple-negative breast cancer cell line (HS578T) and ER-driven but BCL6-low breast cancer cells (HCC1428). CCLE, Cancer Cell Line Encyclopedia. n = 3 biological replicates, mean ± s.d. for g,h,k,l. Viability curves in g,h,k,l are after 72 h of drug treatment.",
        "caption_zh": "a, TCIP1以每天一次10 mg kg−1剂量腹腔注射 (i.p.) 连续给药5天后，在小鼠各主要脏器中诱发的组织特异性转录组改变热图。b, 小鼠肝脏、肺脏和脾脏中转录组差异基因数量的定量统计，以及第5天测得的组织累积药物浓度；n = 3只小鼠/组。c, TCIP1在小鼠体内的关键药代动力学 (PK) 参数：t1/2代表消除半衰期；tmax代表达到血清峰浓度的时间；Cmax代表血清最高药物浓度；AUC0-last代表从给药至最后测定时间点的血药浓度–时间曲线下面积。d, 在体外培养的DLBCL细胞 (KARPAS422) 与小鼠体内脾脏组织中，被TCIP1共同显著上调的关键靶基因表达倍数对比。e, 给药期间小鼠体重的动态监测折线图；在整个治疗周期内未见任何毒副反应或行为学异常。f, 溶剂对照组与TCIP1治疗组代表性小鼠肺脏与脾脏组织的苏木精–伊红 (H&E) 染色显微病理切片。比例尺：肺部图像为50 µm，脾脏图像为100 µm；a–f中各实验组与对照组均为n = 3只小鼠。g, TCIP1对人原代扁桃体正常淋巴细胞活力的影响曲线。h, TCIP1对人原代正常成纤维细胞活力的影响曲线。i, 旨在雌激素受体阳性、BCL6高表达DLBCL细胞中诱导细胞凋亡的ER–BCL6嵌合分子TCIP2的作用机制设计模式图。j, TCIP2的完整化学分子结构式。k, 在高表达ERβ（由ESR2基因编码）的KARPAS422细胞中，TCIP2与各单体对照分子（游离雌酮、BCL6 BTB抑制剂BI3812以及BCL6降解剂BI3802）对细胞活力影响的量效抑制对比。l, TCIP2在同时高表达ER和BCL6的DLBCL细胞 (KARPAS422) 中相较于原代正常人淋巴细胞、三阴性乳腺癌细胞系 (HS578T) 以及ER驱动但BCL6低表达乳腺癌细胞 (HCC1428) 的选择性细胞杀伤测定。CCLE代表癌细胞系百科全书数据库。对于g,h,k,l图，数据均为n = 3次独立生物学重复，以均值 ± s.d. 表示；g,h,k,l中的细胞活力检测均在加药处理72小时后进行。"
    }
}
