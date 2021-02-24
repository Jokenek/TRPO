from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pandas as pd

Form, Window = uic.loadUiType("1_2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

#Все операции скаляра
class Skalar:
    def summAB():
        dataA=form.aSkolar.value()
        dataB=form.bSkolar.value()
        A=dataA+dataB
        form.textBrowser.setText(str(A))
    def _A():
        dataA = form.aSkolar.value()
        A =-dataA
        form.textBrowser.setText(str(A))
    def AB():
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A =dataA*dataB
        form.textBrowser.setText(str(A))
    def AstepenB():
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A =dataA**dataB
        form.textBrowser.setText(str(A))

    def korenAB():
        dataA = form.aSkolar.value()
        dataB = form.bSkolar.value()
        A = dataA ** (1/dataB)
        form.textBrowser.setText(str(A))
    #def Tregonomer():

#Все операции матриц
class Ar:
    def arrayAB():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a=dataA.shape
        b=dataB.shape
        m=a[1]
        n=b[0]
        k=a[0]
        g=0
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g += dataA[i][l]*dataB[l][j]
                if i==(m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
                g=0
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayASkalar():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        skalar = form.doubleSpinBox.value()
        a=dataA.shape
        m=a[1]
        n=a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*skalar
                if i==(m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAsummB():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a=dataA.shape
        m=a[1]
        n=a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]+dataB[i][j]
                if i==(m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAmullB():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a=dataA.shape
        m=a[1]
        n=a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*dataB[i][j]
                if i==(m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayAVector():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        b=dataB.values.tolist()[0]
        a=dataA.shape
        m=a[1]
        n=a[0]
        f = open('end.csv', 'w')
        for j in range(n):
            for i in range(m):
                g = dataA[i][j]*b[i]
                if i==(m-1):
                    f.write(str(g))
                else:
                    f.write(str(g) + ' ;')
            f.write('\n')
        f.close()
        dataEND = pd.read_csv("end.csv", sep=";", header=None)
        form.textBrowser_2.setText(str(dataEND))
    def arrayATr():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        a=dataA.shape
        dataA.T.to_csv('end.csv',sep =';',header = False, index = False)
        form.textBrowser_2.setText(str(dataA.T))

#Все операции вектора
class Vector:
    def vectorSkalar():
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
    def vectorSumm():
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
    def vectorMull():
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
app.exec()