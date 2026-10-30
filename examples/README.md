# 합성 데이터 연습

sample.csv는 툴킷 동작 확인용 합성 자료다.

```bash
python tools/csv_profile.py examples/sample.csv
```

기대 결과: 5행, 완전히 동일한 중복 행 1개, units의 빈 값 1개, units 숫자 합계 400, defects 숫자 합계 16. record_id가 숫자로 읽힌다고 계산용 열로 바꾸면 안 된다. 앞자리 0을 가진 식별자다.

분석 연습: 중복을 제거해야 하는 업무 조건인지 먼저 판단한다. 마지막 행은 생산량이 없어, 전체 불량률을 완전한 데이터인 것처럼 계산하면 안 된다. 중복 제거 후 생산량이 알려진 행만 사용하는 조건에서는 생산량 350, 불량 11, 불량률 약 3.142857%다. 해당 조건과 제외 사유를 명시한다.

```bash
python -m unittest discover -s tests -v
```
