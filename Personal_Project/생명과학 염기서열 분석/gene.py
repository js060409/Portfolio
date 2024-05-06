gene = input("염기서열(대문자로): ")
listed_gene = list(gene)

# 초기 카운트 변수 설정
A_count = 0
T_count = 0
C_count = 0
G_count = 0
error_count = 0

# 각각의 염기 수를 세는 반복문
for i in range(len(listed_gene)):
    if listed_gene[i] == 'A':  # listed_gene[i]로 각 염기를 가져와서 비교
        A_count += 1
    elif listed_gene[i] == 'T':
        T_count += 1
    elif listed_gene[i] == 'C':
        C_count += 1
    elif listed_gene[i] == 'G':
        G_count += 1
    else:
        error_count += 1

# 결과 출력
print('---------------------------------------')
print(listed_gene)
print('아데닌 수: ', A_count)
print('타이민 수: ', T_count)
print('사이토신 수: ', C_count)
print('구아닌 수: ', G_count)
print('오류 발생(염기서열 아닌 수의 수): ', error_count)
print('---------------------------------------')
