class Vars():
    def __init__(self):
        self.i = 42
        self.s = '42'
        self.s2 = 'quarante-deux'
        self.f = 42.0
        self.b = True
        self.l = [42]
        self.d = {42: 42}
        self.t = (42,)
        self.se = set()

def my_var():
    var = Vars()
    for v in var.__dict__.items():
        print(f'{v[1]} est de type {type(v[1])}')

if __name__ == '__main__':
    my_var()