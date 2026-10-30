# 로컬 도구

Python 3.10 이상. pip 설치·네트워크·API 키가 필요 없다. 입력 파일을 수정하지 않으며 결과는 stdout에 JSON으로 출력한다. 한국어 CSV는 UTF-8을 기본으로 읽는다.

## CSV 구조와 수치 확인

```bash
python tools/csv_profile.py examples/sample.csv
python tools/csv_profile.py data.csv --encoding cp949
python tools/csv_profile.py data.csv --delimiter ";" --max-rows 50000
```

행 수, 열별 빈 값, 숫자 값 수·최소·최대·합계, 동일 행 중복 수를 출력한다. 숫자는 Decimal로 계산하고 JSON에서는 문자열로 출력한다. 동일 행은 파싱된 원본 필드값 기준이며 공백·대소문자를 정규화하지 않는다. 빈 물리적 레코드는 건너뛴다. 기본 100,000행 상한이며 `truncated=true`이면 전체 통계가 아니다. `--max-rows 0`은 전체를 읽지만 고유 행 해시 보관에 비례해 메모리가 늘어난다.

헤더가 없거나 비어 있거나 중복되면 오류로 종료한다. 열 수가 다르거나 잘못된 CSV도 읽은 범위에서 오류로 알린다. 첫 행을 헤더로 해석하므로 헤더 없는 파일에는 먼저 명시적인 열 이름을 추가한 작업 복사본을 사용한다. NA·NULL·통화 기호·천 단위 쉼표를 자동 변환하지 않는다. 실제 셀 예시는 출력하지 않는다.

## 제출 파일 확인

```bash
python tools/file_manifest.py examples --require sample.csv
python tools/file_manifest.py /path/to/submission --require report.pdf --require result.csv
```

상대 경로, 바이트 크기, SHA-256, 빈 파일, 필수 파일 여부를 출력한다. 심볼릭 링크와 루트 밖 경로, `.git`, `.venv`, `__pycache__`, `node_modules` 디렉터리는 제외한다. 파일을 스캔하는 동안 수정하지 않는다. 표준 출력 내용을 파일로 저장할 경우 **검사 대상 폴더 밖에** 저장한다.

종료 코드: 0=정상(요구 파일 검사 통과), 1=필수 파일 누락/빈 파일, 2=입력·읽기 오류. `--require`가 없으면 필수 파일 목록이 비어 있으므로 검사 통과만으로 제출 준비가 끝났다고 판단하지 않는다. 파일 내용·문서 형식·정답·개인정보 유무는 검사하지 않는다. 출력에는 파일 경로가 있으므로 결과를 공개 저장소에 올리지 않는다.

## 테스트

```bash
python -m unittest discover -s tests -v
```
