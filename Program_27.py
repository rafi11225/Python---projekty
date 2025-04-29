from PIL import Image

nazwapliku = #nazwa_zdjecia.png

imagine = Image.open(nazwapliku)
szer , wys = imagine.size #size zwraca krotkę (szerokość, wysokość)
print("obrazek ma rozdzielczość:", wys, "x", szer)
