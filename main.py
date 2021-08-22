def get_tokens(path, token_dic):
    f = open(path, "r", encoding='utf-8')

    for x in f:
        print(x)

        newline = x.split()

        for i in range(len(newline)):

            try:
                if token_dic[newline[i]]:
                    number = token_dic[newline[i]]
                    number += 1
                    token_dic[newline[i]] = number
            except:
                token_dic[newline[i]] = 1

    return token_dic


def read_file(path):
    token_dic = {}

    token_dic = get_tokens(path, token_dic)

    # print(token_dic)


if __name__ == '__main__':

    path_ferdowsi = './train_set/ferdowsi_train.txt'
    path_hafez = './train_set/hafez_train.txt'
    path_molavi = './train_set/molavi_train.txt'

    read_file(path_ferdowsi)
