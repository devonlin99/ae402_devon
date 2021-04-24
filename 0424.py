import qq

a = qq.Human('David',70,180)
print(a.name, 'bmi:',a.bmi())

b=qq.Woman('jenny',55,160,33,26,34)
print(b.name, 'bmi:',b.bmi())
b.BWH()

c=qq.Man('Alex',68,179,True)
print(c.name, 'bmi:',c.bmi())
c.description()