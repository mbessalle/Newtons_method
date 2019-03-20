def derivative(f):
    def der(x, dx):
        return (f(x+dx) - f(x))/dx
    return der
 
def newtons_method(f, x, n, dx=0.000001):
    '''f is f(x)'''
    df = derivative(f)
    while n>0:
        x = x - f(x)/df(x, dx)
        n -= 1
    return x
def f(x):
    equation = file[0].split(' ')
    sum = 0;
    for i in range(len(equation)//2):
        factor = int(equation[2*i])
        power = int(equation[2*i+1])
        sum += factor * x**power
     
    return sum

file = open("newton5.in.txt").read().split('\n')
x_approx = float(file[2])  # rough guess
# f refers to the function f(x)
n = int(file[1])
x = newtons_method(f, x_approx, n)
print("x = %0.12f" % x)
# optional test (result should be close to zero)
# change dx and tolerance level to make it a little closer
print("Testing with the above x value ...")
print("%0.12f" % (f(x)))
