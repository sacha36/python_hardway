def print_both(*args):
	arg1,arg2=args
	print "1> %r \n 2> %r" %(arg1,arg2)
def print_just_one(arg1):
	print "1> %r" %arg1
def print_nothing():
	print " i got nothing !!idi nahui ! " 

print_both("hallo","ar ja ")
print_just_one(" das ein gross patapouf")
print_nothing()
