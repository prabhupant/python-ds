def prime(limit):
    
    count = 1
    while (count < limit):

        flag = 0
        for i in range(3, count, 2):
            if (count % i == 0):
                flag = 1

        if (flag == 0):
            print(count)
            
        count += 2

prime(100)
