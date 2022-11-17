import random
povezlo_povezlo = 0
ne_povezlo_ne_povezlo = 0
povezlo_povezlo_2 = 0
ne_povezlo_ne_povezlo_2 = 0
kolichestvo = 1000000
for j in range(kolichestvo):
    spisok = [1, 2, 3]
    winn = random.choice(spisok)
    vibor = random.choice(spisok)
    for i in spisok:
        if i != winn and i != vibor:
            del spisok[spisok.index(i)]
            break
    vibor_2 = random.choice(spisok)
    while vibor == vibor_2:
        vibor_2 = random.choice(spisok)
    if vibor_2 == winn:
        povezlo_povezlo += 1
    else:
        ne_povezlo_ne_povezlo += 1
print(povezlo_povezlo / kolichestvo * 100, "%", ' menyaem', sep='')
spisok = [1, 2, 3]
for j in range(kolichestvo):
    spisok = [1, 2, 3]
    winn = random.choice(spisok)
    vibor = random.choice(spisok)
    if vibor == winn:
        povezlo_povezlo_2 += 1
    else:
        ne_povezlo_ne_povezlo_2 += 1
print(povezlo_povezlo_2 / kolichestvo* 100, "%", ' ne menyaem', sep='')