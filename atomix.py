##basically all elements are objects. if u can figure out how to use this kagigger it's pretty freakin handy. just create an element object and use it in various functions.
##e.g. >>>x=hA()  >>>e(x)  creates hydrogen atom and finds out it's electronic info. everything is handy for something...If i've miscounted something just double check it with the periodic table.
##FOR some mysterious reason it adds an extra electron after 102 so for the last 10 elements just -1 to the values. If someone can work out why this is happening it would be great. Thank you.It seems to defy logic.
import math
log10=math.log10
pi=math.pi
log=math.log
av=6.0221413*10**23
amu=1.66053886 * 10**-27
e= 5.4857990946*10**-4
pro=1.007276466812
neu=1.00866491600
H=pro+e
D=H+neu
T=D+neu
He=(H*2)+(neu*2)
Li=D*3
Be=D*4+neu
B=D*5
C=D*6
N=D*7
O=D*8
F=D*9+neu
Ne=D*10
Na=22.9898
Mg=24.3050
Al=26.9815
Si=28.0855
P=30.9738
S=32.066
Cl=D*17+neu
Ar=D*18
K=D*19+neu
Ca=40.078
Sc=44.9559
Ti=47.88
V=50.9415
Cr=51.9961
Mn=54.9380
Fe=D*26+(neu*4)
Co=D*27+(neu*5)
Ni=58.693
Cu=63.546
Zn=65.39
Ga=69.723
Ge=72.61
As=74.9216
Se=78.96
Br=79.904
Kr=83.80
Rb=85.4678
Sr=D*38+(neu*14)
Y=88.9059
Zr=91.224
Nb=92.9064
Mo=95.94
Tc=98
Ru=101.07
Rh=102.9055
Pd=106.42
Ag=107.8682
Cd=112.411
In=114.82
Sn=118.710
Sb=121.757
Te=127.60
I=D*53+(neu*21)
Xe=D*54+(neu*24)
Cs=D*55+(neu*23)
Ba=137.327
La=138.9055
Ce=140.115
Pr=140.9076
Nd=144.24
Pm=145
Sm=150.36
Eu=151.965
Gd=157.25
Tb=158.9253
Dy=162.50
Ho=164.9303
Er=167.26
Tm=168.9342
Yb=173.04
Ac=227
Th=D*90+(neu*52)
Pa=231.0359
U=D*92+(neu*54)
Np=D*93+(neu*51)
Pu=D*94+(neu*56)
Am=D*95+(neu*51)
Cm=247
Bk=247
Cf=251
Es=252
Fm=257
Md=258
No=259
Lr=260
Rf=267
Db=268
Sg=271
Bh=272
Hs=270
Mt=276
Ds=281
Rg=280
Cn=285
Lu=174.967
Hf=178.49
Ta=180.9479
W=183.85
Re=186.207
Os=190.2
Ir=192.22
Pt=195.08
Au=196.9665
Hg=200.59
TI=204.3833
Pb=D*82+(neu*44)
Bi=D*83+(neu*43)
Po=209
At=210
Rn=D*86+(neu*50)
Fr=223
Ra=D*88+(neu*50)
Atoms=dict(amu=1.66053886 * 10**-27,e= 5.4857990946*10**-4,pro=1.007276466812,neu=1.00866491600,H=pro+e,D=H+neu,T=D+neu,He=(H*2)+(neu*2),Li=D*3,Be=D*4+neu,B=D*5,C=D*6,N=D*7,O=D*8,F=D*9+neu,Ne=D*10,Na=22.9898,Mg=24.3050,Al=26.9815,Si=28.0855,P=30.9738,S=32.066,Cl=D*17+neu,Ar=D*18,K=D*19+neu,Ca=40.078,Sc=44.9559,Ti=47.88,V=50.9415,Cr=51.9961,Mn=54.9380,Fe=D*26+(neu*4),Co=D*27+(neu*5),Ni=58.693,Cu=63.546,Zn=65.39,Ga=69.723,Ge=72.61,As=74.9216,Se=78.96,Br=79.904,Kr=83.80,Rb=85.4678,Sr=D*38+(neu*14),Y=88.9059,Zr=91.224,Nb=92.9064,Mo=95.94,Tc=98,Ru=101.07,Rh=102.9055,Pd=106.42,Ag=107.8682,Cd=112.411,In=114.82,Sn=118.710,Sb=121.757,Te=127.60,I=D*53+(neu*21),Xe=D*54+(neu*24),Cs=D*55+(neu*23),Ba=137.327,La=138.9055,Ce=140.115,Pr=140.9076,Nd=144.24,Pm=145,Sm=150.36,Eu=151.965,Gd=157.25,Tb=158.9253,Dy=162.50,Ho=164.9303,Er=167.26,Tm=168.9342,Yb=173.04,Ac=227,Th=D*90+(neu*52),Pa=231.0359,U=D*92+(neu*54),Np=D*93+(neu*51),Pu=D*94+(neu*56),Am=D*95+(neu*51),Cm=247,Bk=247,Cf=251,Es=252,Fm=257,Md=258,No=259,Lr=260,Rf=267,Db=268,Sg=271,Bh=272,Hs=270,Mt=276,Ds=281,Rg=280,Cn=285,Lu=174.967,Hf=178.49,Ta=180.9479,W=183.85,Re=186.207,Os=190.2,Ir=192.22,Pt=195.08,Au=196.9665,Hg=200.59,TI=204.3833,Pb=D*82+(neu*44),Bi=D*83+(neu*43),Po=209,At=210,Rn=D*86+(neu*50),Fr=223,Ra=D*88+(neu*50))
class proton():
    r=  8.768*10**-16
    A=4*pi*r**2
    m=1.007276466812
    v=(4/3)*pi*r**3
    p=2*pi*r
class neutron():
    r=8.768*10**-16
    A=4*pi*r**2
    m=1.00866491600
    v=(4/3)*pi*r**3
    p=2*pi*r
class electron():
    r=2.817940326727 * 10**-15
    A=4*pi*r**2
    m= 5.4857990946*10**-4
    v=(4/3)*pi*r**3
    p=2*pi*r
def molecule():
    number=int(input('how different many elements?(at least 2)'))
    if number==2:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        weight=(a*A)+(b*B)
        print(weight)
    if number==3:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        weight=(a*A)+(b*B)+(c*C)
        print(weight)
    if number==4:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)
        print(weight)
    if number==5:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)
        print(weight)
    if number==6:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)
        print(weight)
    if number==7:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)
        print(weight)
    if number==8:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)
        print(weight)
    if number==9:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)
        print(weight)
    if number==10:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)
        print(weight)
    if number==11:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)
        print(weight)
    if number==12:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)
        print(weight)
    if number==13:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)
        print(weight)
    if number==14:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)
        print(weight)
    if number==15:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)
        print(weight)
    if number==16:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)
        print(weight)
    if number==17:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)
        print(weight)
    if number==18:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)
        print(weight)
    if number==19:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)
        print(weight)
    if number==20:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)
        print(weight)
    if number==21:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)
        print(weight)
    if number==22:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        V=Atoms.get(input('which element? H for hyrdogen etc.'))
        v=float(input('coefficient of V?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)+(v*V)
        print(weight)
    if number==23:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        V=Atoms.get(input('which element? H for hyrdogen etc.'))
        v=float(input('coefficient of V?'))
        W=Atoms.get(input('which element? H for hyrdogen etc.'))
        w=float(input('coefficient of W?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)+(v*V)+(w*W)
        print(weight)
    if number==24:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        V=Atoms.get(input('which element? H for hyrdogen etc.'))
        v=float(input('coefficient of V?'))
        W=Atoms.get(input('which element? H for hyrdogen etc.'))
        w=float(input('coefficient of W?'))
        X=Atoms.get(input('which element? H for hyrdogen etc.'))
        x=float(input('coefficient of X?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)+(v*V)+(w*W)+(x*X)
        print(weight)
    if number==25:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        V=Atoms.get(input('which element? H for hyrdogen etc.'))
        v=float(input('coefficient of V?'))
        W=Atoms.get(input('which element? H for hyrdogen etc.'))
        w=float(input('coefficient of W?'))
        X=Atoms.get(input('which element? H for hyrdogen etc.'))
        x=float(input('coefficient of X?'))
        Y=Atoms.get(input('which element? H for hyrdogen etc.'))
        y=float(input('coefficient of Y?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)+(v*V)+(w*W)+(x*X)+(y*Y)
        print(weight)
    if number==26:
        A=Atoms.get(input('which element? H for hyrdogen etc.'))
        a=float(input('coefficient of A?'))
        B=Atoms.get(input('which element? H for hyrdogen etc.'))
        b=float(input('coefficient of B?'))
        C=Atoms.get(input('which element? H for hyrdogen etc.'))
        c=float(input('coefficient of C?'))
        D=Atoms.get(input('which element? H for hyrdogen etc.'))
        d=float(input('coefficient of D?'))
        E=Atoms.get(input('which element? H for hyrdogen etc.'))
        e=float(input('coefficient of E?'))
        F=Atoms.get(input('which element? H for hyrdogen etc.'))
        f=float(input('coefficient of F?'))
        G=Atoms.get(input('which element? H for hyrdogen etc.'))
        g=float(input('coefficient of G?'))
        H=Atoms.get(input('which element? H for hyrdogen etc.'))
        h=float(input('coefficient of H?'))
        I=Atoms.get(input('which element? H for hyrdogen etc.'))
        i=float(input('coefficient of I?'))
        J=Atoms.get(input('which element? H for hyrdogen etc.'))
        j=float(input('coefficient of J?'))
        K=Atoms.get(input('which element? H for hyrdogen etc.'))
        k=float(input('coefficient of K?'))
        L=Atoms.get(input('which element? H for hyrdogen etc.'))
        l=float(input('coefficient of L?'))
        M=Atoms.get(input('which element? H for hyrdogen etc.'))
        m=float(input('coefficient of M?'))
        N=Atoms.get(input('which element? H for hyrdogen etc.'))
        n=float(input('coefficient of N?'))
        O=Atoms.get(input('which element? H for hyrdogen etc.'))
        o=float(input('coefficient of O?'))
        P=Atoms.get(input('which element? H for hyrdogen etc.'))
        p=float(input('coefficient of P?'))
        Q=Atoms.get(input('which element? H for hyrdogen etc.'))
        q=float(input('coefficient of Q?'))
        R=Atoms.get(input('which element? H for hyrdogen etc.'))
        r=float(input('coefficient of R?'))
        S=Atoms.get(input('which element? H for hyrdogen etc.'))
        s=float(input('coefficient of S?'))
        T=Atoms.get(input('which element? H for hyrdogen etc.'))
        t=float(input('coefficient of T?'))
        U=Atoms.get(input('which element? H for hyrdogen etc.'))
        u=float(input('coefficient of U?'))
        V=Atoms.get(input('which element? H for hyrdogen etc.'))
        v=float(input('coefficient of V?'))
        W=Atoms.get(input('which element? H for hyrdogen etc.'))
        w=float(input('coefficient of W?'))
        X=Atoms.get(input('which element? H for hyrdogen etc.'))
        x=float(input('coefficient of X?'))
        Y=Atoms.get(input('which element? H for hyrdogen etc.'))
        y=float(input('coefficient of Y?'))
        Z=Atoms.get(input('which element? H for hyrdogen etc.'))
        z=float(input('coefficient of Z?'))
        weight=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)+(h*H)+(i*I)+(j*J)+(k*K)+(l*L)+(m*M)+(n*N)+(o*O)+(p*P)+(q*Q)+(r*R)+(s*S)+(t*T)+(u*U)+(v*V)+(w*W)+(x*X)+(y*Y)+(z*Z)
        print(weight)
    
class masscalc():
    
    def mass(self):
        h=input('element A?')
        i=input('element B?')
        j=input('element C?')
        k=input('element D?')
        l=input('element E?')
        m=input('element F?')
        n=input('element G?')      
        a=float(input('coefficient of A?'))
        A=Atoms.get(h)
        b=float(input('coefficient of B?'))
        B=Atoms.get(i)
        c=float(input('coefficient of C?'))
        C=Atoms.get(j)
        d=float(input('coefficient of D?'))
        D=Atoms.get(k)
        e=float(input('coefficient of E?'))
        E=Atoms.get(l)
        f=float(input('coefficient of F?'))
        F=Atoms.get(m)
        g=float(input('coefficient of G?'))
        G=Atoms.get(n)
        z=(a*A)+(b*B)+(c*C)+(d*D)+(e*E)+(f*F)+(g*G)
        print(z)
class world():
    ONEs= False
    ones=False
    TWOs=False
    twos=False
    TWOp=False
    twop=False
    tWop=False
    Twop=False
    twOp=False
    twoP=False
    THREEs=False
    threes=False
    THREEp=False
    threep=False
    Threep=False
    tHreep=False
    thReep=False
    thrEep=False
    FOURs=False
    fours=False
    THREEd=False
    threed=False
    Threed=False
    tHreed=False
    thReed=False
    thrEed=False
    threEd=False
    threeD=False
    THreed=False
    tHReed=False
    FOURp=False
    fourp=False
    Fourp=False
    fOurp=False
    foUrp=False
    fouRp=False
    FIVEs=False
    fives=False
    FOURd=False
    fourd=False
    Fourd=False
    fOurd=False
    foUrd=False
    fouRd=False
    fourD=False
    FOurd=False
    fOUrd=False
    foURd=False
    FIVEp=False
    fivep=False
    Fivep=False
    fIvep=False
    fiVep=False
    fivEp=False
    SIXs=False
    sixs=False
    FOURf=False
    fourf=False
    Fourf=False
    fOurf=False
    foUrf=False
    fouRf=False
    fourF=False
    FOurf=False
    fOUrf=False
    foURf=False
    fouRF=False
    FOUrf=False
    fOURf=False
    foURF=False
    FIVEd=False
    fived=False
    Fived=False
    fIved=False
    fiVed=False
    fivEd=False
    fiveD=False
    FIved=False
    fIVed=False
    fiVEd=False
    SIXp=False
    sixp=False
    Sixp=False
    sIxp=False
    siXp=False
    sixP=False
    SEVENs=False
    sevens=False
    FIVEf=False
    fivef=False
    Fivef=False
    fIvef=False
    fiVef=False
    fivEf=False
    fiveF=False
    FIvef=False
    fIVef=False
    fiVEf=False
    fivEF=False
    FIVef=False
    fIVEf=False
    fiVEF=False
    SIXd=False
    sixd=False
    Sixd=False
    sIxd=False
    siXd=False
    sixD=False
    SIxd=False
    sIXd=False
    siXD=False
    SIXd=False
    SEVENp=False
    sevenp=False
    Sevenp=False
    sEvenp=False
    seVenp=False
    sevEnp=False
    EIGHTs=False
    eights=False
class heA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    def val(self):
        e=val.get('he')
        print(e)
    def nval(self):
        e=nval.get('he')
        print(e)
    def mass(self):
        m=(H*2)+(neu*2)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
    
    
class neA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True

    def val(self):
        e=val.get('ne')
        print(e)
    def nval(self):
        e=nval.get('ne')
        print(e)
    def mass(self):
        m=D*10
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

class arA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    def val(self):
        e=val.get('ar')
        print(e)
    def nval(self):
        e=nval.get('ar')      
        print(e)
    def mass(self):
        m=D*18
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

class hA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    def val(self):
        e=val.get('h')
        print(e)
    def nval(self):
        e=nval.get('h')
        print(e)
    def mass(self):
        m=pro+e
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class liA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    
    def val(self):
        e=val.get('li')
        print(e)
    def nval(self):
        e=nval.get('li')
        print(e)
    def mass(self):
        m=D*3
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class fA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    def val(self):
        e=val.get('f')
        print(e)
    def nval(self):
        e=nval.get('f')
        print(e)
    def mass(self):
        m=D*9+neu
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
    
class naA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    def val(self):
        e=val.get('na')
        print(e)
    def nval(self):
        e=nval.get('na')
        print(e)
    def mass(self):
        m=D*11+neu
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class kA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    
    def val(self):
        e=val.get('k')
        print(e)
    def nval(self):
        e=nval.get('k')
        print(e)
    def mass(self):
        m=D*19+neu
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

class rbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    
    def val(self):
        e=val.get('rb')
        print(e)
    def nval(self):
        e=nval.get('rb')
        print(e)
    def mass(self):
        m=(D*27)+(T*10)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

class csA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    
    def val(self):
        e=val.get('cs')
        print(e)
    def nval(self):
        e=nval.get('cs')
        print(e)
    def mass(self):
        m=(D*33)+(T*22)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class frA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    
    
    def val(self):
        e=val.get('fr')
        print(e)
    def nval(self):
        e=nval.get('fr')
        print(e)
    def mass(self):
        m=(D*39)+(T*48)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class beA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True

    def val(self):
        e=val.get('be')
        print(e)
    def nval(self):
        e=nval.get('be')
        print(e)
    def mass(self):
        m=(D*3)+T
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

class oA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    def val(self):
        e=val.get('o')
        print(e)
    def nval(self):
        e=nval.get('o')
        print(e)
    def mass(self):
        m=D*8
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class caA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True

    
    def val(self):
        e=val.get('ca')
        print(e)
    def nval(self):
        e=nval.get('ca')
        print(e)
    def mass(self):
        m=D*20
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class mgA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    
    
    def val(self):
        e=val.get('mg')
        print(e)
    def nval(self):
        e=nval.get('mg')
        print(e)
    def mass(self):
        m=D*12
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class cuA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    
    
    def val(self):
        e=val.get('cu')
        print(e)
    def nval(self):
        e=nval.get('cu')
        print(e)
    def mass(self):
        m=(D*27)+(T*3)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class znA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    
    def val(self):
        e=val.get('zn')
        print(e)
    def nval(self):
        e=nval.get('zn')
        print(e)
    def mass(self):
        m=(D*28)+(T*3)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class krA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    
    def val(self):
        e=val.get('kr')
        print(e)
    def nval(self):
        e=nval.get('kr')
        print(e)
    def mass(self):
        m=(D*31)+(T*7)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class srA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    def val(self):
        e=val.get('sr')
        print(e)
    def nval(self):
        e=nval.get('sr')
        print(e)
    def mass(self):
        m=(D*33)+(T*7)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class cdA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    def val(self):
        e=val.get('cd')
        print(e)
    def nval(self):
        e=nval.get('cd')
        print(e)
    def mass(self):
        m=(D*44)+(T*8)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class baA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    def val(self):
        e=val.get('ba')
        print(e)
    def nval(self):
        e=nval.get('ba')
        print(e)
    def mass(self):
        m=(D*56)+(T*8)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class raA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    def val(self):
        e=val.get('ra')
        print(e)
    def nval(self):
        e=nval.get('ra')
        print(e)
    def mass(self):
        m=(D*94)+(T*12)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class bA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    def val(self):
        e=val.get('b')
        print(e)
    def nval(self):
        e=nval.get('b')
        print(e)
    def mass(self):
        m=(D*5)+(T*.25)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class nA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    def val(self):
        e=val.get('n')
        print(e)
    def nval(self):
        e=nval.get('n')
        print(e)
    def mass(self):
        x={'x':0,'y':0,'z':0}
        m=(D*7)-(T*.036)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class scA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    def val(self):
        e=val.get('sc')
        print(e)
    def nval(self):
        e=nval.get('sc')
        print(e)
    def mass(self):
        m=(D*16)+(T*4.2)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
##always rework values dont be lazy like me
class alA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    def val(self):
        e=val.get('al')
        print(e)
    def nval(self):
        e=nval.get('al')
        print(e)
    def mass(self):
        m=26.9815
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class gaA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    def val(self):
        e=val.get('ga')
        print(e)
    def nval(self):
        e=nval.get('ga')
        print(e)
    def mass(self):
        m=69.723
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class yA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    def val(self):
        e=val.get('y')
        print(e)
    def nval(self):
        e=nval.get('y')
        print(e)
    def mass(self):
        m=88.9059
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
        
class agA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    def val(self):
        e=val.get('ag')
        print(e)
    def nval(self):
        e=nval.get('ag')
        print(e)
    def mass(self):
        m=107.8682
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class indA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    def val(self):
        e=val.get('ind')
        print(e)
    def nval(self):
        e=nval.get('ind')
        print(e)
    def mass(self):
        m=114.818
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class laA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    def val(self):
        e=val.get('la')
        print(e)
    def nval(self):
        e=nval.get('la')
        print(e)
    def mass(self):
        m=138.906
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class ndA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    def val(self):
        e=val.get('nd')
        print(e)
    def nval(self):
        e=nval.get('nd')
        print(e)
    def mass(self):
        m=144.24
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class pmA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    def val(self):
        e=val.get('pm')
        print(e)
    def nval(self):
        e=nval.get('pm')
        print(e)
    def mass(self):
        m=(D*41)+(T*21)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class smA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    def val(self):
        e=val.get('sm')
        print(e)
    def nval(self):
        e=nval.get('sm')
        print(e)
    def mass(self):
        m=150.36
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class euA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    def val(self):
        e=val.get('eu')
        print(e)
    def nval(self):
        e=nval.get('eu')
        print(e)
    def mass(self):
        m=151.965
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class gdA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    def val(self):
        e=val.get('gd')
        print(e)
    def nval(self):
        e=nval.get('gd')
        print(e)
    def mass(self):
        m=157.25
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class dyA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    def val(self):
        e=val.get('dy')
        print(e)
    def nval(self):
        e=nval.get('dy')
        print(e)
    def mass(self):
        m=162.50
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class hoA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    def val(self):
        e=val.get('ho')
        print(e)
    def nval(self):
        e=nval.get('ho')
        print(e)
    def mass(self):
        m=164.9303
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class erA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    def val(self):
        e=val.get('er')
        print(e)
    def nval(self):
        e=nval.get('er')
        print(e)
    def mass(self):
        m=167.26
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class tmA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    def val(self):
        e=val.get('tm')
        print(e)
    def nval(self):
        e=nval.get('tm')
        print(e)
    def mass(self):
        m=168.9342
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class ybA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    def val(self):
        e=val.get('yb')
        print(e)
    def nval(self):
        e=nval.get('yb')
        print(e)
    def mass(self):
        m=173.04
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class luA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    def val(self):
        e=val.get('lu')
        print(e)
    def nval(self):
        e=nval.get('lu')
        print(e)
    def mass(self):
        m=174.967
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class tiA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    def val(self):
        e=val.get('ti')
        print(e)
    def nval(self):
        e=nval.get('ti')
        print(e)
    def mass(self):
        m=204.3833
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class acA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    def val(self):
        e=val.get('ac')
        print(e)
    def nval(self):
        e=nval.get('ac')
        print(e)
    def mass(self):
        m=227.028
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class fmA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    def val(self):
        e=val.get('fm')
        print(e)
    def nval(self):
        e=nval.get('fm')
        print(e)
    def mass(self):
        m=(D*100)+(T*18.3)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class mdA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    def val(self):
        e=val.get('md')
        print(e)
    def nval(self):
        e=nval.get('md')
        print(e)
    def mass(self):
        m=(D*101)+(T*18)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class noA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    def val(self):
        e=val.get('no')
        print(e)
    def nval(self):
        e=nval.get('no')
        print(e)
    def mass(self):
        m=(D*102)+(T*17.75)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class lrA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    def val(self):
        e=val.get('lr')
        print(e)
    def nval(self):
        e=nval.get('lr')
        print(e)
    def mass(self):
        m=(D*103)+(T*17.3)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class cA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    def val(self):
        e=val.get('c')
        print(e)
    def nval(self):
        e=nval.get('c')
        print(e)
    def mass(self):
        m=(D*6)-(T*0.029)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class siA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    
    def val(self):
        e=val.get('si')
        print(e)
    def nval(self):
        e=nval.get('si')
        print(e)
    def mass(self):
        m=28.0855
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class mnA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    
    def val(self):
        e=val.get('mn')
        print(e)
    def nval(self):
        e=nval.get('mn')
        print(e)
    def mass(self):
        m=54.9380
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class feA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    def val(self):
        e=val.get('fe')
        print(e)
    def nval(self):
        e=nval.get('fe')
        print(e)
    def mass(self):
        m=(D*24)+(T*2.48)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class coA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    def val(self):
        e=val.get('co')
        print(e)
    def nval(self):
        e=nval.get('co')
        print(e)
    def mass(self):
        m=58.9332
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class niA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    def val(self):
        e=val.get('ni')
        print(e)
    def nval(self):
        e=nval.get('ni')
        print(e)
    def mass(self):
        m=58.693
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class geA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    def val(self):
        e=val.get('ge')
        print(e)
    def nval(self):
        e=nval.get('ge')
        print(e)
    def mass(self):
        m=72.61
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class zrA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    def val(self):
        e=val.get('zr')
        print(e)
    def nval(self):
        e=nval.get('zr')
        print(e)
    def mass(self):
        m=91.224
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class pdA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    def val(self):
        e=val.get('pd')
        print(e)
    def nval(self):
        e=nval.get('pd')
        print(e)
    def mass(self):
        m=106.42
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class snA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    def val(self):
        e=val.get('sn')
        print(e)
    def nval(self):
        e=nval.get('sn')
        print(e)
    def mass(self):
        m=118.710
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class ceA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    def val(self):
        e=val.get('ce')
        print(e)
    def nval(self):
        e=nval.get('ce')
        print(e)
    def mass(self):
        m=140.115
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class prA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    def val(self):
        e=val.get('pr')
        print(e)
    def nval(self):
        e=nval.get('pr')
        print(e)
    def mass(self):
        m=140.908
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class tbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    def val(self):
        e=val.get('tb')
        print(e)
    def nval(self):
        e=nval.get('tb')
        print(e)
    def mass(self):
        m=158.925
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class hfA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    def val(self):
        e=val.get('hf')
        print(e)
    def nval(self):
        e=nval.get('hf')
        print(e)
    def mass(self):
        m=178.49
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class hgA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    def val(self):
        e=val.get('hg')
        print(e)
    def nval(self):
        e=nval.get('hg')
        print(e)
    def mass(self):
        m=200.59
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class pbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    def val(self):
        e=val.get('pb')
        print(e)
    def nval(self):
        e=nval.get('pb')
        print(e)
    def mass(self):
        m=207.2
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class thA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    def val(self):
        e=val.get('th')
        print(e)
    def nval(self):
        e=nval.get('th')
        print(e)
    def mass(self):
        m=232.038
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class amA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    def val(self):
        e=val.get('am')
        print(e)
    def nval(self):
        e=nval.get('am')
        print(e)
    def mass(self):
        m=(D*76)+(T*29.95)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
        
class cmA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    def val(self):
        e=val.get('cm')
        print(e)
    def nval(self):
        e=nval.get('cm')
        print(e)
    def mass(self):
        m=(D*79)+(T*28.99)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class bkA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    def val(self):
        e=val.get('bk')
        print(e)
    def nval(self):
        e=nval.get('bk')
        print(e)
    def mass(self):
        m=(D*79)+(T*29)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class cfA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    def val(self):
        e=val.get('cf')
        print(e)
    def nval(self):
        e=nval.get('cf')
        print(e)
    def mass(self):
        m=(D*82)+(T*28.5)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class esA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    def val(self):
        e=val.get('es')
        print(e)
    def nval(self):
        e=nval.get('es')
        print(e)
    def mass(self):
        m=(D*83)+(T*28)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class rfA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    def val(self):
        e=val.get('rf')
        print(e)
    def nval(self):
        e=nval.get('rf')
        print(e)
    def mass(self):
        m=(D*89)+(T*27)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class pA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    def val(self):
        e=val.get('p')
        print(e)
    def nval(self):
        e=nval.get('p')
        print(e)
    def mass(self):
        m=30.9738
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class clA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    def val(self):
        e=val.get('cl')
        print(e)
    def nval(self):
        e=nval.get('cl')
        print(e)
    def mass(self):
        m=35.4527
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class vA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    def val(self):
        e=val.get('v')
        print(e)
    def nval(self):
        e=nval.get('v')
        print(e)
    def mass(self):
        m=50.9415
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class arsA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    def val(self):
        e=val.get('ars')
        print(e)
    def nval(self):
        e=nval.get('ars')
        print(e)
    def mass(self):
        m=74.9216
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class brA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    def val(self):
        e=val.get('br')
        print(e)
    def nval(self):
        e=nval.get('br')
        print(e)
    def mass(self):
        m=79.904
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class nbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    def val(self):
        e=val.get('nb')
        print(e)
    def nval(self):
        e=nval.get('nb')
        print(e)
    def mass(self):
        m=92.9064
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class sbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    def val(self):
        e=val.get('sb')
        print(e)
    def nval(self):
        e=nval.get('sb')
        print(e)
    def mass(self):
        m=121.76
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class taA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    def val(self):
        e=val.get('ta')
        print(e)
    def nval(self):
        e=nval.get('ta')
        print(e)
    def mass(self):
        m=180.948
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class auA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    def val(self):
        e=val.get('au')
        print(e)
    def nval(self):
        e=nval.get('au')
        print(e)
    def mass(self):
        m=196.967
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class biA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    def val(self):
        e=val.get('bi')
        print(e)
    def nval(self):
        e=nval.get('bi')
        print(e)
    def mass(self):
        m=208.980
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class paA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    def val(self):
        e=val.get('pa')
        print(e)
    def nval(self):
        e=nval.get('pa')
        print(e)
    def mass(self):
        m=231.036
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class dbA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    def val(self):
        e=val.get('db')
        print(e)
    def nval(self):
        e=nval.get('db')
        print(e)
    def mass(self):
        m=(D*85)+(T*30)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class sA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    def val(self):
        e=val.get('s')
        print(e)
    def nval(self):
        e=nval.get('s')
        print(e)
    def mass(self):
        m=32.066
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class crA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    def val(self):
        e=val.get('cr')
        print(e)
    def nval(self):
        e=nval.get('cr')
        print(e)
    def mass(self):
        m=51.9961
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class seA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    def val(self):
        e=val.get('se')
        print(e)
    def nval(self):
        e=nval.get('se')
        print(e)
    def mass(self):
        m=78.96
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class moA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    def val(self):
        e=val.get('mo')
        print(e)
    def nval(self):
        e=nval.get('mo')
        print(e)
    def mass(self):
        m=95.94
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class tcA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    def val(self):
        e=val.get('tc')
        print(e)
    def nval(self):
        e=nval.get('tc')
        print(e)
    def mass(self):
        m=(D*19)+(T*20)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class ruA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    def val(self):
        e=val.get('ru')
        print(e)
    def nval(self):
        e=nval.get('ru')
        print(e)
    def mass(self):
        m=101.07
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class rhA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    def val(self):
        e=val.get('rh')
        print(e)
    def nval(self):
        e=nval.get('rh')
        print(e)
    def mass(self):
        m=102.906
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class teA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    def val(self):
        e=val.get('te')
        print(e)
    def nval(self):
        e=nval.get('te')
        print(e)
    def mass(self):
        m=127.60
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class xeA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    def val(self):
        e=val.get('xe')
        print(e)
    def nval(self):
        e=nval.get('xe')
        print(e)
    def mass(self):
        m=131.29
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class wA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    def val(self):
        e=val.get('w')
        print(e)
    def nval(self):
        e=nval.get('w')
        print(e)
    def mass(self):
        m=183.84
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class osA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    def val(self):
        e=val.get('os')
        print(e)
    def nval(self):
        e=nval.get('os')
        print(e)
    def mass(self):
        m=190.23
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class irA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    def val(self):
        e=val.get('ir')
        print(e)
    def nval(self):
        e=nval.get('ir')
        print(e)
    def mass(self):
        m=192.22
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class ptA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    def val(self):
        e=val.get('pt')
        print(e)
    def nval(self):
        e=nval.get('pt')
        print(e)
    def mass(self):
        m=195.08
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class poA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    def val(self):
        e=val.get('po')
        print(e)
    def nval(self):
        e=nval.get('po')
        print(e)
    def mass(self):
        m=(D*65)+(T*26)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class rnA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    def val(self):
        e=val.get('rn')
        print(e)
    def nval(self):
        e=nval.get('rn')
        print(e)
    def mass(self):
        m=(D*67)+(T*29)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class uA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    def val(self):
        e=val.get('u')
        print(e)
    def nval(self):
        e=nval.get('u')
        print(e)
    def mass(self):
        m=238.029
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class npA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    def val(self):
        e=val.get('np')
        print(e)
    def nval(self):
        e=nval.get('np')
        print(e)
    def mass(self):
        m=237.048
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class puA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    def val(self):
        e=val.get('pu')
        print(e)
    def nval(self):
        e=nval.get('pu')
        print(e)
    def mass(self):
        m=(D*91)+(T*20)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class sgA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    def val(self):
        e=val.get('sg')
        print(e)
    def nval(self):
        e=nval.get('sg')
        print(e)
    def mass(self):
        m=(D*102)+(T*20)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class cnA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    sixD=True
    SIxd=True
    sIXd=True
    siXD=True
    SIXd=True
    def val(self):
        e=val.get('cn')
        print(e)
    def nval(self):
        e=nval.get('cn')
        print(e)
    def mass(self):
        m=(D*110)+(T*21)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class iA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    def val(self):
        e=val.get('i')
        print(e)
    def nval(self):
        e=nval.get('i')
        print(e)
    def mass(self):
        m=126.904
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class reA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    def val(self):
        e=val.get('re')
        print(e)
    def nval(self):
        e=nval.get('re')
        print(e)
    def mass(self):
        m=186.207
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class atA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    def val(self):
        e=val.get('at')
        print(e)
    def nval(self):
        e=nval.get('at')
        print(e)
    def mass(self):
        m=(D*76)+(T*19)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class bhA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    def val(self):
        e=val.get('bh')
        print(e)
    def nval(self):
        e=nval.get('bh')
        print(e)
    def mass(self):
        m=(D*95)+(T*24)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class hsA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    sixD=True
    def val(self):
        e=val.get('hs')
        print(e)
    def nval(self):
        e=nval.get('hs')
        print(e)
    def mass(self):
        m=(D*96)+(T*25)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class mtA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    sixD=True
    SIxd=True
    def val(self):
        e=val.get('mt')
        print(e)
    def nval(self):
        e=nval.get('mt')
        print(e)
    def mass(self):
        m=(D*94)+(T*26)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class dsA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    sixD=True
    SIxd=True
    sIXd=True
    def val(self):
        e=val.get('ds')
        print(e)
    def nval(self):
        e=nval.get('ds')
        print(e)
    def mass(self):
        m=(D*94)+(T*27)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1
class rgA(world):
    x={'x':0,'y':0,'z':0}
    ONEs= True
    ones=True
    TWOs=True
    twos=True
    TWOp=True
    twop=True
    tWop=True
    Twop=True
    twOp=True
    twoP=True
    THREEs=True
    threes=True
    THREEp=True
    threep=True
    Threep=True
    tHreep=True
    thReep=True
    thrEep=True
    FOURs=True
    fours=True
    THREEd=True
    threed=True
    Threed=True
    tHreed=True
    thReed=True
    thrEed=True
    threEd=True
    threeD=True
    THreed=True
    tHReed=True
    FOURp=True
    fourp=True
    Fourp=True
    fOurp=True
    foUrp=True
    fouRp=True
    FIVEs=True
    fives=True
    FOURd=True
    fourd=True
    Fourd=True
    fOurd=True
    foUrd=True
    fouRd=True
    fourD=True
    FOurd=True
    fOUrd=True
    foURd=True
    FIVEp=True
    fivep=True
    Fivep=True
    fIvep=True
    fiVep=True
    fivEp=True
    SIXs=True
    sixs=True
    FOURf=True
    fourf=True
    Fourf=True
    fOurf=True
    foUrf=True
    fouRf=True
    fourF=True
    FOurf=True
    fOUrf=True
    foURf=True
    fouRF=True
    FOUrf=True
    fOURf=True
    foURF=True
    FIVEd=True
    fived=True
    Fived=True
    fIved=True
    fiVed=True
    fivEd=True
    fiveD=True
    FIved=True
    fIVed=True
    fiVEd=True
    SIXp=True
    sixp=True
    Sixp=True
    sIxp=True
    siXp=True
    sixP=True
    SEVENs=True
    sevens=True
    FIVEf=True
    fivef=True
    Fivef=True
    fIvef=True
    fiVef=True
    fivEf=True
    fiveF=True
    FIvef=True
    fIVef=True
    fiVEf=True
    fivEF=True
    FIVef=True
    fIVEf=True
    fiVEF=True
    SIXd=True
    sixd=True
    Sixd=True
    sIxd=True
    siXd=True
    sixD=True
    SIxd=True
    sIXd=True
    siXD=True
    def val(self):
        e=val.get('rg')
        print(e)
    def nval(self):
        e=nval.get('rg')
        print(e)
    def mass(self):
        m=(D*93)+(T*28)
        x=m/av
        print(m)
        print(x)
    def right(self):
        self.x['x']+=1
    def left(self):
        self.x['x']-=1
    def up(self):
        self.x['y']+=1
    def down(self):
        self.x['y']-=1
    def forward(self):
        self.x['z']+=1
    def backward(self):
        self.x['z']-=1

def E(object):
    e=0
    v=True
    l=[object.sevEnp,object.seVenp,object.sEvenp,object.Sevenp,object.sevenp,object.SEVENp,object.SIXd,object.siXD,object.sIXd,object.SIxd,object.sixD,object.siXd,object.sIxd,object.Sixd,object.sixd,object.SIXd,object.fiVEF,object.fIVEf,object.FIVef,object.fivEF,object.fiVEf,object.fIVef,object.FIvef,object.fiveF,object.fivEf,object.fiVef,object.fIvef,object.Fivef,object.fivef,object.FIVEf,object.sevens,object.SEVENs,object.sixP,object.siXp,object.sIxp,object.Sixp,object.sixp,object.SIXp,object.fiVEd,object.fIVed,object.FIved,object.fiveD,object.fivEd,object.fiVed,object.fIved,object.Fived,object.fived,object.FIVEd,object.foURF,object.fOURf,object.FOUrf,object.fouRF,object.foURf,object.fOUrf,object.FOurf,object.fourF,object.fouRf,object.foUrf,object.fOurf,object.Fourf,object.fourf,object.FOURf,object.sixs,object.SIXs,object.fivEp,object.fiVep,object.fIvep,object.Fivep,object.fivep,object.FIVEp,object.foURd,object.fOUrd,object.FOurd,object.fourD,object.fouRd,object.foUrd,object.fOurd,object.Fourd,object.fourd,object.FOURd,object.fives,object.FIVEs,object.fouRp,object.foUrp,object.fOurp,object.Fourp,object.fourp,object.FOURp,object.tHReed,object.THreed,object.threeD,object.threEd,object.thrEed,object.thReed,object.tHreed,object.Threed,object.threed,object.THREEd,object.fours,object.FOURs,object.thrEep,object.thReep,object.tHreep,object.Threep,object.threep,object.THREEp,object.threes,object.THREEs,object.twoP,object.twOp,object.Twop,object.tWop,object.twop,object.TWOp,object.twos,object.TWOs,object.ones,object.ONEs]
    for v in l:
        e+=1
        print(e)
def e(object):
    e=0
    Ee=0
    
    z=0
    s=2
    p=6
    d=10
    f=14
    A=18
    B=22
    C=26
    D=30
    E=34
    F=38
    b=float(1)
    Co=0
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    s6=0
    s7=0
    s8=0
    s9=0
    ##this counts electrons and keeps track of current shell
    if object.ONEs==True:
        e+=b
        
    if object.ones==True:
        e+=b
        s1+=1
        
    if object.TWOs==True:
        e+=b
    if object.twos==True:
        e+=b
    if object.TWOp==True:
        e+=b
    if object.twop==True:
        e+=b
    if object.Twop==True:
        e+=b
    if object.tWop==True:
        e+=b
    if object.twOp==True:
        e+=b
    if object.twoP==True:
        e+=b
        s2+=1
        s1-=1
    if object.THREEs==True:
        e+=b
    if object.threes==True:
        e+=b
    if object.THREEp==True:
        e+=b
    if object.threep==True:
        e+=b
    if object.Threep==True:
        e+=b
    if object.tHreep==True:
        e+=b
    if object.thReep==True:
        e+=b
    if object.thrEep==True:
        e+=b
    if object.FOURs==True:
        e+=b
    if object.fours==True:
        e+=b
        Ee+=2
    if object.THREEd==True:
        e+=b
    if object.threed==True:
        e+=b
    if object.Threed==True:
        e+=b
    if object.tHreed==True:
        e+=b
    if object.thReed==True:
        e+=b
    if object.thrEed==True:
        e+=b
    if object.threEd==True:
        e+=b
    if object.threeD==True:
        e+=b
    if object.THreed==True:
        e+=b
    if object.tHReed==True:
        e+=b
        s3+=1
        s2-=1
        Ee-=2
    if object.FOURp==True:
        e+=b
    if object.fourp==True:
        e+=b
    if object.Fourp==True:
        e+=b
    if object.fOurp==True:
        e+=b
    if object.foUrp==True:
        e+=b
    if object.fouRp==True:
        e+=b
    if object.FIVEs==True:
        e+=b
    if object.fives==True:
        e+=b
        Ee+=2
    if object.FOURd==True:
        e+=b
    if object.fourd==True:
        e+=b
    if object.Fourd==True:
        e+=b
    if object.fOurd==True:
        e+=b
    if object.foUrd==True:
        e+=b
    if object.fouRd==True:
        e+=b
    if object.fourD==True:
        e+=b
    if object.FOurd==True:
        e+=b
    if object.fOUrd==True:
        e+=b
    if object.foURd==True:
        e+=b
    if object.FIVEp==True:
        e+=b
    if object.fivep==True:
        e+=b
    if object.Fivep==True:
        e+=b
    if object.fIvep==True:
        e+=b
    if object.fiVep==True:
        e+=b
    if object.fivEp==True:
        e+=b
    if object.SIXs==True:
        e+=b
    if object.sixs==True:
        e+=b
    if object.FOURf==True:
        e+=b
    if object.fourf==True:
        e+=b
    if object.Fourf==True:
        e+=b
    if object.fOurf==True:
        e+=b
    if object.foUrf==True:
        e+=b
    if object.fouRf==True:
        e+=b
    if object.fourF==True:
        e+=b
    if object.FOurf==True:
        e+=b
    if object.fOUrf==True:
        e+=b
    if object.foURf==True:
        e+=b
    if object.fouRF==True:
        e+=b
    if object.FOUrf==True:
        e+=b
    if object.fOURf==True:
        e+=b
    if object.foURF==True:
        e+=b
        s4+=1
        s3-=1
        Ee+=2
    if object.FIVEd==True:
        e+=b
    if object.fived==True:
        e+=b
    if object.Fived==True:
        e+=b
    if object.fIved==True:
        e+=b
    if object.fiVed==True:
        e+=b
    if object.fivEd==True:
        e+=b
    if object.fiveD==True:
        e+=b
    if object.FIved==True:
        e+=b
    if object.fIVed==True:
        e+=b
    if object.fiVEd==True:
        e+=b
    if object.SIXp==True:
        e+=b
    if object.sixp==True:
        e+=b
    if object.Sixp==True:
        e+=b
    if object.sIxp==True:
        e+=b
    if object.siXp==True:
        e+=b
    if object.sixP==True:
        e+=b
    if object.SEVENs==True:
        e+=b
    if object.sevens==True:
        e+=b
    if object.FIVEf==True:
        e+=b
    if object.fivef==True:
        e+=b
    if object.Fivef==True:
        e+=b
    if object.fIvef==True:
        e+=b
    if object.fiVef==True:
        e+=b
    if object.fivEf==True:
        e+=b
    if object.fiveF==True:
        e+=b
    if object.FIvef==True:
        e+=b
    if object.fIVef==True:
        e+=b
    if object.fiVEf==True:
        e+=b
    if object.fivEF==True:
        e+=b
    if object.FIVef==True:
        e+=b
    if object.fIVEf==True:
        e+=b
    if object.fiVEF==True:
        e+=b
    if object.SIXd==True:
        e+=b
    if object.sixd==True:
        e+=b
    if object.Sixd==True:
        e+=b
    if object.sIxd==True:
        e+=b
    if object.siXd==True:
        e+=b
    if object.sixD==True:
        e+=b
    if object.SIxd==True:
        e+=b
    if object.sIXd==True:
        e+=b
    if object.siXD==True:
        e+=b
    if object.SIXd==True:
        e+=b
    if object.SEVENp==True:
        e+=b
    if object.sevenp==True:
        e+=b
    if object.Sevenp==True:
        e+=b
    if object.sEvenp==True:
        e+=b
    if object.seVenp==True:
        e+=b
    if object.sevEnp==True:
        e+=b
    ##past orbitals in all shells
    Ps=0
    if e in range(0,2):
        Ps=0
    elif e in range(2,4):
        Ps=2
    elif e in range(4,10):
        Ps=4
    elif e in range(10,12):
        Ps=10
    elif e in range(12,18):
        Ps=12
    elif e in range(18,20):
        Ps=18
    elif e in range(20,30):
        Ps=20
    elif e in range(30,36):
        Ps=30
    elif e in range(36,38):
        Ps=36
    elif e in range(38,48):
        Ps=38
    elif e in range(48,54):
        Ps=48
    elif e in range(54,56):
        Ps=54
    elif e in range(56,70):
        Ps=56
    elif e in range(70,80):
        Ps=70
    elif e in range(80,86):
        Ps=80
    elif e in range(86,88):
        Ps=86
    elif e in range(88,102):
        Ps=88
    elif e in range(102,112):
        Ps=102
    elif e in range(112,118):
        Ps=112
    elif e in range(118,120):
        Ps=118
    elif e in range(120,138):
        Ps=120
    elif e in range(138,152):
        Ps=138
    elif e in range(152,162):
        Ps=152
    elif e in range(162,168):
        Ps=162
    elif e in range(168,170):
        Ps=168
    elif e in range(170,188):
        Ps=170
    elif e in range(188,202):
        Ps=188
    elif e in range(202,212):
        Ps=202
    ##previous full shells
    Fs=0
    if e in range(0,2):
        Fs=0
    elif e in range(2,4):
        Fs=2
    elif e in range(4,10):
        Fs=2
    elif e in range(10,12):
        Fs=10
    elif e in range(12,18):
        Fs=10
    elif e in range(18,20):
        Fs=10
    elif e in range(20,30):
        Fs=10
    elif e in range(30,36):
        Fs=28
    elif e in range(36,38):
        Fs=28
    elif e in range(38,48):
        Fs=28
    elif e in range(48,54):
        Fs=28
    elif e in range(54,56):
        Fs=28
    elif e in range(56,70):
        Fs=28
    elif e in range(70,80):
        Fs=60   
    elif e in range(80,86):
        Fs=60
    elif e in range(86,88):
        Fs=60
    elif e in range(88,102):
        Fs=60
    elif e in range(102,112):
        Fs=60
    elif e in range(112,118):
        Fs=60
    elif e in range(118,120):
        Fs=60
    elif e in range(120,138):
        Fs=60
    elif e in range(138,152):
        Fs=110
    elif e in range(152,162):
        Fs=110
    elif e in range(162,168):
        Fs=110
    elif e in range(168,170):
        Fs=110
    elif e in range(170,188):
        Fs=110
    elif e in range(188,202):
        Fs=110
    elif e in range(202,212):
        Fs=110
    ##current orbital
    if e in range(1,2):
        Co=s
    elif e in range(3,4):
        Co=s
    elif e in range(5,10):
        Co=p
    elif e in range(11,12):
        Co=s
    elif e in range(13,18):
        Co=p
    elif e in range(19,20):
        Co=s
    elif e in range(21,30):
        Co=d
    elif e in range(31,36):
        Co=p
    elif e in range(37,38):
        Co=s
    elif e in range(39,48):
        Co=d
    elif e in range(49,54):
        Co=p
    elif e in range(55,56):
        Co=s
    elif e in range(57,70):
        Co=f
    elif e in range(71,80):
        Co=d
    elif e in range(81,86):
        Co=p
    elif e in range(87,88):
        Co=s
    elif e in range(89,102):
        Co=f
    elif e in range(103,112):
        Co=d
    elif e in range(113,118):
        Co=p
    elif e in range(119,120):
        Co=s
    elif e in range(121,138):
        Co=A
    elif e in range(139,152):
        Co=f
    elif e in range(153,162):
        Co=d
    elif e in range(163,168):
        Co=p
    elif e in range(169,170):
        Co=s
    elif e in range(171,188):
        Co=A
    ##shell capacity
    ONE=s
    TWO=s+p
    THREE=s+p+d
    FOUR=s+p+d+f
    FIVE=s+p+d+f+A
    SIX=s+p+d+f+A+B
    SEVEN=s+p+d+f+A+B+C
    EIGHT=s+p+d+f+A+B+C+E
    NINE=s+p+d+f+A+B+C+E+F
    ##which shell
    shell=0
    if e<=2:
        shell=1
    elif e<=10:
        shell=2
    elif e<=18:
        shell=3
    elif e<=36:
        shell=4
    elif e<=54:
        shell=5
    elif e<=86:
        shell=6
    elif e<=118:
        shell=7
    elif e<=168:
        shell=8
    ##what is the capacity total for current shell
    Ct=0
    if shell==1:
        Ct=ONE
    elif shell==2:
        Ct=TWO
    elif shell==3:
        Ct=THREE
    elif shell==4:
        Ct=FOUR
    elif shell==5:
        Ct=FIVE
    elif shell==6:
        Ct=SIX
    elif shell==7:
        Ct=SEVEN
    elif shell==8:
        Ct=EIGHT
    ##what is the next orbital
    nO=0
    if e in range(1,2):
        nO=s
    elif e in range(3,4):
        nO=p
    elif e in range(5,10):
        nO=s
    elif e in range(11,12):
        nO=p
    elif e in range(13,18):
        nO=s
    elif e in range(19,20):
        nO=d
    elif e in range(21,30):
        nO=p
    elif e in range(31,36):
        nO=s
    elif e in range(37,38):
        nO=d
    elif e in range(39,48):
        nO=p
    elif e in range(49,54):
        nO=s
    elif e in range(55,56):
        nO=f
    elif e in range(57,70):
        nO=d
    elif e in range(71,80):
        nO=p
    elif e in range(81,86):
        nO=s
    elif e in range(87,88):
        nO=f
    elif e in range(89,102):
        nO=d
    elif e in range(103,112):
        nO=p
    elif e in range(113,118):
        nO=s
    elif e in range(119,120):
        nO=A
    elif e in range(121,138):
        nO=f
    elif e in range(139,152):
        nO=d
    elif e in range(153,162):
        nO=p
    elif e in range(163,168):
        nO=s
    elif e in range(169,170):
        nO=A
    elif e in range(171,188):
        nO=f
    V=e-Ps
    v=e-Fs
    B=Co-V
    ##for when e == Ps
    if V==0:
        if s1==1:
            V=e-ONE
        elif s2==1:
            V=e-TWO
        elif s3==1:
            V=e-THREE
        elif s4==1:
            V=e-FOUR
        elif s5==1:
            V=e-FIVE
        elif s6==1:
            V=e-SIX
        elif s7==1:
            V=e-SEVEN
        elif s8==1:
            V=e-EIGHT
        elif s9==1:
            V=e-NINE
    ve=V-v
    Es=Ct-v
    Be=(Co-B)+Ee
    

    print('This applies to all Atoms')
    print(e,'Total electrons')
    print(V,'Outer most orbital Valence electrons')
    print(B,'/',Co,'Bonds free')
    print(v,'Shell Valence electrons')
##these only seem to apply to atoms with empty lower level orbitals. it's wierd i know.
    print('This applies where ever above doesnt work., strangely...')
    print(ve,'extra electrons. -ve is irrelevant.')
    print(Es,'shell empty space')
    print(Be,'Bonding electrons')


## This section is for calculateing values from chemistry formulas.Still need to add heaps off stuff here....
def Hfenthalpyreaction():
    
    A=float(input('standard enthalpy A?'))
    B=float(input('standard enthalpy B?'))
    C=float(input('standard enthalpy C?'))
    D=float(input('standard enthalpy D?'))
    a=int(input('amount a?'))
    b=int(input('amount b?'))
    c=int(input('amount c?'))
    d=int(input('amount d?'))
    H=((c*C)+(d*D))-((a*A)+ (b*B))
    print(H,'kJ mol**-1')
def Hformationenthalpybi():
    A=float(input('coefficient of reaction 1?'))
    B=float(input('coefficient of reaction 2?'))
    C=float(input('coefficient of reaction 3?'))
    Ha=float(input('standard enthalpy of reaction 1?'))
    Hb=float(input('standard enthalpy of reaction 2?'))
    Hc=float(input('standard enthalpy of reaction 3?  -Hat'))
    Hf=(Hc*C)+(Hb*B)+(Ha*A)
    print(Hf,'KJ mol-1')


    
def Hatomizationbi():
    A=float(input('coefficient of atom a?'))
    B=float(input('coefficient of atom b?'))
    C=float(input('coefficient of atom c?'))
    Hfa=float(input('formation enthalpy of atom a?'))
    Hfb=float(input('formation enthalpy of atom b?'))
    Hfc=float(input('formation enthalpy of substance c?'))
    Hat=(Hfa*A)+(Hfb*B)-(Hfc*C)
    print(Hat,'KJ mol-1')
def Hatomizationtri():
    A=float(input('coefficient of atom a?'))
    B=float(input('coefficient of atom b?'))    
    D=float(input('coefficient of atom c?'))
    Hfa=float(input('formation enthalpy of atom a?'))
    Hfb=float(input('formation enthalpy of atom b?'))
    Hfd=float(input('formation enthalpy of atom c?'))
    Hfc=float(input('formation enthalpy of substance d?'))
    C=float(input('coefficient of substance d?'))
    Hat=(Hfa*A)+(Hfb*B)+(Hfd*D)-(Hfc*C)
    print(Hat,'KJ mol-1')    
def bondenthalpy():
    A=float(input('coefficient of atom a?'))
    B=float(input('coefficient of atom b?'))
    C=float(input('coefficient of atom c?'))
    Hfa=float(input('formation enthalpy of atom a?'))
    Hfb=float(input('formation enthalpy of atom b?'))
    Hfc=float(input('formation enthalpy of substance c?'))
    Hat=(Hfa*A)+(Hfb*B)-(Hfc*C)
    no=float(input('number of bonds?'))
    be=Hat/no
    print(be,'KJ mol-1')
def qheat():
    c=float(input('specific heat?'))
    m=float(input('mass of substance?'))
    T=float(input('change in temperature?'))
    q=c*m*T
    print(q,'J')
def qheatCT():
    C=float(input('heat capacity?'))
    T=float(input('temperature change?'))
    q=C*T
    
    
def tempchange():
    f=float(input('final temperature?'))
    i=float(input('initial temperature?'))
    T=f-i
    print(T,'K')
def Cheatcapacity():
    q=float(input('heat?'))
    T=float(input('temperature change?'))
    C=q/T
    print(C,'JK**-1')
def cspecificheat():
    C=float(input('heat capacity?'))
    m=float(input('mass?'))
    c=C/m
    print(c,'J')
def Uinternalenergydiff():
    f=float(input('final internal energy?'))
    i=float(input('initial internal energy?'))
    U=f-i
    print(U)
def Ureaction():
    p=float(input('internal energy of products?'))
    r=float(input('internal energy of reactants?'))
    U=p-r
    print(U)
def wwork():
    p=float(input('pressure?'))
    f=float(input('final volume?'))
    i=float(input('initial volume?'))
    vchange=f-i
    w=-p*vchange
    print(w)
def Uchange():
    q=float(input('heat?'))
    w=float(input('work?'))
    U=q+w
    print(U)
def Uchange1():
    qp=float(input('heat at constant pressure?'))
    p=float(input('pressure?'))
    Vf=float(input('final volume?'))
    Vi=float(input('initial volume?'))         
    V=Vf-Vi
    U=qp-p*V
    print(U)
def Henthalpy():
    U=float(input('internal energy?'))
    p=float(input('pressure?'))
    V=float(input('volume?'))
    H=U+(p*V)
    print(H)

def Henthalpychange():
    f=float(input('final internal energy?'))
    i-float(input('initial internal energy?'))
    U=f-i
    F=float(input('final volume?'))
    I=float(input('initial volume?'))
    V=F-I
    p=float(input('at constant pressure?'))
    H=U+(p*V)
    print(H)

def mass():
    d=float(input('density?'))
    v=float(input('volume?'))
    m=d*v
    print(m)
def density():
    m=float(input('mass?'))
    V=float(input('volume?'))
    p=m/V
    print(p)
def amount():
    c=float(input('Mol concentration L?'))
    V=float(input('volume of liquid L?'))
    n=c*V
    print(n,'mol')
def molarity():
    print('concentration')
    n=float(input('amount?mols'))
    V=float(input('Volume?L'))
    c=n/V
    print(c)
def molarmass():
    m=float(input('mass of substance?grams'))
    n=float(input('amount of substance?mol-1'))
    M=m/n
def solubility():
    m=float(input('mass of substance g per L?'))
    M=float(input('mass of molecule g mol-1?'))
    n=(m)/(M)
    print(n,'mol L-1')
def kH():
    cgas=float(input('solubility per L?'))
    pgas=float(input('partial pressure?'))
    kH=(cgas)/(pgas)
    print(kH,'mol L-1 Pa-1')
def cgas():
    kH=float(input('kH value henrys constant?'))
    pgas=float(input('partial pressure of gas?'))
    cgas=(kH)*(pgas)
    print(cgas,'mol L-1')
def Amount():
    m=float(input('solubility?'))
    M=float(input('mass of molecule g mol-1?'))
    n=(m)/(M)
    print(n,'mol')
def molality():
    a=float(input('amount of solute?mol'))
    m=float(input('mass of solvent?kg'))
    b=a/m
    print(b)
def ksp():
    M=float(input('amount of A?'))
    X=float(input('amount of B?'))
    a=float(input('coefficient of A?'))
    b=float(input('coefficient of B?'))
    ksp=((M)**a)*((X)**b)
    print(ksp)
def pH():
    log=math.log
    A=float(input('conj.base molar concentration?'))
    HA=float(input('conj.acid molar concentration?'))
    pKa=float(input('pKa?'))
    pH=pKa + log((A)/(HA)) 
    print(pH)
#acidity constant
def Ka():
    HthreeO=float(input('aqueous acid concentration?'))
    A=float(input('-acid ion concentration?'))
    HA=float(input('initial acid concentration?'))
    Ka=(HthreeO)*(A)/(HA)
    print(Ka)
def HA():
    HthreeO=float(input('aqueous acid concentration?'))
    A=float(input('-acid ion concentration?'))
    ka=float(input('Ka value?'))
    HA=((HthreeO)*(A))/ka
    print(HA)
def H3O():
    HA=float(input('initial acid concentration?'))
    ka=float(input('Ka value?'))
    A=float(input('-acid ion concentration?'))
    HthreeO=((HA)*(ka))/A
    print(HthreeO)
def A():
    HA=float(input('initial acid concentration?'))
    ka=float(input('Ka value?'))
    HthreeO=float(input('aqueous acid concentration?'))
    A=((HA)*(ka))/HthreeO
    print(A)
#base constants
def Kb():
    BH=float(input('aqueous base concentration?'))
    OH=float(input('-base ion concentration?'))
    B=float(input('initial base concentration?'))
    Kb=(BH)*(OH)/(B)
    print(Kb)
def B():
    BH=float(input('aqueous base concentration?'))
    OH=float(input('-base ion concentration?'))
    kb=float(input('Ka value?'))
    B=((BH)*(OH))/kb
    print(B)
def BH():
    B=float(input('initial base concentration?'))
    kb=float(input('Ka value?'))
    OH=float(input('-base ion concentration?'))
    BH=((B)*(kb))/OH
    print(BH)
def OH():
    B=float(input('initial base concentration?'))
    kb=float(input('Ka value?'))
    BH=float(input('aqueous base concentration?'))
    OH=((B)*(kb))/BH
    print(OH)
##pKa
def pKa():
    Ka=float(input('Ka value?'))
    pKa=-log10((Ka))
    print(pKa)
def pKb():
    Kb=float(input('Kb value?'))
    pKb=-log10((Kb))
    print(pKb)
##reaction rates arhenius
def krate():
    z=float(input('collision frequency?  collisions per second'))
    p=float(input('steric factor;fraction of collisions with correct orientations?'))
    e=float(input('fraction of collisions with sufficient energy?'))
    Ea=float(input('activation energy? J mol-1'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('temperature? K'))
    k=z*p*e**(-Ea/(R*T))
    print(k)
def Krate():    
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    e=float(input('fraction of collisions with sufficient energy?'))
    Ea=float(input('activation energy? J mol-1'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('temperature? K'))
    k=A*e**(-Ea/(R*T))
    print(k)
def Arhen():
    print('pre-exponential/frequency factor')
    k=float(input('k rate value?'))
    e=float(input('fraction of collisions with sufficient energy?'))
    Ea=float(input('activation energy? J mol-1'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('temperature? K'))
    A=k/e**(-(Ea/R*T))
    print(A)
def ecol():
    print('natural logarithm of the fraction of collisions with sufficient energy')
    k=float(input('k rate value?'))
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    Ea=float(input('activation energy? J mol-1'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('temperature? K'))
    lne=(log(k/A))/(-(Ea)/(R*T))
    print(lne)
def nEa():
    print('negative activation energy')
    k=float(input('k rate value?'))
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    e=float(input('fraction of collisions with sufficient energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('temperature? K'))    
    nEa=(log(k/A)/log(e))/(R*T)
    print(nEa)
def Lnk():
    Ea=float(input('activation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=float(input('Temperature?'))
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    lnk=-((Ea)/(R))*((1)/(T))+log(A)
    print(lnk)
def Temp():
    Ea=float(input('activation energy? J mol-1'))
    k=float(input('k rate value?'))
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    e=float(input('fraction of collisions with sufficient energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    T=((1/-Ea)/(log(k/A)/log(e)))/R
    print(T)
def Rconst():
    print('this can check accuracy.if ~= 8.314 J mol-1 K-1 then the inputed values are correct')
    Ea=float(input('activation energy? J mol-1'))
    k=float(input('k rate value?'))
    A=float(input('pre-exponential/frequency factor? "z times p for krate"'))
    e=float(input('fraction of collisions with sufficient energy?'))
    T=float(input('temperature? K'))
    R=((1/-Ea)/(log(k/A)/log(e)))/(T)
    print(R)
##this is also correct
def Rconst2():
    print('this can check accuracy.if ~= 8.314 J mol-1 K-1 then the inputed values are correct')
    ktwo=float(input('k2 rate value?'))
    kone=float(input('k1 rate value?'))
    Ttwo=float(input('temperature 2? K'))
    Tone=float(input('temperature 1? K'))
    Ea=float(input('activation energy? J mol-1'))
    R=-(1/(log(ktwo/kone)/((1/Ttwo)-(1/Tone))))*(Ea)
    print(R)
    
def lnk():
    k=float(input('k value?'))
    lnk=log(k)
    print(lnk)
def Tempreci():
    T=float(input('temperature? in Kelvin'))
    tempreci=1/T
    print(tempreci)
def slope():
    difflnk=float(input('difference in lnk values?'))
    difftempreci=float(input('difference in temperature reciprocal?'))
    slope=difflnk/difftempreci
    print(slope,'K')
def Ea():
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    slope=float(input('inverted slope value? "switch positive slope values to negative and vice versa"'))
    Ea=(R)*(slope)
    print(Ea,'joules')
##natural logs k1 & k2
def lnk2Ovak1():
    print('for rate at temperature , and rate at another temperature')
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ttwo=float(input('temperature two?K'))
    Tone=float(input('temperature one?K'))
    lnktwoOvakone=-((Ea)/(R))*(((1)/(Ttwo))-((1)/(Tone)))
    print(lnktwoOvakone,'natural logarithm of ktwo/kone')
def lnk2():
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ttwo=float(input('temperature two?K'))
    Tone=float(input('temperature one?K'))
    kone=float(input('1st k value?'))
    lnktwo=-(Ea/R)*((1/Ttwo)-(1/Tone))+log(kone)
    print(lnktwo)
def lnk1():
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ttwo=float(input('temperature two?K'))
    Tone=float(input('temperature one?K'))
    ktwo=float(input('2nd k value?'))
    lnkone=(Ea/R)*((1/Ttwo)-(1/Tone))+log(ktwo)
    print(lnkone)

def T2():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Tone=float(input('temperature one?K'))
    Ttwo=(1/(log(ktwo)-log(kone)/-(Ea/R)))+Tone
    print(Ttwo)
def T1():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ttwo=float(input('temperature two?K'))
    Tone=(1/(-log(ktwo)-log(kone)/-(Ea/R)))+Ttwo
    print(Tone)
##These are the same for some strange reason but both true
def Ea3():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ttwo=float(input('2nd temperature?'))
    Tone=float(input('1st temperature?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ea=(-log((ktwo)/(kone)))/(((1)/(Ttwo))-((1)/(Tone)))*(R)
    print(Ea,'joules')
def Ea5():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ttwo=float(input('2nd temperature?'))
    Tone=float(input('1st temperature?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ea=(1/-(1/(log(ktwo/kone)/((1/Ttwo)-(1/Tone)))))*(R)
    print(Ea)
##Accuracy rating? could be useless
def R():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ea=float(input('acitvation energy?'))
    Ttwo=float(input('temperature two?K'))
    Tone=float(input('temperature one?K'))
    R=((-log(ktwo/kone))/(Ea))/((1/Ttwo)-(1/Tone))
    print(R)
def One():
    ktwo=float(input('2nd k value?'))
    kone=float(input('1st k value?'))
    Ea=float(input('acitvation energy?'))
    R=float(input('R gas constant? hint.. 8.314 J mol-1 K-1'))
    Ttwo=float(input('temperature two?K'))
    Tone=float(input('temperature one?K'))
    one=(log(ktwo/kone)/-(Ea/R))*(Ttwo)+(1/Tone)
    print(one)
