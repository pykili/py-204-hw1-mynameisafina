a = input("напишите буковки:")
alphabet = ""
for letter in a:
   if letter not in alphabet: alphabet+=letter
print(alphabet)
