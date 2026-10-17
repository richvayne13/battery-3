# -*- coding: utf-8 -*-
"""
topic_q01_fatedge_sliding.py
Q 01 (최신 1번): 전극에서 FAT EDGE, SLIDING이 뭐고 원인이 뭐고 개선안이 뭔지 알려줘
"""

TOPIC_Q01 = {
    "badge": "슬롯 다이 코팅 & 에지 프로파일 제어",
    "nav_title": "전극에서 FAT EDGE, SLIDING이 뭐고 원인이 뭐고 개선안이 뭔지 알려줘",
    "title": "전극 코팅 에지 프로파일(Edge Profile) 불량 완전 해부: Fat Edge(팻 엣지·에지 솟음)와 Sliding(슬라이딩·흘러내림)의 물리적 원인, 3축 개선안 및 Trade-off 제어",
    "summary": [
        "<strong>1. Fat Edge(팻 엣지 / Dog-bone)의 정의와 치명성</strong>: 코팅 폭 양 끝단(Edge) 두께가 중앙부(Center)보다 볼록하게 솟아오르는 현상입니다. 권취 시 양 끝 외경만 뚱뚱해지는 <strong>게이지 밴드(이바리)와 웹 단선(Web Break)</strong>을 유발하고, 롤프레스 압연 시 끝단 과압연·크랙 및 셀 충·방전 시 국부 <strong>리튬 석출(Li-Plating)</strong>을 초래합니다.",
        "<strong>2. Sliding(슬라이딩 / Edge Taper)의 정의와 치명성</strong>: 코팅 끝단이 수직으로 떨어지지 않고 무지부(Foil) 쪽으로 완만하게 경사지며 길게 흘러내리는 현상입니다. 무지부 탭(Tab) 영역을 침범해 <strong>노칭·용접 불량</strong>을 일으키고, 에지부 저로딩으로 인해 음/양극 <strong>N/P Ratio 역전 및 덴드라이트 단락</strong> 위험을 높입니다.",
        "<strong>3. 핵심 발생 원인 (유체역학·슬러리·건조)</strong>: <strong>Fat Edge</strong>는 다이 출구 비드 양 끝단의 표면장력 수축(Neck-in), 직각 심(Shim) 끝단 유속 집중, 건조 초기 에지 급속 증발에 의한 <strong>커피링 효과(Coffee-ring Effect)</strong>가 주원인입니다. 반면 <strong>Sliding</strong>은 코팅 직후 슬러리의 <strong>저전단 점도·항복응력(요변성) 부족</strong>, 과도한 코팅 갭(Gap), 초기 건조(Pinning) 지연 때문에 발생합니다.",
        "<strong>4. 현장 3축 개선 솔루션 (Hardware · Process · Material)</strong>: ① <strong>심(Shim) 끝단 모따기(Chamfer/Step Shim)</strong>로 에지 유량·압력 분산(Fat Edge 억제), ② <strong>코팅 갭(Coating Gap) 축소</strong>로 코팅 비드 구속력 강화, ③ <strong>초기 건조 Zone 온도·IR 히터 튜닝</strong>(Sliding 시 에지 Pinning 강화 vs Fat Edge 시 급속 증발 완화), ④ <strong>슬러리 고요변성(High Thixotropy) 물성 피드백</strong>으로 해결합니다.",
        "<strong>5. 생산·운영 핵심 노하우 (Trade-off 공정 창 관리)</strong>: Fat Edge를 잡으려 유동성을 높이면 Sliding이 길어지고, Sliding을 잡으려 점도·초기건조를 과하게 올리면 Fat Edge가 솟는 <strong>상충 관계(Trade-off)</strong>에 있으므로, 에지 프로파일 스캔 데이터를 기반으로 두 지표를 동시에 USL 이내로 가두는 <strong>공정 창(Process Window) 표준화</strong>가 핵심입니다."
    ],
    "svg_title": "📊 [전극 에지 프로파일(Edge Profile) 3대 단면 비교 및 제어 메커니즘] (A) 이상적 에지 vs Fat Edge(Dog-bone) vs Sliding 단면 | (B) Chamfer Shim(모따기 심) 유동 분산 원리 | (C) Fat Edge - Sliding Trade-off 공정 창",
    "svg": """<svg viewBox="0 0 980 450" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="450" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Cross-Sectional Profiles -->
  <g transform="translate(18, 18)">
    <rect width="450" height="414" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12.5" font-weight="800">■ (A) 전극 코팅 단면 에지 프로파일 3대 형태 비교</text>

    <!-- 1. Ideal Profile -->
    <g transform="translate(16, 40)">
      <rect width="418" height="105" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
      <text x="12" y="18" fill="#34d399" font-size="10" font-weight="800">✔ 1) 이상적인 에지 프로파일 (Ideal Sharp Edge)</text>
      <!-- Foil -->
      <rect x="20" y="75" width="378" height="12" fill="#f59e0b" rx="1"/>
      <text x="160" y="84" fill="#0f172a" font-size="7.5" font-weight="800">집전체 박막 (Al / Cu Foil)</text>
      <!-- Coating Layer -->
      <path d="M 75 75 L 82 40 L 336 40 L 343 75 Z" fill="#0284c7" opacity="0.9"/>
      <text x="165" y="61" fill="#ffffff" font-size="9" font-weight="700">정상 코팅층 (균일 로딩량)</text>
      <text x="22" y="68" fill="#94a3b8" font-size="7.5">무지부(Foil)</text>
      <text x="348" y="68" fill="#94a3b8" font-size="7.5">무지부(Foil)</text>
      <text x="12" y="99" fill="#6ee7b7" font-size="8">• 에지 솟음(Bump) 제로 &amp; 짧은 슬라이딩 폭(규격 이내) ➔ 권취·압연·셀 품질 최상</text>
    </g>

    <!-- 2. Fat Edge Profile -->
    <g transform="translate(16, 158)">
      <rect width="418" height="118" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.2"/>
      <text x="12" y="18" fill="#f87171" font-size="10" font-weight="800">❌ 2) Fat Edge (팻 엣지 / Dog-bone 현상 : 양 끝단 볼록 솟음)</text>
      <!-- Foil -->
      <rect x="20" y="82" width="378" height="12" fill="#f59e0b" rx="1"/>
      <!-- Dog-bone Coating Layer -->
      <path d="M 75 82 L 80 24 Q 95 18 112 48 L 306 48 Q 323 18 338 24 L 343 82 Z" fill="#ef4444" opacity="0.85"/>
      <!-- Reference Normal thickness dashed line -->
      <line x1="70" y1="48" x2="350" y2="48" stroke="#fde047" stroke-width="1.2" stroke-dasharray="4,3"/>
      <text x="155" y="68" fill="#ffffff" font-size="8.5" font-weight="700">중앙 정상 두께 (Center)</text>
      <!-- Bump annotations -->
      <text x="58" y="19" fill="#fde047" font-size="8" font-weight="800">▲ Fat Edge (+ΔH)</text>
      <text x="295" y="19" fill="#fde047" font-size="8" font-weight="800">▲ Fat Edge (+ΔH)</text>
      <text x="12" y="108" fill="#fca5a5" font-size="8">• 원인: Neck-in 표면장력 뭉침 + 초기 건조 커피링 효과 ➔ 권취 이바리/단선, 과압연, Li 석출</text>
    </g>

    <!-- 3. Sliding Profile -->
    <g transform="translate(16, 288)">
      <rect width="418" height="114" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="12" y="18" fill="#fbbf24" font-size="10" font-weight="800">⚠️ 3) Sliding (슬라이딩 / Edge Taper 과다 : 양 끝단 무너져 흘러내림)</text>
      <!-- Foil -->
      <rect x="20" y="78" width="378" height="12" fill="#f59e0b" rx="1"/>
      <!-- Slumped Coating Layer -->
      <path d="M 32 78 Q 75 74 120 44 L 298 44 Q 343 74 386 78 Z" fill="#8b5cf6" opacity="0.85"/>
      <!-- Sliding width arrows -->
      <line x1="32" y1="34" x2="120" y2="34" stroke="#38bdf8" stroke-width="1.8"/>
      <line x1="32" y1="29" x2="32" y2="76" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
      <line x1="120" y1="29" x2="120" y2="44" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="38" y="29" fill="#38bdf8" font-size="8" font-weight="800">◀ 슬라이딩 폭 (W_slide 과다) ▶</text>
      <text x="155" y="65" fill="#ffffff" font-size="8.5" font-weight="700">유효 정상 로딩 구간 축소!</text>
      <text x="12" y="104" fill="#fde68a" font-size="8">• 원인: 저전단 점도(요변성) 부족 + 코팅 갭 과다 + 초기 건조 지연 ➔ 무지부 침범, N/P 역전</text>
    </g>
  </g>

  <!-- PANEL B: Hardware & Process Solutions -->
  <g transform="translate(484, 18)">
    <rect width="478" height="205" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12.5" font-weight="800">■ (B) 하드웨어 핵심 해법: 직각 심(Shim) vs 모따기 챔퍼 심(Chamfer Shim)</text>

    <!-- Left sub-box: Straight Shim -->
    <g transform="translate(16, 40)">
      <rect width="215" height="150" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="800">1) 일반 직각 심 (90° Straight Shim)</text>
      <!-- Shim Plate -->
      <rect x="15" y="28" width="55" height="70" fill="#475569"/>
      <text x="20" y="65" fill="#cbd5e1" font-size="8" font-weight="700">Shim 가이드</text>
      <!-- Slurry Flow arrows -->
      <line x1="90" y1="35" x2="90" y2="90" stroke="#38bdf8" stroke-width="2"/>
      <line x1="125" y1="35" x2="125" y2="90" stroke="#38bdf8" stroke-width="2"/>
      <!-- Edge Neck-in accumulation -->
      <path d="M 70 35 L 70 85 Q 72 95 85 95" fill="none" stroke="#ef4444" stroke-width="2.5"/>
      <circle cx="82" cy="92" r="9" fill="#ef4444" opacity="0.7"/>
      <text x="96" y="96" fill="#fca5a5" font-size="7.5" font-weight="700">끝단 유량 뭉침 (Neck-in)</text>
      <text x="12" y="122" fill="#cbd5e1" font-size="7.8">• 출구 끝단에서 표면장력이 안쪽으로 당김</text>
      <text x="12" y="138" fill="#fca5a5" font-size="7.8" font-weight="700">➔ 양 끝단에 슬러리 과집중 (Fat Edge 유발)</text>
    </g>

    <!-- Right sub-box: Chamfer Shim -->
    <g transform="translate(245, 40)">
      <rect width="217" height="150" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">2) 챔퍼/스텝 심 (Chamfered Shim)</text>
      <!-- Chamfered Shim Plate -->
      <polygon points="15,28 70,28 70,65 45,98 15,98" fill="#059669"/>
      <text x="18" y="58" fill="#ffffff" font-size="8" font-weight="700">Chamfer</text>
      <text x="20" y="70" fill="#fde047" font-size="7.5" font-weight="700">모따기 각도</text>
      <!-- Dispersed Flow arrows -->
      <path d="M 82 35 Q 80 70 62 92" fill="none" stroke="#34d399" stroke-width="2"/>
      <line x1="110" y1="35" x2="110" y2="92" stroke="#38bdf8" stroke-width="2"/>
      <line x1="140" y1="35" x2="140" y2="92" stroke="#38bdf8" stroke-width="2"/>
      <text x="72" y="95" fill="#6ee7b7" font-size="7.5" font-weight="700">압력·유속 자연 감압!</text>
      <text x="12" y="122" fill="#cbd5e1" font-size="7.8">• 출구 직전 유로 확장으로 에지 압력 완화</text>
      <text x="12" y="138" fill="#6ee7b7" font-size="7.8" font-weight="700">➔ Neck-in 상쇄 &amp; 평탄한 에지 확보!</text>
    </g>
  </g>

  <!-- PANEL C: Trade-off Process Window -->
  <g transform="translate(484, 235)">
    <rect width="478" height="197" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12.5" font-weight="800">■ (C) 생산·운영 핵심: Fat Edge ↔ Sliding 상충 관계(Trade-off) 제어</text>

    <g transform="translate(16, 38)">
      <rect width="446" height="145" rx="6" fill="#1e293b"/>
      <!-- Axis -->
      <line x1="45" y1="115" x2="420" y2="115" stroke="#94a3b8" stroke-width="1.5"/>
      <line x1="45" y1="20" x2="45" y2="115" stroke="#94a3b8" stroke-width="1.5"/>
      <text x="125" y="135" fill="#cbd5e1" font-size="8.5" font-weight="700">◀ 저점도 / 넓은 갭 / 느린 초기건조  |  고점도(고요변성) / 좁은 갭 / 빠른 초기 Pinning ▶</text>

      <!-- Sliding Curve (Decreases to right) -->
      <path d="M 60 28 Q 180 40 390 105" fill="none" stroke="#8b5cf6" stroke-width="3"/>
      <text x="65" y="24" fill="#c4b5fd" font-size="8.5" font-weight="800">Sliding 폭 (W_slide)</text>

      <!-- Fat Edge Curve (Increases to right) -->
      <path d="M 60 105 Q 280 40 390 25" fill="none" stroke="#ef4444" stroke-width="3"/>
      <text x="315" y="24" fill="#fca5a5" font-size="8.5" font-weight="800">Fat Edge 높이 (H_fat)</text>

      <!-- Target Process Window Box -->
      <rect x="185" y="22" width="95" height="93" fill="#10b981" opacity="0.18" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4,2"/>
      <text x="195" y="42" fill="#34d399" font-size="9" font-weight="800">🎯 최적 공정 창</text>
      <text x="193" y="55" fill="#6ee7b7" font-size="7.5">(Process Window)</text>
      <text x="192" y="102" fill="#ffffff" font-size="7.5" font-weight="700">Chamfer Shim +</text>
      <text x="192" y="112" fill="#ffffff" font-size="7.5" font-weight="700">Coating Gap + IR 제어</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
<h3>1. Fat Edge와 Sliding의 직관적 개념 정의</h3>
<p>
이차전지 전극 코터(Slot-Die Coater)에서 슬러리를 집전체(Al/Cu Foil) 위에 도포할 때, 코팅이 되는 <strong>유지부(Coated Area)</strong>와 코팅이 되지 않는 <strong>무지부(Uncoated Foil, 탭 영역)</strong>의 경계면인 <strong>양 끝단 에지(Edge) 단면 프로파일</strong>에서 발생하는 대표적인 2대 형상 불량입니다.
</p>

<div class="analogy-card">
  <div class="analogy-title">💡 가장 직관적인 비유: '식빵 위에 땅콩버터 바르기'</div>
  <div class="analogy-desc">
    • <strong>Fat Edge (팻 엣지 / Dog-bone)</strong>: 나이프로 잼을 바를 때 양 끝 테두리에 잼이 밀려 뭉치면서 <strong>양쪽 가장자리만 둑처럼 볼록하게 솟아오른 상태</strong>입니다.<br>
    • <strong>Sliding (슬라이딩 / Edge Taper)</strong>: 잼이 너무 묽어서 바른 직후 가장자리가 수직으로 서 있지 못하고, 옆쪽 빈 식빵(무지부) 쪽으로 <strong>질질 흘러내려 경사면이 길어진 상태</strong>입니다.
  </div>
</div>

<h3>2. 왜 치명적인가? (후공정 수율 및 셀 안전성에 미치는 영향)</h3>
<ul>
  <li><strong>Fat Edge가 유발하는 연쇄 불량</strong>:
    <ol>
      <li><strong>권취(Rewinding) 게이지 밴드(이바리) 및 웹 단선</strong>: 수천 미터의 점보 롤을 감을 때 양 끝단 두께가 $2 \sim 5\,\mu\text{m}$만 더 두꺼워도, 수백 바퀴가 누적되면 양 끝 외경만 볼록하게 솟는 <strong>이바리(Edge Ridging)</strong>가 발생합니다. 이로 인해 양 끝에 과도한 인장 응력이 집중되어 호일이 늘어나고 주름 및 <strong>단선(Web Break)</strong>이 발생합니다.</li>
      <li><strong>롤프레스(Roll Press) 과압연 및 에지 크랙</strong>: 압연 롤을 통과할 때 두꺼운 에지부에 선압(Line Pressure)이 집중되어 활물질이 깨지거나 호일이 찢어지고, 전극이 활처럼 휘는 <strong>캠버(Camber)</strong>를 유발합니다.</li>
      <li><strong>셀 리튬 석출(Li-Plating)</strong>: 국부적으로 로딩량(Loading Level)이 치솟아 충·방전 시 에지부 전류 밀도 왜곡 및 리튬 석출을 유발합니다.</li>
    </ol>
  </li>
  <li><strong>Sliding이 유발하는 연쇄 불량</strong>:
    <ol>
      <li><strong>무지부(Tab) 침범 및 노칭·용접 불량</strong>: 슬라이딩 폭($W_{slide}$)이 규격(통상 수 $\text{mm}$ 이내)을 벗어나 무지부를 침범하면, 노칭(Notching) 공정에서 탭에 코팅 잔여물이 남아 리드 탭 초음파/레이저 용접 불량을 일으킵니다.</li>
      <li><strong>국부 N/P Ratio 역전 (치명적 안전성 문제)</strong>: 슬라이딩 구간은 정상 두께보다 얇게 발린 저로딩 구간입니다. 특히 <strong>음극 에지의 슬라이딩이 길어지면 양극 에지 대비 음극 용량이 부족해져 국부 $\text{N/P Ratio} < 1.0$ 역전</strong>이 발생하고, 충전 시 리튬 덴드라이트(Dendrite)가 자라나 분리막을 뚫는 내부 단락(Short)으로 직결됩니다.</li>
    </ol>
  </li>
</ul>

<h3>3. 발생 원인 심층 해부 (유체역학 · 슬러리 유변학 · 건조 메커니즘)</h3>

<div class="formula-box">
  $$\text{Capillary Number } (Ca) = \frac{\mu \cdot V}{\sigma}, \qquad \text{Yield Stress Condition: } \tau_y > \rho g h \frac{\partial h}{\partial x}$$
</div>

<ul>
  <li><strong>Fat Edge (에지 솟음)의 3대 원인</strong>:
    <ul>
      <li><strong>① 코팅 비드(Bead) 양 끝단의 Neck-in 현상</strong>: 슬롯 다이 립에서 토출된 액상 슬러리는 공기와 만나는 양 끝단에서 <strong>표면장력($\sigma$)</strong>에 의해 안쪽으로 오므라들려는 힘(Capillary Force)을 받습니다. 이때 양 끝단으로 슬러리 유량이 밀려 뭉치면서 에지가 두꺼워집니다.</li>
      <li><strong>② 직각 심(Straight Shim) 끝단의 유속·압력 집중</strong>: 다이 내부 유로를 결정하는 심(Shim) 모서리가 $90^\circ$ 직각이면 다이 출구 양 끝에서 와류와 압력 피크가 발생해 토출량이 끝단에 집중됩니다.</li>
      <li><strong>③ 건조 초기 커피링 효과(Coffee-ring Effect)</strong>: 건조로 Zone 1 진입 시 에지부는 중앙부와 달리 3면이 열풍에 노출되어 용매(NMP 또는 물) 증발 속도가 훨씬 빠릅니다. 증발된 용매를 보충하기 위해 내부에서 에지 쪽으로 모세관 유동(Capillary Flow)이 일어나 고형분 입자가 에지에 쌓입니다.</li>
    </ul>
  </li>
  <li><strong>Sliding (에지 흘러내림)의 3대 원인</strong>:
    <ul>
      <li><strong>① 슬러리 저전단 점도 및 항복응력($\tau_y$) 부족</strong>: 슬러리는 다이 립을 통과할 때(고전단)는 점도가 낮아 잘 흘러야 하지만, 호일 위에 안착한 직후(저전단, $\dot{\gamma} \to 0$)에는 즉각 구조가 회복되는 <strong>요변성(Thixotropy)</strong>과 <strong>항복응력($\tau_y$)</strong>이 높아야 합니다. 이 회복이 느리면 중력과 모세관 퍼짐에 의해 옆으로 무너져 내립니다.</li>
      <li><strong>② 코팅 갭(Coating Gap, $G_c$) 과다</strong>: 백업롤과 다이 립 사이의 간격이 너무 넓으면 코팅 비드를 잡아주는 구속력이 약해져 도포 즉시 양옆으로 퍼집니다.</li>
      <li><strong>③ 초기 건조 고화(Edge Pinning) 지연</strong>: 코팅 직후 건조로 초입에서 에지 경계면이 빠르게 고화(Pinning)되지 못하면, 오븐 내 플로테이션 노즐 풍압에 밀려 옆으로 흘러내립니다.</li>
    </ul>
  </li>
</ul>

<h3>4. 현장 엔지니어의 3축 개선안 및 Trade-off 제어 표</h3>
<p>
현장에서는 <strong>Fat Edge와 Sliding이 서로 반비례(Trade-off) 관계</strong>에 있다는 점을 반드시 고려하여 <strong>하드웨어(다이/심) + 공정 파라미터(갭/건조) + 슬러리 물성(믹싱 피드백)</strong>을 조합해 공정 창(Process Window)을 잡습니다.
</p>

<div class="data-table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>제어 영역</th>
        <th>Fat Edge (에지 솟음) 개선 대책</th>
        <th>Sliding (에지 흘러내림) 개선 대책</th>
        <th>Trade-off 관리 포인트</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. 하드웨어<br>(Slot Die &amp; Shim)</strong></td>
        <td>• <strong>챔퍼 심(Chamfer Shim) / 스텝 심(Step Shim)</strong> 적용: 심 끝단을 사선 모따기하여 에지 토출 압력·유량 분산<br>• 다이 립 끝단 테플론(PTFE) 발수 코팅 점검</td>
        <td>• 심(Shim) 챔퍼 각도 과다 시 축소 조정<br>• 에지 가이드(Edge Dam / 세라믹 블록) 밀착도 점검 및 백업롤 런아웃 교정</td>
        <td>챔퍼 각도를 너무 크게 깎으면 Fat Edge는 사라지나 에지 유량이 부족해져 <strong>Sliding 폭이 급증</strong>함 (모델별 최적 심 규격 표준화 필수)</td>
      </tr>
      <tr>
        <td><strong>2. 코터 &amp; 건조 조건<br>(Process Recipe)</strong></td>
        <td>• <strong>초기 건조 Zone 1 열풍 온도·풍속 완화</strong>: 에지 급속 증발에 의한 커피링(Coffee-ring) 쏠림 억제<br>• 코팅 속도 대비 다이 압력 밸런스 최적화</td>
        <td>• <strong>코팅 갭(Coating Gap) 축소</strong>: 비드 구속력 강화로 퍼짐 차단<br>• <strong>에지 IR 히터 가동 및 Zone 1 초기 고화(Pinning) 강화</strong>로 흘러내림 조기 차단</td>
        <td>코팅 갭($G_c$)을 적정 하한선으로 좁히면 비드 안정성이 높아져 <strong>Fat Edge와 Sliding을 동시에 줄이는 핵심 레버</strong>로 작동함</td>
      </tr>
      <tr>
        <td><strong>3. 슬러리 물성<br>(Mixing 피드백)</strong></td>
        <td>• 슬러리 과도한 표면장력 완화 및 탈포(De-aeration) 강화<br>• 바인더(PVDF, CMC/SBR) 분산 균일도 확보</td>
        <td>• <strong>고형분(Solid Content) 상향</strong> 및 <strong>저전단 점도 / 요변성(TI 지수) 상향</strong> 피드백<br>• 토출 직후 구조 회복 속도 향상</td>
        <td>단일 회전수 점도만 관리하지 않고, 고전단/저전단 점도비(TI, Thixotropic Index)를 출하 스펙으로 관리</td>
      </tr>
    </tbody>
  </table>
</div>

<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"전극 생산·운영의 핵심은 <strong>챔퍼 심(Chamfer Shim) 표준화</strong>로 Fat Edge의 물리적 뭉침을 선제적으로 잡고, 실시간 공초점 레이저/방사선 두께 프로파일러를 보며 <strong>코팅 갭(Gap) 축소와 초기 건조 Pinning(IR/Zone 1)</strong>을 미세 튜닝하여 Fat Edge 높이와 Sliding 폭을 동시에 규격(USL) 내에 가두는 것입니다!"
</blockquote>
"""
}
