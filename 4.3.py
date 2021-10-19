def perceptron(Sensor):
    b = 7  # begin ackiv func
    s = 0  # begin value
    for i in range(15):
        s += int(Sensor[i]) * weights[i]

    if s >= b:
        return True  # Если сумма превысила порог
    else:
        return False  # Cумма меньше порог


num1 = list('001001001001001')
num2 = list('111001111100111')
weights = [1 for i in range(15)]

print(num1)
print(perceptron(num1))
print(num2)
print(perceptron(num2))
