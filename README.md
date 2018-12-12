# cogs18-final-project
This is the repo for cogs18 final project

For this project, I am building a one-time-pad encryptor/decryptor, where the encryption pad is randomly generate for every encryption, so that the encrypted file isn't breakable. The process of encryption is to first to read the fle or input as binary numbers, then gerneteate a one time pad with the same length using the random number generator, and finally do a XOR operation on the raw input and the randombit, and then export the random pad and XOR result as the keys.

my project includes three main function: encode/decode a integer, encode/decode a text message and encode/decode a text file.
