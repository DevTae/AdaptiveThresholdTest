import numpy as np
import random

random.seed(777)
np.random.seed(777)

cmd_count = 4
cmd_ratio = 0.05 / cmd_count # 5% 비율로 명령어 실시 가정
no_cmd_ratio = 1.0 - cmd_ratio

cmd_loc = 0.5
cmd_scale = 0.5
no_cmd_loc = 0.1
no_cmd_scale = 0.1

total_count = 1000

# 명령어와 비명령어에 대한 스코어링 점수 랜덤으로 생성
cmd_data_1 = np.random.normal(loc=cmd_loc, scale=cmd_scale, size=int(total_count*cmd_ratio))
no_cmd_data_1 = np.random.normal(loc=no_cmd_loc, scale=no_cmd_scale, size=int(total_count*no_cmd_ratio))
cmd_data_2 = np.random.normal(loc=cmd_loc, scale=cmd_scale, size=int(total_count*cmd_ratio))
no_cmd_data_2 = np.random.normal(loc=no_cmd_loc, scale=no_cmd_scale, size=int(total_count*no_cmd_ratio))
cmd_data_3 = np.random.normal(loc=cmd_loc, scale=cmd_scale, size=int(total_count*cmd_ratio))
no_cmd_data_3 = np.random.normal(loc=no_cmd_loc, scale=no_cmd_scale, size=int(total_count*no_cmd_ratio))
cmd_data_4 = np.random.normal(loc=cmd_loc, scale=cmd_scale, size=int(total_count*cmd_ratio))
no_cmd_data_4 = np.random.normal(loc=no_cmd_loc, scale=no_cmd_scale, size=int(total_count*no_cmd_ratio))

# 랜덤으로 각각 명령어에 대한 셔플 진행
data_1 = list(cmd_data_1) + list(no_cmd_data_1)
random.seed(111)
random.shuffle(data_1)
data_2 = list(cmd_data_2) + list(no_cmd_data_2)
random.seed(222)
random.shuffle(data_2)
data_3 = list(cmd_data_3) + list(no_cmd_data_3)
random.seed(333)
random.shuffle(data_3)
data_4 = list(cmd_data_4) + list(no_cmd_data_4)
random.seed(444)
random.shuffle(data_4)

# 0 보다 작거나 1 보다 큰 값들에 대한 처리 진행
def clip(data: list, min_value: float = 0, max_value: float = 1) -> list:
    result = []

    for d in data:
        if d > 1:
            result.append(1)
        elif d < 0:
            result.append(0)
        else:
            result.append(round(d, 2))

    return result
    
data_1 = clip(data_1)
data_2 = clip(data_2)
data_3 = clip(data_3)
data_4 = clip(data_4)

# 데이터들에 대하여 csv 파일로 저장
datas = zip(data_1, data_2, data_3, data_4)

with open("data.csv", "w") as f:
    for (d1, d2, d3, d4) in datas:
        f.write(str(d1) + "," + str(d2) + "," + str(d3) + "," + str(d4) + "\n")
