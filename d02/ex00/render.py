from parse import search
import os.path
import sys 

def render(template):
    print('ok')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.template') and os.path.isfile('settings.py') and os.path.isfile(sys.argv[1]):
            setting = open('settings.py', 'r')
            template = open(sys.argv[1], 'r')
            if not setting or not template:
                if not setting:
                    print('cant open settings.py file')
                if not template:
                    print('cant open template file')
            else:
                render(sys.argv[1])
        else:
            print('need a settings.py file at root and a .template file as argument')
    else:
        print('bad argument')