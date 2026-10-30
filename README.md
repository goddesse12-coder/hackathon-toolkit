# Hackathon Toolkit

AI 에이전트를 활용하는 범용 문제 해결 과제용 한국어 지침과 로컬 도구입니다. 특정 대회의 공식 자료나 정답 모음이 아닙니다.

## 시작하기: 복사·붙여넣기 없이

대회에서 외부 복사·붙여넣기가 금지된 경우 아래 짧은 요청을 플랫폼 AI 채팅에 직접 입력합니다. 지침 본문은 플랫폼의 AI가 허용된 GitHub MCP로 읽도록 합니다.

```text
GitHub MCP로 goddesse12-coder/hackathon-toolkit의 START_HERE.md를 읽고 필요한 지침을 적용해줘.
```

1. 플랫폼에서 GitHub 저장소 파일을 읽는 MCP 도구가 실제로 연결되어 있는지 확인합니다.
2. AI가 이 저장소의 `START_HERE.md`와 필요한 `skills/*/SKILL.md`를 읽고, 실제 읽은 파일·참조 버전을 보고하도록 요청합니다.
3. 실제 문제·제출 조건을 기준으로 작업합니다. 필요한 지침만 읽으며 전체 저장소를 한꺼번에 문맥에 넣지 않습니다.
4. 작업 기록과 실제 결과물은 **이 공개 저장소 밖의 과제 작업 공간**에 만듭니다. 제공 데이터·답안을 여기에 커밋하지 않습니다.

[START_PROMPT.txt](START_PROMPT.txt)는 AI가 저장소에서 읽을 수 있는 추가 요청 예시입니다. 참가자가 외부 텍스트를 복사해 넣는 것을 전제로 하지 않습니다. 클립보드·자동 입력·단축키로 복붙 제한을 우회하지 않습니다.

여기서 사용한 GitHub 연결은 COFA의 GitHub MCP 연결과 별개입니다. COFA의 실제 도구명·등록 방법·접근 권한은 제공 환경에서 확인해야 합니다. MCP가 없다고 임의로 외부 서비스를 연결하지 말고, 주최 측이 허용한 Git clone·다운로드 등 플랫폼 내 접근 수단을 확인합니다. 첨부 안내에서는 Git Clone·다운로드도 허용하므로 MCP만이 유일한 경로라고 단정하지 않습니다.

MCP로 파일을 읽었다고 스킬이 자동 설치되거나 Python 코드가 실행되는 것은 아닙니다. 지침은 AI가 읽어 참고하고, 보조 코드는 허용된 실행 환경이 있을 때 별도로 실행합니다. 전체 시험 동안 지속 적용되는지도 앱의 지침 기능과 대화 상태에 따라 달라집니다.

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
