from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pandas as pd
from math import sqrt

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
    #def Tregonomer():

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
        n = [0]
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
        b = dataB.values.tolist()[0]
        a = dataA.shape
        m = a[1]
        n = a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*b[i]
                if i == (m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayATr(self):
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataA.T.to_csv('end.csv',sep =';',header = False, index = False)
        form.textBrowser_2.setText(str(dataA.T))

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
        b = dataA.values.tolist()[0]
        a = dataB.shape
        m = a[1]
        n = a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataB[i][j] * b[i]
                if i == (m - 1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
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
        if ((n==3)&(m==3)):
            x = a[1] * b[2] - a[2] * b[1]
            y = a[2] * b[0] - a[0] * b[2]
            z = a[0] * b[1] - a[1] * b[0]
            form.textBrowser_3.setText(str(x) + '; ' + str(y) + '; ' + str(z))
        else:
            form.textBrowser_3.setText('Введите трехмерных вектор')

#Вызов метода в форме
form.Summ.clicked.connect(Skalar.summAB)
form.Inver.clicked.connect(Skalar._A)
form.pushButton_3.clicked.connect(Skalar.AB)
form.Stepen.clicked.connect(Skalar.AstepenB)
form.Koren.clicked.connect(Skalar.korenAB)
#form.FunkTregonomer.clicked.connect(Skalar.Tregonomer)

form.MullArray.clicked.connect(Ar.arrayAB)
form.ArrayScolar.clicked.connect(Ar.arrayASkalar)
form.ArraySumm.clicked.connect(Ar.arrayAsummB)
form.PoElemArrayMull.clicked.connect(Ar.arrayAmullB)
form.VectorArray.clicked.connect(Ar.arrayAVector)
form.TArray.clicked.connect(Ar.arrayATr)

form.SkolarVector.clicked.connect(Vector.vectorSkalar)
form.SummVector.clicked.connect(Vector.vectorSumm)
form.MullVector.clicked.connect(Vector.vectorMull)
form.MullVectorArray.clicked.connect(Vector.vectorArray)
form.MullVectorVector.clicked.connect(Vector.SkalarProizv)
form.DilinnaVectora.clicked.connect(Vector.DlinnaVectora)
form.VectoSoNoprav.clicked.connect(Vector.CoNapravlen)
form.OrtoganalVectora.clicked.connect(Vector.Ortogon)
form.VectorMull3D.clicked.connect(Vector.VectornoeProizv)
app.exec()