import random


povezlo_povezlo = 0
ne_povezlo_ne_povezlo = 0
povezlo_povezlo_2 = 0
ne_povezlo_ne_povezlo_2 = 0
kolichestvo = 1000000
for j in range(kolichestvo):
    spisok = [1, 2, 3]
    winn = random.choice(spisok)    \\выбирается число уоторое будет выйгрышным
    vibor = random.choice(spisok)   \\ по сути нет разницы которую будет выбирать игрок так что выбор тоже рандом
    for i in spisok:    \\ этот цикл убирает третий вариант который не выйгрышь и который не выбрала прога
        if i != winn and i != vibor:
            del spisok[spisok.index(i)]
            break
    vibor_2 = random.choice(spisok) \\тут программа меняет выбор и за счёт этого выигрывает в большинстве случаев
    while vibor == vibor_2:
        vibor_2 = random.choice(spisok)
    if vibor_2 == winn:
        povezlo_povezlo += 1
    else:
        ne_povezlo_ne_povezlo += 1
print(povezlo_povezlo / kolichestvo * 100, "%", ' menyaem', sep='') \\выводятся значения в процетах
spisok = [1, 2, 3]
for j in range(kolichestvo):    \\в этом цикле программа порсто пытается попасть с первого раза 
    spisok = [1, 2, 3]
    winn = random.choice(spisok)
    vibor = random.choice(spisok)
    if vibor == winn:
        povezlo_povezlo_2 += 1
    else:
        ne_povezlo_ne_povezlo_2 += 1
print(povezlo_povezlo_2 / kolichestvo* 100, "%", ' ne menyaem', sep='') \\выводятся значения в процетах
