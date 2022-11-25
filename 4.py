

score = int(input("시험 점수를 입력하세요 : "))

if (score >= 90) :
    print("점수는 %d 이고 학점은 A 입니다."%score)
elif (score >= 80) :
    print("점수는 %d 이고 학점은 B 입니다."%score)
elif (score >= 70) :
    print("점수는 %d 이고 학점은 C 입니다."%score)
elif (score >= 60) :
    print("점수는 %d 이고 학점은 D 입니다."%score)
else :
    print("점수는 %d 이고 학점은 F 입니다."%score)