# X와 일반식 분리
# 최대 수 초과 최소 진법 찾기
# 일반식에 최소~최대 진법들을 대입하여 유효한 진법들 추론(n진법->10진법, 10진법->n진법 모듈)
# X 식에 유효한 진법들 대입

def NtoTen(num, base):
    return int(num, base)

def TentoN(num, base):
    if num == 0:
        return "0"
    result = ''
    while num:
        result += str(num%base)
        num = num//base
    result = result[::-1]
    return result
    
def solution(expressions):
    answer = []
    X_contain = []
    X_uncontain = []
    digit_possible = []
    max_digit = 0
    
    # X식과 일반식 분리
    for expression in expressions:
        if 'X' in expression:
            X_contain.append(expression)
        else:
            X_uncontain.append(expression)
    
    # 가능한 DIGIT 찾기
    for expression in expressions:
        num1, oper, num2, same, result = expression.split(" ")
        
        for i in range(len(num1)):
            max_digit = max(max_digit, int(num1[i]))
        
        for i in range(len(num2)):
            max_digit = max(max_digit, int(num2[i]))
        
        if result == 'X':
            continue
        else:
            for i in range(len(result)):
                max_digit = max(max_digit, int(result[i]))
    
    # 가능한 digit 배열 생성
    digit_possible = [digit for digit in range(max_digit+1, 10)]
    valid_digit = []
    
    for digit in digit_possible:
        check = 1
    
        for expression in X_uncontain:
            num1, oper, num2, _, result = expression.split(" ")
            if oper == "+":
                if NtoTen(num1, digit) + NtoTen(num2, digit) != NtoTen(result, digit):                 
                    check = 0
                    break
            else:
                if NtoTen(num1, digit) - NtoTen(num2, digit) != NtoTen(result, digit):                 
                    check = 0
                    break
        
        if check == 1:
            valid_digit.append(digit)
    
    # 유효한 진법 리스트
    valid_digit = list(set(valid_digit))
    
    for i in range(len(X_contain)):
        num1, oper, num2, _, result = X_contain[i].split(" ")
        result = set()
        for digit in valid_digit:
            convert_num1 = NtoTen(num1, digit)
            convert_num2 = NtoTen(num2, digit)
            
            if oper == "+":
                result.add(TentoN(convert_num1+convert_num2, digit))
            else:
                result.add(TentoN(convert_num1-convert_num2, digit))
        
        if len(result) == 1:
            X_contain[i] = ' '.join([num1, oper, num2, '=', list(result)[0]])
        else:
            X_contain[i] = ' '.join([num1, oper, num2, '=', '?'])
        
    return X_contain