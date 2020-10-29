alphabet=""
for smth in 'a'*10:
    user_input = input("введите буковки я на коленях УМОЛЯЮ:")
    for letter in user_input:
    	if letter not in alphabet: alphabet+=letter 
print(alphabet)
