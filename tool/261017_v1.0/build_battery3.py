# -*- coding: utf-8 -*-
"""
build_battery3.py
배터리 3 (이차전지 전극 공정 & 생산·운영 Q&A 마스터 백과사전) 정식 빌드 파이프라인.
반도체 3와 100% 동일한 양식으로 최신순 Q&A 대시보드(HTML) 및 마스터 보고서(MD)를 생성합니다.
"""

import json
import os
import sys
import traceback

from template_engine import generate_html, generate_markdown
from topic_q01_fatedge_sliding import TOPIC_Q01
from topic_q02_equipment_abnormal import TOPIC_Q02
from topic_q03_wrinkles import TOPIC_Q03

BASE_DIR = r"C:\Work\배터리3"
CONTEXT_DIR = os.path.join(BASE_DIR, "context")
RESULT_VER_DIR = os.path.join(BASE_DIR, "result", "261017_v1.0")


def build_all():
    try:
        os.makedirs(CONTEXT_DIR, exist_ok=True)
        os.makedirs(RESULT_VER_DIR, exist_ok=True)

        # 최신순(역순) 정렬: Q01(Fat Edge & Sliding) -> Q02(설비 이상 대응) -> Q03(일자주름 & 사선주름)
        topics = [TOPIC_Q01, TOPIC_Q02, TOPIC_Q03]

        # 1. context/topics.json 저장
        topics_json_path = os.path.join(CONTEXT_DIR, "topics.json")
        with open(topics_json_path, "w", encoding="utf-8") as f:
            json.dump(topics, f, ensure_ascii=False, indent=2)
        print(f"[OK] Saved {topics_json_path} ({len(topics)} topics)")

        # 2. HTML 생성 및 저장 (루트 index.html & result/261017_v1.0/index.html)
        html_content = generate_html(topics)
        root_html_path = os.path.join(BASE_DIR, "index.html")
        res_html_path = os.path.join(RESULT_VER_DIR, "index.html")

        for p in (root_html_path, res_html_path):
            with open(p, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"[OK] Generated {p} ({len(html_content):,} bytes)")

        # 3. 마스터 MD 보고서 생성 및 저장
        md_content = generate_markdown(topics)
        md_path = os.path.join(RESULT_VER_DIR, "261017_battery_electrode_master.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"[OK] Generated {md_path}")

        # 4. GitHub Pages용 .nojekyll 및 README.md 생성
        nojekyll_path = os.path.join(BASE_DIR, ".nojekyll")
        with open(nojekyll_path, "w", encoding="utf-8") as f:
            f.write("\n")

        readme_path = os.path.join(BASE_DIR, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"[OK] Generated .nojekyll and README.md")

    except Exception as e:
        print(f"[ERROR] Build failed: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    build_all()
