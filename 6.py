#버블 정렬
# bub = [23,66,24,97,78,12,45,87,9,54]
# i = 0 #크기 비교에서 작은 수
# j = 0 #크기 비교에서 큰 수
# tmp = 0 #작은수를 임시 저장할 변수
# cnt = len(bub)#배열의 길이를 저장해줄 변수
# print(bub,"원래배열")
# print("=======================")
# for i in range(0,cnt):
#     for j in range(0,cnt-1):
#         if bub[i] < bub[j] :
#             tmp = bub[i]
#             bub[i] = bub[j]
#             bub[j] = tmp
#             print(bub,"정렬과정")
# print("=======================")
# print(bub,"정렬완료")      

# #<강사님 풀이>
# print("버블 정렬 프로그램")
# data = [23,66,24,97,78,12,45,87,9,54]

# print("정렬 전 데이터 :",data)

# cnt = len(data) #배열 길이(data의) 구해서 대입해(cnt변수에) 줌
# j = 0 # j 값 초기화

# for i in range(cnt-1,0,-1) :
#     while (j < i) :
#         if (data[j] > data[j+1]) :
#             temp = data[j]
#             data[j] = data[j+1]
#             data[j+1] = temp
        
#         j +=1
#     print("정렬 과정 데이터 : ",data)
#     j=0
# print("정렬 후 데이터 : ",data)
