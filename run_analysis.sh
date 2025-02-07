#!/bin/bash

# analyze.py 실행 후, 표준 출력과 표준 에러를 모두 log.txt에 저장
python3 analyze.py >> log.txt 2>&1

# 스크립트 실행 완료 메시지 출력
echo "analyze.py 실행이 완료되었습니다. 로그는 log.txt 파일에 저장되었습니다."
