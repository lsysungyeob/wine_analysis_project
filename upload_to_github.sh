#!/bin/bash
# analyze.py
git add analyze.py
git commit -m 'Scikit-learn 데이터 분석 Python 코드'

# run_analysis.sh
git add run_analysis.sh
git commit -m 'Python 코드 실행 및 로그 저장 shell 스크립트'

# upload_to_github.sh
git add upload_to_github.sh
git commit -m 'Github 자동 업로드 shell 스크립트'

# output.txt
git add output.txt
git commit -m 'Python 실행 결과 저장 파일'

# log.txt
git add log.txt
git commit -m '실행 로그 저장 파일'

# environment.yml
git add environment.yml
git commit -m 'conda 환경 정보'

# README.md
git add README.md
git commit -m '프로젝트 설명 파일'

# 원격 저장소로 push
git push