x_old = 0
x_new = 6
gamma = 0.01
precision = 0.0001

def f_derivative(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - gamma * f_derivative(x_old)

print("Local minimum occurs at", x_new)