a = input ("введите последовательность цифр:")
b = 0
for i in a:
	if int(i)>b:
			b=int(i)
print("самая большая цифра = " + str(b))
