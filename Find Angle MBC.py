import math

AB = int(input())
BC = int(input())

MC = math.sqrt(pow(AB,2)+pow(BC,2)) / 2

print(str(int(round(math.degrees(math.atan2(AB, BC)))))+ f'{chr(176)}')