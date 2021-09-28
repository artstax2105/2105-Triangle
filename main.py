sides = input('Введите числа')
sides = list(sides.split(','))
sides=[int(x) for x in sides]
sides.sort(reverse=True)
s = 0
p = 0

side ={'1':0,'2':0,'3':0}
for x in range(len(sides)-2):
    if sides[x+1]+sides[x+2]>sides[x]:
        p = (sides[x]+sides[x+1]+sides[x+2])/ 2
        s = (p*(p-sides[x])*(p-sides[x+1])*(p-sides[x+2])) ** 0.5
        side['1']=sides[x]
        side['2'] = sides[x+1]
        side['3'] = sides[x+2]
        break
if s==0:
    print('треугольника с такими сторонами не существует')
else:
    print("Максимальная площадь - ", s)
    print("Стороны при максимальной площади - ", side['1'],side['2'],side['3'])