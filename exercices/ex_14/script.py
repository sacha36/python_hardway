from sys import argv

script,username=argv
prompt=">"
print "Hi %s my name is %s " %(username, script)
print "lets play a game "
print "do you like me %s "%username
likes=raw_input(prompt)

print " where do you live %s  "% username 
lives=raw_input(prompt)

print "what kind of computers do you have %s ?"%username
computer=raw_input(prompt)

print """
Alright, so my name is %r 
and yours is : %r 
and here what u said about liking me : %r 
and where you live : %r
and which computer u like :%r """%(script, username, likes, lives, computer)
