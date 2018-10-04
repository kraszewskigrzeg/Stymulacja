import scipy.special
from math import fabs
from math import sqrt
from cmath import sqrt
import numpy as np


D=0.2                               # [m]  średnica odwiertu
h=3300                              # [m]  głębokość odwiertu
M=40                                # [m]  miąższość warstwy
d=0.0698                            # [m]  średnica przewodu
Q=40                                # [m3] objętość cieczy
ros=1200                            # [kg/m3]  gęstośc właściwa
mi=0.5                              # [Pa*s]lepkość cieczy szczelinującej
C=320                               # [kg/m3]przewidywana koncentracja piasku
rop=2600                            # [kg/m3]gęstość właściwa piasku
R=300                               # [m]przewidywant promień strefy zasilania odwiertu
q=0.02                              # [m3/s]wydajnośc agregaty szczelinującego
rosk=2700                           # [kg/m3]średnia gęstośc skał
qt=192.4                            # [N/m]średni ciężar rur
E=9000000000                        # [Pa]moduł sprężystości poprzeczenej
v=0.2                               # [-]współczynnik Poissona
kc=100*10**(-15)                    # [m2]współczynnik przep. skał złożowych
Cl=0.0001                           # [m/sqrt(s)]wpółczynnik ucieczki cieczy szczelinującej
r=0.1                               # [m]promień odwiertu
hf=7                                # [7]wysokość szczeliny
cosfi=-1
g=9.80665                           # [m/s2]przyśpieszenie ziemskie
Re=2100                             #liczba Reynoldsa
lamb=64/Re                          #lambda

print("współczynnik Crittendona ")

K=0.5*((1+(2*v)/(1-v))+(1-(2*v)/(1-v))*cosfi)
print("K=",K)

print("ciśnienie górotworu ")

Pg=(h*rosk*g)/1000000
print("Pg=",Pg,"[MPa]")

print("ciśnienie szczelinowania")

Ps=Pg*K
print("Ps=",Ps,"[MPa]")

print("ciśnienie ciśnienia tłoczenia")
print("ciśnienie hydrostatyczne cieczy szczelinującej")

rosp=ros*(1-C/rop)+C
print("RoSp=",rosp,"[kg/m3]")

PH=(rosp*h*g)/1000000
print("PH=",PH,"[MPa]")

print("obliczenie cisnienia tłoczenia")
print("powierzchnia")
A=(0.035**(2))*3.1415
print("A=",A,"[m2]")
print("predkośc tłoczenia")
V=q/A
print("V=",V,"[m/s]")

print("straty na tarcie")
PTR=(lamb*(((h-0.5*M)/d))*((V**2)/2)*rosp)/1000000
print("PTR=",PTR,"[MPa]")

print("ciśnienie tłoczenia:")
PT=Ps+PTR-PH
print("PT=",PT,"[MPa]")

print("siła dziąłająca na paker [N]")
F=Ps*(3.1415/4)*(D**2-d**2)
print("F=",F,"[N]")

print("ciężar przewodu tłoczącego")
Ft=(h*qt)/1000
print("Ft=",Ft,"[kN]")


print("Objętość przybitki")

Vp=((3.1415*(d**2))/4)*((h-M))+(((3.1415*(D**2))/4)*M)
print("Vp=",Vp,"[m3]")

print("czas tłoczenia cieczy szczelinującej")
t=Q/q
print("t=",t,"[s]")


print("E'")
Eprim=E/(1-v**2)/1000000
print("E'=",Eprim,"[Mpa]")

print("Qi")
Qi=q/2

print("L'")
Lprim=(q*(t)**(1/2))/(2*3.1415*hf*Cl)
print("Lprim=",Lprim)

print("ciśnienie netto")
Pnet=(((16*mi*Qi*Eprim**3)/(3.14158*hf**4))*Lprim)**(1/4)
print("Pnet=",Pnet,"[MPa]")

print("maksymalna szerokoscszczeliny")
w=(2*Pnet*hf*(1-v**2))/(E/1000000)
print("w=",w,"[m]")

print("średnia szerokośc szczeliny")
wsr=(3.1415/4)*w
print("wsr=",wsr,"[m]")


print("powierzchnia szczeliny")

e=2.718

Sp=(2*Cl*((3.1415*t)**(1/2)))/wsr
Sp2=Sp**2
print("Sp=",Sp)

print("obliczenie wartości erfc")

def erfc (Sp):
    print("erfc=",scipy.special.erfc(Sp))
erfc(Sp)


print("powierzchnia szczeliny")

Af=((Qi*wsr)/(4*3.1415*(Cl**2)))*(((e**(Sp2))*scipy.special.erfc(Sp))+((2/(3.1415**(1/2)))*Sp)-1)
print("Af=",Af,"[m2]")

print("promień zasięgu szczeliny")
L=Af/(2*hf)
print("L=",L)

print("błąd |L-L'|")
dL=fabs(L-Lprim)

print("|L-L'|=",dL,"[m]")

print("#########################################################################################")
print("iteracja 1")

Lprim1=L

print("ciśnienie netto")
Pnet1=(((16*mi*Qi*Eprim**3)/(3.14158*hf**4))*Lprim1)**(1/4)
print("Pnet=",Pnet1,"[MPa]")

print("maksymalna szerokoscszczeliny")
w1=(2*Pnet1*hf*(1-v**2))/(E/1000000)
print("w=",w1,"[m]")

print("średnia szerokośc szczeliny")
wsr1=(3.1415/4)*w1
print("wsr=",wsr1,"[m]")


print("powierzchnia szczeliny")

e=2.718

Sp1=(2*Cl*((3.1415*t)**(1/2)))/wsr1
Sp21=Sp1**2
print("Sp=",Sp1)

print("obliczenie wartości erfc")

def erfc (Sp1):
    print("erfc=",scipy.special.erfc(Sp1))
erfc(Sp1)


print("powierzchnia szczeliny")
Af1=((Qi*wsr1)/(4*3.1415*(Cl**2)))*(((e**(Sp21))*scipy.special.erfc(Sp1))+((2/(3.1415**(1/2)))*Sp1)-1)
print("Af=",Af1,"[m2]")

print("promień zasięgu szczeliny")
L1=Af1/(2*hf)
print("L=",L1)

#błąd |L-L'|
dL1=fabs(L1-Lprim1)
print("|L-L'|=",dL1,"[m]")

print("#########################################################################################")
print("iteracja 2")

L2=L1
print("ciśnienie netto")
Pnet2=(((16*mi*Qi*Eprim**3)/(3.14158*hf**4))*L2)**(1/4)
print("Pnet=",Pnet2,"[MPa]")

print("maksymalna szerokoscszczeliny")
w2=(2*Pnet2*hf*(1-v**2))/(E/1000000)
print("w=",w2,"[m]")

print("średnia szerokośc szczeliny")
wsr2=(3.1415/4)*w2
print("wsr=",wsr2,"[m]")

print("powierzchnia szczeliny")

e=2.718

Sp2=(2*Cl*((3.1415*t)**(1/2)))/wsr2
Sp22=Sp2**2
print("Sp=",Sp2)

print("obliczenie wartości erfc")

def erfc (Sp):
    print("erfc=",scipy.special.erfc(Sp2))
erfc(Sp2)


print("powierzchnia szczeliny")
Af2=((Qi*wsr2)/(4*3.1415*(Cl**2)))*(((e**(Sp22))*scipy.special.erfc(Sp2))+((2/(3.1415**(1/2)))*Sp2)-1)
print("Af=",Af2,"[m2]")

print("promień zasięgu szczeliny")
L2=Af2/(2*hf)
print("L=",L2)

print("błąd |L-L'|")
dL2=fabs(L2-L1)
print("|L-L'|=",dL2,"[m]")

print("#########################################################################################")
print("iteracja 3")

L3=L2
print("ciśnienie netto")
Pnet3=(((16*mi*Qi*Eprim**3)/(3.14158*hf**4))*L2)**(1/4)
print("Pnet=",Pnet3,"[MPa]")

print("maksymalna szerokoscszczeliny")
w3=(2*Pnet3*hf*(1-v**2))/(E/1000000)
print("w=",w3,"[m]")

print("średnia szerokośc szczeliny")
wsr3=(3.1415/4)*w3
print("wsr=",wsr3,"[m]")


print("powierzchnia szczeliny")

e=2.718

Sp3=(2*Cl*((3.1415*t)**(1/2)))/wsr3
Sp23=Sp3**2
print("Sp=",Sp3)

print("obliczenie wartości erfc")

def erfc (Sp):
    print("erfc=",scipy.special.erfc(Sp3))
erfc(Sp3)


print("powierzchnia szczeliny")
Af3=((Qi*wsr3)/(4*3.1415*(Cl**2)))*(((e**(Sp23))*scipy.special.erfc(Sp3))+((2/(3.1415**(1/2)))*Sp3)-1)
print("Af=",Af3,"[m2]")

print("promień zasięgu szczeliny")
L3=Af3/(2*hf)
print("L=",L3)

print("błąd |L-L'|")
dL3=fabs(L3-L2)
print("|L-L'|=",dL3,"[m]")

print("#########################################################################################")

L = (q*t**(1/2))/(2*3.1415*hf*Cl)

err = L

iter = 0
while err > 1:
    Pnet = (((16 * mi * Qi * Eprim ** 3) / (3.14158 * hf ** 4)) * L) ** (1 / 4)
    w = (2 * Pnet * hf * (1 - v ** 2)) / (E / 1000000)
    wsr = (3.1415 / 4) * w
    Sp = (2 * Cl * ((3.1415 * t) ** (1 / 2))) / wsr
    Sp2 = Sp ** 2
    Sp = scipy.special.erfc(Sp)
    Af = ((Qi * wsr) / (4 * 3.1415 * (Cl ** 2))) * (
    ((e ** (Sp2)) * scipy.special.erfc(Sp)) + ((2 / (3.1415 ** (1 / 2))) * Sp) - 1)
    Lnew = Af / (2 * hf)
    err = abs(Lnew - L)
    L = Lnew
    iter = iter +1
    print(err)



