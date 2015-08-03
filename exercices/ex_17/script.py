from sys import argv
from os.path import exists
script,input_file, output_file=argv
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: ValueError: need more than 1 value to unpack

print script
print "input_file %r "% input_file
print "output file is : %r " % output_file
print " is output existe %r" % exists(output_file)
file_in=open(input_file)
text_to_copy=file_in.read()
print len(text_to_copy)
file_end=open(output_file,"w")
print "truncating"
file_end.truncate()
file_end.write(text_to_copy)
print "finish"
file_end.close()
file_in.close()

