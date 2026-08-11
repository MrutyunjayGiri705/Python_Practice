for i in range(2, 101):   
    coun = 0              
    for j in range(2, i): 
        if i % j == 0:
            coun += 1
    if coun == 0:         
        print(i)
