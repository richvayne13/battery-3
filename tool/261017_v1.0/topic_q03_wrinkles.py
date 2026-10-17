# -*- coding: utf-8 -*-
"""
topic_q03_wrinkles.py
Q 03: 넌 전극코터전문가야 일자주름과 사선주름은 각각 어떻게 잡아야 돼?
"""

TOPIC_Q03 = {
    "badge": "웹 핸들링(Web Handling) & 주름 제어 역학",
    "nav_title": "넌 전극코터전문가야 일자주름과 사선주름은 각각 어떻게 잡아야 돼?",
    "title": "전극 코터 웹 핸들링(Web Handling) 주름 제어 완벽 가이드: 일자주름(종주름, MD Wrinkle)과 사선주름(대각선 주름, Diagonal Wrinkle)의 발생 역학 및 현장 교정법",
    "summary": [
        "<strong>1. 두 주름의 물리적 메커니즘 구분</strong>: <strong>일자주름(종주름, MD Wrinkle)</strong>은 웹 진행 방향(MD)과 나란하게 잡히는 주름으로, 과도한 장력에 의한 포아송 수축 등 <strong>폭 방향(TD) 압축 응력($\\sigma_{TD}$)</strong>이 박막 호일의 임계 좌굴 하중을 넘을 때 발생합니다. 반면 <strong>사선주름(대각선 주름, Diagonal Wrinkle)</strong>은 작업자 측(OS)과 구동 측(DS) 사이의 <strong>좌우 장력 불균형 및 전단 응력($\\tau_{xy}$, 비틀림)</strong> 때문에 대각선으로 타고 흐릅니다.",
        "<strong>2. 일자주름(종주름) 3대 교정 솔루션</strong>: ① 주름 발생 구간의 <strong>설정 장력(Set Tension) 하향 및 리와인더 Taper Tension 상향</strong>, ② 주름 인입 롤 직전의 <strong>익스팬더 롤(Bow Roll, 활롤) 곡률(Bow 양) 및 진입 각도 최적화</strong>로 폭 방향 펼침력 부여, ③ 건조로 상·하부 노즐 풍압 밸런싱(플러터링 방지) 및 초기 건조 온도 완화로 유지부-무지부 수축 차이를 줄입니다.",
        "<strong>3. 사선주름(대각선 주름) 판독 공식과 3대 교정 솔루션</strong>: 웹 진행 방향 기준으로 <strong>사선주름의 윗부분이 향하는 쪽이 장력이 더 강하거나(팽팽하거나) 롤에 먼저 닿는 쪽</strong>입니다. ① 주름 발원지 가이드 롤의 <strong>수평도(Level)·평행도(Parallelism) 영점 교정(1순위)</strong>, ② <strong>좌우(OS/DS) 코팅 로딩량 편차 및 닙 롤(Nip Roll) 좌우 공압 밸런싱</strong>, ③ <strong>EPC(사행 제어기) 게인(Gain) 및 반응 속도 완화</strong>로 헌팅(Hunting) 비틀림을 제거합니다."
    ],
    "svg_title": "📊 [전극 코터 일자주름(MD) vs 사선주름(Diagonal) 발생 역학 및 교정 도감] (A) 일자주름: 폭 방향 압축 좌굴 & Bow Roll 교정 | (B) 사선주름: 롤 얼라인먼트 틀어짐에 의한 전단 응력 & 교정 방향 공식",
    "svg": """<svg viewBox="0 0 980 440" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="440" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Longitudinal (MD) Wrinkle -->
  <g transform="translate(18, 18)">
    <rect width="460" height="404" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12.5" font-weight="800">■ (A) 일자주름 (종주름, MD Wrinkle): 폭 방향 압축 좌굴</text>

    <!-- Top Diagram: Mechanism -->
    <g transform="translate(16, 40)">
      <rect width="428" height="175" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="10" font-weight="800">1) 발생 메커니즘: MD 장력 과다 ➔ TD 포아송 수축 좌굴</text>

      <!-- Top Roll & Bottom Roll -->
      <rect x="95" y="28" width="238" height="16" rx="4" fill="#475569"/>
      <rect x="95" y="132" width="238" height="16" rx="4" fill="#475569"/>
      <!-- Web Foil between rolls -->
      <path d="M 105 44 Q 120 88 105 132 L 323 132 Q 308 88 323 44 Z" fill="#334155" stroke="#94a3b8" stroke-width="1"/>

      <!-- Vertical MD Tension Arrows -->
      <text x="15" y="90" fill="#fde047" font-size="8.5" font-weight="800">MD 장력 과다</text>
      <text x="15" y="103" fill="#fde047" font-size="8">(Tension ↑↑)</text>

      <!-- Horizontal TD Compression Arrows -->
      <line x1="75" y1="88" x2="112" y2="88" stroke="#ef4444" stroke-width="2.5"/>
      <polygon points="112,84 120,88 112,92" fill="#ef4444"/>
      <line x1="353" y1="88" x2="316" y2="88" stroke="#ef4444" stroke-width="2.5"/>
      <polygon points="316,84 308,88 316,92" fill="#ef4444"/>
      <text x="332" y="78" fill="#fca5a5" font-size="8" font-weight="700">TD 압축 응력</text>

      <!-- Longitudinal Wrinkle Lines in center -->
      <line x1="185" y1="48" x2="185" y2="128" stroke="#ef4444" stroke-width="2.5"/>
      <line x1="214" y1="46" x2="214" y2="130" stroke="#ef4444" stroke-width="3"/>
      <line x1="243" y1="48" x2="243" y2="128" stroke="#ef4444" stroke-width="2.5"/>
      <text x="162" y="164" fill="#fca5a5" font-size="8.5" font-weight="700">★ 진행 방향(MD)과 나란한 세로 일자주름 발생!</text>
    </g>

    <!-- Bottom Diagram: Solution (Bow Roll & Tension) -->
    <g transform="translate(16, 226)">
      <rect width="428" height="162" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="20" fill="#34d399" font-size="10" font-weight="800">2) 핵심 해결책: 장력 하향 + 익스팬더 롤(Bow Roll) 펼침 제어</text>

      <!-- Bowed Roll Illustration -->
      <path d="M 90 55 Q 214 32 338 55" fill="none" stroke="#38bdf8" stroke-width="10" stroke-linecap="round"/>
      <text x="155" y="36" fill="#38bdf8" font-size="8.5" font-weight="800">익스팬더 롤 (Bow Roll / 활롤)</text>
      <!-- Outward spreading arrows -->
      <line x1="180" y1="58" x2="115" y2="75" stroke="#34d399" stroke-width="2"/>
      <line x1="248" y1="58" x2="313" y2="75" stroke="#34d399" stroke-width="2"/>
      <text x="148" y="78" fill="#6ee7b7" font-size="8" font-weight="700">◀ 폭 방향(TD) 양옆으로 펴줌 ▶</text>

      <text x="14" y="102" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#38bdf8" font-weight="700">솔루션 1 (장력)</tspan>: 해당 구간 Set Tension 하향 &amp; 권취 Taper Tension 상향</text>
      <text x="14" y="120" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#38bdf8" font-weight="700">솔루션 2 (Bow Roll)</tspan>: 활롤 곡률(Bow 양) 및 웹 진입 각도(Apex) 조정</text>
      <text x="14" y="138" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#38bdf8" font-weight="700">솔루션 3 (건조로)</tspan>: 상·하 노즐 풍압 밸런싱 &amp; Zone 1 급격한 온도 완화</text>
      <text x="14" y="154" fill="#94a3b8" font-size="7.8">  (유지부-무지부 경계 열수축 편차에 의한 경계 일자주름 동시 억제)</text>
    </g>
  </g>

  <!-- PANEL B: Diagonal (Shear) Wrinkle -->
  <g transform="translate(496, 18)">
    <rect width="466" height="404" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12.5" font-weight="800">■ (B) 사선주름 (대각선 주름, Diagonal Wrinkle): 좌우 비대칭 전단 응력</text>

    <!-- Top Diagram: Misaligned Roll & Shear Wrinkle -->
    <g transform="translate(16, 40)">
      <rect width="434" height="175" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fbbf24" font-size="10" font-weight="800">1) 발생 메커니즘: 롤 얼라인먼트 틀어짐 &amp; OS/DS 좌우 장력 편차</text>

      <!-- Bottom reference roll (parallel) -->
      <rect x="95" y="132" width="240" height="14" rx="3" fill="#475569"/>
      <!-- Top misaligned roll (tilted!) -->
      <g transform="rotate(-5, 215, 38)">
        <rect x="95" y="30" width="240" height="15" rx="3" fill="#ef4444"/>
      </g>
      <text x="342" y="35" fill="#fca5a5" font-size="8" font-weight="800">DS측 거리 긺 (Tight!)</text>
      <text x="18" y="45" fill="#93c5fd" font-size="8" font-weight="800">OS측 거리 짧음 (Loose)</text>

      <!-- Web Foil -->
      <polygon points="105,46 325,32 325,132 105,132" fill="#334155" stroke="#94a3b8" stroke-width="1"/>

      <!-- Diagonal Wrinkle Lines sloping towards Tight side (DS top-right) -->
      <line x1="125" y1="125" x2="225" y2="45" stroke="#fde047" stroke-width="2.5"/>
      <line x1="165" y1="125" x2="275" y2="42" stroke="#fde047" stroke-width="3"/>
      <line x1="210" y1="125" x2="310" y2="45" stroke="#fde047" stroke-width="2.5"/>

      <text x="18" y="164" fill="#fde047" font-size="8.2" font-weight="700">★ 현장 판독 공식: 사선주름 윗머리가 향하는 방향(↗)이 장력이 강한(Tight) 쪽!</text>
    </g>

    <!-- Bottom Diagram: Solutions for Diagonal Wrinkle -->
    <g transform="translate(16, 226)">
      <rect width="434" height="162" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="20" fill="#38bdf8" font-size="10" font-weight="800">2) 핵심 해결책: 롤 평행도/수평도 영점 교정 + 좌우 두께·닙압 밸런싱</text>

      <rect x="14" y="30" width="406" height="44" rx="5" fill="#0f172a" stroke="#475569"/>
      <text x="24" y="47" fill="#fde047" font-size="8.5" font-weight="800">🔧 롤 얼라인먼트(Alignment) 교정 법칙</text>
      <text x="24" y="63" fill="#cbd5e1" font-size="8">• 사선주름이 최초 시작되는 롤을 찾아 수준기·레이저 트래커로 수평(Level) 및 평행(Parallelism) 교정</text>

      <text x="14" y="96" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#fbbf24" font-weight="700">솔루션 1 (롤 정렬 1순위)</tspan>: 주름 발원지 가이드 롤·석션 롤·쿨링 롤 평행도 영점 복원</text>
      <text x="14" y="114" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#fbbf24" font-weight="700">솔루션 2 (로딩 &amp; 닙압)</tspan>: OS/DS 코팅 두께(Loading) 편차 제거 및 닙 롤 좌우 공압 균등화</text>
      <text x="14" y="132" fill="#e2e8f0" font-size="8.5">✔ <tspan fill="#fbbf24" font-weight="700">솔루션 3 (EPC 안정화)</tspan>: EPC 사행 제어기 Gain 및 반응 속도 완화로 급격한 대각선 헌팅 억제</text>
      <text x="14" y="150" fill="#94a3b8" font-size="7.8">  (원단 점보 롤 장착 센터링 불량으로 EPC가 한쪽 끝단 Limit에 몰려 있는지 동시 확인)</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
<h3>1. 일자주름과 사선주름의 물리적 본질 비교</h3>
<p>
전극 코터에서 $6 \sim 15\,\mu\text{m}$에 불과한 얇은 알루미늄(Al) 또는 구리(Cu) 호일을 수십 미터 주행시킬 때 발생하는 주름은 그 모양에 따라 원인이 완전히 다릅니다. 따라서 현장에서 주름을 잡을 때는 먼저 <strong>"웹 진행 방향(MD)과 나란한 일자주름인가, 좌우(OS/DS) 대각선으로 흐르는 사선주름인가?"</strong>부터 판별해야 합니다.
</p>

<div class="analogy-card">
  <div class="analogy-title">💡 가장 직관적인 물리 비유: '비닐랩 당기기 vs 셔츠 비틀어 당기기'</div>
  <div class="analogy-desc">
    • <strong>일자주름 (종주름, MD Wrinkle)</strong>: 얇은 비닐랩을 위아래로 너무 세게 잡아당기면, 가로 방향(폭 방향)이 가운데로 오므라들면서 <strong>세로로 길게 골이 파이는 현상(폭 방향 압축 좌굴)</strong>입니다.<br>
    • <strong>사선주름 (대각선 주름, Diagonal Wrinkle)</strong>: 셔츠 양 끝을 잡고 당길 때 왼손과 오른손의 높이나 당기는 힘이 다르면 <strong>한쪽에서 반대쪽으로 비스듬하게 대각선 주름이 잡히는 현상(좌우 비대칭 전단 응력)</strong>입니다.
  </div>
</div>

<div class="formula-box">
  $$\text{일자주름 조건: } \sigma_{TD} = -\nu \cdot \sigma_{MD} \ge \sigma_{cr, \text{buckling}}, \qquad \text{사선주름 조건: } \tau_{xy} = G \cdot \gamma_{xy} \ge \tau_{cr, \text{shear}}$$
</div>

<h3>2. 일자주름 (종주름, MD Longitudinal Wrinkle) 완벽 교정법</h3>
<p>
웹 진행 방향(MD)과 나란하게 길게 뻗는 주름으로, 핵심 원인은 <strong>과도한 MD 장력에 의한 폭 방향(TD) 포아송 수축</strong>, <strong>긴 롤 간 거리(Free Span)</strong>, <strong>익스팬더 롤(Bow Roll) 세팅 불량</strong>, 그리고 <strong>유지부-무지부 수축률 차이</strong>입니다.
</p>

<ol>
  <li><strong>구간 장력(Tension) 하향 및 권취 Taper Tension 재설정 (1순위)</strong>:
    <ul>
      <li>주름이 발생하는 구간(예: Unwinder, Oven, Outfeed, Rewinder)의 설정 장력($T_{set}$)이 박막의 탄성 좌굴 한계를 넘었을 때 발생합니다.</li>
      <li>해당 구간의 <strong>장력을 $5 \sim 10\%$ 단위로 단계적으로 낮추어</strong> 폭 방향 압축 응력을 풀어줍니다.</li>
      <li>리와인더(권취부)에서 발생하는 일자주름은 권경이 커질수록 내부 압축력이 누적되어 생기므로 <strong>Taper Tension 비율을 상향</strong>하여 외경부 장력을 더 부드럽게 감쇠시킵니다.</li>
    </ul>
  </li>
  <li><strong>익스팬더 롤 (Expander Roll / Bow Roll, 활롤) 최적화</strong>:
    <ul>
      <li>주름이 인입되는 주요 롤 전단에 설치된 <strong>Bow Roll(가운데가 활처럼 휜 롤)의 곡률(Bow 양)과 웹 진입 각도(Apex Angle)</strong>를 조정합니다.</li>
      <li>웹이 Bow Roll의 정점(Apex)을 타고 넘어갈 때 양 끝단(OS/DS) 방향으로 자연스러운 펼침력(Spreading Force)이 작용하여 중앙에 몰린 일자주름을 양옆으로 깨끗하게 펴줍니다.</li>
    </ul>
  </li>
  <li><strong>건조로(Dryer) 노즐 풍압 밸런스 및 초기 건조 온도 완화</strong>:
    <ul>
      <li>부상형 건조로(Air Flotation Dryer) 내부에서 상·하부 노즐 풍량 밸런스가 깨져 웹이 위아래로 펄럭이면(Fluttering) 폭 방향 수축으로 일자주름이 잡힙니다 ➔ <strong>상·하부 블로워 풍압을 재조정</strong>해 정현파(Sine Wave) 형태로 안정 부상시킵니다.</li>
      <li>코팅부(유지부)와 미코팅부(무지부) 경계선에 집중되는 일자주름은 슬러리 건조 수축과 호일 열팽창의 차이 때문이므로 <strong>초기 건조 구간(Zone 1~2)의 온도를 완만하게 낮추어</strong> 급격한 경계 수축을 완화합니다.</li>
    </ul>
  </li>
</ol>

<h3>3. 사선주름 (대각선 주름, Diagonal / Shear Wrinkle) 완벽 교정법</h3>
<p>
작업자 측(OS, Operator Side)과 구동 측(DS, Drive Side) 사이를 대각선으로 가로지르는 주름입니다. <strong>90% 이상이 설비의 좌우 대칭성(롤 얼라인먼트, 좌우 코팅 두께, 닙 압력, EPC)이 깨졌을 때</strong> 발생합니다.
</p>

<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:15px; margin:16px 0;">
  <strong style="color:#fde047; font-size:1rem;">🧭 [현장 엔지니어 필수 공식] 사선주름 방향 판독법</strong><br>
  웹이 흘러가는 진행 방향(MD)을 바라보았을 때, <strong>사선주름의 윗머리(끝단)가 향하는 쪽이 장력이 더 강하거나(Tight) 롤이 먼저 닿아 이동 거리가 길어진 쪽</strong>입니다.<br>
  • 예: 주름이 <strong>OS(아래) ➔ DS(위) 방향(↗)</strong>으로 사선으로 뻗어 있다면, <strong>DS(구동 측) 장력이 더 세거나 롤의 DS 측이 틀어져 있는 상태</strong>입니다.
</div>

<ol>
  <li><strong>가이드 롤 얼라인먼트 (수평도 Level &amp; 평행도 Parallelism) 교정 (1순위)</strong>:
    <ul>
      <li>수십 개의 아이들 롤(Idler Roll), 석션 롤(Suction Roll), 쿨링 롤 중 단 하나라도 수평이나 평행이 틀어지면 좌우 웹의 경로 길이 차이로 인해 전단 응력($\tau_{xy}$)이 발생합니다.</li>
      <li>라인을 따라 역추적하여 <strong>사선주름이 최초로 시작되는 발원지 롤</strong>을 찾은 뒤, 수준기·블록게이지·레이저 트래커를 이용해 해당 롤의 <strong>수평도(Level)와 전후 롤 간 평행도(Parallelism)를 영점 교정</strong>합니다.</li>
    </ul>
  </li>
  <li><strong>좌우(OS/DS) 코팅 로딩량 편차 및 닙 롤(Nip Roll) 공압 밸런싱</strong>:
    <ul>
      <li>슬롯 다이의 OS/DS 두께 편차가 존재하면 두꺼운 쪽의 유효 직경과 장력이 커져 사선주름을 유발합니다 ➔ 두께 측정기 프로파일을 확인해 <strong>OS/DS 로딩량 편차를 다이 볼트로 먼저 평탄화</strong>합니다.</li>
      <li>닙 롤(Outfeed Nip / Laminator Nip)의 <strong>OS/DS 에어 실린더 압력이 동일한지</strong>, 감압지(Prescale) 테스트를 통해 좌우 선압 밸런스를 맞춥니다.</li>
    </ul>
  </li>
  <li><strong>EPC (Edge Position Control, 사행 제어기) 과보정(Hunting) 억제</strong>:
    <ul>
      <li>언와인더나 오븐 출구 EPC가 웹 에지를 맞추기 위해 좌우로 급격하게 흔들리면(Hunting), 웹 전체에 대각선 전단력이 가해져 사선주름이 발생합니다.</li>
      <li>EPC 컨트롤러의 <strong>게인(Gain) 값과 반응 속도를 낮추어 부드럽게 추종</strong>하도록 만들고, 원단 점보 롤 장착 위치 자체가 센터에서 벗어나 EPC가 한쪽 끝(Limit)에 쏠려 있지 않은지 재정렬합니다.</li>
    </ul>
  </li>
</ol>

<h3>4. 일자주름 vs 사선주름 현장 트러블슈팅 요약 비교표</h3>

<div class="data-table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>비교 항목</th>
        <th>일자주름 (종주름, MD Wrinkle)</th>
        <th>사선주름 (대각선 주름, Diagonal Wrinkle)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>외관 형상</strong></td>
        <td>웹 진행 방향(MD)과 나란하게 길게 뻗는 세로줄 주름</td>
        <td>작업자 측(OS) ↔ 구동 측(DS)으로 비스듬히 흐르는 대각선 주름</td>
      </tr>
      <tr>
        <td><strong>물리적 원인</strong></td>
        <td>폭 방향(TD) <strong>압축 응력($\sigma_{TD}$)에 의한 좌굴(Buckling)</strong></td>
        <td>좌우(OS/DS) <strong>장력 비대칭 및 전단 응력($\tau_{xy}$, 비틀림)</strong></td>
      </tr>
      <tr>
        <td><strong>1순위 점검</strong></td>
        <td>• 구간 설정 장력(Tension) 과다 여부<br>• 익스팬더 롤(Bow Roll) 곡률 및 진입 각도</td>
        <td>• <strong>주름 발원지 롤의 수평도(Level) 및 평행도(Parallelism)</strong><br>• 좌우(OS/DS) 코팅 두께(Loading) 편차</td>
      </tr>
      <tr>
        <td><strong>2순위 점검</strong></td>
        <td>• 건조로 상·하 노즐 풍압 불균형(Fluttering)<br>• 유지부-무지부 경계 급격한 건조 수축</td>
        <td>• 닙 롤(Nip Roll) OS/DS 공압 실린더 압력 편차<br>• EPC 사행 제어기 게인(Gain) 과다 및 헌팅</td>
      </tr>
      <tr>
        <td><strong>핵심 해결책</strong></td>
        <td><strong>장력 하향 + 권취 Taper 상향 + Bow Roll 펼침 강화 + 초기 건조 완화</strong></td>
        <td><strong>롤 얼라인먼트 영점 교정 + OS/DS 로딩·닙압 균등화 + EPC Gain 완화</strong></td>
      </tr>
    </tbody>
  </table>
</div>
"""
}
