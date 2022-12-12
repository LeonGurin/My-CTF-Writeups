with open('attachment.txt', 'r', encoding='utf8') as f:
    data = f.read()

for i in data:
    if i == '🥂':
        print('>', end='')
    elif i == '🍾':
        print('.', end='')
    elif i == '🍷':
        print('-', end='')
    elif i == '🍸':
        print('[', end='')
    elif i == '🍹':
        print('<', end='')
    elif i == '🍺':
        print('+', end='')
    elif i == '🥃':
        print(']', end='')