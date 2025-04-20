from PIL import Image

nazwapliku = "Tivolt.jpg"

imagine = Image.open(nazwapliku)
szer , wys = imagine.size #size zwraca krotkę (szerokość, wysokość)
print("obrazek ma rozdzielczość:", wys, "x", szer)
