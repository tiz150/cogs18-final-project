import random

class oneTimeEncryption:
    """
        class to encrypt/decrypt message using one-time-pad encryption

        Attributes
        ----------
        none

        Methods
        -------
        encodeInteger(integer_in)
            encrypte integer using one-time-pad encryption.
            ONLY WORK WITH POSITIVE INTEGER
            return key1 and key2

        decodeInteger(key_1, key_2)
            decrypte integer using key1 and key2.
            return decrypted integer

        encodeText(textIn)
            encrypte text(string) using one-time-pad encryption.
            return key1 and key2

        decodeText(key_1, key_2)
            decrypte text using key1 and key2.
            return decrypted text

        encodeTextFile(file_name):
            encrypte a textfile with file_name using one-time-pad encryption.
            write encrypted file_name(key1) and file_name(key2) to the current location

        decodeText(key_1, key_2):
            decrypte an ecncrypted text file, use key_1 and key_2 as the keys
            write decrypted text file with original name to the current location

        __randomBinaryString(length):
            a private function to generate random numbers as string
    """

    @staticmethod
    def encodeInteger(integer_in):
        """
        encode an interger, produce shorter key than encode an integer as a string
        ONLY WORK WITH POSITIVE INTEGER

        :param
            integer_in: the integer to be encrypted

        :return:
            key1: encrypted key one
            key2: encrypted key two
        """

        # if input is not integer
        if(not isinstance(integer_in, int)):
            print("input is not integer")
            return

        key_1 = ""
        key_2 = ""
        binary_in = str(bin(integer_in))

        #generate key_1 and derviate key_2
        key_1 = oneTimeEncryption.__randomBinaryString(len(binary_in) - 2)
        for a, b in zip(binary_in[2:], key_1):
            key_2 += str([int(a) ^ int(b)][0])

        return key_1, key_2

    @staticmethod
    def decodeInteger(key_1, key_2):
        """
        decrypte an integer with given keys

        :param key_1: key one of the encrypted integer
        :param key_2: key two of the encrypted integer
        :return: originalInt: the original integer
        """

        # if the keys are not binary number, terminate the function
        try:
            # decode the int
            decoded_int = '{0:0{1}b}'.format(int(key_1,2) ^ int(key_2,2),len(key_1))
        except ValueError:
            print("incorrect key")
            return

        return int(decoded_int, 2)


    @staticmethod
    def encodeText(text_in):
        """
        encode a string

        :param text_in: the string to be encoded
        :return: key1: key one of the encoded string
                 key2: key two of the encoded string
        """
        key_1 = ""
        key_2 = ""
        raw_text_bit = ""
        key_bit = ""

        for char in text_in:
            # remove the first two characters(0b) from the binary number
            raw_text_bit = bin(ord(char))[2:]

            # fill zero to make the binary number 14 digits(max value of ord()), so it doesn't give away information
            for x in range(len(raw_text_bit), 14):
                raw_text_bit = "0" + raw_text_bit

            key_bit = oneTimeEncryption.__randomBinaryString(14)
            key_1 += key_bit + " "

            # encrypte text
            for a, b in zip(key_bit, raw_text_bit):
                key_2 += str([int(a) ^ int(b)][0])
            key_2 += " "
        return key_1, key_2

    @staticmethod
    def decodeText(key_1, key_2):
        """
        decode a string
        :param key_1:  key one of the encoded string
        :param key_2: key two of the encoded string
        :return: decoded string
        """

        decoded_text = ""
        decoded_bit = ""

        # convert string to array for decoding
        key_1 = key_1.split(" ")
        key_2 = key_2.split(" ")

        #remove empty array entries
        while "" in key_1: key_1.remove("")
        while "" in key_2: key_2.remove("")

        # decode the text
        for a,b in zip(key_1, key_2):
            decoded_bit = '{0:0{1}b}'.format(int(a,2) ^ int(b,2),len(a))
            decoded_text += chr(int(decoded_bit, 2))
        return decoded_text


    @staticmethod
    def encodeTextFile(file_name):
        """
        encode a text file
        :param file_name: the file name of the text file
        :return:  file1: the file key one
                  file2: the file key two
        """

        # if the file not found, terminate the program
        try:
            raw_file = open(file_name, "r")
        except FileNotFoundError:
            print("File not found")
            return

        # read the file and encode it
        keys = oneTimeEncryption.encodeText(raw_file.read());
        try:
            dot_index = file_name.index(".")
        except ValueError:
            dot_index = len(file_name)

        # create new key files
        encoded_file_one = open(file_name[:dot_index] + "(key1)" + file_name[dot_index:], "w");
        encoded_file_two = open(file_name[:dot_index] + "(key2)" + file_name[dot_index:], "w");

        # store the key into files
        encoded_file_one.write(keys[0])
        encoded_file_two.write(keys[1])

    @staticmethod
    def decodeTextFile(Key_name_1, Key_name_2):
        """
        decode a text file

        :param Key_name_1:  file key 1's name
        :param Key_name_2:  file key 2's name
        :return: the decoded file
        """
         # if file is not found
        try:
            encoded_file_one = open(Key_name_1, "r")
            encoded_file_two = open(Key_name_2, "r")
        except FileNotFoundError:
            print("File not found")
            return

        # create the file and write decoded message
        decoded_text = oneTimeEncryption.decodeText(encoded_file_one.read(), encoded_file_two.read());
        decoded_text_file = open(Key_name_1.replace("(key1)", ""), "w");
        decoded_text_file.write(decoded_text)


    @staticmethod
    def __randomBinaryString(length):
        """
        generate a string contain random numbers for encryption functions
        :param length: the length of the random string
        :return: the random string
        """
        randomString = ""

        for x in range(0,length):
            randomString += str(random.choice([0,1]))

        return randomString



