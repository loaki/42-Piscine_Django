from parse import search

def td_sample(element, number, small, molar):
    if element:
        td_sample = f'''
        <td style="border: 1px solid black">
            <h4 style="text-align: center">{element}</h4>
            <ul>
                <li>No {number}</li>
                <li>{small}</li>
                <li>{molar}</li>
            </ul>
        </td>'''
    else:
        td_sample = f'''
            <td>
            </td>'''
    return td_sample

def parse_table(table):
    list_table = []
    for l in table:
        name = l.split()[0]
        pos = search('position:{},', l)[0]
        num = search('number:{},', l)[0]
        small = search('small: {},', l)[0]
        molar = search('molar:{},', l)[0]
        list_table.append((name, pos, num, small, molar))
    return list_table

def periodic_table():
    html_first = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>periodic_table</title>
</head>
<body>
<h1>Periodic Table</h1>
<table>
    <tr>'''
    html_last = '''
    </tr>
</table>
</body>
</html>'''
    td = ''
    # td += td_sample('hydrogen', '2', 'H', '12')
    # td += td_sample('', '', '', '')
    # td += td_sample('hydrogen', '2', 'H', '12')
    pt = open('periodic_table.txt', 'r')
    list_table = parse_table(pt)
    td = ''
    last_pos = 0
    for elem in list_table:
        if last_pos == 17:
            td+='</tr><tr>'
        for _ in range(last_pos, int(elem[1])-1):
            td+=td_sample('','','','')
        td+=td_sample(elem[0], elem[2], elem[3], elem[4])
        last_pos = int(elem[1])
    html = open('periodic_table.html', 'w')
    html.write(html_first+td+html_last)
    

if __name__ == '__main__':
    periodic_table()