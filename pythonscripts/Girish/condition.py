s = "isecevemdmlkm"
vowel = "aeiou"
#a = "m"

#if (a == "z"):
#	print("a" is "z")
#	print("stil in if block")
#print("out of if block")

if (s[0] in vowel):
	print(s[0])
	print("it has a vowel")
	Print("still in if block")
#print("out of if block")
elif(s[0].isdigit()):
	print("its not a vowel but a digit!")
else:
	print("its nthing above")
print("out of if block")
