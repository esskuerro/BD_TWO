f = open("bd/bd1.txt", "w")
f.write("Okay KO")
f.close()
for i in range(20):
    f = open(f"{i}")
    f.write(f"{random.randint(1, 1000)}")
    f.close()