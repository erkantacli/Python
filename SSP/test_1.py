def kugel_volumen(radius, kommastellen):
    pi = 3.14159
    volumen = (4/3) * pi * radius ** 3
    volumen = round(volumen, kommastellen)

    return pi, radius, volumen

pi, r, vol = kugel_volumen(5, 3)
print ("Eine Kugel mit dem Radius " + str(r) +
        " hat das Volumen " + str(vol) +
        "\n In der Formel benutz man pi = " + str(pi)) 