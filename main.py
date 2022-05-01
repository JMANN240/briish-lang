import sys

class BriishInterpereter:
    def __init__(self):
        self.cells = [0]
        self.n = 0
        self.pointer = 0
    
    def interperet(self, code, debug=False):
        self.pointer = 0
        words = code.split(' ')
        while(self.pointer < len(words)):
            word = words[self.pointer]
            if word == "maffs":
                self.cells[self.n]+=1
            elif word == "bloody":
                self.cells[self.n]-=1
            elif word == "roight":
                self.n+=1
                if self.n >= len(self.cells):
                    self.cells.insert(len(self.cells),0)
            elif word == "bruv":
                self.n-=1
                if self.n < 0:
                    self.cells.insert(0, 0)
                    self.n = 0
            elif word == "oi":
                print(chr(self.cells[self.n]), end="")
            elif word == "innit?":
                self.cells[self.n] = ord(str(input())[0])
            elif word == "loike":
                if self.cells[self.n] == 0:
                    count = 1
                    while (count != 0):
                        self.pointer += 1
                        if words[self.pointer] == "loike":
                            count += 1
                        elif words[self.pointer] == "roight?":
                            count -= 1
            elif word == "roight?":
                if self.cells[self.n] != 0:
                    count = 1
                    while (count != 0):
                        self.pointer -= 1
                        if words[self.pointer] == "roight?":
                            count += 1
                        elif words[self.pointer] == "loike":
                            count -= 1
            else:
                raise SyntaxError
            if(debug == True):
                if(self.n != 0):
                    print(str(self.cells[:self.n])[:-1] + ", {" + str(self.cells[self.n]) + "}, " + str(self.cells[self.n + 1:])[1:])
                elif(self.n == 0):
                    print("[{" + str(self.cells[self.n]) + "}, " + str(self.cells[self.n + 1:])[1:])
                elif(self.n == len(self.cells) - 1):
                    print(str(self.cells[:self.n])[:-1] + ", {" + str(self.cells[self.n]) + "}]")
            self.pointer+=1
    
    def fromBF(self, bf_string):
        conversion = {
            '>': 'roight',
            '<': 'bruv',
            '+': 'maffs',
            '-': 'bloody',
            '.': 'oi',
            ',': 'innit?',
            '[': 'loike',
            ']': 'roight?'
        }
        return ' '.join([conversion[bf_char] for bf_char in bf_string])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a .brit file to interpret")
    elif len(sys.argv) > 2:
        print("Please only provide one .brit file to interpret")
    else:
        bi = BriishInterpereter()
        try:
            with open(sys.argv[1], 'r') as file:
                try:
                    words = ' '.join([line.strip() for line in file.readlines()])
                    bi.interperet(words)
                except:
                    print("\nMalformed Bri'ish!")
        except:
            print("Error opening file")