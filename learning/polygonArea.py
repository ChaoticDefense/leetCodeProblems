from math import pi, sin, tan

def areaCalc(r, N):
    s = 2*r*sin(pi/N)
    A = N*s**2/(4*tan(pi/N))
    return A, s

radius = 1
N = 3

areaCircle = pi*radius**2
tmpArea, s = areaCalc(radius, N)

while abs(areaCircle - tmpArea) / areaCircle * 100 >= 1e-6:
    tmpArea, s = areaCalc(radius, N)
    N += 1
    

print(f'Num of sides needed: {N}')
print(f'Area of Circle: {areaCircle}')
print(f'Area of polygon: {tmpArea}')
print(f'Side length: {s}')