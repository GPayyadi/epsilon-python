#!/bin/python
##Below is Positional Argument
'''
#def function(arg):		#: is for starting the function
#	print(arg)		# Indentation or space is not clear then it will consider as break
def add(arg1,arg2,arg3):
	sum = arg1 + arg2 + arg3
	return sum		#This Return is important to print the result
#
arg1 = 12			#If value are in " then it will be concatenation
arg2 = 32
arg3 = 40
#result = add(arg1,arg2,arg3)
#print(result)			
print(add(arg1,arg2,arg3))	#standard way of calling function

#function(arg1)			# Calling function
#function(arg2)
#
#Keyowrd  arguments
#def function(arg1, arg2):
#    print(arg1, arg2)
'''
#Below is default positional argument

def function(arg1 = "arg1 ",arg2 = " arg2",arg3 = "default argumnet 3" ):
    print("********************")
    print(arg1)
    print(arg2)
    print(arg3)
arg1 = "argument 1"
arg2 = "my argument"
arg3 = "my argument 3"
function(arg1,arg3, arg2)
function()				#when there is no argument defined in function then it will consider the default
function(arg1)
function(arg1,arg2)
function("only argument ", "2nd argument")
