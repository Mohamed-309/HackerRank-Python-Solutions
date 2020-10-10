def swap_case(s):
   new_word = ""
   for letter in s:
       if letter.islower() == True:
           letter = letter.upper()
           new_word += letter
       else:
           letter = letter.lower()
           new_word += letter
   return new_word
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
