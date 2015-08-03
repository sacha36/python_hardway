from sys import argv

script, filename=argv 
print " before we start %r"% filename


target=open(filename,"w")

target.truncate()

line1=raw_input("1>")
line2=raw_input("2>")
line3=raw_input("3>")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()
txt=open(filename)
print txt.read()
