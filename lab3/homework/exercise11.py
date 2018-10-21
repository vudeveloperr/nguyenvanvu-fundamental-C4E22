def is_inside( x , y , a , b , c , d ):
    q = a+c
    p = b+d
    if a <= x & x <= q & b <= y & y <= p :
        print("inside retangle")

    else :
        print("not inside retangle")
        
x = int(input("nhập hoành độ của điểm cần xét : "))
y = int(input("nhập tung độ của điểm cần xét : "))
a = int(input("nhập hoành độ của điểm đầu : "))
b = int(input("nhập tung độ của điểm đầu : "))
c = int(input("nhập chiều rộng hcn : "))
d = int(input("nhập chiều dài hcn : "))        
is_inside(x , y , a , b , c , d )


