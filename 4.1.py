def perceptron(Sensor):
    b = 7  # begin ackiv func
    s = 0  # begin value
    for i in range(15):
        s += int(Sensor[i]) * weights[i]

    if s >= b:
        return True  # Если сумма превысила порог
    else:
        return False  # Cумма меньше порог
