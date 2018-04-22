"""
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
"""


def accum(str1):
    str_out = ''
    for i, x in enumerate(str1):
        str_out += x.upper()
        for j in range(i):
            str_out += x.lower()
        str_out += '-'
    return str_out[:-1]


def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum3(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


if __name__ == '__main__':
    print(accum3(input('Input a string: ')))
