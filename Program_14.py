GeneratorLiczb = (
    element for  element in range (100, 471)
    if (element % 7 == 0)
    if (element % 5 != 0)
    )
for item in GeneratorLiczb:
    print(item)

