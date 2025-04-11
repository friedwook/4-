#슬라이드 72

#사용자 요구를 판단
judjgment_number = int(input('1.입력한 수식 계산 2.두 수 사이의 합계: '))

if judjgment_number == 1: #입력값이 1인 경우
    expression = input('***수식을 입력하세요:') #수식 받기
    answer =  eval(expression) #수식 계산
    print(expression, '결과는' ,answer, '입니다') #결과 출력
elif judjgment_number == 2: #입력값이 2인 경우
    #첫번째, 두번째 숫자 받기
    firstNumber = int(input('***첫 번째 숫자를 입력하세요:')) 
    secondNumber = int(input('***두 번째 숫자를 입력하세요:'))
    count_between_numbers = abs(secondNumber-firstNumber) + 1 #두 수 사이 수의 개수 구구하기
    answer = count_between_numbers*(firstNumber+secondNumber)/2 #두 수 사이 숫자의 개수 * 평균 = 답
    print(firstNumber,"+...+",secondNumber, '는', answer,'입니다') #결과 출력

\
