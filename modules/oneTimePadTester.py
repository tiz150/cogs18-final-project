import unittest
from oneTimePad import oneTimeEncryption

# noticed that I combined the test for encoding and decoding, since it is the only way to know if the key is correct
# or not

class oneTimePadTester(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.testEncodeDecodeInteger()
        self.testEncodeDecodeText()

    """
        testing method for encode/decode integer
    """
    def testEncodeDecodeInteger(self):
        original_int = 0
        key_1, key_2 = oneTimeEncryption.encodeInteger(original_int)
        self.assertEqual(original_int, oneTimeEncryption.decodeInteger(key_1, key_2))

        original_int = 1099909
        key_1, key_2 = oneTimeEncryption.encodeInteger(original_int)
        self.assertEqual(original_int, oneTimeEncryption.decodeInteger(key_1, key_2))

        original_int = 100
        key_1, key_2 = oneTimeEncryption.encodeInteger(original_int)
        self.assertEqual(original_int, oneTimeEncryption.decodeInteger(key_1, key_2))

    """
        testing method for encode/decode text
    """
    def testEncodeDecodeText(self):
        original_message = "aaa"
        key_1, key_2 = oneTimeEncryption.encodeText(original_message)
        self.assertEqual(original_message, oneTimeEncryption.decodeText(key_1, key_2))

        original_message = ""
        key_1, key_2 = oneTimeEncryption.encodeText(original_message)
        self.assertEqual(original_message, oneTimeEncryption.decodeText(key_1, key_2))


        original_message = "aa$%^&Sffakfmsa,f,agmdksgmkdslgmdsgmdslgmd,smgdklsmgkdlsgmdlskgmdlksgmdslkgmdslkgkdsmgkds"
        key_1, key_2 = oneTimeEncryption.encodeText(original_message)
        self.assertEqual(original_message, oneTimeEncryption.decodeText(key_1, key_2))


oneTimePadTester()