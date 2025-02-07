from sklearn.datasets import load_wine
import pandas as pd

# wine 데이터셋 로드
wine = load_wine()

# 데이터를 DataFrame으로 변환 (특성 이름을 컬럼으로 지정)
features = wine.feature_names
df = pd.DataFrame(wine.data, columns=features)

# 데이터셋의 행(row)과 열(column) 개수 계산
num_rows, num_cols = df.shape

# 데이터셋의 특성별로 평균과 표준편차를 계산하고
# 각 특성의 평균, 표준편차, 최대값, 최소값을 출력
# 결과를 output.txt에 저장
print('와인 데이터셋의 분석을 시작합니다.')

with open('output.txt', 'w') as f:
    f.write('와인 데이터셋 분석\n')
    print(f'와인 데이터셋의 행의 갯수는 {num_rows}, 열의 갯수는 {num_cols}.')
    f.write(f'행: {num_rows}, 열: {num_cols}\n')
    f.write('각 특성별 정보\n')
    f.write(f'{'feature':30}|{'mean':7}|{'std':7}|{'max':7}|{'min':7}\n')
    f.write('-' * 62 + '\n')
    for feature in features:
        mean = df[feature].mean()
        std = df[feature].std()
        max = df[feature].max()
        min = df[feature].min()
        
        f.write(f'{feature:30}|{mean:7.2f}|{std:7.2f}|{max:7}|{min:7}\n')
    
print('와인 데이터셋의 분석이 끝났습니다. 결과는 output.txt파일에 정장되었습니다.')
    