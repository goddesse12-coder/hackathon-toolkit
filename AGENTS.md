# Toolkit maintenance and use

이 저장소를 과제에 사용할 때 START_HERE.md를 읽고 관련 skills/*/SKILL.md만 선택한다. 실제 문제·데이터·결과물·인증정보는 공개 툴킷 밖에 둔다. 자동 탐색을 지원하지 않는 앱에서는 START_HERE.md를 직접 읽도록 요청한다.

이 툴킷 자체를 수정할 때 Python 표준 라이브러리만 사용하는 도구의 호환성을 유지한다. 새 외부 의존성을 추가하면 tools/README.md에 설치 조건을 명시한다. 변경한 스크립트는 `python -m unittest discover -s tests -v`로 검증한다. 지침에 도구 설치나 외부 게시를 암묵적으로 승인하는 문구를 추가하지 않는다.
