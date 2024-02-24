chuoikq = ""
nhac = input("Nhập thể loại nhạc yêu thích ( dừng lại ấn phím 0): ")

while nhac != "0" :
    chuoikq +=   nhac + ","
    nhac = input("Nhập thể loại nhạc yêu thích ( dừng lại ấn phím 0): ")
chuoikq = chuoikq[:-1]

print ("Các thể loại nhạc bạn yêu thích: ", chuoikq)
    
#demo điền chuỗi liên tiếp, dừng lại nằm trong input của đoạn nhập
