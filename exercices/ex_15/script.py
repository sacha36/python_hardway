from sys import argv 


script,filename=argv
print " i am  reading this %r file "% filename
txt = open(filename)

print "here the content of the file "
print "%r "% txt.read()
