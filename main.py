def decode_resistor_colors(bands):
    res = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet' : 7, 'gray' : 8, 'white' : 9, 'gold' : 5, 'silver' : 10}
    code = bands.split(" ")
    power = int(res[code[0]] + res[code[1]]) * int(res[code[2]])
    if power < 1000:
        output = power + ' ohms, '
    elif power < 100000:
         output = (power / 1000) + 'k ohms, '
    else:
         output = (power / 1000000) + 'M ohms, '
    if len(code) is 3:
        output.join('20%')
    else:
        output.join(res[code[3]] + '%')
    return output
