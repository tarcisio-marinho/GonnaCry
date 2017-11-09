CC=gcc
CFLAGS=-lcrypto 
OUTPUT=bin/gonnacry
RM=rm

out: gonnacry.o lib/crypto.o lib/struct.o lib/func.o
	$(CC) gonnacry.o lib/crypto.o lib/struct.o lib/func.o -o $(OUTPUT) $(CFLAGS) 

main: gonnacry.c 
	$(CC) -c gonnacry.c 

crypto: lib/crypto.c lib/crypto.h
	$(CC) -c lib/crypto.c

func: lib/func.c lib/func.h
	$(CC) -c lib/func.c

struct: lib/struct.c lib/struct.h
	$(CC) -c lib/struct.c

clean:
	$(RM) *.o bin/gonnacry lib/*.o