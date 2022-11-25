# money = int(input("금액입력"))

# c500 = money // 500
# money = money - 500*c500
# c100 = money // 100
# money = money - 100*c100
# c50 = money // 50
# money = money - 50*c50


# print(f"500 코인 : {c500} 개 \n100 코인 : {c100} 개 \n50 코인 : {c50} 개 \n나머지 : {money}")

# 7개의 연산자(+ - * / // % **)를 입력받아 연산결과를 출력하는 프로그램 개발

# a = int(input("A값 입력:"))
# b = int(input("B값 입력:"))
# cal = str(input("계산하고싶은 연산자 입력 (+ - * / // % **) :"))

# if (cal == '+') :
#     print(f"{a} + {b} = {a+b}")
# elif(cal == '-') :
#     print(f"{a} - {b} = {a-b}")
# elif(cal == '*') :
#     print(f"{a} * {b} = {a*b}")
# elif(cal == '/') :
#     print(f"{a} / {b} = {a/b}")
# elif(cal == '//') :
#     print(f"{a} // {b} = {a//b}")
# elif(cal == '%') :
#     print(f"{a} % {b} = {a%b}")
# elif(cal == '**') :
#     print(f"{a} ** {b} = {a**b}")
# else :
#     print("올바른 연산자를 입력하여 주세요!!") #(+ - * / // % **) 이외의 연산자 입력시 반환

#큰 정수 입력 받아 년 일 시간 분 초로 변환

# sec = int(input("큰 정수를 입력해주세요:"))

# year = sec // (60*60*24*365)
# sec = sec - year * (60*60*24*365)
# day = sec // (60*60*24)
# sec = sec - day * (60*60*24)
# cio = sec // (60*60)
# sec = sec - cio * (60*60)
# min = sec // 60
# sec = sec - min*60

# print(f"{year}년{day}일{cio}시간{min}분{sec}초 입니다.")


# x = int(input("큰 정수를 입력 받아 년, 일, 시간, 분, 초로 변환 :"))
# y = 0
# d = 0
# h = 0
# m = 0
# s = 0

# s = x % 60
# m = x // 60

# if (m >= 60) :
#     temp = m  // temp 임시 변수에 넣어놓고 초를 분으로 나누기 먼저함
#     m = m % 60  
#     h = temp // 60

# if (h >= 24) :
#     temp = h
#     h = h % 24
#     d = temp // 24

# if (d >= 365) :
#     temp = d
#     d = d % 24
#     y = temp // 365

# print(f"{y}년{d}일{h}시간{m}분{s}초 입니다.")

# # 2 이상 정수를 입력 받아, 소수판별
# a = int(input("소수 판별할 2 이상 정수 입력:"))
# c=0  # 판별 후 출력해주기 위해
# for i in range(2,a,1):
#     if (a%i==0):         #숫자에 자신이나1로 나눠지는 수가 소수인데 나머지 값이 0 이면 자기자신 외의 다른 숫자로도 나눠져서 소수가 아님.
#         c=1

# if(c==1):                         #c안에 1이 되면 "소수가 아닙니다." 라고 출력
#     print("소수가 아닙니다.")
# else:
#     print("소수입니다.")

# x = int(input("2보다 큰 정수 입력:"))
# flag = 0

# for i in range(2,x+1,1):
#     if (x%i) == 0:
#         flag = i
#         break
# if (flag == x) :
#     print(x , '는 소수 입니다.')
# else :
#     print(x , '는 소수가 아닙니다.')

