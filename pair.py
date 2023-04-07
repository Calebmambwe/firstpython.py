def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(a, b):
    def pair2(f):
        return f(a)
    return pair2


def cdr(a,b):
    def pair3(f):
        return f(b)
    return pair3