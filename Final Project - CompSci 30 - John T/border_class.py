class border:
    def __init__(self, text, width):
        self.text = text.splitlines()
        self.width = width
    
    def create_border(self):
        g_line = "+{0}+".format("-"*(self.width-2))
        print(g_line)
        for line in self.text:
            print("| {0:<{1}} |".format(line, self.width-4))
        print(g_line)