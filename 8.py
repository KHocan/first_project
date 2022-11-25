#반복문
# import turtle
# turtle.shape("turtle")
# for i in range(4):
#     turtle.right(90)
#     turtle.forward(100)

# for i in [1,2,3,4,5]:
#     print("파이썬",i)

# s = 0
# for i in [1,2,3,4,5] :
#     s = s + i
#     print("i :",i,",s :",s)
# print("s:",s)

# n = 1
# s = 0
# while n <= 10:
#     if n % 2 == 0:
#         s = s + n
#         print("n:",n,"s:",s)
#     n = n + 1
# print("s:",s)

# for i in "abc":
#     print("파이썬"+i)

# s = 0
# i = 1
# while(i <=5):
#     s = s + i
#     i = i + 1
#     print("s :",s,"i :",i)
# print("s : ",s)

# s = 0
# i = 1
# while(i <=10):
#     if (i % 2 == 0):
#         i = i + 1
#         continue
#     s = s + i
#     i = i + 1
    
#     print("s :",s,"i :",i)
# print("s : ",s)

# s = 0
# i = 1
# while(1):
    
#     if (i % 2 == 1):
#         s = s + i
    
#     i = i + 1

#     if (i > 10) :
#         break

# print("s : ",s)

# pw = ""
# while pw !="abcd":
#     pw = input("pw 를 입력하세요 :")
# print("로그인 성공!")

# 코드 오류있음
# q = ""
# while q != "q":
#     cnt = int(input("누적 합을 구할 정수 입력 :"))

#     s = 0

#     for i in range(cnt+1):
#         s = s + i
    
#     print("합",s)

#     q = input("종료는 q 다시 실행은 아무키나 누르세요 :")

#마방진 만들기 (홀수 2차원  정방행렬)

#규칙
# 첫 시작은 행:0 열 차수//2
# 1. 1~차수x차수(반복문)
# 2. 다음수는 행-1, 열 -1 위치에 놓는다.
# 3. 다음 수 넣을 위치에 이전의 수가 저장되있을때 행+2, 열+1
# 4. 행,열의 각 각 위치가 범위를 넘어가면 행,열의 끝으로 이동
# 5. 행,열 두개가 모두 위치 범위가 넘어가면 행 = 1, 열 = 0
#<교수님 풀이편>
q = ""

while q != "q":
    def m_print(x):
        if x == 0:
            print("마방진 초기화 출력")
        else:
            print("마방진 결과 출력")

        for i in range(num):
            for j in range(num):
                print("%3d"%(magic[i][j]), end="")
            print()
    print("가로 세로 대각선의 합이 같은 2차원 마방진 구성")
    print("마방진 차수는 3이상 홀수를 입력하시오.")
    num = int(input("마방진 차수 : "))
    magic = [[0] * num for _ in range(num)]

    m_print(0)
    print("\n\n")

    cnt = 1
    i = 0    #0 행 부터 시작
    j = num // 2 #열중앙에 위치하기 위하여

    while (num * num) >= cnt : # 입력된 차수만큼 2차 배열 생성
        if magic[i][j] != 0: # 배열값이 0이 아니면
            i += 2
            j += 1       #i에 i+2 , j에 j+1을 대입
        
        magic[i][j] = cnt

        if i:
            i -= 1
            if j:
                j -= 1
            else:
                j = num - 1 #열의 제일 끝으로 오른쪽 끝으로 이동
        else:
            if j:
                j -= 1
                i = num - 1 #행의 제일 끝으로 이동
            else:    # 행,열 두개가 모두 위치 범위가 넘어가면 행 = 1, 열 = 0
                i = 1  
                j = 0
        cnt += 1
    m_print(1)

    q = input("종료는 q 다시 실행은 아무키나 누르세요 : ")



##<애들풀이편>
# n = int(input("마방진 차수 입력 :"))
# magic=[]
# for i in range(n):
#     magic.append([0]*n)

# posx = 0
# posy = n//2
# magic[posx][posy] = 1
# x = 0
# y = 0
# for i in range(2, n*n + 1):
#     x = posx
#     y = posy
#     posx -= 1
#     posy += 1

#     if(posx <0):
#         posx = n - 1
#     if(posy > n - 1):
#         posy = 0
#     if(magic[posx][posy] == 0):
#         magic[posx][posy] = i
#     else:
#         posx = x+1
#         posy = y
#         magic[posx][posy] = i
# for i in range(n):
#     for j in range(n):
#         print("%3d"%(magic[i][j]),end="")
#     print()

   
