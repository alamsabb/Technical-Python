def generator_fun():
    yield "yield"
    yield "Keyword"
    yield "in"
    yield "Python"
    
generator_object = generator_fun()
print(type(generator_object))
for i in generator_object:
    print(i)
print(generator_object)