#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, simpledialog
import cmath


class Calculator:
    def __init__(self, complexA_Na, complexA_Nb, complexB_Na, complexB_Nb):
        self.number_A = complex(float(complexA_Na), float(complexA_Nb))
        self.number_B = complex(float(complexB_Na), float(complexB_Nb))

    def process(self):
        """
        Metodo principal que realiza las operaciones con los numeros complejos, y muestra los resultados
        """
        messagebox.showinfo(message="Procesando", title="Procesando")
        messagebox.showinfo(
            message="Numero complejos dados \n A = " + str(self.number_A) + "\n B = " + str(self.number_B),
            title="Procesando")
        try:
            dict_result = {}
            dict_result['sum'] = self.number_A + self.number_B
            dict_result['subtraction'] = self.number_A - self.number_B
            dict_result['multiplication'] = self.number_A * self.number_B
            dict_result['division'] = self.number_A / self.number_B
            dict_result['modA'] = cmath.sqrt((self.number_A.real) ** 2 + (self.number_A.imag) ** 2)
            dict_result['modB'] = cmath.sqrt((self.number_B.real) ** 2 + (self.number_B.imag) ** 2)

            messagebox.showinfo(
                message="RESULTADOS \n SUMA " + str(self.round_complex(dict_result['sum'])) + "\n RESTA " + str(
                    self.round_complex(dict_result['subtraction'])) + "\n MULTIPLICASION " + str(
                    self.round_complex(dict_result['multiplication'])) + "\n DIVISION " + str(
                    self.round_complex(dict_result['division'])) + "\n MOD A " + str(
                    self.round_complex(dict_result['modA'])) + "\n MOD B " + str(
                    self.round_complex(dict_result['modB'])),
                title="Resultados")
        except IOError:
            print("Se incumple con el formato")

    def round_complex(self, x):
        """
        Metodo que redondea numero complejos

        :param x: número complejo
        :return: número complejo redondeado
        """
        return complex(round(x.real, 2), round(x.imag, 2))


def main():
    """
    Metodo principla donde se instancia el objeto de la clase Calculator, y se le pasa por parametros los
    números para instaciar numeros complejos
    :return: 0
    """
    root = tk.Tk()
    aA = simpledialog.askfloat("Input", "Número Real para primer complejo")
    aB = simpledialog.askfloat("Input", "Número Imaginario para primer complejo")
    bA = simpledialog.askfloat("Input", "Número Real para segundo complejo")
    bB = simpledialog.askfloat("Input", "Número Imaginario para segundo complejo")

    sort_words = Calculator(aA, aB, bA, bB)
    sort_words.process()

    root.mainloop()

    return 0


if __name__ == '__main__':
    main()
