CC=gcc
CFLAGS=-lcrypto 
OUTPUT=bin/gonnacry
RM=rm

out: main.o crypto.o struct.o func.o
	$(CC) gonnacry.o crypto.o struct.o func.o -o $(OUTPUT) $(CFLAGS) 

main.o: gonnacry.c 
	$(CC) -c gonnacry.c -o gonnacry.o

crypto.o: lib/crypto.c lib/crypto.h
	$(CC) -c lib/crypto.c -o crypto.o

func.o: lib/func.c lib/func.h
	$(CC) -c lib/func.c -o func.o

struct.o: lib/struct.c lib/struct.h
	$(CC) -c lib/struct.c -o struct.o

clean:
	$(RM) *.o bin/gonnacry