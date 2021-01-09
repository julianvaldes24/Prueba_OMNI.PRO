#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog, messagebox
import csv, json


class Product:
    def __init__(self, id, name, barcode, maker, category, gender):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.maker = maker
        self.category = category
        self.gender = gender


class Sorter:
    def __init__(self, products):
        self.products = products

    def process(self):
        messagebox.showinfo(message="Procesando", title="Procesando")
        try:
            makers = []
            [makers.append(x.maker) for x in self.products if x.maker not in makers]
            dict_result = {}
            for make in makers:
                dict_result.update(self._sort_manufacturer(make))

            json_object = json.dumps(dict_result, indent=4)
            print(json_object)

            messagebox.showinfo(message="Resultado\n" + str(json_object), title="Resultado")

        except IOError:
            print("Se incumple con el formato")

    def _sort_manufacturer(self, maker):
        sub_list = list(filter(lambda product: product.maker == maker, self.products))
        categories = []
        [categories.append(x.category) for x in sub_list if x.category not in categories]
        dict_result = {}
        for cat in categories:
            dict_result.update(self._sort_category(sub_list, cat))
        return {maker: dict_result}

    def _sort_category(self, list_inp, category):
        sub_list = list(filter(lambda product: product.category == category, list_inp))
        genders = []
        [genders.append(x.gender) for x in sub_list if x.gender not in genders]
        dict_result = {}
        for gender in genders:
            dict_result.update(self._sort_gender(sub_list, gender))
        return {category: dict_result}

    def _sort_gender(self, list_inp, gender):
        list_result = []
        for product in list_inp:
            if product.gender == gender:
                list_result.append(product.id)
        return {gender: list_result}


def open_file():
    path = filedialog.askopenfilename(initialdir="", title="Seleccione el archivo")

    if path:
        return path
    else:
        messagebox.showinfo(message="Debe seleccionar un archivo", title="Error")
        return open_file()


def main():
    # path = open_file()
    products = []
    with open("products.csv", newline='') as File:
        reader = csv.reader(File)
        data = list(reader)
        for row in data[1:]:
            product = Product(row[0], row[1], row[2], row[3], row[4], row[5])
            products.append(product)
    sorter = Sorter(products)
    sorter.process()

    return 0


if __name__ == '__main__':
    main()
