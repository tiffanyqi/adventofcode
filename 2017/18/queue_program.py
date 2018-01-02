def parse(program, dictionary, frequencies):
    """
    dictionary = things that are held in sent
    frequencies = things that are being received
    """
    index = 0
    while index <= len(program):
        p = program[index][0].split(' ')
        op = p[0]
        letter = p[1]

        try:
            dictionary[letter]
        except KeyError:
            dictionary[letter] = 0

        if len(p) == 3:
            value = p[2]
            try:
                value = int(value)
            except ValueError:
                value = int(dictionary[value])

            try:
                if op == 'set':
                    dictionary[letter] = value
                elif op == 'add':
                    dictionary[letter] += value
                elif op == 'mul':
                    dictionary[letter] *= value
                elif op == 'mod':
                    dictionary[letter] = dictionary[letter] % value
                elif op == 'jgz' and dictionary[letter] != 0:
                    index += value - 1
            except ZeroDivisionError:
                pass

        else:
            if op == 'snd':
                frequencies[letter] = dictionary[letter]
            elif op == 'rcv':
                return frequencies[letter]

        index += 1
        print index, p[0], dictionary, frequencies
