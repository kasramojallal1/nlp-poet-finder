def get_tokens(path, token_dic):
    f = open(path, "r", encoding='utf-8')

    num_lines = 0

    for x in f:

        num_lines += 1
        newline = x.split()

        for i in range(len(newline)):
            if '\u200c' in newline[i]:
                arr = newline[i].split('\u200c')
                for j in range(len(arr)):
                    newline.append(arr[j])
            if '\u200b' in newline[i]:
                arr = newline[i].split('\u200b')
                for j in range(len(arr)):
                    newline.append(arr[j])

        for i in range(len(newline)):

            if '\u200c' in newline[i]:
                continue

            try:
                if token_dic[newline[i]]:
                    number = token_dic[newline[i]]
                    number += 1
                    token_dic[newline[i]] = number
            except:
                token_dic[newline[i]] = 1

    return token_dic, num_lines


def get_bigrams(path, bi_gram):
    f = open(path, "r", encoding='utf-8')

    for x in f:
        newline = x.split()

        for i in range(len(newline)):
            if '\u200c' in newline[i]:
                arr = newline[i].split('\u200c')
                for j in range(len(arr)):
                    newline.append(arr[j])
            if '\u200b' in newline[i]:
                arr = newline[i].split('\u200b')
                for j in range(len(arr)):
                    newline.append(arr[j])

        for i in range(len(newline)):

            if '\u200c' in newline[i]:
                continue

            try:
                if bi_gram[newline[i]]:
                    word_dic = bi_gram[newline[i]]
                    if i == 0:
                        number = word_dic['s']
                        number += 1
                        word_dic['s'] = number
                    else:
                        if i == len(newline) - 1:
                            number = word_dic['e']
                            number += 1
                            word_dic['e'] = number
                        try:
                            if word_dic[newline[i - 1]]:
                                number = word_dic[newline[i - 1]]
                                number += 1
                                word_dic[newline[i - 1]] = number
                        except:
                            word_dic[newline[i - 1]] = 1
            except:
                continue

    return bi_gram


def read_file(path):
    token_dic = {}
    # normal_token_dic = {}
    bigram = dict()

    token_dic, num_lines = get_tokens(path, token_dic)

    vocab_count = 0
    for key in token_dic:
        vocab_count += token_dic[key]

    # for key in token_dic:
    #     number = token_dic[key]
    #     if number >= 2:
    #         normal_token_dic[key] = number

    for key in token_dic:
        bigram[key] = {'s': 0, 'e': 0}

    new_bigram = get_bigrams(path, bigram)

    # for key in new_bigram:
    #     print(key)
    #     print(new_bigram[key])


    return token_dic, new_bigram, vocab_count, num_lines


def calculate_poet(words):
    global dic_ferdowsi, dic_hafez, dic_molavi,\
        bigram_ferdowsi, bigram_hafez, bigram_molavi,\
        la1, la2, la3, vocab_ferdowsi, vocab_hafez, vocab_molavi,\
        num_lines_ferdowsi, num_lines_hafez, num_lines_molavi


    result = []
    for i in range(len(words)):

        if i == 0:
            value = 0
            try:
                value += la3 * bigram_ferdowsi[words[i]]['s'] / num_lines_ferdowsi
            except KeyError:
                pass
            try:
                value += la2 * dic_ferdowsi[words[i]] / vocab_ferdowsi
            except KeyError:
                pass
            value += la1 * eps

            result.append(value)

        elif i == len(words) - 1:
            value = 0
            try:
                value += la3 * bigram_ferdowsi[words[i]]['e'] / dic_ferdowsi[words[i]]
            except KeyError:
                pass
            try:
                value += la2 * num_lines_ferdowsi / vocab_ferdowsi
            except KeyError:
                pass
            value += la1 * eps

            result.append(value)

        else:
            value = 0
            try:
                value += la3 * bigram_ferdowsi[words[i]][words[i - 1]] / dic_ferdowsi[words[i - 1]]
            except KeyError:
                pass
            try:
                value += la2 * dic_ferdowsi[words[i]] / vocab_ferdowsi
            except KeyError:
                pass
            value += la1 * eps

            result.append(value)

    result2 = []
    for i in range(len(words)):

        if i == 0:
            value = 0
            try:
                value += la3 * bigram_hafez[words[i]]['s'] / num_lines_hafez
            except KeyError:
                pass
            try:
                value += la2 * dic_hafez[words[i]] / vocab_hafez
            except KeyError:
                pass
            value += la1 * eps

            result2.append(value)

        elif i == len(words) - 1:
            value = 0
            try:
                value += la3 * bigram_hafez[words[i]]['e'] / dic_hafez[words[i]]
            except KeyError:
                pass
            try:
                value += la2 * num_lines_hafez / vocab_hafez
            except KeyError:
                pass
            value += la1 * eps

            result2.append(value)

        else:
            value = 0
            try:
                value += la3 * bigram_hafez[words[i]][words[i - 1]] / dic_hafez[words[i - 1]]
            except KeyError:
                pass
            try:
                value += la2 * dic_hafez[words[i]] / vocab_hafez
            except KeyError:
                pass
            value += la1 * eps

            result2.append(value)

    result3 = []
    for i in range(len(words)):

        if i == 0:
            value = 0
            try:
                value += la3 * bigram_molavi[words[i]]['s'] / num_lines_molavi
            except KeyError:
                pass
            try:
                value += la2 * dic_molavi[words[i]] / vocab_molavi
            except KeyError:
                pass
            value += la1 * eps

            result3.append(value)

        elif i == len(words) - 1:
            value = 0
            try:
                value += la3 * bigram_molavi[words[i]]['e'] / dic_molavi[words[i]]
            except KeyError:
                pass
            try:
                value += la2 * num_lines_molavi / vocab_molavi
            except KeyError:
                pass
            value += la1 * eps

            result3.append(value)

        else:
            value = 0
            try:
                value += la3 * bigram_molavi[words[i]][words[i - 1]] / dic_molavi[words[i - 1]]
            except KeyError:
                pass
            try:
                value += la2 * dic_molavi[words[i]] / vocab_molavi
            except KeyError:
                pass
            value += la1 * eps

            result3.append(value)

    res = 1
    for i in range(len(result)):
        res *= result[i]

    res2 = 1
    for i in range(len(result2)):
        res2 *= result2[i]

    res3 = 1
    for i in range(len(result3)):
        res3 *= result3[i]

    max_val = max(res, res2, res3)

    if max_val == res:
        return 1
    elif max_val == res2:
        return 2
    elif max_val == res3:
        return 3

    return 0


def read_test(path):

    f = open(path, "r", encoding='utf-8')

    poet_real = 0

    success = 0
    all_lines = 0

    for x in f:

        newline = x.split()

        if '1' in newline:
            poet_real = 1
            newline.remove('1')
        elif '2' in newline:
            poet_real = 2
            newline.remove('2')
        elif '3' in newline:
            poet_real = 3
            newline.remove('3')
        else:
            poet_real = 0

        value = calculate_poet(newline)
        if value == poet_real:
            success += 1
        all_lines += 1

    success_rate = success / all_lines
    return success_rate * 100




if __name__ == '__main__':

    path_test = './test_set/testcase.txt'
    path_ferdowsi = './train_set/ferdowsi_train.txt'
    path_hafez = './train_set/hafez_train.txt'
    path_molavi = './train_set/molavi_train.txt'

    la1, la2, la3, eps = 0.1, 0.2, 0.7, 1e-5

    dic_ferdowsi, bigram_ferdowsi, vocab_ferdowsi, num_lines_ferdowsi = read_file(path_ferdowsi)
    dic_hafez, bigram_hafez, vocab_hafez, num_lines_hafez = read_file(path_hafez)
    dic_molavi, bigram_molavi, vocab_molavi, num_lines_molavi = read_file(path_molavi)

    rate = read_test(path_test)

    print('lam1:' + str(la1) + ' lam2:' + str(la2) + ' lam3:' + str(la3) + ' eps:' + str(eps))
    print('success rate: ' + str(rate))

