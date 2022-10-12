def numbers():
    f = open('numbers.txt', 'r')
    for l in f:
        for n in l.split(','):
            print(n)
    f.close()

if __name__ == '__main__':
    numbers()