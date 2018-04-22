def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    # TODO: specify sample time
    bits = bits.strip('0')
    if '0' in bits:
        sample_1 = len(min(filter(lambda x: x != '', bits.split('0'))))
    if '1' in bits:
        sample_0 = len(min(filter(lambda x: x != '', bits.split('1'))))
    sample_times = min(sample_0, sample_1)

    words = bits[::sample_times].split('0000000')
    for i, word in enumerate(words):
        chars = word.split('000')
        for j, char in enumerate(chars):
            morse = char.split('0')
            for k, x in enumerate(morse):
                morse[k] = x.replace('111', '-').replace('1', '.')
            chars[j] = ''.join(morse)
        words[i] = ' '.join(chars)
    return '   '.join(words)


def decodeMorse(morse_code):
    # Time: 522ms
    msg = ''
    morse_code = morse_code.strip().replace('   ', ' * ')
    for x in morse_code.split():
        if x != '*':
            msg += MORSE_CODE[x]
        else:
            msg += ' '

    return msg
