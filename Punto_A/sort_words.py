#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog, messagebox
import os


class SortWords:
    def __init__(self, entry):
        self.entry = entry

    def process(self):
        """
        Metodo principal que realizan el ordenamiento y orquestan la salida del documento

        """
        messagebox.showinfo(message="Procesando", title="Procesando")
        try:
            with open(self.entry) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            content.pop(0)
            frequency = {i: content.count(i) for i in content}
            number_words = len(frequency)
            result = ' '.join(map(str, list(frequency.values())))
            self._create_output(number_words, result)
        except IOError:
            print("Se incumple con el formato")
        finally:
            if not (f.closed):
                f.close()

    def _create_output(self, number_words, result):
        """
        Esta función crea el docuemnto de salida con los datos que le entran al metodo

        :param number_words:
        :param result:
        """
        try:
            f = open("output.txt", "w")
            f.write(str(number_words) + "\n" + str(result))
            f.close()
            dir_path = os.getcwd()
            messagebox.showinfo(message="Archivo creado en " + str(dir_path) + "/" + str(f.name), title="Exito")
        except:
            print("No es posible crear el fichero")


def open_file():
    """returns path

    Esta función es recursiva y se llama hasta que el usuario seleccione un documento de entrada

    :return: path
    """
    path = filedialog.askopenfilename(initialdir="", title="Seleccione el archivo")

    if path:
        return path
    else:
        messagebox.showinfo(message="Debe seleccionar un archivo", title="Error")
        return open_file()


def main():
    """
    Metodo principla donde se instancia el objeto de la clase SortWords

    :return: 0
    """
    path = open_file()
    sort_words = SortWords(path)
    sort_words.process()

    return 0


if __name__ == '__main__':
    main()
