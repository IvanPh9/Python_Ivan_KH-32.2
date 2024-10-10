# Функція відкриття файлу
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file
# Функція друку файлів по рядках
def Print(file_name):
    file_r = Open(file_name, "r")
    if file_r != None:
        chunk = file_r.read()
        print(chunk)

        print(f"File {file_name} was closed!")

        file_r.close()
# Оголошуємо назви файлів
file1_name = "TF18_1.txt"
file2_name = "TF18_2.txt"
file3_name = "TF18_3.txt"
file_1_w = Open(file1_name, "w")
file_2_w = Open(file2_name, "w")
if file_1_w:
    file_1_w.write("8dH7kLmQ2z4XyN9aW5pT1vB3fG6cJ0sZrV8uE7qL2dS9oP1kM3tF4wX5jC6nR0gV7hY9i")
    print(f"Information was succesfully added to {file1_name}")
    file_1_w.close()
    print(f"File {file1_name} was closed!")
if file_2_w:
    file_2_w.write("f3D5lP9zX7aK4vT1yB2qW6mN0rV8uJ3sC1hG7oL5xZ4nP2iR8wF6kY9tM0cS9jE7dH1g")
    print(f"Information was succesfully added to {file2_name}")
    file_2_w.close()
    print(f"File {file2_name} was closed!")
# Першочергово відкриваємо файли для читання і тимчасовий файл
file_1_r = Open(file1_name, "r")
file_2_r = Open(file2_name, "r")
temp_w = Open(file3_name, "w")

if file_1_r and file_2_r and temp_w:
    # Переписуємо вміст із file1 в тимчасовий файл
    while True:
        chunk = file_1_r.read(20)
        if not chunk:
            break
        temp_w.write(chunk)
        temp_w.write("\n")
    file_1_r.close()
    print(f"File {file1_name} was closed!")
    temp_w.close()
    print(f"File {file3_name} was closed!")

    # Відкриваємо тимчасовий файл для читання і file1 для запису
    temp_r = Open(file3_name, "r")
    file_1_w = Open(file1_name, "w")

    # Переписуємо вміст із file2 у file1
    while True:
        chunk = file_2_r.read(20)
        if not chunk:
            break
        file_1_w.write(chunk)
        file_1_w.write("\n")
    file_2_r.close()
    print(f"File {file2_name} was closed!")
    file_1_w.close()
    print(f"File {file1_name} was closed!")

    # Відкриваємо file2 для запису
    file_2_w = Open(file2_name, "w")

    # Переписуємо вміст із тимчасового файлу в file2
    chunk = temp_r.read()
    file_2_w.write(chunk)
    temp_r.close()
    print(f"File {file3_name} was closed!")
    file_2_w.close()
    print(f"File {file2_name} was closed!")

    print(f"Content successfully swapped between {file1_name} and {file2_name} using {file3_name}.")
    Print(file1_name)
    Print(file2_name)
