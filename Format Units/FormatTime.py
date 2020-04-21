
def format_time(seconds):
    mins, hours, n = 0, 0, 0
    units = {0 : 'Seconds', 1 : 'Minutes', 2 : 'Hours'}
    while seconds >= 60:
        seconds -= 60
        mins += 1
        n = 1
    while mins >= 60:
        mins -= 60
        hours += 1
        n = 2
    if n == 2:
        return f'{hours}:{mins:02d}:{seconds:02d} {units[n]}'
    elif n == 1:
        return f'{mins:2d}:{seconds:02d} {units[n]}'
    else:
        return f'{seconds:.2f} {units[n]}'


def main():
    print('21,600 Seconds = ', format_time(21600))

if __name__=='__main__':
    main()