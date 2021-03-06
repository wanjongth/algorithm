# # 입력을 받는다. (숫자형)
# num = int(input())
# # 받은것을 N에 담음(백업, 나중에 비교하기 위함)
# N = num
# # 사용할 변수의 초기값을 지정합니다(초기화라고합니다) -> 그릇만드는것
# new_num = 0
# sum_num = 0
# count = 0
# # 조건이 참인동안 반복! -while
# while True:
#     sum_num = num//10 + num%10 # 몫: 수의 첫번째자리, 나머지 : 수의 두번째자리
#     new_num = (num%10)*10 + sum_num%10 # 나머지 숫자-> 몫 : 첫번째자리, 더한수의 나머지 -> 두번째자리
#     count += 1
#     #무한루프 확인
#     #print(count)
#     num = new_num # 사용한 수를 다시 사용하기위해 num자리로 change
#     if new_num == N: #만약 이번에 사용한 수가 처음 입력한 수와 같다면
#         break #while문 빠져나옴
# print(count)

#코드2
i = int(input())

N = i #26
count = 0
while True:

    if i < 10 :
        firstNumber = i
        firstNumber = str(firstNumber)
    else :
        firstNumber = i%10 #6
        firstNumber = str(firstNumber) #"6"

    result = i//10 + i%10 # 2 + 6 =8

    if i < 10 :
        secondNumber = str(result) # "8"
    else :
        secondNumber = result%10
        secondNumber = str(secondNumber)

    finalNumber = firstNumber + secondNumber # "6"+"8"
    i = int(finalNumber)

    count += 1
    
    if N == i:
        break;
print(count)

# 코드3

# a=input()              #26   int를 list로 저장 x
# if int(a)<10:
#     a="0"+a
# b=list(map(int,a))     #[2,6]  #연산이 가능하게 int list로 변환 
# num= 1
# c=str(b[1])+str((b[0]+b[1])%10)   #68
  
# while True: 
#     d=list(map(int,c))        # [6,8]
    
    
#     if d==b:
#         break                  
#     c=str(d[1])+str((d[0]+d[1])%10) #8
#     num+=1 
   
              
#                   #안에서 계속 돌도록
# print(num)