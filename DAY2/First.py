def outer():
    name="Sabbir"
    def inner():
        nonlocal name # nonlocal is used to change the value of the variable of the outer function
        print(name)
        name="Alam"
        return name
    name = inner()  
    print(name) 
    # def inner(name):
    #     print(name)
    #     name="Alam"
    #     return name
    # name = inner(name)  
    # print(name)
    
    
outer()