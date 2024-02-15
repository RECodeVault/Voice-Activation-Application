import speech_recognition as sr 
import pyautogui
import pyttsx3
import time
import keyboard
import random

# speech engine install
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # voice for male

# speaking
def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def filter_list(keywords, word_list):
    return [word for word in word_list if any(keyword in word.lower() for keyword in keywords)]

# parses the list passed through
def parseCommand():
    while True:
        listener = sr.Recognizer()
        print('Listening for a command')

        try:
                with sr.Microphone() as source:
                        input_speech = listener.listen(source, timeout=10000000)
                        temp = listener.recognize_google(input_speech, language='en_gb')
                print('Recognizing speech...')
                if not temp:
                      continue
                else:
                        words = temp.lower().split()
                
                        # List of keywords to filter
                        keywords_to_filter = ['forward', 'left', 'right', 'write', 'back', 'jump', 'run', 'rump', 'turn', 'turner', 'scroll', 'crouch', 'up', 
                                              'grab', 'clicker', 'toggle', 'release', 'dance', 'exit', 'control']

                        filtered_words = filter_list(keywords_to_filter, words)
                        
                        if filtered_words:
                                print(f'The input was: {filtered_words}')
                                return filtered_words
                        else:
                                continue

        except sr.WaitTimeoutError:
                print('Speech recognition timed out. No speech detected.')
        except sr.UnknownValueError:
                continue
        except Exception as exception:
                print('I did not quite catch that')
                print(exception)
                return temp

# types keyboard inputs 
def type_keyboard(query = ''):
    keyboard.press('w')
    time.sleep(2)
    keyboard.release('w')

    if 'forward' in query:
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')
    elif 'left' in query:
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')
    elif 'right' in query or 'write' in query:
        keyboard.press('d')
        time.sleep(1)
        keyboard.release('d')
    elif 'back' in query:
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')
    else:
        speak('Command not regognized')

def random_choice():
        commands = ['forward', 'left', 'right', 'write', 'back', 'jump', 'run', 'rump', 'turn', 'turner', 
                   'scroll', 'crouch', 'up', 'grab', 'clicker', 'toggle', 'release']
        return random.choice(commands)

# main

def main():
        speak('Ready')

        while True:
                # Parse as list
                query = [command.lower() for command in parseCommand()]
                

                if query[0] == 'forward':
                        keyboard.press('w')
                        time.sleep(1)
                        keyboard.release('w')

                elif query[0] == 'left':
                        keyboard.press('a')
                        time.sleep(1)
                        keyboard.release('a')

                elif query[0] == 'right' or query[0] == 'write':
                        keyboard.press('d')
                        time.sleep(1)
                        keyboard.release('d')

                elif query[0] == 'back':
                        keyboard.press('s')
                        time.sleep(1)
                        keyboard.release('s')
                
                elif query[0] == 'jump':
                        keyboard.press('space')
                        keyboard.release('space')

                elif query[0] == 'run':
                        keyboard.press('shift')
                        keyboard.press('w')
                        time.sleep(3)
                        keyboard.release('shift')
                        keyboard.release('w')
                
                elif query[0] == 'rump':
                        keyboard.press('shift')
                        keyboard.press('w')
                        time.sleep(0.5)
                        keyboard.press('space')
                        time.sleep(0.5)
                        keyboard.release('space')
                        keyboard.release('shift')
                        keyboard.release('w')
                
                elif query[0] == 'scroll':
                        pyautogui.scroll(100)

                elif query[0] == 'crouch':
                        keyboard.press('control')
                        
                elif query[0] == 'up':
                        keyboard.press('shift')
                        keyboard.press('w')
                        time.sleep(0.5)
                        keyboard.release('shift')
                        keyboard.release('w')
                
                elif query[0] == 'grab':
                        keyboard.press('e')
                        time.sleep(0.5)
                        keyboard.release('e')

                elif query[0] == 'clicker':
                        pyautogui.mouseDown(button='right')
                        time.sleep(1)
                        pyautogui.mouseUp(button='right')
                
                elif query[0] == 'toggle':
                        pyautogui.mouseDown(button='left')

                elif query[0] == 'release':
                        keyboard.press('g')
                        keyboard.release('g')
                
                # SITUATIONAL, MAY NOT WORK ON SOME GAMES DUE TO ANTICHEAT

                elif query[0] == 'turn':
                        pyautogui.moveTo(90, 0)
                
                elif query[0] == 'turner':
                        pyautogui.moveTo(-90, 0)

                elif query[0] == 'help':
                        speak('Here are a list of commands you can use')
                        print("Usage: <command>\n"
                                "Commands: \n"
                                "\t--forward--\n"
                                "\t--left--\n"
                                "\t--right--\n"
                                "\t--back--\n"
                                "\t--jump--\n"
                                "\t--run--\n"
                                "\t--scroll--\n"
                                "\t--crouch--\n"
                                "\t--up--\n"
                                "\t--grab--\n"
                                "\t--clicker--\n"
                                "\t--toggle--\n"
                                "\t--release--\n"
                                "\t--turn--\n"
                                "\t--turner--\n"
                                "\t--exit--\n")
                        
                # Stops AI
                elif query[0] == 'exit':
                        speak('Exiting')
                break

if __name__ == '__main__':
    main()