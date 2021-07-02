def return_even() :
    int_list = []
    
    for i in range(0,50):
        if (i+1) % 2 == 0 :
            int_list.append(i+1)
            
    return int_list
