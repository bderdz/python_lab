from math import sin, cos, radians

GRAVITY = 9.81

angle = None

# if not (angle >= 0 and angle <= 90):
#     print("Błędny kąt")

while angle is None or not (angle >= 0 and angle <= 90):
    angle = float(input("Podaj kąt: "))

velocity = float(input("Podaj prędkość: "))
# print(angle)
# print(velocity)
angle = radians(angle)

z = (velocity ** 2 * sin(2 * angle)) / GRAVITY
print(z)
