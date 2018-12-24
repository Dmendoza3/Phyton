def fizzbuzz(num):
    for i in range(1, num):
        string = ""
        if(i % 3 == 0):
            string = string + "fizz"
        if(i % 5 == 0):
            string = string + "buzz"
        if(string != ""):
            print(string, end = " ")
        else:
            print(i, end = " ")
    
fizzbuzz(16)
        