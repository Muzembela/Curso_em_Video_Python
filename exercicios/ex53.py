s = input('Digite s: ')
e = True
for c in range(len(s)):
	if(s[c] != s[-(c+1)]):
		e = False
		break
if e and len(s) > 0:
	print("Is palindrome")
else :
	print("Not is palindrome")
print(s[::-1])