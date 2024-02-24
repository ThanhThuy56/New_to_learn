

# if x <= 1:
#     print("%d KHÔNG là số nto" %x)
# else:
#     j =2
#     while x % j != 0:
#         j += 1
    
#     if j == x:
#         print("%d là số nto" %x)
#     else:
#         print("%d là KHÔNG số nto" %x)

def check_so_nto(x):

    count = 0

    for i in range(1,x+1):
        if x%i==0:
            count += 1

    if count ==2:
        return True
        
    else:
        return False
 
x = eval (input("Nhập số cần ktra : "))        
check_so = check_so_nto(x)
print(check_so)
    