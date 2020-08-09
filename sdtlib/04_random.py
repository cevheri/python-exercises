import random

random.random()
0.8064301704207291

random.random()
0.6825988062501599


for i in range(10):
     print("{:.4f}".format(random.random()))


random.uniform(0.5, 1.5)
0.9624863371746406

random.uniform(0.5, 1.5)
0.900446344810926


random.randint(45, 500)
random.randrange(10)
random.randrange(10, 500)


liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat']

random.choice(liste)
'ali'

random.choice(liste)
'mehmet'

random.choice(liste)
'selin'

random.choice("Python")

l = list(range(10))
random.shuffle(l)
[8, 0, 7, 9, 1, 4, 6, 5, 3, 2]


l = range(100)

random.sample(l, 5)
[56, 74, 2, 3, 80]













