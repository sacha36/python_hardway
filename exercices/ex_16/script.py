from sys import argv

script,target_file=argv

print "hi, here the file : %r"%target_file
file1 =open(target_file,"w")
line1=raw_input("1>")
line2=raw_input("2>")
line3=raw_input("3>")
txt=open(target_file)
print txt.read()

print "i am truncating the file "
file1.truncate()
print txt.read()
file1.write(line1)
file1.write("\n")
file1.write(line2)
file1.write("\n")
file1.write(line3)
file1.write("\n")
print "here the new content "
file1.close()
txt=open(target_file)
print txt.read()

