#
import random

k = random.uniform(-5, 5)  # Coefficient at x.
c = random.uniform(-5, 5)  # free member of the direct equation

print('Initial straight: Y=', k, '*X+', c)  # Entering the initial direct data
rate = 0.001  # Learning speed


#  Set point X:Y
data = {
    22: 150,
    23: 155,
    24: 160,
    25: 162,
    26: 171,
    27: 174,
    28: 180,
    29: 183,
    30: 189,
    31: 192
}

# Subtract y


def procceed(x):
    return x * k + c


# training
for i in range(10000):
    x = random.choice(list(data.keys()))  # Get a random x coordinate point
    true_result = data[x]
    out = procceed(x)    # Get Request
    delta = true_result - out  # We read the network error
    k += delta * rate * x
    c += delta * rate

print('Ready straight: Y=', k, '*X+', c)
