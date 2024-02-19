try:
    raise ArithmeticError("error")
except ArithmeticError as e:
    print(e)
    