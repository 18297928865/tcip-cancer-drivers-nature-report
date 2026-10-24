# -*- coding: utf-8 -*-
import os
import re
import html
import trans_part1_intro
import trans_part2_results1
import trans_part3_results2
import trans_part4_results3
import trans_part5_results4
import trans_part6_results5
import trans_part7_discussion
import trans_part8_methods
import trans_part9_extended_data
import part6_phd_presentation_review

base_dir = r"C:\Users\20855\.gemini\antigravity\scratch\tcip-cancer-drivers-nature-report"

def linkify_citations(text):
    if not text:
        return ""
    def replace_ed(m):
        raw = m.group(0)
        num_m = re.search(r'Extended Data Fig\.\s*(\d+)', raw, re.IGNORECASE)
        if num_m:
            fig_num = num_m.group(1)
            return f'<a href="#ed-fig{fig_num}" class="fig-ref-pill ed-ref" onclick="jumpToFig(\'ed-fig{fig_num}\')">{raw}</a>'
        return raw

    def replace_main(m):
        raw = m.group(0)
        num_m = re.search(r'Fig\.\s*(\d+)', raw)
        if num_m:
            fig_num = num_m.group(1)
            return f'<a href="#fig{fig_num}" class="fig-ref-pill main-ref" onclick="jumpToFig(\'fig{fig_num}\')">{raw}</a>'
        return raw

    text = re.sub(r'Extended Data Fig\.\s*\d+[a-z,\s\-]*(?=[^\w\-]|$)', replace_ed, text, flags=re.IGNORECASE)
    text = re.sub(r'(?<!Extended Data )Fig\.\s*\d+[a-z,\s\-]*(?=[^\w\-]|$)', replace_main, text)
    return text

def render_terms(terms):
    if not terms:
        return ""
    chips = []
    for t in terms:
        name = html.escape(t.get('term', ''))
        desc = html.escape(t.get('desc', ''))
        chips.append(f'''
        <div class="term-badge">
            <span class="term-name"><i class="fas fa-book-medical"></i> {name}</span>
            <span class="term-desc">{desc}</span>
        </div>''')
    return f'<div class="terms-container">{"".join(chips)}</div>'

def render_paragraph(p, idx):
    en_html = linkify_citations(p.get('en', ''))
    zh_html = linkify_citations(p.get('zh', ''))
    terms_html = render_terms(p.get('terms', []))
    
    return f'''
    <div class="bilingual-block" id="p-block-{idx}">
        <div class="text-col en-col">
            <div class="lang-tag"><i class="fas fa-globe-americas"></i> English Original</div>
            <p class="para-text en-text">{en_html}</p>
        </div>
        <div class="text-col zh-col">
            <div class="lang-tag"><i class="fas fa-language"></i> 中文逐句精准翻译</div>
            <p class="para-text zh-text">{zh_html}</p>
        </div>
        {terms_html}
    </div>'''

def render_figure(fig):
    if not fig:
        return ""
    fig_id = fig.get('id', '')
    img_path = fig.get('image', '')
    title_en = fig.get('title_en', '')
    title_zh = fig.get('title_zh', '')
    caption_en = linkify_citations(fig.get('caption_en', ''))
    caption_zh = linkify_citations(fig.get('caption_zh', ''))
    
    return f'''
    <div class="figure-card" id="{fig_id}">
        <div class="figure-header">
            <div class="fig-badge"><i class="fas fa-chart-line"></i> {fig_id.upper()}</div>
            <div class="fig-titles">
                <h4 class="fig-title-en">{title_en}</h4>
                <h4 class="fig-title-zh">{title_zh}</h4>
            </div>
            <button class="zoom-btn" onclick="openLightbox('{img_path}', '{title_en}', '{fig_id}')">
                <i class="fas fa-search-plus"></i> 查看高清大图
            </button>
        </div>
        <div class="figure-image-wrapper" onclick="openLightbox('{img_path}', '{title_en}', '{fig_id}')">
            <img src="{img_path}" alt="{title_en}" class="paper-figure" loading="lazy">
            <div class="image-overlay"><i class="fas fa-expand"></i> 点击全屏缩放查看</div>
        </div>
        <div class="figure-caption">
            <div class="caption-tab-btns">
                <button class="cap-btn active" onclick="switchCapTab(this, '{fig_id}-zh')">中文图解与分析</button>
                <button class="cap-btn" onclick="switchCapTab(this, '{fig_id}-en')">Original English Caption</button>
            </div>
            <div class="caption-content active" id="{fig_id}-zh">
                <p>{caption_zh}</p>
            </div>
            <div class="caption-content" id="{fig_id}-en">
                <p>{caption_en}</p>
            </div>
        </div>
    </div>'''

def render_extended_figure(fig):
    fig_id = fig.get('id', '')
    num = fig.get('number', '')
    img_path = fig.get('image', '')
    title_en = fig.get('title_en', '')
    title_zh = fig.get('title_zh', '')
    caption_en = linkify_citations(fig.get('caption_en', ''))
    caption_zh = linkify_citations(fig.get('caption_zh', ''))
    terms_html = render_terms(fig.get('terms', []))
    
    return f'''
    <div class="figure-card ed-figure-card" id="{fig_id}">
        <div class="figure-header">
            <div class="fig-badge ed-badge"><i class="fas fa-microscope"></i> EXTENDED DATA {num}</div>
            <div class="fig-titles">
                <h4 class="fig-title-en">{title_en}</h4>
                <h4 class="fig-title-zh">{title_zh}</h4>
            </div>
            <button class="zoom-btn" onclick="openLightbox('{img_path}', '{title_en}', '{fig_id}')">
                <i class="fas fa-search-plus"></i> 高清缩放
            </button>
        </div>
        <div class="figure-image-wrapper" onclick="openLightbox('{img_path}', '{title_en}', '{fig_id}')">
            <img src="{img_path}" alt="{title_en}" class="paper-figure" loading="lazy">
            <div class="image-overlay"><i class="fas fa-expand"></i> 点击全屏查看补充数据</div>
        </div>
        <div class="figure-caption">
            <div class="caption-tab-btns">
                <button class="cap-btn active" onclick="switchCapTab(this, '{fig_id}-zh')">中文图解详注</button>
                <button class="cap-btn" onclick="switchCapTab(this, '{fig_id}-en')">Original English Caption</button>
            </div>
            <div class="caption-content active" id="{fig_id}-zh">
                <p>{caption_zh}</p>
            </div>
            <div class="caption-content" id="{fig_id}-en">
                <p>{caption_en}</p>
            </div>
        </div>
        {terms_html}
    </div>'''

print("Step 1 helper functions loaded.")

# CSS and HTML Skeleton
HTML_HEADER = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nature 重磅精读: 重编程癌症驱动因子以激活凋亡程序 (TCIP1/BCL6 双功能邻近分子)</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+SC:wght@400;600;700&family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    :root {
      --primary: #9b111e;         /* Nature classic burgundy */
      --primary-dark: #660b13;
      --primary-light: #c41e3a;
      --primary-subtle: #fff5f5;
      --navy: #0f172a;
      --navy-light: #1e293b;
      --slate: #334155;
      --slate-light: #64748b;
      --bg-page: #f8fafc;
      --bg-card: #ffffff;
      --border: #e2e8f0;
      --border-focus: #fecdd3;
      --accent: #2563eb;
      --accent-bg: #eff6ff;
      --pill-bg: #f1f5f9;
      --pill-border: #cbd5e1;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --gold: #b45309;
      --gold-bg: #fef3c7;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Noto Sans SC", sans-serif;
      color: var(--text-main);
      background-color: var(--bg-page);
      line-height: 1.8;
      font-size: 15.5px;
      -webkit-font-smoothing: antialiased;
    }

    /* Reading Progress Bar */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3.5px;
      background: linear-gradient(90deg, #9b111e, #e11d48, #f59e0b);
      z-index: 99999;
      width: 0%;
      transition: width 0.1s ease;
    }

    /* Top Navbar */
    .top-navbar {
      position: sticky;
      top: 0;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      z-index: 1000;
      padding: 0 24px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: var(--shadow-sm);
    }
    .nav-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: var(--navy);
      font-weight: 700;
    }
    .brand-logo {
      background: var(--primary);
      color: #fff;
      font-family: 'Merriweather', serif;
      font-weight: 700;
      font-size: 14px;
      padding: 4px 9px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .brand-title {
      font-size: 14px;
      font-weight: 600;
      color: var(--navy);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 480px;
    }

    .nav-controls {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .mode-btn {
      border: 1px solid var(--border);
      background: #fff;
      color: var(--slate);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .mode-btn:hover {
      background: #f1f5f9;
      color: var(--navy);
      border-color: #cbd5e1;
    }
    .mode-btn.active {
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }

    /* Main Container & Layout */
    .app-container {
      display: flex;
      max-width: 1540px;
      margin: 0 auto;
      padding: 24px 20px;
      gap: 32px;
    }

    /* Sidebar TOC */
    .toc-sidebar {
      width: 290px;
      flex-shrink: 0;
      position: sticky;
      top: 80px;
      height: calc(100vh - 100px);
      overflow-y: auto;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 16px;
      box-shadow: var(--shadow-sm);
    }
    .toc-title {
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .toc-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .toc-link {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 10px;
      font-size: 13px;
      color: var(--slate);
      text-decoration: none;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
      line-height: 1.4;
    }
    .toc-link:hover {
      background: #f1f5f9;
      color: var(--primary);
      padding-left: 14px;
    }
    .toc-link.active {
      background: var(--primary-subtle);
      color: var(--primary);
      font-weight: 600;
      border-left: 3px solid var(--primary);
    }
    .toc-badge {
      font-size: 10px;
      background: #e2e8f0;
      color: #475569;
      padding: 1px 6px;
      border-radius: 10px;
      font-weight: 600;
    }

    /* Content Area */
    .main-content {
      flex: 1;
      min-width: 0;
      max-width: 1140px;
    }

    /* Paper Header Card */
    .paper-header {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 36px 36px 28px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }
    .paper-header::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: linear-gradient(90deg, #9b111e, #c41e3a, #e11d48);
    }
    .journal-meta {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      margin-bottom: 18px;
    }
    .journal-badge {
      background: var(--primary);
      color: #ffffff;
      padding: 3px 10px;
      border-radius: 4px;
      font-weight: 700;
      letter-spacing: 0.5px;
      font-family: 'Merriweather', serif;
    }
    .meta-item {
      color: var(--slate-light);
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .paper-title-en {
      font-family: 'Merriweather', Georgia, serif;
      font-size: 28px;
      line-height: 1.35;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 12px;
    }
    .paper-title-zh {
      font-size: 22px;
      font-weight: 600;
      line-height: 1.45;
      color: var(--primary);
      margin-bottom: 22px;
    }
    .authors-block {
      background: #f8fafc;
      border-left: 3px solid var(--primary);
      padding: 16px 20px;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      font-size: 13.5px;
      margin-bottom: 24px;
    }
    .author-names {
      font-weight: 600;
      color: var(--navy);
      margin-bottom: 6px;
    }
    .author-affils {
      color: var(--slate);
      line-height: 1.6;
    }

    /* Executive highlights card */
    .highlights-box {
      background: linear-gradient(135deg, #fffaf0 0%, #fef3c7 100%);
      border: 1px solid #fde68a;
      border-radius: var(--radius-md);
      padding: 20px;
      margin-top: 20px;
    }
    .highlights-title {
      font-size: 14.5px;
      font-weight: 700;
      color: #92400e;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .highlights-list {
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      font-size: 13px;
      color: #78350f;
    }
    .highlight-card {
      background: rgba(255, 255, 255, 0.7);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .highlight-card strong {
      color: #92400e;
      display: block;
      margin-bottom: 4px;
    }

    /* Section Structure */
    .article-section {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 32px;
      margin-bottom: 28px;
      box-shadow: var(--shadow-sm);
      scroll-margin-top: 80px;
    }
    .section-header {
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 16px;
      margin-bottom: 24px;
    }
    .section-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      background: #f1f5f9;
      color: var(--slate);
      padding: 3px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
    }
    .section-title-en {
      font-family: 'Merriweather', Georgia, serif;
      font-size: 22px;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 6px;
    }
    .section-title-zh {
      font-size: 18px;
      font-weight: 600;
      color: var(--primary);
    }
    .subsection-divider {
      margin: 32px 0 20px;
      padding-top: 16px;
      border-top: 1px dashed var(--border);
    }
    .subsection-title-en {
      font-family: 'Merriweather', serif;
      font-size: 17.5px;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 4px;
    }
    .subsection-title-zh {
      font-size: 15.5px;
      font-weight: 600;
      color: #8b0000;
      margin-bottom: 16px;
    }

    /* Bilingual Paragraph Block */
    .bilingual-block {
      background: #fafbfc;
      border: 1px solid #eef2f6;
      border-radius: var(--radius-md);
      padding: 18px 20px;
      margin-bottom: 20px;
      transition: all 0.2s ease;
    }
    .bilingual-block:hover {
      background: #ffffff;
      border-color: #cbd5e1;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.04);
    }
    .bilingual-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .text-col {
      position: relative;
    }
    .lang-tag {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--slate-light);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .para-text {
      line-height: 1.85;
      font-size: 15px;
    }
    .en-text {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: #334155;
    }
    .zh-text {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
      color: #1e293b;
    }

    /* Single Column Modes */
    body.mode-zh .en-col { display: none !important; }
    body.mode-zh .bilingual-grid { grid-template-columns: 1fr !important; }
    body.mode-en .zh-col { display: none !important; }
    body.mode-en .bilingual-grid { grid-template-columns: 1fr !important; }

    /* Terms Chips */
    .terms-container {
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px dotted #e2e8f0;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .term-badge {
      display: inline-flex;
      flex-direction: column;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-left: 3px solid var(--primary);
      border-radius: 4px;
      padding: 4px 10px;
      font-size: 12px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .term-name {
      font-weight: 600;
      color: var(--primary);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
    }
    .term-desc {
      color: var(--slate);
      font-size: 11px;
      line-height: 1.4;
      margin-top: 2px;
    }

    /* Figure Citation Pills */
    .fig-ref-pill {
      display: inline-flex;
      align-items: center;
      padding: 1px 7px;
      margin: 0 2px;
      border-radius: 4px;
      font-size: 12.5px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
    }
    .main-ref {
      background: #fee2e2;
      color: #991b1b;
      border: 1px solid #fecaca;
    }
    .main-ref:hover {
      background: #fca5a5;
      color: #7f1d1d;
    }
    .ed-ref {
      background: #e0e7ff;
      color: #3730a3;
      border: 1px solid #c7d2fe;
    }
    .ed-ref:hover {
      background: #c7d2fe;
      color: #312e81;
    }

    /* Figure Cards */
    .figure-card {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: var(--radius-lg);
      margin: 32px 0 28px;
      overflow: hidden;
      box-shadow: var(--shadow-md);
      scroll-margin-top: 90px;
      transition: all 0.3s ease;
    }
    .figure-card.highlight-flash {
      border-color: #e11d48;
      box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.3);
    }
    .figure-header {
      background: #f8fafc;
      border-bottom: 1px solid #e2e8f0;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }
    .fig-badge {
      background: var(--navy);
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .ed-badge {
      background: #3730a3 !important;
    }
    .fig-titles {
      flex: 1;
      min-width: 260px;
    }
    .fig-title-en {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 2px;
    }
    .fig-title-zh {
      font-size: 13.5px;
      font-weight: 600;
      color: var(--primary);
    }
    .zoom-btn {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      color: var(--slate);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .zoom-btn:hover {
      background: #f1f5f9;
      color: var(--navy);
    }
    .figure-image-wrapper {
      position: relative;
      background: #ffffff;
      padding: 16px;
      text-align: center;
      cursor: zoom-in;
      border-bottom: 1px solid #e2e8f0;
    }
    .paper-figure {
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      display: block;
      margin: 0 auto;
      box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .image-overlay {
      position: absolute;
      bottom: 24px;
      right: 24px;
      background: rgba(15, 23, 42, 0.75);
      color: #ffffff;
      font-size: 12px;
      padding: 5px 12px;
      border-radius: 20px;
      backdrop-filter: blur(4px);
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .figure-caption {
      padding: 20px 24px;
      background: #fcfdfe;
    }
    .caption-tab-btns {
      display: flex;
      gap: 8px;
      margin-bottom: 14px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 10px;
    }
    .cap-btn {
      border: none;
      background: none;
      padding: 5px 12px;
      font-size: 13px;
      font-weight: 600;
      color: var(--slate-light);
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.15s;
    }
    .cap-btn.active {
      background: #f1f5f9;
      color: var(--primary);
    }
    .caption-content {
      display: none;
      font-size: 13.5px;
      line-height: 1.75;
      color: #334155;
    }
    .caption-content.active {
      display: block;
    }

    /* Methods Subsections */
    .method-item {
      background: #fafbfc;
      border: 1px solid #e2e8f0;
      border-radius: var(--radius-md);
      margin-bottom: 18px;
      padding: 20px;
      scroll-margin-top: 85px;
    }
    .method-header {
      display: flex;
      align-items: baseline;
      gap: 12px;
      margin-bottom: 14px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 8px;
    }
    .method-num {
      background: #475569;
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .method-title-en {
      font-size: 15px;
      font-weight: 700;
      color: var(--navy);
    }
    .method-title-zh {
      font-size: 14px;
      font-weight: 600;
      color: var(--primary);
    }

    /* Lightbox Modal */
    #lightbox-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(15, 23, 42, 0.92);
      z-index: 999999;
      backdrop-filter: blur(8px);
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    #lightbox-modal.active {
      display: flex;
    }
    #lightbox-img {
      max-width: 95%;
      max-height: 90vh;
      border-radius: 6px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      object-fit: contain;
      background: #ffffff;
    }
    #lightbox-close {
      position: absolute;
      top: 24px;
      right: 32px;
      color: #ffffff;
      font-size: 36px;
      cursor: pointer;
      opacity: 0.8;
      transition: opacity 0.2s;
    }
    #lightbox-close:hover {
      opacity: 1;
    }

    /* Back to top button */
    #back-to-top {
      position: fixed;
      bottom: 28px;
      right: 28px;
      width: 44px;
      height: 44px;
      background: var(--navy);
      color: #fff;
      border: none;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: var(--shadow-lg);
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s ease;
      z-index: 1000;
    }
    #back-to-top.visible {
      opacity: 1;
      transform: translateY(0);
    }
    #back-to-top:hover {
      background: var(--primary);
    }

    /* Responsive */
    @media (max-width: 1080px) {
      .toc-sidebar { display: none; }
      .bilingual-grid { grid-template-columns: 1fr; gap: 14px; }
      .paper-header { padding: 24px; }
      .paper-title-en { font-size: 22px; }
      .paper-title-zh { font-size: 18px; }
    }
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progress-bar"></div>

  <!-- Top Navigation Bar -->
  <nav class="top-navbar">
    <a href="#" class="nav-brand">
      <span class="brand-logo">NATURE</span>
      <span class="brand-title">Rewiring cancer drivers to activate apoptosis (TCIP1)</span>
    </a>
    <div class="nav-controls">
      <div style="display: flex; gap: 6px;">
        <button class="mode-btn active" id="btn-both" onclick="setReadingMode('both')">
          <i class="fas fa-columns"></i> 中英双语
        </button>
        <button class="mode-btn" id="btn-zh" onclick="setReadingMode('zh')">
          <i class="fas fa-language"></i> 纯中文
        </button>
        <button class="mode-btn" id="btn-en" onclick="setReadingMode('en')">
          <i class="fas fa-globe"></i> English
        </button>
      </div>
      <a href="https://github.com/18297928865/tcip-cancer-drivers-nature-report" target="_blank" class="mode-btn" style="text-decoration:none;">
        <i class="fab fa-github"></i> GitHub
      </a>
    </div>
  </nav>

  <div class="app-container">
    
    <!-- Table of Contents Sidebar -->
    <aside class="toc-sidebar">
      <div class="toc-title"><i class="fas fa-list-ul"></i> 论文导航目录</div>
      <ul class="toc-list">
        <li><a href="#sec-header" class="toc-link"><span>0. 论文概览与核心创新</span> <span class="toc-badge">Meta</span></a></li>
        <li><a href="#sec-abstract" class="toc-link"><span>1. 摘要 Abstract</span> <span class="toc-badge">Abs</span></a></li>
        <li><a href="#sec-intro" class="toc-link"><span>2. 引言 Introduction</span> <span class="toc-badge">Intro</span></a></li>
        <li><a href="#sec-results-1" class="toc-link"><span>3. 结果 1: TCIP1差异杀伤</span> <span class="toc-badge">Fig 1</span></a></li>
        <li><a href="#sec-results-2" class="toc-link"><span>4. 结果 2: 三元复合物机制</span> <span class="toc-badge">Fig 2</span></a></li>
        <li><a href="#sec-results-3" class="toc-link"><span>5. 结果 3: 促凋亡基因激活</span> <span class="toc-badge">Fig 3</span></a></li>
        <li><a href="#sec-results-4" class="toc-link"><span>6. 结果 4: 重编程自抑回环</span> <span class="toc-badge">Fig 4</span></a></li>
        <li><a href="#sec-results-5" class="toc-link"><span>7. 结果 5: 细胞特异与普适</span> <span class="toc-badge">Fig 5</span></a></li>
        <li><a href="#sec-discussion" class="toc-link"><span>8. 讨论与前瞻 Discussion</span> <span class="toc-badge">Disc</span></a></li>
        <li><a href="#sec-methods" class="toc-link"><span>9. 研究方法详述 Methods</span> <span class="toc-badge">19项</span></a></li>
        <li><a href="#sec-extended-data" class="toc-link"><span>10. 扩展数据 Extended Data</span> <span class="toc-badge">ED 1-9</span></a></li>
        <li><a href="#phd-review" class="toc-link" style="color:var(--primary); font-weight:600;"><span>11. 博士文献汇报与答辩</span> <span class="toc-badge" style="background:var(--primary); color:#fff;">JC Suite</span></a></li>
      </ul>
    </aside>

    <!-- Main Scientific Content -->
    <main class="main-content">
'''

print("Step 2 HTML skeleton ready.")

def build_html():
    p1 = trans_part1_intro.PART1_DATA
    p2 = trans_part2_results1.PART2_DATA
    p3 = trans_part3_results2.PART3_DATA
    p4 = trans_part4_results3.PART4_DATA
    p5 = trans_part5_results4.PART5_DATA
    p6 = trans_part6_results5.PART6_DATA
    p7 = trans_part7_discussion.PART7_DATA
    p8 = trans_part8_methods.PART8_DATA
    p9 = trans_part9_extended_data.PART9_DATA

    out = []
    out.append(HTML_HEADER)

    # 0. Header Hero Card
    meta = p1['meta']
    out.append(f'''
      <!-- Section 0: Paper Metadata & Highlights -->
      <section class="paper-header" id="sec-header">
        <div class="journal-meta">
          <span class="journal-badge">NATURE</span>
          <span class="meta-item"><i class="far fa-file-alt"></i> Article</span>
          <span class="meta-item"><i class="far fa-calendar-alt"></i> {meta.get("pub_date", "Published: 26 July 2023")}</span>
          <span class="meta-item"><i class="fas fa-book"></i> {meta.get("citation_en", "Nature 620, 417-427 (2023)")}</span>
          <span class="meta-item"><i class="fas fa-link"></i> <a href="https://doi.org/{meta.get('doi', '10.1038/s41586-023-06348-2')}" target="_blank" style="color:var(--primary);text-decoration:none;">DOI: {meta.get("doi", "10.1038/s41586-023-06348-2")}</a></span>
        </div>
        
        <h1 class="paper-title-en">{meta.get("title_en", "")}</h1>
        <h2 class="paper-title-zh">{meta.get("title_zh", "")}</h2>

        <div class="authors-block">
          <div class="author-names"><i class="fas fa-users"></i> {meta.get("authors_en", "")}</div>
          <div class="author-affils"><i class="fas fa-university"></i> {meta.get("affiliations_en", "")}</div>
          <div class="author-affils" style="margin-top:6px; color:#475569;"><i class="fas fa-map-marker-alt"></i> {meta.get("affiliations_zh", "")}</div>
        </div>

        <div class="highlights-box">
          <div class="highlights-title"><i class="fas fa-star"></i> 核心科学突破与创新亮点 (Executive Innovation Highlights)</div>
          <div class="highlights-list">
            <div class="highlight-card">
              <strong>1. 邻近诱导药理学新范式 (Proximity Pharmacology)</strong>
              突破传统PROTAC仅介导降解的局限，首创转录化学诱导邻近剂 (TCIPs)，将转录阻抑蛋白与转录激活复合物招募至同一位点。
            </div>
            <div class="highlight-card">
              <strong>2. 显性增殖驱动转变为显性致死 (Gain-of-Function Cell Killing)</strong>
              将弥漫大B细胞淋巴瘤 (DLBCL) 绝对依赖的高表达致癌驱动因子 BCL6 直接转化为内源性促凋亡基因的强力启动器。
            </div>
            <div class="highlight-card">
              <strong>3. 纳摩尔级高选择性杀伤 (Sub-nanomolar Potency)</strong>
              TCIP1 和 TCIP2 在 BCL6 驱动的 DLBCL 细胞中显示极低 IC50 (低至 ~1-10 nM)，而在健康非肿瘤细胞及其他细胞中完全无细胞毒性。
            </div>
            <div class="highlight-card">
              <strong>4. 克服生理自抑与耐药突变 (Bypassing Autoinhibition)</strong>
              不仅激活外源促凋亡靶标 (BCL2L11/PUMA)，同时强力反转 BCL6 启动子的自抑制回环，诱发巨量 BCL6 过表达，形成正反馈“自杀回环”。
            </div>
          </div>
        </div>
      </section>
    ''')

    # 1. Abstract
    out.append('''
      <!-- Section 1: Abstract -->
      <section class="article-section" id="sec-abstract">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-bookmark"></i> Abstract</span>
          <h3 class="section-title-en">Abstract</h3>
          <h4 class="section-title-zh">论文摘要</h4>
        </div>
    ''')
    abs_data = p1.get('abstract', {})
    if isinstance(abs_data, dict):
        out.append(render_paragraph(abs_data, "abs-0"))
    elif isinstance(abs_data, list):
        for i, p in enumerate(abs_data):
            out.append(render_paragraph(p, f"abs-{i}"))
    out.append('</section>')

    # 2. Introduction
    out.append('''
      <!-- Section 2: Introduction -->
      <section class="article-section" id="sec-intro">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-book-open"></i> Introduction</span>
          <h3 class="section-title-en">Introduction</h3>
          <h4 class="section-title-zh">引言与立论依据</h4>
        </div>
    ''')
    for i, p in enumerate(p1.get('intro', [])):
        out.append(render_paragraph(p, f"intro-{i}"))
    out.append('</section>')

    # 3. Results 1
    out.append(f'''
      <!-- Section 3: Results 1 -->
      <section class="article-section" id="sec-results-1">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-flask"></i> Results 1</span>
          <h3 class="section-title-en">{p2.get("section_title_en", "")}</h3>
          <h4 class="section-title-zh">{p2.get("section_title_zh", "")}</h4>
        </div>
    ''')
    for i, p in enumerate(p2.get('paragraphs', [])):
        out.append(render_paragraph(p, f"r1-{i}"))
    out.append(render_figure(p2.get('figure')))
    out.append('</section>')

    # 4. Results 2
    out.append(f'''
      <!-- Section 4: Results 2 -->
      <section class="article-section" id="sec-results-2">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-flask"></i> Results 2</span>
          <h3 class="section-title-en">{p3.get("section_title_en", "")}</h3>
          <h4 class="section-title-zh">{p3.get("section_title_zh", "")}</h4>
        </div>
    ''')
    for i, p in enumerate(p3.get('paragraphs', [])):
        out.append(render_paragraph(p, f"r2-{i}"))
    out.append(render_figure(p3.get('figure')))
    out.append('</section>')

    # 5. Results 3
    out.append('''
      <!-- Section 5: Results 3 -->
      <section class="article-section" id="sec-results-3">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-flask"></i> Results 3</span>
          <h3 class="section-title-en">Mechanism of TCIP1-mediated Cell Killing</h3>
          <h4 class="section-title-zh">TCIP1 介导细胞杀伤的促凋亡转录机制</h4>
        </div>
    ''')
    for sub_idx, sub in enumerate(p4.get('subsections', [])):
        out.append(f'''
          <div class="subsection-divider">
            <h4 class="subsection-title-en">{sub.get("title_en", "")}</h4>
            <h5 class="subsection-title-zh">{sub.get("title_zh", "")}</h5>
          </div>
        ''')
        for i, p in enumerate(sub.get('paragraphs', [])):
            out.append(render_paragraph(p, f"r3-{sub_idx}-{i}"))
    out.append(render_figure(p4.get('figure')))
    out.append('</section>')

    # 6. Results 4
    out.append('''
      <!-- Section 6: Results 4 -->
      <section class="article-section" id="sec-results-4">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-flask"></i> Results 4</span>
          <h3 class="section-title-en">Epigenetic Remodeling and Target Genes</h3>
          <h4 class="section-title-zh">表观遗传重塑与直接靶基因鉴定</h4>
        </div>
    ''')
    for sub_idx, sub in enumerate(p5.get('subsections', [])):
        out.append(f'''
          <div class="subsection-divider">
            <h4 class="subsection-title-en">{sub.get("title_en", "")}</h4>
            <h5 class="subsection-title-zh">{sub.get("title_zh", "")}</h5>
          </div>
        ''')
        for i, p in enumerate(sub.get('paragraphs', [])):
            out.append(render_paragraph(p, f"r4-{sub_idx}-{i}"))
    out.append(render_figure(p5.get('figure')))
    out.append('</section>')

    # 7. Results 5
    out.append('''
      <!-- Section 7: Results 5 -->
      <section class="article-section" id="sec-results-5">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-flask"></i> Results 5</span>
          <h3 class="section-title-en">Cell Type Specificity and Generality</h3>
          <h4 class="section-title-zh">细胞类型特异性与TCIP策略的普适性</h4>
        </div>
    ''')
    for sub_idx, sub in enumerate(p6.get('subsections', [])):
        out.append(f'''
          <div class="subsection-divider">
            <h4 class="subsection-title-en">{sub.get("title_en", "")}</h4>
            <h5 class="subsection-title-zh">{sub.get("title_zh", "")}</h5>
          </div>
        ''')
        for i, p in enumerate(sub.get('paragraphs', [])):
            out.append(render_paragraph(p, f"r5-{sub_idx}-{i}"))
    out.append(render_figure(p6.get('figure')))
    out.append('</section>')

    # 8. Discussion
    out.append(f'''
      <!-- Section 8: Discussion -->
      <section class="article-section" id="sec-discussion">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-comment-dots"></i> Discussion</span>
          <h3 class="section-title-en">{p7.get("title_en", "Discussion")}</h3>
          <h4 class="section-title-zh">{p7.get("title_zh", "讨论与前景展望")}</h4>
        </div>
    ''')
    for i, p in enumerate(p7.get('paragraphs', [])):
        out.append(render_paragraph(p, f"disc-{i}"))
    out.append('</section>')

    # 9. Methods
    out.append(f'''
      <!-- Section 9: Methods -->
      <section class="article-section" id="sec-methods">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-tools"></i> Methods</span>
          <h3 class="section-title-en">{p8.get("title_en", "Methods")}</h3>
          <h4 class="section-title-zh">{p8.get("title_zh", "实验材料与方法详述 (19项完整规范)")}</h4>
        </div>
    ''')
    for idx, sec in enumerate(p8.get('sections', [])):
        sec_id = sec.get('id', f"method-{idx}")
        title_en = sec.get('title_en', '')
        title_zh = sec.get('title_zh', '')
        en_text = linkify_citations(sec.get('en', ''))
        zh_text = linkify_citations(sec.get('zh', ''))
        terms_html = render_terms(sec.get('terms', []))
        
        out.append(f'''
          <div class="method-item" id="{sec_id}">
            <div class="method-header">
              <span class="method-num">M{idx+1}</span>
              <div>
                <div class="method-title-en">{title_en}</div>
                <div class="method-title-zh">{title_zh}</div>
              </div>
            </div>
            <div class="bilingual-grid">
              <div class="text-col en-col">
                <div class="lang-tag"><i class="fas fa-globe-americas"></i> English Method</div>
                <p class="para-text en-text">{en_text}</p>
              </div>
              <div class="text-col zh-col">
                <div class="lang-tag"><i class="fas fa-language"></i> 中文详述</div>
                <p class="para-text zh-text">{zh_text}</p>
              </div>
            </div>
            {terms_html}
          </div>
        ''')
    out.append('</section>')

    # 10. Extended Data Figures
    out.append(f'''
      <!-- Section 10: Extended Data Figures -->
      <section class="article-section" id="sec-extended-data">
        <div class="section-header">
          <span class="section-badge"><i class="fas fa-images"></i> Extended Data</span>
          <h3 class="section-title-en">{p9.get("title_en", "Extended Data Figures")}</h3>
          <h4 class="section-title-zh">{p9.get("title_zh", "补充扩展数据图解与详析 (Extended Data Fig. 1-9)")}</h4>
        </div>
    ''')
    for fig in p9.get('figures', []):
        out.append(render_extended_figure(fig))
    out.append('</section>')

    # 11. PhD Journal Club Review Section
    review_raw = part6_phd_presentation_review.PHD_PRESENTATION_REVIEW
    end_idx = review_raw.find('</section>')
    if end_idx != -1:
        review_clean = review_raw[:end_idx + len('</section>')]
    else:
        review_clean = review_raw
    out.append(review_clean)

    # Closing tags, lightbox, back-to-top, and JavaScript
    out.append('''
    </main>
  </div>

  <!-- Modal Lightbox for Figures -->
  <div id="lightbox-modal" onclick="closeLightbox(event)">
    <span id="lightbox-close" onclick="closeLightbox(event)">&times;</span>
    <img id="lightbox-img" src="" alt="Enlarged Scientific Figure">
  </div>

  <!-- Back to top button -->
  <button id="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="返回顶部">
    <i class="fas fa-arrow-up"></i>
  </button>

  <!-- Interactive JavaScript -->
  <script>
    // Reading Mode Switching
    function setReadingMode(mode) {
      document.body.classList.remove('mode-zh', 'mode-en');
      document.getElementById('btn-both').classList.remove('active');
      document.getElementById('btn-zh').classList.remove('active');
      document.getElementById('btn-en').classList.remove('active');

      if (mode === 'zh') {
        document.body.classList.add('mode-zh');
        document.getElementById('btn-zh').classList.add('active');
      } else if (mode === 'en') {
        document.body.classList.add('mode-en');
        document.getElementById('btn-en').classList.add('active');
      } else {
        document.getElementById('btn-both').classList.add('active');
      }
    }

    // Lightbox Controls
    function openLightbox(imgSrc, title, figId) {
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      img.src = imgSrc;
      img.alt = title;
      modal.classList.add('active');
    }

    function closeLightbox(e) {
      if (e.target.id === 'lightbox-modal' || e.target.id === 'lightbox-close') {
        document.getElementById('lightbox-modal').classList.remove('active');
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.getElementById('lightbox-modal').classList.remove('active');
      }
    });

    // Caption Tab Switcher
    function switchCapTab(btn, targetId) {
      const parent = btn.closest('.figure-caption');
      parent.querySelectorAll('.cap-btn').forEach(b => b.classList.remove('active'));
      parent.querySelectorAll('.caption-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      const target = parent.querySelector('#' + targetId);
      if (target) target.classList.add('active');
    }

    // Jump to Figure and Highlight
    function jumpToFig(figId) {
      const el = document.getElementById(figId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        el.classList.add('highlight-flash');
        setTimeout(() => el.classList.remove('highlight-flash'), 2500);
      }
    }

    // Reading Progress & Scrollspy
    window.addEventListener('scroll', function() {
      const winScroll = document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';

      // Back to top
      const backBtn = document.getElementById('back-to-top');
      if (winScroll > 400) {
        backBtn.classList.add('visible');
      } else {
        backBtn.classList.remove('visible');
      }

      // TOC Scrollspy
      const sections = document.querySelectorAll('section[id], .article-section[id], #phd-review');
      let currentId = '';
      sections.forEach(sec => {
        const top = sec.offsetTop - 120;
        if (winScroll >= top) {
          currentId = sec.getAttribute('id');
        }
      });
      if (currentId) {
        document.querySelectorAll('.toc-link').forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + currentId) {
            link.classList.add('active');
          }
        });
      }
    });
  </script>

</body>
</html>
''')

    final_html = "".join(out)
    out_file = os.path.join(base_dir, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print(f"DONE! Written {len(final_html)} chars to {out_file}. File size: {os.path.getsize(out_file)} bytes.")

if __name__ == '__main__':
    build_html()
