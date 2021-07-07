main = list(map(int, input().split()))
rows = main[0]
columns = main[1]

for i in range(int(rows / 2)):
    stringPrint = ".|." * ((i * 2) + 1)
    print(stringPrint.center(columns, "-"))

print("WELCOME".center(columns, "-"))

for i in reversed(range(int(rows / 2))):
    stringPrint = ".|." * ((i * 2) + 1)
    print(stringPrint.center(columns, "-"))
