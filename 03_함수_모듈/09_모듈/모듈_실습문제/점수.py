def 평균구하기(점수리스트):
# 평균 계산해서 return
    return sum(점수리스트) / len(점수리스트)

def 등급매기기(평균):
    if 평균 >= 90:
        return 'A'
    elif 평균 >= 80:
        return 'B'
    else :
        return 'C'
# 90이상 → "A"
# 80이상 → "B"
# 나머지 → "C"