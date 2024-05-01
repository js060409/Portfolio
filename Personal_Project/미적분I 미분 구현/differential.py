def split_function(term):
    if '*x^' in term:
        coefficient, exponent = map(int, term.split('*x^'))

        if exponent == 1:
            derivative_str = str(coefficient)
        elif exponent == 0:
            derivative_str = '0'
        else:
            derivative_str = str(coefficient * exponent) + '*x^' + str(exponent - 1)

        return derivative_str
    elif 'x' in term:
        return term.split('x')[0]
    else:
        return '0'

def differentiate(function):
    terms = function.split(' + ')
    derivative_terms = map(split_function, terms)
    return ' + '.join(derivative_terms)

input_string = input('함수를 입력하세요(계수*x^지수 + ~ ~ ~ 의 형식): ')
result = differentiate(input_string)
print("해당 함수를 적분한 값은:", result)
