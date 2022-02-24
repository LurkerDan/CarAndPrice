import re


class Analyzer:

    # Удаление знаков HTML разметки из массива
    def delete_sings(self, arr):
        self.arr = arr
        clear_arr = []

        for i in range(len(arr)):
            move = dict.fromkeys((ord(c) for c in u" \xa0\n\t\₸"))
            temp = (arr[i].translate(move))
            clear_arr.append(temp)

        return clear_arr

    # Удаление лишних пробелов из массива
    def delete_space(self, arr):
        self.arr = arr
        clear_arr = []

        for i in range(len(arr)):
            temp = arr[i].split(' ')

            while any(element in '' for element in temp):
                temp.remove('')

            clear_str = ' '.join(temp)
            clear_arr.append(clear_str)
        return clear_arr

    # Поиск целочисленных значений из строки
    def find_int(self, string):
        str_pages = re.findall(r'\d+', string)
        int_pages = int(str_pages[0] + str_pages[1])
        total_pages = int_pages // 20
        return total_pages
