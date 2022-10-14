import os
import sys 

def render(template, settings):
    for s in settings:
        key = s.split('=')[0].strip()
        value = s.split('=')[1].strip()
        if value[0] == value[-1] and (value[0] == "'" or value[0] == '"'):
            value = value[1:-1]
        for l in template:
            l.format(name=key)
    print(template)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.template') and os.path.isfile('settings.py') and os.path.isfile(sys.argv[1]):
            settings = open('settings.py', 'r')
            template = open(sys.argv[1], 'r')
            if not settings or not template:
                if not settings:
                    print('cant open settings.py file')
                if not template:
                    print('cant open template file')
            else:
                render(template, settings)
        else:
            print('need a settings.py file at root and a .template file as argument')
    else:
        print('bad argument')