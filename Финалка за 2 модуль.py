a = ""
delitel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
while 1 > 0:
    n = int(input("Введите число от 3 до 20: "))
    if n in range(3, 21):
        break
    else:
        print("Не правильное значение")
        continue
for i in range(len(delitel)):
    for j in range(i + 1, len(delitel)):
        if n % (delitel[i]+delitel[j]) == 0:
            a += str(delitel[i]) + str(delitel[j])
print(n, "-", a)