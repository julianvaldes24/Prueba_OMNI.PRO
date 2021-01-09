#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
from networkdays import networkdays


class DatesAndTimes:
    def __init__(self, dateA, dateB):
        self.date_A = dateA
        self.date_B = dateB

    def process(self):
        messagebox.showinfo(message="Procesando", title="Procesando")
        messagebox.showinfo(
            message="Fechas dadas \n A = " + str(self.date_A) + "\n B = " + str(self.date_B),
            title="Procesando")
        try:
            messagebox.showinfo(
                message="RESULTADOS \nCONTEO DE DIAS " + str(self._days_of_the_week_counter()) + "\n" +
                        "\nHORAS LABORALES" + str(self._working_hours()) + "\n" + "\nDIFERENCIA SIN UTC" +
                        str(self._difference_between_dates(True)) + "\n" +
                        "\nDIFERENCIA CON UTC " + self._difference_between_dates(False),
                title="Resultados")
        except IOError:
            print("Se incumple con el formato")

    def _get_dates_list(self, date_A, date_B, week_days_off):

        # HOLIDAYS = {datetime.date(2012, 12, 25), }
        days = networkdays.Networkdays(datetime.date(date_A.year, date_A.month, date_A.day),
                                       datetime.date(date_B.year, date_B.month, date_B.day), holidays={},
                                       weekdaysoff=week_days_off)
        days_list = days.networkdays()
        return days_list

    def _days_of_the_week_counter(self):
        days_list = self._get_dates_list(self.date_A, self.date_B, {})
        days_of_week = [day.strftime("%A") for day in days_list]
        return str("\nLunes : " + str(days_of_week.count('Monday')) +
                   "\nMartes : " + str(days_of_week.count('Tuesday')) +
                   "\nMierconele : " + str(days_of_week.count('Wednesday')) +
                   "\nJueves : " + str(days_of_week.count('Thursday')) +
                   "\nViernes : " + str(days_of_week.count('Friday')) +
                   "\nSabado : " + str(days_of_week.count('Saturday')) +
                   "\nDomingo : " + str(days_of_week.count('Sunday')))

    def _working_hours(self):
        days_list = self._get_dates_list(self.date_A, self.date_B, {6, 7})
        return "\nHoras de trabajo " + str(len(days_list) * 8)

    def _difference_between_dates(self, tzinfo):
        if tzinfo:
            delta = self.date_B.replace(tzinfo=None) - self.date_A.replace(tzinfo=None)
        else:
            delta = self.date_B - self.date_A

        seconds = delta.total_seconds()
        minutes = seconds / 60
        hours = minutes / 60
        days = delta.days

        return str(
            "\nDias : " + str(days) + "\nHoras : " + str(hours) + "\nMinutos : " + str(minutes) + "\nSegundos : " + str(
                seconds))


def format_date(str_date):
    return datetime.datetime.strptime(str_date, '%d/%m/%Y %H:%M:%S %z')  # [:-6]


def main():
    root = tk.Tk()
    a = format_date(simpledialog.askstring("Input", "Fecha A Formato DD/MM/YYYY hh:mm:ss +xxxx"))
    b = format_date(simpledialog.askstring("Input", "Fecha B Formato DD/MM/YYYY hh:mm:ss +xxxx"))

    print(a)
    print(b)

    sort_words = DatesAndTimes(a, b)
    sort_words.process()

    root.mainloop()

    return 0


if __name__ == '__main__':
    main()
