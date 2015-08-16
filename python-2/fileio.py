#!usr/bin/python

##file IO operations

newfname = "test.log"
newf = open(newfname,'w')
newf.write("1.Testing log.\n")
newf.write("2.Testing log.\n")
newf.write("3.Testing log.\n")

newf.close()

newf = open(newfname,'r')
#newfcont = newf.read()
for line in newf:
    print line.rstrip()