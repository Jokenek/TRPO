from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import pandas as pd
import numpy as np

Form, Window = uic.loadUiType("1_2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
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

class Ar:
    def arrayAB():
        dataA = pd.read_csv("a.csv", sep=";", header=None)
        dataB = pd.read_csv("b.csv", sep=";", header=None)
        a=dataA.shape
        b=dataB.shape
        m=a[1]
        n=b[0]
        k=a[0]
        print(m, n, k)
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
form.Summ.clicked.connect(Skalar.summAB)
form.Inver.clicked.connect(Skalar._A)
form.pushButton_3.clicked.connect(Skalar.AB)
form.Stepen.clicked.connect(Skalar.AstepenB)
form.Koren.clicked.connect(Skalar.korenAB)
#form.FunkTregonomer.clicked.connect(Skalar.Tregonomer)

form.MullArray.clicked.connect(Ar.arrayAB)
app.exec()