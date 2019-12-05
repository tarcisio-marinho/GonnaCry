CC=gcc
CFLAGS=-lcrypto 
OUTPUT=bin/gonnacry
RM=rm

main: main.o crypto.o struct.o func.o
	$(CC) lib/gonnacry.o lib/crypto.o lib/struct.o lib/func.o -o $(OUTPUT) $(CFLAGS) 

main.o: gonnacry.c 
	$(CC) -c gonnacry.c -o lib/gonnacry.o

crypto.o: lib/crypto.c lib/crypto.h
	$(CC) -c lib/crypto.c -o lib/crypto.o

func.o: lib/func.c lib/func.h
	$(CC) -c lib/func.c -o lib/func.o

struct.o: lib/struct.c lib/struct.h
	$(CC) -c lib/struct.c -o lib/struct.o

clean:
	$(RM) bin/gonnacry lib/*.o

run:
	./$(OUTPUT)