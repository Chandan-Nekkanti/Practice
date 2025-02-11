import random


def ran_func(x,y):
    u1 = random.randint(1,6)
    u2 =  random.randint(1,6)
    u3 =  random.randint(1,6)
    u4 =  random.randint(1,6)
    a = u1 + u2
    print(x + "'s"+" score: "+str(a))
    b = u3 + u4
    print(y + "'s"+" score: "+str(b))
    if a > b:
        print(x+" wins!")
    else:
        print(y+" wins!")


