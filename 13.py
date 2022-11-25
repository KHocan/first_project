##마방진 달팽이
# data = [[0] * 5 for i in range(5)]  # 0이 5행5열로 들어가 있는 2차원 리스트
# n = 0; s= 1; i = 0; j = -1; k = 5
 
# while True:
#     for p in range(1, k + 1):
#         n += 1
#         j += s
#         data[i][j] = n
#     # for 끝 ===================================================
#     k -= 1
#     if k <= 0:
#         break
#     for p in range(1, k + 1):
#         n += 1
#         i += s
#         data[i][j] = n        
#     # for 끝 ===================================================
#     s *= -1
# # while 끝 ===================================================
        
    
# # 2차원 리스트 출력하기
# for i in range(len(data)):
#     for j in range(len(data[0])):
#         print('%3d ' % data[i][j], end = '')
#     print()
#달팽이 마방진 - 교수편

#규칙

print("1부터 (n*n)까지 연속적인달팽이모양으로 입력")
print("입력은 2 이상 정수입력")

n = int(input("입력 차수 : "))
magic = [[0]*n for _ in range(n)] # 차수n 만큼 반복
dir = 0
cnt = 1 #카운터용
i = 0 #행
j = 0 #열
row = 0
col = 0
limit = 0

while(n*n) >= cnt:
    magic[i][j] = cnt
    cnt += 1
    if dir == 0:
        if col < (n-2) - limit:
            col += 1
            j = col
        else:
            j += 1
            dir = 1
    elif dir == 1:
        if row < (n-2) - limit:
            row += 1
            i = row
        else:
            i += 1
            dir = 2
    elif dir == 2:
        if col > limit:
            j = col
            col -= 1
        else:
            j = limit
            limit += 1
            dir = 3
    else:
        if row > limit:
            i = row
            row -= 1
        else:
            i = limit
            dir = 0

for k in range(n):
    for m in range(n):
        print("%3d"%(magic[k][m]),end = ' ')
    print()

