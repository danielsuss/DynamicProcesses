import math

lm = 2
c = 1
a = 0.15

y = (math.log(1/lm))/-1*a

x = y/(c*(1-math.exp(-a*y)))

print(f"x: {x}")
print(f"y: {y}")