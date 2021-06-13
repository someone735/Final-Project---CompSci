import string
class encrypt:
    def __init__(self, inputText):
        self.inputText = inputText
        self.rotation = 2
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
    def encryptString (self):
        newText = self.inputText
        upper_list = []
        lower_list = []
        for i in range(len(newText)):
            if newText[i] in self.upper:
                upper_list.append(i)
            if newText[i] in self.lower:
                lower_list.append(i)

        for i in upper_list:
            old_char = newText[i]
            old_position = self.upper.find(old_char)
            if old_position+self.rotation >= 26:
                old_position -= 26
            new_char = self.upper[old_position+self.rotation]
            newText = newText[:i] + new_char + newText[i+1:]

        for i in lower_list:
            old_char = newText[i]
            old_position = self.lower.find(old_char)
            new_char = self.lower[old_position-self.rotation]
            newText = newText[:i] + new_char + newText[i+1:]

        return newText