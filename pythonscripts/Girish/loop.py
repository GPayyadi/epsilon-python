s = "4fsvdtdbebesdvedsvzv"
vowel ="aeiou"

#for i in s:
#	print(i)
i = 0
while(i < len(s)):
#	print(s[i])
	if(s[i] in vowel):
		print('got a vowel "' + s[i] + '" breaking now')
#		break							# To break after it gets one vowel
		i += 1
#		continue						# To continue for whole string to get all vowel
		if(s[i] == "d"):
			pass
	print(s[i])
	i += 1
