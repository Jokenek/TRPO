from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pandas as pd
from math import sqrt
import math
from numpy import linalg
import numpy as np
Form, Window = uic.loadUiType("1_2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

#Все операции скаляра
class Skalar:
    def summAB(self):
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A = dataA+dataB
        form.textBrowser.setText(str(A))
    def _A (self):
        dataA = form.aSkolar.value()
        A = -dataA
        form.textBrowser.setText(str(A))
    def AB(self):
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A = dataA * dataB
        form.textBrowser.setText(str(A))
    def AstepenB(self):
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A =dataA**dataB
        form.textBrowser.setText(str(A))

    def korenAB(self):
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A = dataA ** (1/dataB)
        form.textBrowser.setText(str(A))
    def Tregonomer(self):
        dataA = form.aSkolar.value()
        sin = math.sin(dataA)
        cos = math.cos(dataA)
        tg = math.tan(dataA)
        try:
            ctg = math.cos(dataA) / math.sin(dataA)
        except ZeroDivisionError:
            ctg = '-'
        form.textBrowser.setText('sin(A)= ' + str(sin) +'\n'+ 'cos(A)= ' + str(cos) +'\n'
                                 +'tg(A)= ' + str(tg) +'\n'+'ctg(A)= ' + str(ctg) +'\n')
#Все операции матриц
class Ar:
    def arrayAB(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a = dataA.shape
        b = dataB.shape
        m = a[1]
        n = b[0]
        k = a[0]
        g = 0
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g += dataA[i][l]*dataB[l][j]
                if i == (m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
                g = 0
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayASkalar(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        skalar = form.doubleSpinBox.value()
        a = dataA.shape
        m = a[1]
        n = a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*skalar
                if i == (m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAsummB(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a=dataA.shape
        m=a[1]
        n=a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]+dataB[i][j]
                if i == (m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAmullB(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a = dataA.shape
        m = a[1]
        n = a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*dataB[i][j]
                if i == (m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAVector(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a = dataA.shape
        b = dataB.shape
        m = b[0]
        n = b[1]
        bV = dataB.values.tolist()[0]
        g = 0
        f = open('end.csv', 'w')
        for i in range(n):
            for j in range(m):
                g += dataA[j][i] * bV[j]
            if i == (m - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
            g = 0
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayATr(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataA.T.to_csv('end.csv', sep =';', header = False, index = False)
        form.textBrowser_2.setText(str(dataA.T))
    def opred(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None).to_numpy()
        b = np.linalg.det(dataA)
        opred=round(b,3)
        tr=np.trace(dataA)
        form.textBrowser_2.setText('Определитель: ' + str(opred)+'\n'+'След: ' + str(tr))
    def obrat(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None).to_numpy()
        b = np.linalg.inv(dataA)
        b=np.round(b,3)
        end =pd.DataFrame(data=b)
        form.textBrowser_2.setText(str(end))

#Все операции вектора
class Vector:
    def vectorSkalar(self):
        dataA = pd.read_csv("b.csv", sep=";", header=None)
        skalar = form.doubleSpinBox_2.value()
        b = dataA.values.tolist()[0]
        a = dataA.shape
        n = a[1]
        f = open('end.csv', 'w')
        for i in range(n):
            g = skalar*b[i]
            if i == (n - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
        f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_3.setText(str(dataEND))
    def vectorSumm(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        f = open('end.csv', 'w')
        for i in range(n):
            g = a[i]+b[i]
            if i == (n - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
        f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_3.setText(str(dataEND))
    def vectorMull(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        f = open('end.csv', 'w')
        for i in range(n):
            g = a[i]*b[i]
            if i == (n - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
        f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_3.setText(str(dataEND))
    def vectorArray(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a = dataA.shape
        b = dataB.shape
        m = b[0]
        n = b[1]
        bV = dataB.values.tolist()[0]
        g = 0
        f = open('end.csv', 'w')
        for i in range(n):
            for j in range(m):
                g += dataA[j][i] * bV[j]
            if i == (m - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
            g = 0
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_3.setText(str(dataEND))
    def SkalarProizv(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        g = 0
        for i in range(n):
            g += a[i]*b[i]
        form.textBrowser_3.setText(str(g))
    def DlinnaVectora(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        g = 0
        for i in range(n):
            g += a[i]*a[i]
        g = sqrt(g)
        form.textBrowser_3.setText(str(g))
    def CoNapravlen(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        f = open('end.csv', 'w')
        for i in range(n):
            try:
                g = a[i] / b[i]
            except ZeroDivisionError:
                g = 0
            if i == (n - 1):
                f.write(str(g))
            else:
                f.write(str(g) + ' ;')
        f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        end = dataEND.values.tolist()[0]
        flag = 0
        for i in range(n-1):
            if(end[i]!=end[i+1]):
                form.textBrowser_3.setText('Данные вектора не сонаправленные')
                flag = 1
                break
        if (flag == 0):
            for i in range(n):
                if (end[i]<0):
                    form.textBrowser_3.setText('Данные вектора не сонаправленные')
                    break
                if (i==n-1):
                    form.textBrowser_3.setText('Данные вектора сонаправленные')
    def Ortogon(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        n = l[1]
        g = 0
        for i in range(n):
            g += a[i] * b[i]
        if (g == 0):
            form.textBrowser_3.setText('Вектора ортогональны, так как их скалярное произведение равно нулю.')
        else:
            form.textBrowser_3.setText('Вектора не ортогональны, так как их скалярное произведение не равно нулю.')
    def VectornoeProizv(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a = dataA.values.tolist()[0]
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b = dataB.values.tolist()[0]
        l = dataA.shape
        k = dataB.shape
        m = k[1]
        n = l[1]
        if ((n == 3) & (m == 3)):
            x = a[1] * b[2] - a[2] * b[1]
            y = a[2] * b[0] - a[0] * b[2]
            z = a[0] * b[1] - a[1] * b[0]
            form.textBrowser_3.setText(str(x) + '; ' + str(y) + '; ' + str(z))
        else:
            form.textBrowser_3.setText('Введите трехмерных вектор')
class help:
    def helpSkalar(self):
        form.textBrowser.setText('Для ввода значениий заполните графы А и B. \nПосле чего нажмите на интересующую вас '
                                 'операцию и вы увидите результат ее выполения в этомже окне.')
    def helpVector(self):
        form.textBrowser_3.setText('Для ввода значениий скалярного значения заполните грфу "Скаляр". Для ввода веторов и '
                                 'массиво используйте файлы а.csv и b.csv. Векторные значения заполняются сторого по '
                                 'столбцам. После чего нажмите на интересующую вас операцию и вы увидите результат ее '
                                 'выполения в этомже окне, а также оо будет загружен в файл end.csv находящийся в корне '
                                 'программы.')
    def helpArray(self):
        form.textBrowser_2.setText('Для ввода значениий скалярного значения заполните грфу "Скаляр". Для ввода веторов и '
                                 'массиво используйте файлы а.csv и b.csv. Векторные значения заполняются сторого по '
                                 'столбцам. После чего нажмите на интересующую вас операцию и вы увидите результат ее '
                                 'выполения в этомже окне, а также оо будет загружен в файл end.csv находящийся в корне '
                                 'программы.')
#Вызов метода в форме
form.Summ.clicked.connect(Skalar.summAB)
form.Inver.clicked.connect(Skalar._A)
form.pushButton_3.clicked.connect(Skalar.AB)
form.Stepen.clicked.connect(Skalar.AstepenB)
form.Koren.clicked.connect(Skalar.korenAB)
form.FunkTregonomer.clicked.connect(Skalar.Tregonomer)

form.MullArray.clicked.connect(Ar.arrayAB)
form.ArrayScolar.clicked.connect(Ar.arrayASkalar)
form.ArraySumm.clicked.connect(Ar.arrayAsummB)
form.PoElemArrayMull.clicked.connect(Ar.arrayAmullB)
form.VectorArray.clicked.connect(Ar.arrayAVector)
form.TArray.clicked.connect(Ar.arrayATr)
form.SledAndOpred.clicked.connect(Ar.opred)
form.Yarra.clicked.connect(Ar.obrat)

form.SkolarVector.clicked.connect(Vector.vectorSkalar)
form.SummVector.clicked.connect(Vector.vectorSumm)
form.MullVector.clicked.connect(Vector.vectorMull)
form.MullVectorArray.clicked.connect(Vector.vectorArray)
form.MullVectorVector.clicked.connect(Vector.SkalarProizv)
form.DilinnaVectora.clicked.connect(Vector.DlinnaVectora)
form.VectoSoNoprav.clicked.connect(Vector.CoNapravlen)
form.OrtoganalVectora.clicked.connect(Vector.Ortogon)
form.VectorMull3D.clicked.connect(Vector.VectornoeProizv)

form.HelpS.clicked.connect(help.helpSkalar)
form.HelpV.clicked.connect(help.helpVector)
form.HelpM.clicked.connect(help.helpArray)
app.exec()