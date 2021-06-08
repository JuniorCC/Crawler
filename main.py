
from selenium import webdriver

import time
import re


def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Firefox()
    f2 = open('2021_cases', 'w')
    f = open('2021_onpe', 'w')
    iter_rows = 0
    # 010000 to 015000
    for x in range(433, 5000):#
        number = 10000 + x
        s_number = "0" + str(number)
        url = "https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/Actas/Numero/"+s_number
        driver.get(url)
        driver.maximize_window()
        time.sleep(12)
        table = driver.find_element_by_id("table1")
        iter_rows = 0
        f.write(s_number)
        snippet = ""
        for row in table.find_elements_by_xpath(".//tr"):
            if iter_rows == 1:
                snippet = row.text + "\n"
                #print("titles-" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 2:
                snippet = row.text + "\n"
                #print("Castillo-" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 3:
                snippet = row.text + "\n"
                val = re.search(r"\b\d+\b", row.text)
                val = val.group(0) # value
                if len(str(val)) >= 2:
                    val = val.lstrip("0")
                pure_value = int(val)
                if pure_value < 20:
                    f2.write("--begin--\n" + s_number +"\n" + str(pure_value) + "\n" + "--end--")
                    print("case " + s_number + " " + str(pure_value))
                #print("keiko-" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 4:
                snippet = row.text + "\n"
                #print("Validos" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 5:
                snippet = row.text + "\n"
                #print("Blanco" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 6:
                snippet = row.text + "\n"
                #print("Nulos" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 6:
                snippet = row.text + "\n"
                #print("Impugnados" + row.text)
                iter_rows = iter_rows + 1
            elif iter_rows == 7:
                snippet = row.text + "\n"
                #print("Emitidos" + row.text)
                iter_rows = iter_rows + 1
            else:
                iter_rows = iter_rows + 1
        f.write(snippet)
        f.write('----------end----------')
    f.close()
    f2.close()
    print(str(iter_rows) + 'PyCharm')