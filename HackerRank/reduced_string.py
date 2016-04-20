def reduce(string,map):
    for i in range(len(string)):
        if i < len(string) - 1:
            if string[i] == string[i+1]:
                if i == 0:
                    reduce(string[2:],map)
                    break
                else:
                    reduce(string[:i] + string[i+2:], map)
                    break
    else:
        print(string if string else 'Empty string')