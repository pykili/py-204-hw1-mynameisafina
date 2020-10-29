inp = str(input("введите последовательность букв:"))

most_frequent_character = ''
count = 0

for char in inp:
	if inp.count(char) > count:
		most_frequent_character = char
		count = inp.count(char)

print(most_frequent_character)
