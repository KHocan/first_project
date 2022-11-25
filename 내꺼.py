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