#quick_multiplier

doubler = lambda x: x * 2
print(doubler(12))

tripler = lambda x: x * 3
print(tripler(12))

def multiplier(y):
    return lambda x: x*y

times4 = multiplier(4)
times5 = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 =  multiplier(9)
times10 =  multiplier(10)
print(times4(5))
print(times5(5))
print(times6(5))
print(times7(5))
print(times8(5))
print(times9(5))
print(times10(5))
      