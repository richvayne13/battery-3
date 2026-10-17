# [Data Dictionary] 배터리 3 (전극 공정 & 생산·운영 마스터 백과사전) 데이터 사전

- **작성일자**: 2026-10-17
- **대상 프로젝트**: `C:\Work\배터리3`
- **데이터 소스**: 사용자 실시간 질의응답(Q&A) 및 이차전지 전극 공정(Slurry Mixing, Slot-Die Coating, Drying, Roll-to-Roll Web Handling, Roll Pressing, Slitting/Notching) 엔지니어링 지식 베이스

---

## 1. 데이터 스키마 (`topics.json` / 토픽 객체 구조)

| 필드명 | 데이터 타입 | 필수 여부 | 설명 및 단위/규칙 |
| :--- | :---: | :---: | :--- |
| `id` | `string` | 필수 | 각 질문 섹션의 고유 HTML 앵커 ID (`q-01`, `q-02`, ... 최신순 재정렬) |
| `num` | `string` | 필수 | 2자리 순번 문자열 (`01`, `02`, `03`, ...) |
| `badge` | `string` | 필수 | 질문의 도메인 카테고리 및 최신 질문 배지 텍스트 |
| `title` | `string` | 필수 | 본문 상단에 표시되는 상세 마스터 강의 제목 |
| `nav_title` | `string` | 필수 | 좌측 사이드바 목차에 표시되는 사용자 실제 질문 기반 직관적 제목 |
| `summary` | `array<string>` | 필수 | 상단 `강의 핵심 요약 포인트` 박스에 들어갈 4~5개 핵심 요약 불릿 HTML |
| `svg_title` | `string` | 필수 | 정밀 도면(SVG) 상단 캡션 타이틀 |
| `svg` | `string` | 필수 | 다크 테마(`#0b1120`) 기반 풀컬러 고해상도 벡터 도면(`<svg viewBox="0 0 980 440">`) |
| `lecture` | `string` | 필수 | 일상 비유, 물리·유체역학 수식(KaTeX), 트러블슈팅 표가 포함된 마스터 강의 본문 HTML |

---

## 2. 주요 물리량 및 공정 단위 정의 (전극 코터 & 웹 핸들링)

| 파라미터 기호 | 명칭 | 물리적 단위 | 공정 관리 의미 |
| :--- | :--- | :---: | :--- |
| $T$ | 웹 장력 (Web Tension) | $\text{N}$ 또는 $\text{kgf}$ | Unwinder, Coater, Oven, Rewinder 구간별 박막 인장력 |
| $\sigma_{TD}$ | 폭 방향 압축 응력 | $\text{MPa}$ | 포아송 비($\nu$) 및 장력 과다에 의해 폭 방향(TD)으로 작용하는 좌굴 응력 (일자주름 원인) |
| $\tau_{xy}$ | 전단 응력 (Shear Stress) | $\text{MPa}$ | 롤 평행도/수평도 틀어짐 및 OS/DS 장력 비대칭에 의해 발생하는 대각선 비틀림 응력 (사선주름 원인) |
| $G_c$ | 코팅 갭 (Coating Gap) | $\mu\text{m}$ | 백업롤(Backup Roll) 위의 호일 표면과 슬롯 다이 립(Die Lip) 끝단 사이의 간격 ($50 \sim 200\,\mu\text{m}$) |
| $L_{load}$ | 로딩 레벨 (Loading Level) | $\text{mg/cm}^2$ | 단위 면적당 도포된 전극 활물질 합제 질량 (양극/음극 용량 결정) |
| $H_{fat}$ | 팻 엣지 높이 (Fat Edge Bump) | $\mu\text{m}$ | 코팅 양 끝단(Edge)이 중앙부 정상 두께 대비 볼록하게 솟아오른 높이 편차 |
| $W_{slide}$ | 슬라이딩 폭 (Sliding Width) | $\text{mm}$ | 코팅 끝단에서 두께가 경사지며 무지부로 흘러내리는 테이퍼(Taper) 구간의 폭 |
| $\text{LEL}$ | 폭발하한계 (Lower Explosive Limit) | $\%$ | 건조로 내부 NMP 유기용매 가스 농도 안전 관리 지표 (통상 $25\% \text{ LEL}$ 이하 인터록 제어) |
