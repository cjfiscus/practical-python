# bounce.py
#
# Exercise 1.5
height = 100
bounces = 10

for i in range(1,11):
    height = height * (3/5)
    print(i, round(height, 4))
