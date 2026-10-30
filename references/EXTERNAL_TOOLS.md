# 필요할 때 참고할 외부 도구

2026-10-30에 원본 저장소 안내를 확인했다. 아래 목록은 설치된 도구 목록이 아니며 COFA에서의 작동이나 대회 사용 허가를 보증하지 않는다. 설치·접속이 허용된 경우 필요한 것만 사용하고 버전을 기록한다.

| 원본 | 용도 | 대회에 적용할 때 |
|---|---|---|
| https://github.com/OthmanAdi/planning-with-files | 파일 기반 계획·진행 기록 | 자동 훅은 호스트 지원이 필요. 이 툴킷은 별도로 작성한 수동 기록 지침 제공 |
| https://github.com/obra/superpowers | 개발 계획·디버깅·완료 검증 | 전체 프레임워크보다 현재 문제에 맞는 절차를 선별 |
| https://github.com/microsoft/markitdown | PDF·Office 파일의 텍스트/Markdown 추출 | 표·수치는 원본 대조. 스캔 문서의 OCR은 별도 기능 확인 |
| https://github.com/duckdb/duckdb | CSV·Parquet·JSON 집계와 결합 | 분모·조인 키·집계 단위를 먼저 정의 |
| https://github.com/anthropics/skills | 문서·보고서·웹 테스트 등의 스킬 사례 | 개별 라이선스 확인. docx/pdf/pptx/xlsx는 README에서 source-available로 구분 |
| https://github.com/github/github-mcp-server | AI에서 GitHub 파일 접근 | 앱 호환성과 인증 필요. 참고 용도라면 읽기 전용 설정 |

## 선택적 명령 예시

MarkItDown의 필요한 형식만 설치하는 예시:

```bash
python -m pip install "markitdown[pdf,docx,pptx,xlsx]"
markitdown input.pdf -o input.md
```

실행 허용 여부와 로컬 파일 경로를 확인한 뒤 사용한다. 기본 텍스트 추출을 위해 외부 LLM·Azure 서비스를 연결할 필요는 없다. 해당 추가 기능을 사용하면 별도 인증·네트워크·자료 전송 조건이 적용된다.

## 공개 안내

- 대회: https://skhynix-hackathon.com/
- COFA: https://www.getcofa.com/

대회별 도구·자료 규정은 참가자에게 제공된 최신 안내를 우선한다. 공개 제품 데모는 해당 시험의 실제 도구 목록이나 채점표를 확정하지 않는다.
