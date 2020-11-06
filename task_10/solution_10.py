a=input("введите слово или не вводите делайте что хотите я вам не указываю: ")
is_palindrom=""
for i in a:
	is_palindrom=i+is_palindrom
if a==is_palindrom:
	print(True)
else:
	print(False)
