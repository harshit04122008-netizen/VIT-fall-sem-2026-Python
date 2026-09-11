N = int(input())
a , b , c = map(int,input().split())

D = (b**2) - (4*a*c)

if D > 0 :

    ans1 = (-b + (D**(1/2)))/(2*a)
    ans2 = (-b - (D**(1/2)))/(2*a)
    
    T = (ans1,ans2)
    print(T)

elif D == 0:

    ans1 = (-b)/(2*a)
    T = (ans1,ans1)

else:

    i1 = (-b + (D**(1/2)))/(2*a)
    i2 = (-b - (D**(1/2)))/(2*a)

    print(((float(round(i1.real)),i1.imag),(float(round(i2.real)),i2.imag)))