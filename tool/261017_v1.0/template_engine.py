# -*- coding: utf-8 -*-
"""
template_engine.py
반도체3와 100% 동일한 UI/UX 레이아웃을 기반으로 배터리3 대시보드(HTML) 및 마스터 보고서(MD)를 생성하는 엔진 모듈.
"""

import json
import os
from datetime import datetime


def generate_html(topics: list) -> str:
    """질문 리스트(최신순 정렬)를 받아 반도체3 양식의 index.html 문자열을 반환합니다."""
    total_count = len(topics)
    latest_nav_title = topics[0]["nav_title"] if topics else ""

    # 1. 좌측 내비게이션 아이템 생성
    nav_items_html = []
    for idx, t in enumerate(topics, start=1):
        num_str = f"{idx:02d}"
        q_id = f"q-{num_str}"
        active_cls = " active" if idx == 1 else ""
        nav_items_html.append(
            f'      <li class="nav-item"><a href="#{q_id}" class="nav-link{active_cls}">'
            f'<span class="nav-num">{num_str}</span>'
            f'<span class="nav-text">{t["nav_title"]}</span></a></li>'
        )
    nav_list_str = "\n".join(nav_items_html)

    # 2. 본문 질문 카드 섹션 생성
    sections_html = []
    for idx, t in enumerate(topics, start=1):
        num_str = f"{idx:02d}"
        q_id = f"q-{num_str}"
        sec_cls = "topic-section latest-card-highlight" if idx == 1 else "topic-section"
        badge_prefix = "⭐ 최신 질문 " if idx == 1 else "📌 핵심 주제 "
        badge_text = f"{badge_prefix}({t['badge']})"

        summary_lis = "\n".join([f"          <li>{s}</li>" for s in t["summary"]])

        sec_block = f"""
    <!-- Q {num_str} : {t["title"]} -->
    <section class="{sec_cls}" id="{q_id}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q {num_str}</span>
          <span class="latest-tag">{badge_text}</span>
          <h2 class="topic-title">{t["title"]}</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">강의 핵심 요약 포인트</span>
        <ul class="summary-list">
{summary_lis}
        </ul>
      </div>
      <div class="lecture-content">
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            {t["svg_title"]}
          </div>
          {t["svg"]}
        </div>
        {t["lecture"]}
      </div>
    </section>"""
        sections_html.append(sec_block)

    sections_str = "\n".join(sections_html)

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>배터리 3 : 이차전지 전극 공정 &amp; 생산·운영 Q&amp;A 마스터 백과사전</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>
  <style>
    :root {{
      --bg-body: #0b0f19;
      --bg-card: #131b2e;
      --bg-sidebar: #0f172a;
      --border: #222f49;
      --text-main: #f1f5f9;
      --text-sub: #cbd5e1;
      --text-muted: #64748b;
      
      --accent-blue: #38bdf8;
      --accent-amber: #f59e0b;
      --accent-green: #10b981;
      
      --summary-bg: linear-gradient(135deg, rgba(14, 165, 233, 0.12) 0%, rgba(99, 102, 241, 0.12) 100%);
      --summary-border: #0284c7;
      
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
      --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.5);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background-color: var(--bg-body);
      color: var(--text-main);
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }}

    body.sidebar-collapsed aside {{
      transform: translateX(-100%);
    }}

    body.sidebar-collapsed main {{
      margin-left: 0;
      max-width: 100%;
      padding: 40px 80px 100px;
    }}

    .drawer-toggle-btn {{
      background: rgba(30, 41, 59, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      border-radius: 6px;
      padding: 5px 11px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .drawer-toggle-btn:hover {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}

    .drawer-float-open-btn {{
      position: fixed;
      top: 18px;
      left: 18px;
      z-index: 99;
      background: #0f172a;
      border: 1.5px solid #38bdf8;
      color: #38bdf8;
      border-radius: 8px;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 800;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
      transition: all 0.2s ease;
    }}
    .drawer-float-open-btn:hover {{
      background: #38bdf8;
      color: #0f172a;
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(56, 189, 248, 0.4);
    }}
    body.sidebar-collapsed .drawer-float-open-btn {{
      display: inline-flex;
    }}

    aside {{
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      width: 380px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      display: flex;
      flex-direction: column;
      z-index: 50;
      box-shadow: var(--shadow-lg);
    }}

    .sidebar-header {{
      padding: 22px 20px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(180deg, rgba(30,41,59,0.5) 0%, rgba(15,23,42,0) 100%);
    }}

    .sidebar-header h1 {{
      font-size: 1.18rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .sidebar-header p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 5px;
      line-height: 1.4;
    }}

    .search-box {{
      padding: 12px 18px;
      border-bottom: 1px solid var(--border);
    }}

    .search-input {{
      width: 100%;
      padding: 9px 13px;
      background-color: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.85rem;
      outline: none;
      transition: all 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--accent-blue);
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}

    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 10px 8px;
      list-style: none;
    }}

    .nav-list::-webkit-scrollbar {{
      width: 5px;
    }}
    .nav-list::-webkit-scrollbar-thumb {{
      background: var(--border);
      border-radius: 4px;
    }}

    .nav-item {{
      margin-bottom: 3px;
    }}

    .nav-link {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 9px 12px;
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.84rem;
      line-height: 1.4;
      font-weight: 500;
      border-radius: var(--radius-sm);
      transition: all 0.15s ease;
    }}

    .nav-link:hover {{
      background-color: rgba(255, 255, 255, 0.05);
      color: var(--accent-blue);
      transform: translateX(3px);
    }}

    .nav-link.active {{
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.15), rgba(99, 102, 241, 0.05));
      color: var(--accent-blue);
      font-weight: 700;
      border-left: 3px solid var(--accent-blue);
    }}

    .nav-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      color: var(--accent-blue);
      background-color: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 2px 5px;
      border-radius: 4px;
      white-space: nowrap;
      margin-top: 1px;
    }}

    .nav-text {{
      flex: 1;
      word-break: keep-all;
    }}

    main {{
      margin-left: 380px;
      flex: 1;
      padding: 40px 60px 100px;
      max-width: 1250px;
      transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-width 0.3s cubic-bezier(0.4, 0, 0.2, 1), padding 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    header.main-header {{
      margin-bottom: 44px;
      padding-bottom: 22px;
      border-bottom: 1px solid var(--border);
    }}

    .badge-top {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 20px;
      color: var(--accent-blue);
      font-size: 0.8rem;
      font-weight: 600;
      margin-bottom: 14px;
    }}

    .main-title {{
      font-size: 2.1rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.3;
      margin-bottom: 10px;
    }}

    .main-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}

    .topic-section {{
      background-color: var(--bg-card);
      border: 6px solid #2a3d66;
      border-radius: var(--radius-lg);
      padding: 34px 38px;
      margin-bottom: 52px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
      scroll-margin-top: 25px;
      transition: all 0.25s ease;
    }}

    .topic-section:hover {{
      border-color: #38bdf8;
      box-shadow: 0 12px 35px rgba(56, 189, 248, 0.25);
    }}

    .latest-card-highlight {{
      border: 6px solid #0284c7;
      background: linear-gradient(180deg, rgba(2, 132, 199, 0.1) 0%, var(--bg-card) 100%);
      box-shadow: 0 10px 35px rgba(2, 132, 199, 0.3);
    }}

    .topic-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 22px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }}

    .topic-title-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .topic-badge {{
      background: linear-gradient(135deg, #0284c7, #6366f1);
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: 6px;
    }}

    .latest-tag {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #10b981;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}

    .topic-title {{
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }}

    .interview-summary-card {{
      background: var(--summary-bg);
      border: 1.5px solid var(--summary-border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin-bottom: 28px;
      position: relative;
      box-shadow: 0 4px 20px rgba(2, 132, 199, 0.15);
    }}

    .summary-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #0284c7;
      color: #ffffff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 12px;
      letter-spacing: 0.03em;
    }}

    .summary-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .summary-list li {{
      font-size: 0.96rem;
      line-height: 1.65;
      color: #e2e8f0;
      position: relative;
      padding-left: 24px;
      font-weight: 500;
    }}

    .summary-list li::before {{
      content: "✔";
      position: absolute;
      left: 0;
      top: 1px;
      color: var(--accent-blue);
      font-size: 0.92rem;
      font-weight: 800;
    }}

    .summary-list li strong {{
      color: #38bdf8;
      font-weight: 700;
    }}

    .lecture-content {{
      line-height: 1.75;
      color: var(--text-sub);
    }}

    .lecture-content h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-main);
      margin: 24px 0 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .lecture-content h3::before {{
      content: "";
      width: 4px;
      height: 16px;
      background: var(--accent-blue);
      border-radius: 2px;
      display: inline-block;
    }}

    .lecture-content p {{
      margin-bottom: 12px;
      font-size: 0.95rem;
    }}

    .lecture-content ul, .lecture-content ol {{
      margin: 10px 0 18px 22px;
    }}

    .lecture-content li {{
      margin-bottom: 8px;
      font-size: 0.94rem;
    }}

    .formula-box {{
      background: rgba(30, 41, 59, 0.4);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 14px 18px;
      margin: 16px 0;
      text-align: center;
      font-size: 1.05rem;
      color: #f8fafc;
    }}

    .analogy-card {{
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(217, 119, 6, 0.04) 100%);
      border-left: 4px solid var(--accent-amber);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 14px 18px;
      margin: 18px 0;
    }}

    .analogy-title {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent-amber);
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .analogy-desc {{
      font-size: 0.9rem;
      color: #f1f5f9;
      line-height: 1.6;
    }}

    .data-table-wrap {{
      overflow-x: auto;
      margin: 18px 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}

    table.data-table th {{
      background-color: #1e293b;
      color: var(--text-main);
      padding: 11px 14px;
      font-weight: 600;
      border-bottom: 1px solid var(--border);
    }}

    table.data-table td {{
      padding: 11px 14px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      color: var(--text-sub);
    }}

    table.data-table tr:hover td {{
      background-color: rgba(255, 255, 255, 0.02);
    }}

    .mobile-top-bar {{ display: none; }}
    .mobile-fab-container {{ display: none; }}
    .drawer-backdrop {{ display: none; }}

    @media (max-width: 900px) {{
      body {{
        flex-direction: column !important;
        overflow-x: hidden !important;
        width: 100% !important;
      }}

      .mobile-top-bar {{
        display: flex !important;
        position: sticky;
        top: 0;
        left: 0;
        right: 0;
        height: 52px;
        background: rgba(9, 13, 26, 0.95);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-bottom: 1px solid #1e293b;
        padding: 0 14px;
        align-items: center;
        justify-content: space-between;
        z-index: 1000;
        box-shadow: 0 4px 16px rgba(0,0,0,0.4);
      }}

      .mobile-menu-btn {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #1e293b;
        color: #38bdf8;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 6px 12px;
        font-size: 0.88rem;
        font-weight: 700;
        cursor: pointer;
      }}

      .mobile-header-title {{
        font-size: 0.95rem;
        font-weight: 800;
        color: #f8fafc;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 55vw;
      }}

      .mobile-top-btn {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        background: #1e293b;
        color: #cbd5e1;
        border: 1px solid #334155;
        border-radius: 8px;
        font-size: 0.9rem;
        cursor: pointer;
      }}

      aside {{
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        bottom: 0 !important;
        width: 84vw !important;
        max-width: 320px !important;
        height: 100vh !important;
        z-index: 1200 !important;
        transform: translateX(-100%) !important;
        transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 4px 0 24px rgba(0,0,0,0.7) !important;
        background: #0b1120 !important;
        overflow-y: auto !important;
      }}

      body.drawer-open aside {{
        transform: translateX(0) !important;
      }}

      .drawer-backdrop {{
        display: block !important;
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(3px);
        -webkit-backdrop-filter: blur(3px);
        z-index: 1100;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.25s ease;
      }}

      body.drawer-open .drawer-backdrop {{
        opacity: 1 !important;
        pointer-events: auto !important;
      }}

      main {{
        margin-left: 0 !important;
        padding: 16px 12px 100px !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        overflow-x: hidden !important;
      }}

      .drawer-float-open-btn {{
        display: none !important;
      }}

      .mobile-fab-container {{
        display: flex !important;
        position: fixed;
        bottom: 24px;
        right: 16px;
        gap: 8px;
        z-index: 950;
      }}

      .mobile-fab-btn {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #0284c7;
        color: #ffffff;
        border: none;
        border-radius: 30px;
        padding: 10px 16px;
        font-size: 0.88rem;
        font-weight: 800;
        box-shadow: 0 4px 16px rgba(2, 132, 199, 0.45);
        cursor: pointer;
      }}

      .mobile-fab-btn.top-btn {{
        background: #1e293b;
        color: #38bdf8;
        border: 1px solid #334155;
        padding: 10px 12px;
        border-radius: 50%;
        width: 42px;
        height: 42px;
        justify-content: center;
      }}

      .topic-section {{
        padding: 16px 12px !important;
        margin-bottom: 20px !important;
        border-radius: 12px !important;
      }}

      .topic-title {{
        font-size: 1.18rem !important;
        line-height: 1.45 !important;
        word-break: keep-all !important;
      }}

      .interview-summary-card {{
        padding: 14px 12px !important;
        border-radius: 8px !important;
      }}

      .summary-list {{
        padding-left: 16px !important;
        font-size: 0.88rem !important;
        line-height: 1.7 !important;
      }}

      .lecture-content div[style*="background:#090d1a"] {{
        padding: 12px 10px !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
      }}
      
      .lecture-content div[style*="background:#090d1a"] svg {{
        min-width: 600px;
        max-width: none !important;
        height: auto;
      }}
    }}
  </style>
</head>
<body>

  <!-- 📱 모바일 상단 헤더 바 -->
  <div class="mobile-top-bar">
    <button class="mobile-menu-btn" onclick="openDrawer()" aria-label="목차 열기">
      <span style="font-size:1.1rem; line-height:1;">☰</span> <span>목차 ({total_count})</span>
    </button>
    <div class="mobile-header-title">배터리 3 Q&amp;A 백과사전</div>
    <button class="mobile-top-btn" onclick="scrollToTop()" aria-label="맨 위로">
      <span>⬆</span>
    </button>
  </div>

  <!-- 📱 모바일 서랍 배경 오버레이 -->
  <div id="drawerBackdrop" class="drawer-backdrop" onclick="closeDrawer()"></div>

  <!-- 📱 모바일 우측 하단 플로팅 액션 버튼 (FAB) -->
  <div class="mobile-fab-container">
    <button class="mobile-fab-btn" onclick="openDrawer()">
      <span>📑</span> <span>목차 열기</span>
    </button>
    <button class="mobile-fab-btn top-btn" onclick="scrollToTop()" title="맨 위로">
      <span>⬆</span>
    </button>
  </div>

  <!-- 목차 서랍 열기 플로팅 버튼 (서랍 접혔을 때 표시) -->
  <button id="sidebarFloatOpenBtn" class="drawer-float-open-btn" title="목차 펼치기"><span>📑</span> <span>목차 열기</span></button>

  <aside>
    <div class="sidebar-header">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1>배터리 3 Q&amp;A 백과사전</h1>
        <button id="sidebarCollapseBtn" class="drawer-toggle-btn" title="목차 서랍 닫기">◀ 목차 접기</button>
      </div>
      <p>질문하신 순서의 역순(최신순)으로 정렬된 탭</p>
    </div>
    <div class="search-box">
      <input type="text" id="searchInput" class="search-input" placeholder="전극 공정·설비 키워드 검색...">
    </div>
    <ul class="nav-list" id="navList">
{nav_list_str}
    </ul>
  </aside>

  <!-- 메인 컨텐츠 영역 -->
  <main>
    <header class="main-header">
      <div class="badge-top">⚡ 질문 기반 역순(최신순) 마스터 핸드북</div>
      <h2 class="main-title">이차전지 전극 공정 &amp; 생산·운영 Q&amp;A 백과사전</h2>
      <p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'{latest_nav_title}'</strong>이(가) 최신 1번(Q 01)으로 위치하며, 총 <strong>{total_count}개</strong> 질문이 차근차근 누적되어 있습니다.</p>
    </header>
{sections_str}
  </main>

  <script>
    const searchInput = document.getElementById('searchInput');
    const sections = document.querySelectorAll('.topic-section');
    const navLinks = document.querySelectorAll('.nav-link');

    searchInput.addEventListener('input', (e) => {{
      const keyword = e.target.value.toLowerCase();
      sections.forEach(sec => {{
        const text = sec.innerText.toLowerCase();
        if (text.includes(keyword)) {{
          sec.style.display = 'block';
        }} else {{
          sec.style.display = 'none';
        }}
      }});
    }});

    window.addEventListener('scroll', () => {{
      let current = '';
      sections.forEach(sec => {{
        const secTop = sec.offsetTop - 120;
        if (window.scrollY >= secTop) {{
          current = sec.getAttribute('id');
        }}
      }});

      navLinks.forEach(link => {{
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${{current}}`) {{
          link.classList.add('active');
          if (current) localStorage.setItem('battery3_last_q', current);
        }}
      }});
    }});

    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const sidebarFloatOpenBtn = document.getElementById('sidebarFloatOpenBtn');

    if (sidebarCollapseBtn) {{
      sidebarCollapseBtn.addEventListener('click', () => {{
        document.body.classList.add('sidebar-collapsed');
        localStorage.setItem('battery3_sidebar_collapsed', 'true');
      }});
    }}

    if (sidebarFloatOpenBtn) {{
      sidebarFloatOpenBtn.addEventListener('click', () => {{
        document.body.classList.remove('sidebar-collapsed');
        localStorage.setItem('battery3_sidebar_collapsed', 'false');
      }});
    }}

    if (localStorage.getItem('battery3_sidebar_collapsed') === 'true') {{
      document.body.classList.add('sidebar-collapsed');
    }}

    function openDrawer() {{
      document.body.classList.add('drawer-open');
    }}

    function closeDrawer() {{
      document.body.classList.remove('drawer-open');
    }}

    function scrollToTop() {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    document.addEventListener('DOMContentLoaded', function() {{
      const mobileLinks = document.querySelectorAll('#navList a');
      mobileLinks.forEach(function(link) {{
        link.addEventListener('click', function() {{
          if (window.innerWidth <= 900) {{
            closeDrawer();
          }}
        }});
      }});
    }});
  </script>
</body>
</html>
"""
    return html


def generate_markdown(topics: list, live_url: str = "https://richvayne13.github.io/battery-3/") -> str:
    """질문 리스트를 받아 마스터 보고서(MD) 문자열을 반환합니다."""
    now_str = datetime.now().strftime("%Y년 %m월 %d일")
    rows = []
    for idx, t in enumerate(topics, start=1):
        num_str = f"{idx:02d}"
        star = " ⭐ [최신 1번]" if idx == 1 else ""
        # strip html tags for summary preview
        import re
        clean_summaries = [re.sub(r"<[^>]+>", "", s) for s in t["summary"]]
        kw_summary = " / ".join(clean_summaries[:2])
        rows.append(f"| **Q {num_str}** | **{t['nav_title']}**{star} | {t['badge']} · {kw_summary} |")

    table_str = "\n".join(rows)
    md = f"""# [보고서] 배터리 3 : 이차전지 전극 공정 & 생산·운영 Q&A 마스터 백과사전

- **작성일자**: {now_str}
- **저장경로**: `C:\\Work\\배터리3\\result\\261017_v1.0\\261017_battery_electrode_master.md`
- **배포 대시보드**: [C:\\Work\\배터리3\\index.html](file:///C:/Work/%EB%B0%B0%ED%84%B0%EB%A6%AC3/index.html)
- **온라인 라이브 서비스**: [{live_url}]({live_url})

---

## 1. 개요 및 목적
본 보고서와 대시보드는 **사용자께서 직접 질문하신 문장 그대로 좌측 내비게이션 탭의 제목으로 구성**하고, **가장 최근에 질문하신 순서(역순/최신순)로 1번부터 차근차근 배치**하여 이차전지 전극 공정 및 생산·운영 핵심 지식을 한눈에 마스터할 수 있도록 구축되었습니다.

각 질문 섹션은 항상 **[강의 핵심 요약 포인트]**가 선행되고, 이어지는 **[세부 마스터 강의 노트]**에서 직관적인 고해상도 풀컬러 SVG 시각 다이어그램과 심층 엔지니어링 원리, 현장 트러블슈팅 테이블을 다룹니다.

---

## 2. 사용자 질문 기반 목차 (최신순 Q&A 대기록 - 총 {len(topics)}문항)

| 순번 | 좌측 탭 제목 (사용자 실제 질문) | 핵심 요약 키워드 |
| :---: | :--- | :--- |
{table_str}
"""
    return md
