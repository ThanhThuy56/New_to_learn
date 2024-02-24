# S = (x^2 +1)^n

n = int(input('Nhập n: '))
x = eval(input('Nhập x: '))

if n==0 :
    S = 1
else:
    S = 1
    for i in range (0,n):
        S = S * (x * x + 1 )
        #S *= (x * x + 1)
        
print (S)
 