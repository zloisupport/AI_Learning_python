import random

# Training simple (0..9)

num0 = list('111101101101111')

num1 = list('001001001001001')

num2 = list('111001111100111')

num3 = list('111001111001111')

num4 = list('101101111001001')

num5 = list('111100111001111')

num6 = list('111100111101111')

num7 = list('111001001001001')

num8 = list('111101111101111')

num9 = list('111101111001111')

num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

# List a11 num 0..9

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

tema = 3  # learning num
n_sensor = 15  # amount sensor
weights = [0 for i in range(n_sensor)]  # zeroing weights


# func determines is number 5
# return true number = 5

def perceptron(Sensor):
    b = 7  # Activate fun threshold
    s = 0  # Begin summ
    for i in range(n_sensor):
        s += int(Sensor[i])*weights[i]
        if s >= b:
            return True  # Summ exceeded threshold
        else:
            return False  # Summ less threshold


# Decreasing the weight
def decrease(number):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[i] -= 1


# Increase the weight
def increase(number):
    for i in range(n_sensor):
        if int(number[i]) == 1:
            weights[i] += 1


# Training
n = 100000  # number of lessons
for i in range(n):
    j = random.randint(0, 9)  # Generate random  number j 0..9
    r = perceptron(nums[j])  # Summator result (true,false)

    if j != tema:  # If the generator produced a random number j not equal to 5
        if r:  # If the adder said Yes (this is a 5), and j is not a 5. Wrong
            decrease(nums[j])
    else:
        # If the adder said NO (this is not a 5), and j is  5. True
        if not r:
            increase(nums[tema])
# print(j)

print("1 is 5", perceptron(num51))
print("2 is 5", perceptron(num52))
print("3 is 5", perceptron(num53))
print("4 is 5", perceptron(num54))
print("5 is 5", perceptron(num55))
print("6 is 5", perceptron(num56))
