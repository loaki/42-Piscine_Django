import os
import sys 
import settings

def get_book_variable_module_name(module_name):
    module = globals().get(module_name, None)
    book = {}
    if module:
        book = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
    return book

def render(template, file_name):
    cv = "".join(template.readlines())
    book = get_book_variable_module_name('settings')
    for key, value in book.items():
        cv = cv.replace('{'+key+'}', str(value))
    out = open(file_name+'.html', 'w')
    out.write(cv)
    out.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.template') and os.path.isfile('settings.py') and os.path.isfile(sys.argv[1]):
            template = open(sys.argv[1], 'r')
            if not template:
                print('cant open template file')
            else:
                render(template, sys.argv[1].split('.template')[0])
            template.close()
        else:
            print('need a settings.py file at root and a .template file as argument')
    else:
        print('bad argument')