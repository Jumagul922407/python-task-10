# 10-чү тапшырма: Файлдар менен иштөө

# Жөнөкөй тексттик файл түзүү жана ага жазуу
with open("example.txt", "w") as file:
    file.write("Салам, бул файлдар менен иштөө боюнча тапшырма.
")
    file.write("Python менен иштеп жатабыз.
")

# Файлдан окуу
with open("example.txt", "r") as file:
    content = file.read()
    print("Файлдын мазмуну:")
    print(content)

# Файлга жаңы сап кошуу
with open("example.txt", "a") as file:
    file.write("Жаңы сап кошулду.
")
