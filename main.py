# calorias items[0][1], peso items[0][2]
items = [
    ["Leche de soya", 500, 0.5],
    ["Galleta integral", 300, 0.1],
    ["Agua mineral", 100, 0.5],
    ["Pan con pollo", 700, 0.25],
    ["Huevo duro", 300, 0.15],
    ["Nueves", 400, 0.15],
    ["Yogurt", 500, 0.5],
    ["Manzana", 400, 0.3]
]

cromosomas = [
    "11001110",
    "01011111",
    "11011101",
    "01111011",
]

for cromosoma in cromosomas:
    print(cromosoma)
    fitness_calorias = 0
    fitness_peso = 0
    fitness_total = 0
    x=0
    for c in cromosoma:
        print(c)
        if c=="1":
            print("Si va: ", items[x])
            fitness_calorias += items[x][1]
            fitness_peso += items[x][2]
        else:
            print("No va: ", items[x])
        x+=1

    print("fitness_calorias:", fitness_calorias)
    print("fitness_peso:", fitness_peso)

