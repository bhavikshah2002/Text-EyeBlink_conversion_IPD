import time
eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'
    }


class texttomorsecode():
    
    def text_to_morse(self,text):
        morse_code=[]
        self.outstr = ''
        self.space = ' '
        self.senc = 0
        self.wordprocces = 0
        self.lenword = len(text)
        for i in text:
            if i not in eng_to_morse:
                print('Data not formatted properly')
                return ['']
            else:
                morse_code.append(eng_to_morse[i])
        return morse_code


# c= texttomorsecode()
# ans=c.text_to_morse('python')
# print(ans)
