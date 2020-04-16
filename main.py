"""
STUFF:
- akademik jest 12 x 10
- okna są 2x2 odzielone o 1 od siebie

-------------------
format .piwo7:
PIWO_7_FILE
12 10

50
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 16711680 0 0 0 0 16711680 0 0 0
0 0 0 16711680 0 0 0 0 16711680 0 0 0
0 0 0 16711680 0 0 0 0 16711680 0 0 0
0 0 0 16711680 0 0 0 0 16711680 0 0 0
0 0 0 16711680 0 0 0 0 16711680 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 16711680 0 0 0 0 0 0 16711680 0 0
0 0 16711680 16711680 16711680 16711680 16711680 16711680 16711680 16711680 0 0
0 0 0 0 0 0 0 0 0 0 0 0

50
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 255 0 0 0 0 255 0 0 0
0 0 0 255 0 0 0 0 255 0 0 0
0 0 0 255 0 0 0 0 255 0 0 0
0 0 0 255 0 0 0 0 255 0 0 0
0 0 0 255 0 0 0 0 255 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 255 255 255 255 255 255 255 255 0 0
0 0 255 0 0 0 0 0 0 255 0 0
0 0 0 0 0 0 0 0 0 0 0 0

-------------------
- 2 linijka to rozdziałka
- liczby przed arrayami to odstęp czasu klatki - przydatne
- kolory trzymane są w RGB XXXYYYZZZ
- edytor pozwala na super dużo kolorów, Minecraft nie, więc coś trzeba ogarnąć


Projekt W.Ó.D.A.

piksel P.I.W.O - 2x2 pixel W.Ó.D.A.

x i y, co 3, czyli

piwo(0, 0) = wóda(0, 0)
piwo(1, 0) = wóda(3, 0)
||
piwo(x, y) = wóda(x*3, y*3)

"""
from nbtschematic import SchematicFile


# wymiary projektu W.Ó.D.A.
# X /\
# Y ->
# Z


def wóda(x, y, color):
    j = x * 3
    k = y * 3
    col = color
    # TODO color based on rgb values
    sf.blocks[j, k, 0] = col
    sf.blocks[j + 1, k, 0] = col
    sf.blocks[j, k + 1, 0] = col
    sf.blocks[j + 1, k + 1, 0] = col


X = 26
Y = 38
Z = 1
sf = SchematicFile(shape=(X, Y, Z))
assert sf.blocks.shape == (X, Y, Z)
for x in range(X):
    for y in range(Y):
        for z in range(Z):
            sf.blocks[x, y, z] = 80

for x in range(0, X, 3):
    for y in range(0, Y, 3):
        for z in range(Z):
            sf.blocks[x, y, z] = 95
            sf.blocks[x + 1, y, z] = 95
            sf.blocks[x, y + 1, z] = 95
            sf.blocks[x + 1, y + 1, z] = 95
sf.blocks[0, 0, 0] = 41
wóda(2, 3, 4)
wóda(2, 4, 4)
sf.blocks[0, 37, 0] = 41
wóda(5, 5, 7)
sf.blocks[25, 37, 0] = 41
print(sf.blockentities[0,0,0])
# nie wiem czemu wychodzi do góry nogami, //flip up i //flip left naprawia
sf.save('example.schematic')
