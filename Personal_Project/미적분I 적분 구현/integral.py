def split_function(term):
    if '*x^' in term:
        coefficient, exponent = map(int, term.split('*x^'))
        exponent += 1
        coefficient = round(coefficient / exponent, 4)
        return str(coefficient) + '*x^' + str(exponent)
    elif 'x' in term:
        coefficient = int(term.split('x')[0])
        if coefficient == 0:
            return '0*x^1'
        else:
            return str(coefficient) + '*x^1'
    else:
        return term + '*x^1'

def integrate(function):
    terms = function.split(' + ')
    integral_terms = map(split_function, terms)
    return ' + '.join(integral_terms) + '+ c'

input_string = input('함수를 입력하세요(계수*x^지수 + ~ ~ ~ 의 형식): ')
result = integrate(input_string)
print("해당 함수를 적분한 값은:", result)
