import sympy

x = symbols("x") 
fx = 4*(x**4)+3*x

func = Derivative(fx, x).doit()
func_2 =Derivative(func, x).doit()

print("도함수: ", func)

c = int(input("어느 지점에서의 도함수 값?: "))
Value = func.subs({x:c})

print("도함수 값",Value)
print("이계도함수: ",func_2)
