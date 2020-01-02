import numpy as np
def Anagram(str1, str2):
  #a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
  if len(str1) != len(str2):
    return False;
  str1 = str1.lower()
  str2 = str2.lower()
  num = 1<<8 #256
  #letters = [0] * num
  
  #a= np.array([1 3 4]], dtype=int)
  letters = np.zeros((1<<8,), dtype=int)
  #print(a.dtype)
  #print(type(a))
  #print(a)
  
  for c in str1:
    letters[ord(c)] = letters[ord(c)]+1
  print(letters)
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
print(Anagram("zljljdqo88wqjqjnddqjadssakhuwwjncpqipwjeqmndansdazz", "jadssakhuwwjncpqipwjeqmndansdazzzljljdqo88wqjqjnddq"))
