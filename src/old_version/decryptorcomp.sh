#!/bin/bash

gcc decryptor.c lib/struct.c lib/func.c lib/crypto.c -o bin/decryptor -lcrypto

