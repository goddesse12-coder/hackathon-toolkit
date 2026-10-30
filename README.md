# Hackathon Toolkit

AI 에이전트를 활용하는 범용 문제 해결 과제용 한국어 지침과 로컬 도구입니다. 특정 대회의 공식 자료나 정답 모음이 아닙니다.

## 시작하기

1. 대회가 허용하는 플랫폼 안에서 이 저장소를 읽거나 복제합니다.
2. AI에게 `START_HERE.md`를 읽도록 요청합니다. 실제 문제와 제출 조건도 함께 제공합니다.
3. 필요한 스킬만 선택합니다. 아래 폴더를 전부 문맥에 넣을 필요는 없습니다.
4. 작업 기록과 실제 결과물은 **이 공개 저장소 밖의 비공개 작업 경로**에 만듭니다. 대회 제공 데이터나 답안을 여기에 커밋하지 않습니다.

바로 복사할 전체 시작 프롬프트는 [START_PROMPT.txt](START_PROMPT.txt)에 있습니다.

```text
이 저장소의 START_HERE.md를 읽어줘.
현재 과제의 목표·제출 형식·제약을 먼저 정리하고 필요한 스킬만 선택해줘.
대회 규정과 문제 요구사항을 우선하고, 불가능한 도구는 가능한 대안으로 바꿔줘.
사용한 저장소 버전과 자료 경로를 기록하고, 실제 검증 결과를 남겨줘.
```

GitHub MCP는 읽기 경로 중 하나입니다. Git clone이나 파일 다운로드도 주최 측이 허용하면 사용할 수 있습니다. MCP로 파일을 읽었다고 스킬이 자동 설치되거나 Python 코드가 실행되는 것은 아닙니다. COFA의 자동 스킬 탐색 경로와 훅 지원 여부는 확인하지 않았습니다. `skills/*/SKILL.md`는 직접 읽어 적용하거나 플랫폼이 지원하는 방식으로 등록하세요.

## 구성

| 상황 | 읽을 파일 |
|---|---|
| 여러 단계·여러 파일 과제 | [task-planning](skills/task-planning/SKILL.md) |
| 자료 조사·근거 비교 | [evidence-research](skills/evidence-research/SKILL.md) |
| CSV·수치 분석 | [data-analysis](skills/data-analysis/SKILL.md) |
| 코드나 실행 오류 | [systematic-debugging](skills/systematic-debugging/SKILL.md) |
| 보고서·제안서 | [report-writing](skills/report-writing/SKILL.md) |
| 제출 전 점검 | [submission-verification](skills/submission-verification/SKILL.md) |

- [규격](specs/OUTPUT_CONTRACT.md): 제출 요구사항과 근거 기록 방법
- [템플릿](templates/task-plan.md): 작업 경로에 복사해 채우는 계획·출처·의사결정·검증 양식
- [도구 사용법](tools/README.md): Python 3.10 이상, 외부 의존성 없음
- [외부 도구 참고](references/EXTERNAL_TOOLS.md): 필요할 때 확인할 원본 저장소
- [검증 예제](examples/README.md): 합성 CSV와 기대 결과

## 운영 범위

사용 가능 여부는 해당 대회의 최신 상세 가이드로 판단하세요. 사용자가 제공한 2026년 안내에는 공개 저장소 활용, 플랫폼 안의 AI를 통한 접근, Git Clone·다운로드, 2차 예선 결과 통지 전까지 공개 유지 조건이 있습니다. 이는 전체 규정을 대신하지 않습니다. 외부 브라우저 접근·외부 서비스 호출·자료 반출은 별도 허용 여부를 확인해야 합니다.

파일을 처음 읽은 효과가 대화 초기화 후에도 유지된다고 보장하지 않습니다. 이어서 작업할 때 START_HERE와 작업 경로의 계획·진행 기록을 다시 읽도록 요청하세요. 자동 승인, 무한 재시도, 외부 계정 연결, 일괄 설치 훅은 포함하지 않습니다.

이 저장소의 지침·템플릿·스크립트는 직접 작성한 자료이며 MIT 라이선스로 제공합니다. 외부 자료는 링크로 소개하며 원문 코드·스킬을 재배포하지 않습니다. [출처 안내](THIRD_PARTY_NOTICES.md)
