def Anagram(str1, str2):
  #a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
  if len(str1) != len(str2):
    return False;

  str1 = str1.lower()
  str2 = str2.lower()
  num = 1<<8
  letters = [0] * num

  for c in str1:
    letters[ord(c)] = letters[ord(c)]+1
  #print(letters)
  for c in str2:
    letters[ord(c)] = letters[ord(c)]-1
  
  for i in letters:
    if i != 0:
      return False
  
  return True


# Driver Code 
print(Anagram("Banana", "banana"))
print(Anagram("Banana", "circuit"))
print(Anagram("Listen", "silent"))
print(Anagram("Cinema", "iceman"))


#h: v=6W_Fve7qIe4