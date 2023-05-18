MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
import pygame 
import time
sentence=input("Enter the sentence what you want to convert to morse code.\n").upper()
morse_code=''
for word in sentence.split():
    morse_word=' '.join(MORSE_CODE_DICT.get(char,'') for char in word)
    morse_code+=morse_word+' '
print(morse_code)
def play_morse_code(morse_code):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.2)
        def play_sound(morse):
            if morse=='.':
                pygame.mixer.music.load('dot.wav')
                time.sleep(0.1)
            elif morse=='-':   
                pygame.mixer.music.load('dash.wav')
                time.sleep(0.2)
            pygame.mixer.music.play()
            time.sleep(0.5)
        for char in morse_code:
            if char=='.' or char=='-':
                  play_sound(char)
            elif char==' ':
                 time.sleep(0.7)
play_morse_code(morse_code)
                   