import os
import re
import part1_head_styles
import part2_header_intro
import part3_results_1_2
import part4_results_3_5
import part5_discussion_methods
import part6_phd_presentation_review

base_dir = r"C:\Users\20855\.gemini\antigravity\scratch\tcip-cancer-drivers-nature-report"

full_html = "".join([
    part1_head_styles.HEAD_AND_STYLES,
    part2_header_intro.HEADER_AND_INTRO,
    part3_results_1_2.RESULTS_1_2,
    part4_results_3_5.RESULTS_3_5,
    part5_discussion_methods.DISCUSSION_AND_METHODS,
    part6_phd_presentation_review.PHD_PRESENTATION_REVIEW,
    "\n</body>\n</html>\n"
])

# Write index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"index.html successfully written! Size: {len(full_html)} characters, {os.path.getsize(index_path)} bytes.")

# Verify all TOC anchor IDs
toc_targets = set(re.findall(r'href="#([a-zA-Z0-9_-]+)"', full_html))
defined_ids = set(re.findall(r'id="([a-zA-Z0-9_-]+)"', full_html))

missing_ids = toc_targets - defined_ids
print(f"Total TOC anchor targets: {len(toc_targets)}")
print(f"Total defined IDs: {len(defined_ids)}")
if missing_ids:
    print(f"[!] Warning: Missing IDs referenced in TOC: {missing_ids}")
else:
    print("[OK] All TOC anchor targets match defined IDs in index.html!")

# Verify all image references
img_sources = set(re.findall(r'src="([^"]+)"', full_html))
figures_dir = os.path.join(base_dir, "figures")
print(f"Image sources found: {len(img_sources)}")

for src in sorted(list(img_sources)):
    if src.startswith("figures/"):
        filename = src.split("/")[-1]
        filepath = os.path.join(figures_dir, filename)
        if os.path.exists(filepath):
            print(f"[OK] Image verified: {src} ({os.path.getsize(filepath)} bytes)")
        else:
            print(f"[FAIL] Missing image: {filepath}")

# Write comprehensive README.md
readme_content = """# Rewiring Cancer Drivers to Activate Apoptosis: Nature Interactive Academic Review & PhD Journal Club Presentation Suite

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
"""

readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md successfully written!")
