test: all db

all: fun_finder_pb2.py Client.jar makefile

db: offline.py
	./offline.py test

com/fun_finder/FunFinderProtos.java: fun_finder.proto
	protoc -I=/root/fun_finder --java_out=/root/fun_finder/ /root/fun_finder/fun_finder.proto

fun_finder_pb2.py: fun_finder.proto
	protoc -I=/root/fun_finder --python_out=/root/fun_finder/ /root/fun_finder/fun_finder.proto

#Client.jar: Client.class
#	jar cf Client.jar Client.class

#Client.class: Client.java com/fun_finder/FunFinderProtos.java
#	javac Client.java
