def mutate_string(string, position, character):
    lst = list(string)
    new_word = ""
    lst[position] = character
    for i in lst:
        new_word += i
    return new_word
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)