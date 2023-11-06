x = []
y = []

size = int(input("Enter size of the table\n"))

for i in range(0, size):
    elements_x = int(input("Enter "+str(i+1)+" element of x\t"))
    elements_y = int(input("Enter "+str(i+1)+" element of y\t"))
    x.append(elements_x)
    y.append(elements_y)

sum_x = sum_y = sum_xy = sum_x2 = 0

for i in range(int(size)):
    sum_y = sum_y + y[i]
    sum_x = sum_x + x[i]
    sum_xy = sum_xy + y[i] * x[i]
    sum_x2 = sum_x2 + x[i]**2

m_top = size * sum_xy - sum_x * sum_y
m_bottom = size * sum_x2 - (sum_x ** 2)
m = m_top / m_bottom

b_top = sum_y - m * sum_y
b = b_top / int(size)

x_input = input("Enter x\n")
y_output = m * float(x_input) + b

print(y_output)
