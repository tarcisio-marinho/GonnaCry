#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/err.h>
#include <stdio.h>
#include <string.h>

#define KEY_LENGTH  2048
#define PUB_EXP     3 // >=1024 -> maximum number of permitted primes -> modulus bit length


typedef struct Key_par{
    char *public_key, *private_key;
}RSAKeys;


int main(void) {
    size_t pri_len;            // Length of private key
    size_t pub_len;            // Length of public key
    RSAKeys *keys = NULL;
    char   *pri_key;           // Private key
    char   *pub_key;           // Public key
    char   msg[KEY_LENGTH/8];  // Message to encrypt
    char   *encrypt = NULL;    // Encrypted message
    char   *decrypt = NULL;    // Decrypted message
    char   *err;               // Buffer for any error messages

    keys = malloc(sizeof(RSAKeys));
    // Generate key pair
    printf("Generating RSA (%d bits) keypair...", KEY_LENGTH);
    fflush(stdout);
    RSA *keypair = RSA_generate_key(KEY_LENGTH, PUB_EXP, NULL, NULL);

    // To get the C-string PEM form:
    BIO *pri = BIO_new(BIO_s_mem());
    BIO *pub = BIO_new(BIO_s_mem());

    PEM_write_bio_RSAPrivateKey(pri, keypair, NULL, NULL, 0, NULL, NULL);
    PEM_write_bio_RSAPublicKey(pub, keypair);

    pri_len = BIO_pending(pri);
    pub_len = BIO_pending(pub);

    keys->private_key = malloc(pri_len + 1);
    keys->public_key = malloc(pub_len + 1);

    BIO_read(pri, keys->private_key, pri_len);
    BIO_read(pub, keys->public_key, pub_len);

    keys->private_key[pri_len] = '\0';
    keys->public_key[pub_len] = '\0';


    // access the keys
    printf("\n%s\n%s\n", keys->private_key, keys->public_key);

    
    // Get the message to encrypt
    printf("Message to encrypt: ");
    fgets(msg, KEY_LENGTH-1, stdin);
    msg[strlen(msg)-1] = '\0';

    
    // Encrypt the message
    encrypt = malloc(RSA_size(keypair));
    int encrypt_len;
    err = malloc(130);
    if((encrypt_len = RSA_public_encrypt(strlen(msg)+1, (unsigned char*)msg, (unsigned char*)encrypt,
                                         keypair, RSA_PKCS1_OAEP_PADDING)) == -1) {
        ERR_load_crypto_strings();
        ERR_error_string(ERR_get_error(), err);
        fprintf(stderr, "Error encrypting message: %s\n", err);
        goto free_stuff;
    }

    
    // Write the encrypted message to a file
    FILE *out = fopen("out.bin", "w");
    fwrite(encrypt, sizeof(*encrypt),  RSA_size(keypair), out);
    fclose(out);
    printf("Encrypted message written to file.\n");
    free(encrypt);
    encrypt = NULL;

    
    // Read it back
    printf("Reading back encrypted message and attempting decryption...\n");
    encrypt = malloc(RSA_size(keypair));
    out = fopen("out.bin", "r");
    fread(encrypt, sizeof(*encrypt), RSA_size(keypair), out);
    fclose(out);

    
    // Decrypt it
    decrypt = malloc(encrypt_len);
    if(RSA_private_decrypt(encrypt_len, (unsigned char*)encrypt, (unsigned char*)decrypt,
                           keypair, RSA_PKCS1_OAEP_PADDING) == -1) {
        ERR_load_crypto_strings();
        ERR_error_string(ERR_get_error(), err);
        fprintf(stderr, "Error decrypting message: %s\n", err);
        goto free_stuff;
    }
    
    // original content
    printf("Decrypted message: %s\n", decrypt);


    // dealocate memory 
    free_stuff:
    RSA_free(keypair);
    BIO_free_all(pub);
    BIO_free_all(pri);
    free(keys->private_key);
    free(keys->public_key);
    free(keys);
    free(encrypt);
    free(decrypt);
    free(err);

    return 0;
}