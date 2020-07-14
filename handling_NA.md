# 결측치 처리

1) 결측값(결측치)의 종류

1. Random : 무작위로 정보가 없는 결측치

   -> MCAR(Missing completely at random) / MAR(Missing at random)

   -> 삭제(전체 or 부분) / 조건부 대치 / 예측모형 예측

2. No Random : 결측값 자체가 패턴이 있음

   -> MNAR(Missing not at random)

   -> 관계 깊은 칼럼을 파악해 평균/중앙값/최빈값/예측값 대치

2) 시각화

1. seaborn 시각화
   - import seaborn as sns \ sns.heatmap(df.isnul(),cbar=False)
2. missingno 시각화
   - import missingno as msno \ msno.matrix(df) \ msno.bar(df)

3) 제거하기(Deletion)

- 목록 삭제(Listwise)
- 단일값 삭제(Pairwise)
  - 각 칼럼마다 결측값이 존재하기 때문에 개별 분석은 가능하나 통합적인 분석이 어려움
- df.dropna()

4) 채우기(Imputation)

- 결측치 대체 시 확인할 사항들
  1. 결측치의 비율
  2. 데이터의 분포
  3. 다른 변수와 관계가 있는지

- 평균화 기법
  - 평균(mean), 중앙값(median), 최빈값(mode)
- 예측 기법(Predictive Techniques)
  - 회귀분석, SVM, 머신러닝

1. fillna() 결측치 채우기

   - 특정한 단일값으로 채우기 : df.fillna(value)
   - 결측치 바로 이전 값으로 채우기 : df.fillna(method='pad')
   - 결측치 바로 뒤의 값으로 채우기 : df.fillna(method='bfill')

2. replace() 함수로 결측치 채우기

   - df.replace(to_replace=np.nan, value=value)

3. interpolate() 함수로 결측치 채우기

   - df.interpolate(method='linear',limit_direction='forward')
   - df.interpolate(method='polynomial',order=2)
   - df.interpolate(method='pad',limit=2)
   - https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html

4. mice

5. sklearn.impute

   - https://scikit-learn.org/stable/modules/impute.html

   