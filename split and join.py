def split_and_join(line):
    fst = line.split(" ")
    snd = "-".join(fst)
    return snd
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)