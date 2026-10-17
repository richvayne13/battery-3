# -*- coding: utf-8 -*-
"""
topic_q02_equipment_abnormal.py
Q 02: 설비에 이상이 발생했을 때 대응 방안
"""

TOPIC_Q02 = {
    "badge": "설비 이상 대응 프로토콜 & 안전·품질 인터록",
    "nav_title": "설비에 이상이 발생했을 때 대응 방안 (전극 코터 4-Step 표준 프로토콜)",
    "title": "전극 코터(Electrode Coater) 설비 이상 발생 시 표준 대응 프로토콜: 4-Step 초동 조치·격리·4M1E 원인 진단 및 4대 중대 트러블 핀셋 매뉴얼",
    "summary": [
        "<strong>1. 초동 조치(Step 1 - Stop &amp; Protect)의 핵심 구분</strong>: 웹 단선, 롤 끼임, NMP 폭발하한계(LEL) 경보 등 <strong>중대 안전·설비 이상 시에는 즉시 비상 정지(E-Stop) + 슬러리 펌프 차단 + 코터 헤드 후퇴(Retract)</strong>를 수행하되 배기 팬(Exhaust)은 절대 끄지 않고 유지합니다. 반면 단순 외관·두께 이상 시에는 오븐 내 열변형 2차 단선을 막기 위해 <strong>헤드만 후퇴(Coating Off) 후 저속 주행(Creep Run) 또는 정상 정지</strong>로 대응합니다.",
        "<strong>2. 품질 격리 및 현상 보존(Step 2 - Containment &amp; Snapshot)</strong>: 알람을 무작정 리셋하거나 닦아내기 전에 <strong>발생 미터(m) 구간에 불량 마킹 테이프 부착 및 전산 Hold 처리</strong>로 후공정(롤프레스/슬리팅) 유출을 원천 차단하고, 이상 전후 5분간의 <strong>구간 장력·송액 압력·오븐 풍압/온도·EPC 로그</strong>를 먼저 캡처합니다.",
        "<strong>3. 4M1E 기반 계통별 원인 진단(Step 3 - Root Cause Analysis)</strong>: ① <strong>웹 핸들링 계통</strong>(로드셀 영점, 댄서 롤 고착, 롤 얼라인먼트, 베어링 고착), ② <strong>슬러리·다이 계통</strong>(필터 차압 $\\Delta P$ 상승, 모노 펌프 맥동, 다이 립 응집체 걸림), ③ <strong>건조·유틸리티 계통</strong>(플로테이션 노즐 막힘, 배기 댐퍼/LEL 센서)으로 좁혀 근본 원인을 제거합니다.",
        "<strong>4. 단계적 재가동 검증 및 재발 방지(Step 4 - Verification &amp; Fool-Proof)</strong>: 조치 후 즉시 본생산 속도로 올리지 않고 <strong>저속 통판 및 장력 안정화 ➔ 슬러리 퍼지(Purge) 확인 ➔ 더미(Dummy) 초물 검사(로딩량·외관·잔류용매) 합격 ➔ 본생산 가속(Ramp-up)</strong> 절차를 준수하며, 알람 인터록 임계치를 보강합니다."
    ],
    "svg_title": "📊 [전극 코터 설비 이상 대응 4-Step 아키텍처 & 4대 중대 트러블 대응 체계] (A) 4단계 표준 대응 시퀀스 | (B) 비상 정지(E-Stop) vs 코팅 오프 저속 운전 분기 로직 | (C) 4대 치명적 설비 이상 핀셋 점검 포인트",
    "svg": """<svg viewBox="0 0 980 440" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="440" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: 4-Step Standard Response Protocol -->
  <g transform="translate(18, 18)">
    <rect width="944" height="175" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12.5" font-weight="800">■ (A) 전극 코터 설비 이상 발생 시 4-Step 표준 대응 시퀀스 (Standard Action Protocol)</text>

    <!-- Step 1 -->
    <g transform="translate(16, 42)">
      <rect width="215" height="118" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1.2"/>
      <rect x="0" y="0" width="215" height="24" rx="6" fill="#ef4444"/>
      <text x="12" y="16" fill="#ffffff" font-size="9.5" font-weight="800">STEP 1. 초동 조치 &amp; 설비 보호</text>
      <text x="10" y="42" fill="#fca5a5" font-size="8.5" font-weight="700">• 코터 헤드 즉시 후퇴 (Retract)</text>
      <text x="10" y="58" fill="#cbd5e1" font-size="8">• 슬러리 모노 펌프 차단 &amp; 밸브 전환</text>
      <text x="10" y="74" fill="#cbd5e1" font-size="8">• 단선/LEL 알람 시 E-Stop (배기 유지!)</text>
      <text x="10" y="90" fill="#fde047" font-size="8">• 외관 불량 시 저속 주행(오븐 열단선 방지)</text>
      <text x="10" y="106" fill="#94a3b8" font-size="7.5">➔ 고가 슬롯 다이 립 찍힘·2차 사고 차단</text>
    </g>

    <!-- Arrow 1->2 -->
    <polygon points="235,98 245,93 245,103" fill="#38bdf8"/>

    <!-- Step 2 -->
    <g transform="translate(248, 42)">
      <rect width="215" height="118" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
      <rect x="0" y="0" width="215" height="24" rx="6" fill="#d97706"/>
      <text x="12" y="16" fill="#ffffff" font-size="9.5" font-weight="800">STEP 2. 품질 격리 &amp; 현상 보존</text>
      <text x="10" y="42" fill="#fde68a" font-size="8.5" font-weight="700">• 불량 구간(m) 마킹 &amp; LOT Hold</text>
      <text x="10" y="58" fill="#cbd5e1" font-size="8">• 비전/두께 측정기 알람 이력 대조</text>
      <text x="10" y="74" fill="#cbd5e1" font-size="8">• 리셋 전 HMI 트렌드 로그 스냅샷 확보</text>
      <text x="10" y="90" fill="#38bdf8" font-size="8">• (장력, 펌프압, 필터 ΔP, 오븐 온도)</text>
      <text x="10" y="106" fill="#94a3b8" font-size="7.5">➔ 후공정(롤프레스/슬리팅) 불량 유출 0%</text>
    </g>

    <!-- Arrow 2->3 -->
    <polygon points="467,98 477,93 477,103" fill="#38bdf8"/>

    <!-- Step 3 -->
    <g transform="translate(480, 42)">
      <rect width="215" height="118" rx="6" fill="#1e293b" stroke="#0284c7" stroke-width="1.2"/>
      <rect x="0" y="0" width="215" height="24" rx="6" fill="#0284c7"/>
      <text x="12" y="16" fill="#ffffff" font-size="9.5" font-weight="800">STEP 3. 4M1E 근본 원인 진단</text>
      <text x="10" y="42" fill="#7dd3fc" font-size="8.5" font-weight="700">• 웹 핸들링: 로드셀/댄서/얼라인먼트</text>
      <text x="10" y="58" fill="#cbd5e1" font-size="8">• 슬러리/다이: 필터 차압(ΔP), 립 이물</text>
      <text x="10" y="74" fill="#cbd5e1" font-size="8">• 건조로: 상·하 풍속, 배기 댐퍼, TC</text>
      <text x="10" y="90" fill="#cbd5e1" font-size="8">• 자재: 원단 호일 캠버/두께, 점도 변화</text>
      <text x="10" y="106" fill="#94a3b8" font-size="7.5">➔ 데이터 기반 원인 특정 및 물리적 복구</text>
    </g>

    <!-- Arrow 3->4 -->
    <polygon points="699,98 709,93 709,103" fill="#38bdf8"/>

    <!-- Step 4 -->
    <g transform="translate(712, 42)">
      <rect width="216" height="118" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
      <rect x="0" y="0" width="216" height="24" rx="6" fill="#059669"/>
      <text x="12" y="16" fill="#ffffff" font-size="9.5" font-weight="800">STEP 4. 초물 검증 &amp; 재발 방지</text>
      <text x="10" y="42" fill="#6ee7b7" font-size="8.5" font-weight="700">• 저속 통판(Threading) &amp; 텐션 안정화</text>
      <text x="10" y="58" fill="#cbd5e1" font-size="8">• 슬러리 퍼지(Purge) 유량 균일성 확인</text>
      <text x="10" y="74" fill="#cbd5e1" font-size="8">• 더미 코팅 후 초물 검사(로딩/외관/NMP)</text>
      <text x="10" y="90" fill="#34d399" font-size="8">• 인터록 임계치 강화 &amp; PM 주기 반영</text>
      <text x="10" y="106" fill="#94a3b8" font-size="7.5">➔ 합격 판정 후 정상 속도 Ramp-up 복귀</text>
    </g>
  </g>

  <!-- PANEL B & C: 4 Critical Abnormalities Pinpoint Matrix -->
  <g transform="translate(18, 205)">
    <rect width="944" height="217" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12.5" font-weight="800">■ (B) 전극 코터 4대 치명적 설비 이상별 핀셋 대응 매뉴얼</text>

    <!-- Box 1: Web Break -->
    <g transform="translate(16, 40)">
      <rect width="220" height="162" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="20" fill="#f87171" font-size="10" font-weight="800">① 웹 단선 (Web Break)</text>
      <text x="12" y="40" fill="#fde047" font-size="8" font-weight="700">[즉각 조치]</text>
      <text x="12" y="54" fill="#cbd5e1" font-size="7.8">• 헤드 후퇴 + 오븐 히터 즉시 하향</text>
      <text x="12" y="74" fill="#38bdf8" font-size="8" font-weight="700">[핵심 점검]</text>
      <text x="12" y="88" fill="#cbd5e1" font-size="7.8">• 파단면 형상 분석(인장 vs 엣지 크랙)</text>
      <text x="12" y="102" fill="#cbd5e1" font-size="7.8">• 직전 구간 장력 스파이크 &amp; 이바리 확인</text>
      <text x="12" y="122" fill="#34d399" font-size="8" font-weight="700">[재발 방지]</text>
      <text x="12" y="136" fill="#cbd5e1" font-size="7.8">• 오븐 내 잔류박 제거 후 재통판</text>
      <text x="12" y="150" fill="#6ee7b7" font-size="7.8">• 구간 장력·Taper 및 원단 엣지 검수</text>
    </g>

    <!-- Box 2: Line Defect / Die Lip -->
    <g transform="translate(246, 40)">
      <rect width="220" height="162" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="20" fill="#fbbf24" font-size="10" font-weight="800">② 줄무늬 / 코팅 빠짐 (Line Defect)</text>
      <text x="12" y="40" fill="#fde047" font-size="8" font-weight="700">[즉각 조치]</text>
      <text x="12" y="54" fill="#cbd5e1" font-size="7.8">• 비전 좌표 확인 및 헤드 후퇴(Coating Off)</text>
      <text x="12" y="74" fill="#38bdf8" font-size="8" font-weight="700">[핵심 점검]</text>
      <text x="12" y="88" fill="#cbd5e1" font-size="7.8">• 슬롯 다이 립(Lip) 응집체·이물 걸림</text>
      <text x="12" y="102" fill="#cbd5e1" font-size="7.8">• 슬러리 필터 하우징 차압(ΔP) 상승</text>
      <text x="12" y="122" fill="#34d399" font-size="8" font-weight="700">[재발 방지]</text>
      <text x="12" y="136" fill="#cbd5e1" font-size="7.8">• 전용 수지/황동 헤라로 립 클리닝</text>
      <text x="12" y="150" fill="#6ee7b7" font-size="7.8">• 메쉬 필터 교체 및 탈포·교반 점검</text>
    </g>

    <!-- Box 3: Loading Fluctuation -->
    <g transform="translate(476, 40)">
      <rect width="220" height="162" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="20" fill="#38bdf8" font-size="10" font-weight="800">③ 두께·로딩량 헌팅 (Loading 편차)</text>
      <text x="12" y="40" fill="#fde047" font-size="8" font-weight="700">[즉각 조치]</text>
      <text x="12" y="54" fill="#cbd5e1" font-size="7.8">• USL/LSL 공차 이탈 시 정지 &amp; 구간 Hold</text>
      <text x="12" y="74" fill="#38bdf8" font-size="8" font-weight="700">[핵심 점검]</text>
      <text x="12" y="88" fill="#cbd5e1" font-size="7.8">• 모노 펌프 맥동 &amp; 유량계(MFM) 피드백</text>
      <text x="12" y="102" fill="#cbd5e1" font-size="7.8">• 백업롤 진동 및 배관 내 미세 기포 유입</text>
      <text x="12" y="122" fill="#34d399" font-size="8" font-weight="700">[재발 방지]</text>
      <text x="12" y="136" fill="#cbd5e1" font-size="7.8">• 배관 에어 벤트(Air Vent) 퍼지 실시</text>
      <text x="12" y="150" fill="#6ee7b7" font-size="7.8">• 펌프-유량계 PID 제어 루프 재튜닝</text>
    </g>

    <!-- Box 4: Dryer LEL Alarm -->
    <g transform="translate(706, 40)">
      <rect width="222" height="162" rx="6" fill="#1e293b" stroke="#a855f7"/>
      <text x="12" y="20" fill="#c084fc" font-size="10" font-weight="800">④ 건조로 LEL (NMP 농도) 알람</text>
      <text x="12" y="40" fill="#fde047" font-size="8" font-weight="700">[즉각 조치]</text>
      <text x="12" y="54" fill="#fca5a5" font-size="7.8" font-weight="700">• 슬러리 공급 즉시 차단 + 배기 팬 최대 가동!</text>
      <text x="12" y="74" fill="#38bdf8" font-size="8" font-weight="700">[핵심 점검]</text>
      <text x="12" y="88" fill="#cbd5e1" font-size="7.8">• 배기(Exhaust) 댐퍼 닫힘 / 팬 벨트 슬립</text>
      <text x="12" y="102" fill="#cbd5e1" font-size="7.8">• 코팅 유량 과투입 또는 Zone 온도 급등</text>
      <text x="12" y="122" fill="#34d399" font-size="8" font-weight="700">[재발 방지]</text>
      <text x="12" y="136" fill="#cbd5e1" font-size="7.8">• LEL 안전치(20~25% 이하) 퍼지 후 진입</text>
      <text x="12" y="150" fill="#6ee7b7" font-size="7.8">• 차압계·풍속계 인터록 및 LEL 센서 교정</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
<h3>1. 전극 코터 설비 이상 대응의 3대 핵심 철학</h3>
<p>
이차전지 전극 코터는 수십 미터 길이의 고온 건조로($100 \sim 160^\circ\text{C}$), 초정밀 슬롯 다이 헤드(가공 공차 $\pm 1 \sim 2\,\mu\text{m}$), 그리고 $6 \sim 15\,\mu\text{m}$ 두께의 얇은 금속 호일(Al/Cu Foil)이 맞물려 고속 주행하는 연속 공정 설비입니다. 따라서 설비 이상 발생 시 <strong>단순히 기계를 멈추고 다시 켜는 것이 아니라, 2차 대형 사고를 막고 불량 유출을 원천 봉쇄하는 체계적 프로토콜</strong>로 움직여야 합니다.
</p>

<div class="analogy-card">
  <div class="analogy-title">💡 설비 이상 대응 3대 원칙 (Safety &amp; Protection ➔ Containment ➔ RCA)</div>
  <div class="analogy-desc">
    1. <strong>사람과 슬롯 다이(Slot Die) 보호 최우선</strong>: 호일이 겹치거나 단선될 때 수천만 원짜리 슬롯 다이 립(Lip)이 찍히지 않도록 <strong>코터 헤드 즉시 후퇴(Retract)</strong>가 1순위입니다.<br>
    2. <strong>오븐 내 열변형(2차 단선) 및 가스 체류 방지</strong>: 고온 건조로 안에 호일이 정지해 있으면 열팽창·수축으로 연쇄 단선이 발생하고, 양극 NMP 증기가 고이면 폭발 위험이 있으므로 <strong>배기 팬(Exhaust Blower)은 어떤 상황에서도 가동을 유지</strong>합니다.<br>
    3. <strong>현상 보존 및 데이터 선(先) 확보</strong>: 알람을 무작정 리셋(Reset)하거나 현장을 닦아내기 전에 <strong>장력(Tension)·펌프 압력·두께 프로파일 로그</strong>를 먼저 캡처합니다.
  </div>
</div>

<h3>2. 단계별 실전 대응 프로세스 (4-Step Standard Protocol)</h3>

<h4>[Step 1] 초동 조치: 이상 유형별 정지 방식의 즉각 분리 (Stop &amp; Protect)</h4>
<ul>
  <li><strong>중대 설비/안전 이상 (웹 단선, 롤 감김, 설비 충돌음, NMP LEL 농도 경보)</strong>:
    <ul>
      <li>즉시 <strong>비상 정지(E-Stop)</strong>를 누르고 <strong>슬러리 공급 모노 펌프(Mono Pump) 차단 및 회수 밸브(Return Valve) 전환</strong>, <strong>코터 헤드 후퇴(Back-off)</strong>를 동시에 수행합니다.</li>
      <li>단선 시 고온 오븐 내부에 멈춘 호일이 과열되지 않도록 오븐 히터 온도를 낮추되, <strong>배기 팬(Exhaust)은 계속 가동하여 잔류 NMP 가스를 배출</strong>합니다.</li>
    </ul>
  </li>
  <li><strong>공정/품질 이상 (주름 심화, 줄무늬 발생, 두께/로딩 편차 알람, 핀홀)</strong>:
    <ul>
      <li>갑작스러운 E-Stop은 급격한 관성 변화와 오븐 열축적으로 멀쩡하던 웹까지 끊어뜨리는 2차 단선을 유발합니다.</li>
      <li>따라서 <strong>코터 헤드만 후퇴(Coating Off)시켜 슬러리 도포를 중단한 뒤, 무지부 상태로 저속 운전(Creep Run)</strong>하거나 정상 감속 정지(Cycle Stop)를 수행하여 웹 라인(Threading)을 살려둡니다.</li>
    </ul>
  </li>
</ul>

<h4>[Step 2] 품질 격리 및 현상 보존 (Containment &amp; Traceability)</h4>
<ul>
  <li><strong>불량 구간 물리적 마킹 및 전산 LOT Hold</strong>:
    <ul>
      <li>비전 검사기(Surface Vision)와 베타선/X-ray 두께 측정기(Web Gauge)의 알람 발생 시점부터 복구 시점까지의 <strong>권취 미터(m) 구간(Start ~ End)</strong>을 정확히 특정합니다.</li>
      <li>해당 권취 롤에 <strong>실물 불량 마킹 테이프 부착 및 MES 전산 Hold 등록</strong>을 수행하여 후공정(롤프레스·슬리팅)으로 불량이 넘어가는 것을 100% 차단합니다.</li>
    </ul>
  </li>
  <li><strong>트렌드 데이터 스냅샷(Snapshot) 선확보</strong>:
    <ul>
      <li>PLC/HMI에서 이상 발생 전후 5분간의 <strong>① 구간별 장력(Load Cell / Dancer 위치), ② 모노 펌프 RPM 및 다이 내부 압력, ③ 필터 전후 차압($\Delta P$), ④ 오븐 Zone별 온도·정압, ⑤ EPC 이동 스트로크</strong>를 캡처합니다.</li>
    </ul>
  </li>
</ul>

<h4>[Step 3] 4M1E 관점의 원인 진단 및 트러블슈팅 (Root Cause Analysis)</h4>
<ul>
  <li><strong>웹 핸들링(Web Handling) 계통</strong>: 로드셀(Load Cell) 영점 틀어짐, 댄서 롤(Dancer Roll) 공압 실린더 고착, 아이들 롤(Idler Roll) 베어링 파손으로 인한 구름 저항 증가, 롤 평행도 틀어짐 점검.</li>
  <li><strong>슬러리 송액 및 슬롯 다이 계통</strong>: 필터 하우징 차압($\Delta P$) 상승 여부(겔·응집체 막힘), 배관 내 미세 기포 유입, 슬롯 다이 립(Lip) 끝단 슬러리 마름( 굳음) 또는 이물 끼임 점검.</li>
  <li><strong>건조로(Dryer) 및 유틸리티 계통</strong>: 플로테이션 상·하부 노즐 막힘, 급·배기 팬 인버터 트립 또는 댐퍼 개도율 틀어짐, 열매체/스팀 비례제어 밸브 헌팅 점검.</li>
</ul>

<h4>[Step 4] 복구 검증 및 재발 방지 (Verification &amp; Fool-Proof)</h4>
<ul>
  <li><strong>단계적 재가동(Ramp-up) 절차 준수</strong>:
    <ol>
      <li>저속 통판 상태에서 각 구간 <strong>장력(Tension) 및 EPC 사행 제어 안정화</strong> 확인</li>
      <li>코터 헤드 전진 전 <strong>슬러리 퍼지(Purge)</strong>를 통해 맥동 및 기포 없는 균일 토출 확인</li>
      <li>시험 코팅 투입 후 <strong>초물 검사(로딩량, TD 프로파일, 외관 줄무늬 유무, 잔류 NMP/수분) 합격 판정</strong></li>
      <li>정상 양산 속도로 단계적 가속(Ramp-up) 복귀</li>
    </ol>
  </li>
  <li><strong>인터록(Interlock) 및 예지보전(PM) 고도화</strong>: 동일 이상이 재발하지 않도록 상위 관리 한계(예: 필터 차압 경보치, 장력 변동폭 상한)를 촘촘히 재설정하고 예방보전(PM) 점검표에 반영합니다.</li>
</ul>

<h3>3. 전극 코터 4대 대표 설비 이상별 즉각 대응 매트릭스</h3>

<div class="data-table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>이상 유형</th>
        <th>초동 조치 (1분 이내)</th>
        <th>핵심 원인 점검 포인트</th>
        <th>근본 복구 및 재발 방지 대책</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. 웹 단선<br>(Web Break)</strong></td>
        <td>• 헤드 즉시 후퇴 및 슬러리 차단<br>• 오븐 히터 온도 하향 (배기 팬은 유지)</td>
        <td>• 파단면 형상 분석 (인장 파단 vs 엣지 찢김)<br>• 직전 구간 장력 스파이크 및 원단 엣지 크랙/이바리 확인</td>
        <td>• 오븐 내 잔류 호일 완전 제거 후 재통판(Threading)<br>• 구간 장력·Taper 재설정 및 원단 입고 검수 강화</td>
      </tr>
      <tr>
        <td><strong>2. 세로 줄무늬 / 코팅 빠짐<br>(Line Defect / Scratch)</strong></td>
        <td>• 비전 알람 폭 방향 좌표 확인<br>• 헤드 후퇴(Coating Off) 후 저속 유지</td>
        <td>• 슬롯 다이 립(Lip) 끝단 응집체·건조물 걸림 여부<br>• 슬러리 필터 하우징 차압($\Delta P$) 상승 여부</td>
        <td>• 전용 플라스틱/황동 헤라로 다이 립 클리닝 (철제 헤라 절대 금지)<br>• 메쉬 필터 교체 및 믹싱 탈포·분산 조건 피드백</td>
      </tr>
      <tr>
        <td><strong>3. 로딩량(두께) 급변 및 헌팅<br>(Loading Fluctuation)</strong></td>
        <td>• 스펙(USL/LSL) 이탈 시 코팅 중단<br>• 이탈 구간 전산 Hold 및 마킹</td>
        <td>• 모노 펌프(Mono Pump) 토출 맥동 및 유량계(MFM) 오차<br>• 백업롤(Backup Roll) 진동 및 배관 내 기포 유입</td>
        <td>• 배관 에어 벤트 퍼지 및 맥동 감쇠기(Damper) 점검<br>• 유량계-펌프 클로즈드 루프(Closed-loop) 게인 재조정</td>
      </tr>
      <tr>
        <td><strong>4. 건조로 LEL 가스 알람<br>(Safety Interlock)</strong></td>
        <td>• <strong>즉시 슬러리 공급 차단(인터록)</strong><br>• <strong>배기 팬(Exhaust) 100% 최대 가동 유지</strong></td>
        <td>• 배기 댐퍼 닫힘, 팬 벨트 슬립, 급기 유량 부족<br>• 슬러리 과투입 또는 건조 온도 급상승</td>
        <td>• 챔버 내 NMP 농도가 안전 기준($\text{LEL } 20\sim 25\%$ 이하)으로 낮아진 후 재가동<br>• LEL 센서 정기 캘리브레이션 및 풍속 차압 인터록 강화</td>
      </tr>
    </tbody>
  </table>
</div>
"""
}
