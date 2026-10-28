# Rewiring Cancer Drivers to Activate Apoptosis: Nature Interactive Academic Review & PhD Journal Club Presentation Suite[(https://18297928865.github.io/tcip-cancer-drivers-nature-report/)]

[![Nature](https://img.shields.io/badge/Nature-10.1038%2Fs41586--023--06348--2-E60000.svg)](https://doi.org/10.1038/s41586-023-06348-2)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-blue.svg)](https://18297928865.github.io/tcip-cancer-drivers-nature-report/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An interactive, scholarly, bilingual (English & Chinese) review website and master PhD Journal Club presentation suite for the landmark *Nature* paper:
> **Rewiring cancer drivers to activate apoptosis**  
> *Nature* 620, 417–427 (10 August 2023).  
> **Authors**: Sai Gourisankar, Andrey Krokhotin, Wenzhi Ji (季文智), Nathanael S. Gray, Gerald R. Crabtree et al.  
> **Affiliations**: Stanford University School of Medicine, MD Anderson Cancer Center, Howard Hughes Medical Institute (HHMI).

---

## 🌟 Highlights & Key Features

- **Nature-Benchmark Visual Hierarchy**: Custom Nature Crimson & Deep Slate design, dual-language bilingual layout, sticky scroll-spy navigation, real-time reading progress bar, and interactive lightbox zoom for all 14 figures.
- **Complete Figure Coverage**: Exhaustive multi-paragraph bilingual analyses for all 5 Main Figures and 9 Extended Data Figures (`fig1`–`fig5`, `ed_fig1`–`ed_fig9`).
- **Deep Mechanistic Breakdown**:
  1. **Gain-of-Function vs. Loss-of-Function**: Inverting oncogenic BCL6 repression into dominant-positive pro-apoptotic transcriptional driving.
  2. **1.3 nM Super-Potency & Catalytic Low Occupancy**: Overcoming >10 μM inactive monomers; triggering apoptosis with only 1–2% target site occupancy.
  3. **15-Minute Pol II Ser2 Pause-Release**: Direct recruitment of CDK9/P-TEFb and runaway inversion of the BCL6 Intron 1 negative autoregulatory loop.
  4. **Dominant-Positive Phenotype in Trans**: Sparing neither heterozygous mutant cells nor escape pathways.
  5. **Synthetic AND-Gate Selectivity**: Normal fibroblasts, lymphocytes, and C57BL/6 mice show zero organ toxicity at 10 mg/kg/day.
- **30-Year Proximity Pharmacology Evolution**:
  - Full timeline & multi-dimensional comparative matrix: CID (1993) → PROTAC (2001) → Molecular Glue (2014) → LYTAC/AUTAC (2020) → TCIP (2023).
- **PhD Journal Club Presentation Suite**:
  - **Slides 1–8**: 16–18 minute turnkey presentation script with English spoken narration and scholarly Chinese commentary.
  - **Top 5 Defense Q&As**: Model answers addressing the in vivo Hook effect, normal GC B cell sparing, apoptosis vs. MYC activation, TCIP vs. PROTAC degraders, and clinical resistance mitigations.

---

## 🗂️ Project Structure

```text
tcip-cancer-drivers-nature-report/
├── index.html                   # Complete compiled interactive webpage (96KB+)
├── figures/                     # 14 high-resolution paper figures
│   ├── fig1.png ~ fig5.png      # Nature Main Figures 1 to 5
│   └── ed_fig1.png ~ ed_fig9.png# Extended Data Figures 1 to 9
├── assemble.py                  # HTML compilation & verification script
├── part1_head_styles.py         # Head, responsive CSS, typography, top navbar
├── part2_header_intro.py        # Hero banner, abstract, background & BCL6 biology
├── part3_results_1_2.py         # Results Section 1 & 2 (TCIP1 design, PRISM, ternary complex)
├── part4_results_3_5.py         # Results Section 3 to 5 (PRO-seq, Pol II pause-release, in vivo PK/PD, TCIP2)
├── part5_discussion_methods.py  # Discussion, LoF vs GoF paradigm, STAR Methods
├── part6_phd_presentation_review.py # PhD Journal Club Suite (Slides 1-8, Q&As 1-5, JS)
└── README.md                    # Project documentation
```

---

## 🚀 Local Preview

Simply open `index.html` in any modern web browser:
```bash
# On Windows PowerShell
Start-Process index.html

# Or via Python local HTTP server
python -m http.server 8080
# Visit http://localhost:8080 in your browser
```

---

## 📖 Citation

```bibtex
@article{Gourisankar2023TCIP,
  title={Rewiring cancer drivers to activate apoptosis},
  author={Gourisankar, Sai and Krokhotin, Andrey and Ji, Wenzhi and Hurtado, Ana M. and 
          Dey, Bappaditya and Gray, Nathanael S. and Crabtree, Gerald R.},
  journal={Nature},
  volume={620},
  number={7973},
  pages={417--427},
  year={2023},
  publisher={Nature Publishing Group},
  doi={10.1038/s41586-023-06348-2}
}
```

---

## 📜 License
This project is open-sourced under the MIT License for educational, academic journal club, and research discussion purposes. All original paper figures and experimental data remain the intellectual property of Springer Nature and the authors.
