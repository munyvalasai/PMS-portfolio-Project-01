class EncryptDecryptPassword:

    def __init__(self, text, shift_key):
        self.text = text
        self.shift_key = shift_key
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encryyptPassword(self):
        """ To encrypting the password! """
        end_text = ""
        self.shift_key = self.shift_key % 52

        for char in self.text:
            if char in self.alphabets:
                position = self.alphabets.index(char)
                new_position = position + self.shift_key
                if new_position >= 52:
                    new_position = new_position % 52
                end_text += self.alphabets[new_position]
            else:
                end_text += char
        return end_text

    def decryptPassword(self):
        """ To decrypting the password! """
        end_text = ""
        self.shift_key = self.shift_key % 52

        for char in self.text:
            if char in self.alphabets:
                position = self.alphabets.index(char)
                new_position = position - self.shift_key
                if new_position >= 52:
                    new_position = new_position % 52
                end_text += self.alphabets[new_position]
            else:
                end_text += char
        return end_text