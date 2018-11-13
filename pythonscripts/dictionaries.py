# key value pairs
# ordered
# fast access 

address = {"fname":"ashish", "lname":"Pandey", "fname":"Awi"}
#address2 = {"name": { "fname":"ashish", "lname":"Pandey"}}

'''
print(address2["name"])
'''
address["pincode"] = "227807"
print(address)
if "fname" not in address.keys():
	address["fname"] = "Ashish"
print(list(address.keys()))		#Keys Object
print(list(address.values()))		#Value Objects
print(list(address.items()))		#Items Objects
for k,v in address.items():
	print(k + v)
i = address.pop("fname")		#pop will delete the value and return the corresponding value
v = address["fname"]
#print(help(address.pop))
print(i)
print(address)
#print(dir(address))


