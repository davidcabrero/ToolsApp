import easyocr
reader = easyocr.Reader(['en'])
imagen = input("Introduce nombre de archivo: ")
# result = reader.readtext('misc/text.png')
result = reader.readtext('misc/text.png')
print()
print(result)
print()
for item in result:
    print(item[1])


