from tkinter import *
import scipy.special
from math import fabs
e=2.718
okno=Tk()
okno.title("Stymulacja")

zapWy=Label(okno,text="zapisane wyniki")

Dane=Label(okno,text="Dane")

ED     = Entry(okno)
Eh     = Entry(okno)
EM     = Entry(okno)
Ed     = Entry(okno)
EQ     = Entry(okno)
Eros   = Entry(okno)
Emi    = Entry(okno)
EC     = Entry(okno)
Erop   = Entry(okno)
ER     = Entry(okno)
Eq     = Entry(okno)
Erosk  = Entry(okno)
Eqt    = Entry(okno)
EE     = Entry(okno)
Ev     = Entry(okno)
Ekc    = Entry(okno)
ECl    = Entry(okno)
Er     = Entry(okno)
Ehf    = Entry(okno)
Ecosfi = Entry(okno)
Eg     = Entry(okno)
ERe    = Entry(okno)



ED        .insert(0,'0.2                  ')
Eh        .insert(0,'3300                 ')
EM        .insert(0,'40                   ')
Ed        .insert(0,'0.0698               ')
EQ        .insert(0,'40                   ')
Eros      .insert(0,'1200                 ')
Emi       .insert(0,'0.5                  ')
EC        .insert(0,'320                  ')
Erop      .insert(0,'2600                 ')
ER        .insert(0,'300                  ')
Eq        .insert(0,'0.02                 ')
Erosk     .insert(0,'2700                 ')
Eqt       .insert(0,'192.4                ')
EE        .insert(0,'9000000000           ')
Ev        .insert(0,'0.2                  ')
Ekc       .insert(0,'0.00000000000001     ')
ECl       .insert(0,'0.0001               ')
Er        .insert(0,'0.1                  ')
Ehf       .insert(0,'7                    ')
Ecosfi    .insert(0,'-1                   ')
Eg        .insert(0,'9.80665              ')
ERe       .insert(0,'2100                 ')

LD     = Label(okno,text=  "średnica odwiertu")
Lh     = Label(okno,text=  "głębokość odwiertu")
LM     = Label(okno,text=  "miąższość warstwy")
Ld     = Label(okno,text=  "średnica przewodu")
LQ     = Label(okno,text=  "objętość cieczy")
Lros   = Label(okno,text=  "gęstośc właściwa")
Lmi    = Label(okno,text=  "lepkość cieczy szczelinującej")
LC     = Label(okno,text=  "przewidywana koncentracja piasku")
Lrop   = Label(okno,text=  "gęstość właściwa piasku")
LR     = Label(okno,text=  "przewidywant promień strefy zasilania odwiertu")
Lq     = Label(okno,text=  "wydajnośc agregaty szczelinującego")
Lrosk  = Label(okno,text=  "średnia gęstośc skał")
Lqt    = Label(okno,text=  "średni ciężar rur")
LE     = Label(okno,text=  "moduł sprężystości poprzeczenej")
Lv     = Label(okno,text=  "współczynnik Poissona")
Lkc    = Label(okno,text=  "współczynnik przep. skał złożowych")
LCl    = Label(okno,text=  "wpółczynnik ucieczki cieczy szczelinującej")
Lr     = Label(okno,text=  "promień odwiertu")
Lhf    = Label(okno,text=  "wysokość szczeliny")
Lcosfi = Label(okno,text=  "cosfi")
Lg     = Label(okno,text=  "przyśpieszenie ziemskie")
LRe    = Label(okno,text=  "liczba Reynoldsa")


wyniki= Text(okno)

def zapiszdane() :

    wartoscD=ED.get()
    LD2=Label(okno)
    LD2["text"]=wartoscD
    LD2.grid(row=1, column=2)
    D=str(wartoscD)

    wartosch = Eh.get()
    LD3 = Label(okno)
    LD3["text"] = wartosch
    LD3.grid(row=2, column=2)
    h = str(wartoscD)

    wartoscM = EM.get()
    LD4 = Label(okno)
    LD4["text"] = wartoscD
    LD4.grid(row=3, column=2)
    M = str(wartoscM)
    
    wartoscd = Ed.get()
    LD5 = Label(okno)
    LD5["text"] = wartoscd
    LD5.grid(row=4, column=2)
    d = str(wartoscd)

    wartoscQ = EQ.get()
    LD6 = Label(okno)
    LD6["text"] = wartoscQ
    LD6.grid(row=5, column=2)
    Q = str(wartoscQ)
    
    wartoscros = Eros.get()
    LD7 = Label(okno)
    LD7["text"] = wartoscros
    LD7.grid(row=6, column=2)
    ros = str(wartoscros)

    wartoscmi = Emi.get()
    LD7 = Label(okno)
    LD7["text"] = wartoscmi
    LD7.grid(row=7, column=2)
    mi = str(wartoscmi)
    
    wartoscC = EC.get()
    LD8 = Label(okno)
    LD8["text"] = wartoscC
    LD8.grid(row=8, column=2)
    C = str(wartoscC)

    wartoscrop = Erop.get()
    LD9 = Label(okno)
    LD9["text"] = wartoscrop
    LD9.grid(row=9, column=2)
    rop = str(wartoscrop)

    wartoscR = ER.get()
    LD10 = Label(okno)
    LD10["text"] = wartoscR
    LD10.grid(row=10, column=2)
    R = str(wartoscR)

    wartoscq = Eq.get()
    LD11 = Label(okno)
    LD11["text"] = wartoscq
    LD11.grid(row=11, column=2)
    q = str(wartoscq)

    wartoscrosk = Erosk.get()
    LD12 = Label(okno)
    LD12["text"] = wartoscrosk
    LD12.grid(row=12, column=2)
    rosk = str(wartoscrosk)

    wartoscqt = Eqt.get()
    LD13 = Label(okno)
    LD13["text"] = wartoscqt
    LD13.grid(row=13, column=2)
    qt = str(wartoscqt)

    wartoscE = EE.get()
    LD14 = Label(okno)
    LD14["text"] = wartoscE
    LD14.grid(row=14, column=2)
    E = str(wartoscE)

    wartoscv = Ev.get()
    LD15 = Label(okno)
    LD15["text"] = wartoscv
    LD15.grid(row=15, column=2)
    v = str(wartoscv)

    wartosckc = Ekc.get()
    LD16 = Label(okno)
    LD16["text"] = wartosckc
    LD16.grid(row=16, column=2)
    kc = str(wartosckc)

    wartoscC1 = ECl.get()
    LD17 = Label(okno)
    LD17["text"] = wartoscC1
    LD17.grid(row=17, column=2)
    C1 = str(wartoscC1)

    wartoscr = Er.get()
    LD18 = Label(okno)
    LD18["text"] = wartoscr
    LD18.grid(row=18, column=2)
    r = str(wartoscr)

    wartoschf = Ehf.get()
    LD19 = Label(okno)
    LD19["text"] = wartoschf
    LD19.grid(row=19, column=2)
    hf = str(wartoschf)

    wartosccosfi = Ecosfi.get()
    LD20 = Label(okno)
    LD20["text"] = wartosccosfi
    LD20.grid(row=20, column=2)
    cosfi = str(wartosccosfi)

    wartoscg = Eg.get()
    LD21 = Label(okno)
    LD21["text"] = wartoscg
    LD21.grid(row=21, column=2)
    g = str(wartoscg)

    wartoscRe = ERe.get()
    LD22 = Label(okno)
    LD22["text"] = wartoscRe
    LD22.grid(row=22, column=2)
    Re = str(wartoscRe)




def oblicz():
    D     = float(ED        .get())
    h     = float(Eh        .get())
    M     = float(EM        .get())
    d     = float(Ed        .get())
    Q     = float(EQ        .get())
    ros   = float(Eros      .get())
    mi    = float(Emi       .get())
    C     = float(EC        .get())
    rop   = float(Erop      .get())
    R     = float(ER        .get())
    q     = float(Eq        .get())
    rosk  = float(Erosk     .get())
    qt    = float(Eqt       .get())
    E     = float(EE        .get())
    v     = float(Ev        .get())
    kc    = float(Ekc       .get())
    C1    = float(ECl       .get())
    r     = float(Er        .get())
    hf    = float(Ehf       .get())
    cosfi = float(Ecosfi    .get())
    g     = float(Eg        .get())
    Re    = float(ERe       .get())

    lamb  = 64/Re
    wyniki.insert(END, "Lambda=" + str(lamb)+'\n')

    K = 0.5 * ((1 + (2 * v) / (1 -v)) + (1 - (2 *v) / (1 -v)) * cosfi)
    wyniki.insert(END,"współczynnik Crittendona="+ str(K)+'\n')

    Pg = (h * rosk * g) / 1000000
    wyniki.insert(END,"Ciśnienie Górotworu="+ str(Pg)+'\n')

    Ps = Pg * K
    wyniki.insert(END,"Ciśnienie Szczelinowania="+ str(Ps)+'\n')

    rosp = ros * (1 - C / rop) + C
    wyniki.insert(END, "Ciśnienie hydrostatyczne cieczy szczelinującej=" + str(rosp)+'\n')

    PH = (rosp * h * g) / 1000000
    wyniki.insert(END, "Ciśnienie hydrostatyczne=" + str(PH)+'\n')

    A = (0.035 ** (2)) * 3.1415
    wyniki.insert(END, "Powierzchnia=" + str(A)+'\n')

    V = q / A
    wyniki.insert(END, "Prędkość tłoczenia=" + str(V)+'\n')

    PTR = (lamb * (((h - 0.5 * M) / d)) * ((V ** 2) / 2) * rosp) / 1000000
    wyniki.insert(END, "Straty na tarcie=" + str(PTR)+'\n')

    PT = Ps + PTR - PH
    wyniki.insert(END, "Ciśnienie tłoczenia=" + str(PT)+'\n')

    F = Ps * (3.1415 / 4) * (D ** 2 - d ** 2)
    wyniki.insert(END, "Fiła działająca na paker=" + str(F)+'\n')

    Ft = (h * qt) / 1000
    wyniki.insert(END, "Ciężar przewodu tłoczącego=" + str(Ft)+'\n')

    Vp = ((3.1415 * (d ** 2)) / 4) * ((h - M)) + (((3.1415 * (D ** 2)) / 4) * M)
    wyniki.insert(END, "objętośc przybitki=" + str(Vp)+'\n')

    t = Q / q
    wyniki.insert(END, "czas tłcozenia=" + str(t)+'\n')

    Eprim = E / (1 - v ** 2) / 1000000
    wyniki.insert(END, "E'=" + str(Eprim)+'\n')

    Qi = q / 2
    wyniki.insert(END, "Qi=" + str(Qi)+'\n')

    Lprim = (q * (t) ** (1 / 2)) / (2 * 3.1415 * hf * C1)
    wyniki.insert(END, "L'=" + str(Lprim)+'\n')

    Pnet = (((16 * mi * Qi * Eprim ** 3) / (3.14158 * hf ** 4)) * Lprim) ** (1 / 4)
    wyniki.insert(END, "Ciśnienie netto=" + str(Pnet)+'\n')

    w = (2 * Pnet * hf * (1 - v ** 2)) / (E / 1000000)
    wyniki.insert(END, "maksymalna szerokość szczeliny=" + str(w)+'\n')

    wsr = (3.1415 / 4) * w
    wyniki.insert(END, "średnia szerokość szczeliny=" + str(wsr)+'\n')

    Sp = (2 * C1 * ((3.1415 * t) ** (1 / 2))) / wsr

    Sp2 = Sp ** 2

    Af = ((Qi * wsr) / (4 * 3.1415 * (C1 ** 2))) * (
    ((e ** (Sp2)) * scipy.special.erfc(Sp)) + ((2 / (3.1415 ** (1 / 2))) * Sp) - 1)
    wyniki.insert(END, "powierzchnia szczeliny=" + str(Af)+'\n')

    L = Af / (2 * hf)
    wyniki.insert(END, "promień zaisęgu szczeliny=" + str(L)+'\n')

    dL = abs(L - Lprim)
    wyniki.insert(END, "Błąd|L-L'|=" + str(dL)+'\n')

    err = L

    iter = 0
    while err > 1:
        wyniki.insert(END, "iteracja" + str(iter)+'\n')

        Pnet = (((16 * mi * Qi * Eprim ** 3) / (3.14158 * hf ** 4)) * L) ** (1 / 4)
        wyniki.insert(END, "Pnet=" + str(Pnet)+'\n')
        w = (2 * Pnet * hf * (1 - v ** 2)) / (E / 1000000)
        wyniki.insert(END, "Mksymalna szerokość szczeliny=" + str(w)+'\n')
        wsr = (3.1415 / 4) * w
        wyniki.insert(END, "średnia szerokosc szczeliny" + str(wsr)+'\n')
        Sp = (2 * C1 * ((3.1415 * t) ** (1 / 2))) / wsr

        Sp2 = Sp ** 2

        Af = ((Qi * wsr) / (4 * 3.1415 * (C1 ** 2))) * (
            ((e ** (Sp2)) * scipy.special.erfc(Sp)) + ((2 / (3.1415 ** (1 / 2))) * Sp) - 1)
        wyniki.insert(END, "Powierzchnia szczeliny=" + str(Af)+'\n')

        Lnew = Af / (2 * hf)
        wyniki.insert(END, "nowe L=" + str(Lnew)+'\n')

        err = abs(Lnew - L)
        wyniki.insert(END, "Błąd=" + str(err)+'\n')
        L = Lnew
        iter = iter + 1
    wyniki.insert(END,"########################################################################"+"\n")


def clear():
    wyniki.delete('1.0',END)

wyczysc=Button(okno,text="wyczyść pole tekstowe",command=clear)


zapiszdane()
gromadzdane=Button(okno,text="zapisz dane",command=zapiszdane)

oblicz=Button(okno, text="Oblicz", command=oblicz)

#umiejscowienie
Dane.grid(row=0, column=0)
LD    .grid(row=1)
Lh    .grid(row=2)
LM    .grid(row=3)
Ld    .grid(row=4)
LQ    .grid(row=5)
Lros  .grid(row=6)
Lmi   .grid(row=7)
LC    .grid(row=8)
Lrop  .grid(row=9)
LR    .grid(row=10)
Lq    .grid(row=11)
Lrosk .grid(row=12)
Lqt   .grid(row=13)
LE    .grid(row=14)
Lv    .grid(row=15)
Lkc   .grid(row=16)
LCl   .grid(row=17)
Lr    .grid(row=18)
Lhf   .grid(row=19)
Lcosfi.grid(row=20)
Lg    .grid(row=21)
LRe   .grid(row=22)


ED    .grid(row=1,column=1)
Eh    .grid(row=2,column=1)
EM    .grid(row=3,column=1)
Ed    .grid(row=4,column=1)
EQ    .grid(row=5,column=1)
Eros  .grid(row=6,column=1)
Emi   .grid(row=7,column=1)
EC    .grid(row=8,column=1)
Erop  .grid(row=9,column=1)
ER    .grid(row=10,column=1)
Eq    .grid(row=11,column=1)
Erosk .grid(row=12,column=1)
Eqt   .grid(row=13,column=1)
EE    .grid(row=14,column=1)
Ev    .grid(row=15,column=1)
Ekc   .grid(row=16,column=1)
ECl   .grid(row=17,column=1)
Er    .grid(row=18,column=1)
Ehf   .grid(row=19,column=1)
Ecosfi.grid(row=20,column=1)
Eg    .grid(row=21,column=1)
ERe   .grid(row=22,column=1)




gromadzdane.grid(row=24, column=1)
wyniki.grid(column=3,row=1, rowspan=23)
zapWy.grid(row=0,column=2)
oblicz.grid(row=24, column=2)
wyczysc.grid(row=23, column=2)

okno.mainloop()
