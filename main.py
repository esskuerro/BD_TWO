import random
import os

c = os.walk("BD")
for i in c:
    print(f"{i[2]}\n")
    for j in i[2]:
        print(j)

for i in range(20):
    f = open(f"BD/{random.randint(0, 100)}", 'w')
    f.write(f"{random.randint(1, 1000)}")
    f.close()
    summa = 0

# for i in range(20):
#    f = open(f"BD/{i}", 'r')
#    a = int(f.read())
#    summa = summa + a
#    f.close()
#print(summa)

#for i in range():
#    os.remove(f"BD/{i}")