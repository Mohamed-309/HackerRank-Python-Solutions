def count_substring(string, sub_string):
    count = 0
    for itr in range(0, len(string)):
        if string[itr:itr+len(sub_string)] == sub_string:
            count +=1 
        else: continue
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)