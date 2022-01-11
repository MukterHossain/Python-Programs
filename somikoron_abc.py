a = int(input('type a : '))
b = int(input('type b : '))
c = int(input('type c : '))
d = b*2-4*a*c
if d>0:
    x1= (-b+d*0.5)/2*a
    x2= (-b-d*0.5)/2*a
    print(x1,x2)
else:
    if d <= 0:
        x = int(-b/2*a)
        print(x)
    else:
        print('type a number')

    

