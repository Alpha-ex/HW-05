from pathlib import Path
import sys


def get_cats_info(path):
    cats_list = []

    try:
        with open(
        "d:\\goit\\goit-algo-hw-04\\goit-algo-hw-04\\Cats.txt", "r", encoding="cp1251") as file:
            for line in file:
                cat_info = line.strip().split(',')
                if len(cat_info) == 3:
                    cat_dict = {
                        "id": cat_info[0].strip(),
                        "name": cat_info[1].strip(),
                        "age": int(cat_info[2].strip())
                    }
                    cats_list.append(cat_dict)

    except FileNotFoundError:
        print(f"Файл не знайдено")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")

    return cats_list

file_path = 'd:\\goit\\goit-algo-hw-04\\goit-algo-hw-04\\Cats.txt'
cats_info = get_cats_info(file_path)

if cats_info:
    for cat in cats_info:
        print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")