from PIL import Image

# Načítaj PNG a ulož ho ako ICO s viacerými rozlíšeniami pre Windows
img = Image.open('icon.png')
img.save('icon.ico', format='ICO', sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
print('Ikona bola úspešne vytvorená ako icon.ico!')