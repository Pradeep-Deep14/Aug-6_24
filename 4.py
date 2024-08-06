def mystery(x): 
    x[0] = x 
    x = [1, 2, 3]  
    print(x == x[0])

my_list=[0]
mystery(my_list)