# -*- coding: utf-8 -*-
"""
part1_head_styles.py
Defines the HTML5 skeleton, modern Nature-style academic typography, responsive layout,
color palettes, interactive lightbox, sticky navigation sidebar, reading progress bar,
and scientific callout styling.
"""

HEAD_AND_STYLES = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nature 顶刊精读与文献汇报：重构肿瘤驱动基因诱导癌细胞凋亡 (TCIP 邻近诱导转录疗法)</title>
<style>
  :root {
    --primary: #8b0000;         /* 经典 Nature 枣红/深绯红 */
    --primary-dark: #5c0000;
    --primary-light: #b22222;
    --primary-bg: #fff5f5;
    --secondary: #1a365d;       /* 深邃学术蓝 */
    --secondary-light: #2b6cb0;
    --accent: #c53030;
    --accent-bg: #fffaf0;
    --accent-border: #feebc8;
    --dark: #1a202c;
    --text: #2d3748;
    --text-muted: #718096;
    --bg-page: #f7fafc;
    --bg-card: #ffffff;
    --border: #e2e8f0;
    --border-accent: #fed7d7;
    --highlight: #fefcbf;
    --term-tag: #edf2f7;
    --term-text: #2d3748;
    --term-border: #cbd5e0;
    --shadow: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
    --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
    --radius: 8px;
    --radius-lg: 12px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
    color: var(--text);
    background-color: var(--bg-page);
    line-height: 1.85;
    font-size: 16px;
    scroll-behavior: smooth;
  }

  /* 顶部阅读进度条 */
  #progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(90deg, #b22222, #e53e3e, #dd6b20);
    z-index: 9999;
    width: 0%;
    transition: width 0.1s ease;
  }

  /* 顶部全局导航 */
  .top-navbar {
    position: sticky;
    top: 0;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }

  .nav-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 17px;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
  }

  .nav-badge {
    background: var(--primary);
    color: #fff;
    font-size: 11px;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }

  .nav-links {
    display: flex;
    gap: 18px;
    align-items: center;
  }

  .nav-links a {
    color: var(--text);
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    transition: color 0.2s;
  }

  .nav-links a:hover {
    color: var(--primary);
  }

  /* 页面容器主体 */
  .layout-container {
    max-width: 1360px;
    margin: 30px auto;
    padding: 0 24px;
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 32px;
    align-items: start;
  }

  @media (max-width: 1080px) {
    .layout-container {
      grid-template-columns: 1fr;
    }
    .sidebar-toc {
      display: none !important;
    }
  }

  /* 侧边目录 (Sticky TOC) */
  .sidebar-toc {
    position: sticky;
    top: 80px;
    background: #fff;
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 20px 16px;
    box-shadow: var(--shadow);
    max-height: calc(100vh - 110px);
    overflow-y: auto;
  }

  .toc-title {
    font-size: 14px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .toc-list {
    list-style: none;
    font-size: 13px;
  }

  .toc-item {
    margin-bottom: 4px;
  }

  .toc-item a {
    display: block;
    padding: 6px 10px;
    color: var(--text);
    text-decoration: none;
    border-radius: 6px;
    transition: all 0.2s;
    line-height: 1.4;
  }

  .toc-item a:hover {
    background: var(--primary-bg);
    color: var(--primary);
  }

  .toc-item.active a {
    background: var(--primary-bg);
    color: var(--primary);
    font-weight: 600;
    border-left: 3px solid var(--primary);
  }

  .toc-item.sub {
    margin-left: 14px;
    font-size: 12.5px;
  }

  /* 主内容卡片 */
  .main-content {
    min-width: 0;
  }

  /* 论文头部 Hero */
  .paper-hero {
    background: linear-gradient(135deg, #2b1111 0%, #1a202c 100%);
    color: #fff;
    padding: 44px 40px;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
  }

  .paper-hero::before {
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    width: 320px;
    height: 100%;
    background: radial-gradient(circle, rgba(229,62,62,0.18) 0%, rgba(0,0,0,0) 70%);
    pointer-events: none;
  }

  .journal-badge {
    display: inline-block;
    background: #e53e3e;
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 4px 12px;
    border-radius: 4px;
    letter-spacing: 1px;
    margin-bottom: 18px;
    text-transform: uppercase;
  }

  .paper-hero h1 {
    font-size: 28px;
    line-height: 1.4;
    font-weight: 800;
    margin-bottom: 14px;
    color: #ffffff;
  }

  .title-en {
    font-size: 18px;
    line-height: 1.5;
    color: #cbd5e0;
    font-style: italic;
    font-family: Georgia, serif;
    margin-bottom: 24px;
  }

  .paper-meta {
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 18px;
    font-size: 13.5px;
    color: #e2e8f0;
    line-height: 1.7;
  }

  .meta-authors strong {
    color: #feb2b2;
  }

  .meta-links {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 13px;
  }

  .meta-links a {
    color: #90cdf4;
    text-decoration: underline;
  }

  /* 博士文献汇报备战导读 Banner */
  .phd-guide-banner {
    background: linear-gradient(135deg, #fffaf0 0%, #feebc8 100%);
    border-left: 5px solid #dd6b20;
    border-radius: var(--radius);
    padding: 22px 24px;
    margin-bottom: 30px;
    box-shadow: var(--shadow);
  }

  .phd-guide-banner h3 {
    color: #9c4221;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .phd-guide-banner p {
    color: #744210;
    font-size: 14.5px;
    line-height: 1.75;
  }

  /* 卡片模块 */
  .card-section {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 36px 36px;
    margin-bottom: 32px;
    box-shadow: var(--shadow);
  }

  .section-heading {
    font-size: 22px;
    font-weight: 800;
    color: var(--secondary);
    border-bottom: 2px solid var(--border);
    padding-bottom: 12px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .section-heading .sec-id {
    background: var(--primary);
    color: #fff;
    font-size: 12px;
    font-weight: 800;
    padding: 3px 9px;
    border-radius: 4px;
    letter-spacing: 0.5px;
  }

  .subsection-heading {
    font-size: 18px;
    font-weight: 700;
    color: var(--primary);
    margin: 26px 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* 文本与段落排版 */
  p {
    margin-bottom: 18px;
    color: #2d3748;
    text-align: justify;
  }

  /* 机制解析卡片 / 导读卡片 */
  .mechanism-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid var(--primary);
    border-radius: var(--radius);
    padding: 20px 22px;
    margin: 22px 0;
  }

  .mechanism-card.blue {
    border-left-color: #2b6cb0;
    background: #ebf8ff;
  }

  .mechanism-card.green {
    border-left-color: #2f855a;
    background: #f0fff4;
  }

  .mechanism-card.purple {
    border-left-color: #6b46c1;
    background: #faf5ff;
  }

  .mechanism-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* 词汇高亮 / 专业概念注解 */
  .term-tag {
    display: inline-block;
    background: var(--term-tag);
    color: var(--term-text);
    border: 1px solid var(--term-border);
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 13.5px;
    font-weight: 600;
  }

  .badge-chem {
    background: #e6fffa;
    color: #234e52;
    border: 1px solid #b2f5ea;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 700;
  }

  .badge-gene {
    background: #fefcbf;
    color: #744210;
    border: 1px solid #faf089;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 700;
  }

  /* 图版展示区 */
  .figure-wrapper {
    margin: 28px 0;
    background: #fdfdfd;
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }

  .figure-img-container {
    text-align: center;
    cursor: zoom-in;
    position: relative;
    overflow: hidden;
    border-radius: var(--radius);
    background: #fff;
    padding: 10px;
  }

  .figure-img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    transition: transform 0.25s ease;
  }

  .figure-img:hover {
    transform: scale(1.01);
  }

  .zoom-hint {
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 6px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 4px;
  }

  .figure-caption {
    margin-top: 18px;
    font-size: 14.5px;
    line-height: 1.7;
    color: #4a5568;
    background: #f7fafc;
    padding: 16px 20px;
    border-radius: var(--radius);
    border-left: 3px solid var(--secondary);
  }

  .figure-caption strong.fig-title {
    color: var(--secondary);
    display: block;
    margin-bottom: 6px;
    font-size: 15px;
  }

  /* 表格设计 */
  .custom-table {
    width: 100%;
    border-collapse: collapse;
    margin: 22px 0;
    font-size: 14.5px;
    background: #fff;
  }

  .custom-table th {
    background: #f1f5f9;
    color: #1e293b;
    font-weight: 700;
    padding: 12px 14px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }

  .custom-table td {
    padding: 12px 14px;
    border: 1px solid #e2e8f0;
    color: #334155;
    vertical-align: top;
  }

  .custom-table tr:nth-child(even) {
    background-color: #f8fafc;
  }

  .custom-table tr:hover {
    background-color: #f1f5f9;
  }

  /* 幻灯片演讲脚本卡片 */
  .slide-card {
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: var(--radius);
    margin-bottom: 20px;
    box-shadow: var(--shadow);
    overflow: hidden;
  }

  .slide-header {
    background: #1e293b;
    color: #fff;
    padding: 10px 18px;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .slide-body {
    padding: 18px;
  }

  .script-box {
    background: #fffdf5;
    border-left: 4px solid #f59e0b;
    padding: 12px 16px;
    border-radius: 4px;
    margin-top: 10px;
    font-size: 14px;
    color: #78350f;
    line-height: 1.65;
  }

  .script-box strong {
    color: #92400e;
  }

  /* 导师尖锐问答卡片 */
  .qa-card {
    background: #ffffff;
    border: 1px solid #fed7d7;
    border-radius: var(--radius);
    margin-bottom: 22px;
    overflow: hidden;
    box-shadow: var(--shadow);
  }

  .qa-q {
    background: #fff5f5;
    color: #9b2c2c;
    padding: 14px 18px;
    font-weight: 700;
    font-size: 15px;
    border-bottom: 1px solid #feb2b2;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .qa-a {
    padding: 16px 20px;
    font-size: 14.5px;
    color: #2d3748;
    line-height: 1.75;
  }

  .qa-a strong.highlight-point {
    color: #2b6cb0;
  }

  /* 图片点击放大弹窗 (Modal Lightbox) */
  #lightbox-modal {
    display: none;
    position: fixed;
    z-index: 10000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.92);
    align-items: center;
    justify-content: center;
    padding: 20px;
    cursor: zoom-out;
  }

  #lightbox-img {
    max-width: 95%;
    max-height: 95%;
    border-radius: 6px;
    box-shadow: 0 0 25px rgba(255, 255, 255, 0.2);
    transition: transform 0.2s ease;
  }

  #lightbox-close {
    position: absolute;
    top: 20px;
    right: 30px;
    color: #fff;
    font-size: 36px;
    font-weight: bold;
    cursor: pointer;
    user-select: none;
  }

  /* 回到顶部按钮 */
  #back-to-top {
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 44px;
    height: 44px;
    background: var(--primary);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    opacity: 0;
    visibility: hidden;
    transition: all 0.25s ease;
    z-index: 999;
  }

  #back-to-top.show {
    opacity: 1;
    visibility: visible;
  }

  #back-to-top:hover {
    background: var(--primary-dark);
    transform: translateY(-2px);
  }

  /* 页脚 */
  footer {
    border-top: 1px solid var(--border);
    background: #fff;
    padding: 36px 24px;
    text-align: center;
    color: var(--text-muted);
    font-size: 13.5px;
    margin-top: 60px;
  }
</style>
</head>
<body>

  <!-- 顶部进度条 -->
  <div id="progress-bar"></div>

  <!-- 顶部导航栏 -->
  <header class="top-navbar">
    <a href="#" class="nav-logo">
      <span class="nav-badge">Nature 2023</span>
      <span>TCIP · 肿瘤驱动基因重构激活凋亡</span>
    </a>
    <nav class="nav-links">
      <a href="#overview">研究概览</a>
      <a href="#sec1">TCIP1杀伤</a>
      <a href="#sec2">三元复合物</a>
      <a href="#sec3">MYC抑制</a>
      <a href="#sec4">机制与转录延伸</a>
      <a href="#sec5">体内安全性与普适性</a>
      <a href="#methods">STAR方法</a>
      <a href="#phd-review" style="color: var(--primary); font-weight: 700;">🎓 博士精读汇报</a>
    </nav>
  </header>

  <!-- 布局双栏结构 -->
  <div class="layout-container">
    <!-- 侧边 Sticky TOC 目录 -->
    <aside class="sidebar-toc">
      <div class="toc-title">
        <span>📑 文献精读目录</span>
      </div>
      <ul class="toc-list">
        <li class="toc-item"><a href="#overview">1. 论文概览与导读</a></li>
        <li class="toc-item sub"><a href="#abstract">中英文双语摘要</a></li>
        <li class="toc-item sub"><a href="#intro">立项背景与科学假说</a></li>
        <li class="toc-item"><a href="#sec1">2. TCIP1 选择性杀死 DLBCL</a></li>
        <li class="toc-item sub"><a href="#fig1">Figure 1: TCIP 设计与活性</a></li>
        <li class="toc-item sub"><a href="#ed-fig1">Extended Data 1-3: 筛选与优化</a></li>
        <li class="toc-item"><a href="#sec2">3. 三元复合物介导细胞杀伤</a></li>
        <li class="toc-item sub"><a href="#fig2">Figure 2: 化学挽救与 TR-FRET</a></li>
        <li class="toc-item sub"><a href="#ed-fig4">Extended Data 4-5: 结合动力学与周期</a></li>
        <li class="toc-item"><a href="#sec3">4. 快速抑制 MYC 及其靶基因</a></li>
        <li class="toc-item sub"><a href="#fig3">Figure 3: MYC 下调与转录组变化</a></li>
        <li class="toc-item sub"><a href="#ed-fig6">Extended Data 6: GSEA 通路富集</a></li>
        <li class="toc-item"><a href="#sec4">5. 转录激活机制与自反馈重构</a></li>
        <li class="toc-item sub"><a href="#fig4">Figure 4: Pol II 延伸与 BCL6 回路</a></li>
        <li class="toc-item sub"><a href="#ed-fig7">Extended Data 7-8: ChIP-seq 轨迹</a></li>
        <li class="toc-item sub"><a href="#ed-fig9">Extended Data 9: 正反馈自杀循环</a></li>
        <li class="toc-item"><a href="#sec5">6. 体内靶向安全性与普适性</a></li>
        <li class="toc-item sub"><a href="#fig5">Figure 5: 小鼠毒理与 ER-TCIP2</a></li>
        <li class="toc-item"><a href="#discussion">7. 全文讨论与范式革命</a></li>
        <li class="toc-item"><a href="#methods">8. 详尽实验方法 (STAR Methods)</a></li>
        <li class="toc-item" style="margin-top: 10px; border-top: 1px dashed var(--border); padding-top: 8px;">
          <a href="#phd-review" style="color: var(--primary); font-weight: 700;">🎓 博士文献汇报专栏</a>
        </li>
        <li class="toc-item sub"><a href="#novelties">五大核心新颖点拆解</a></li>
        <li class="toc-item sub"><a href="#implications">生物学与转化意义</a></li>
        <li class="toc-item sub"><a href="#background-depth">邻近药理学背景拓展</a></li>
        <li class="toc-item sub"><a href="#ppt-guide">15-20min PPT 讲稿脚本</a></li>
        <li class="toc-item sub"><a href="#defense-qa">导师尖锐提问 5 连问应答</a></li>
      </ul>
    </aside>

    <!-- 右侧主体内容容器 -->
    <main class="main-content">
'''
