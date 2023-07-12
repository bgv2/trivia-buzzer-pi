#!/usr/bin/python3
from aiy.board import Board, Led
#from aiy.voice.audio import aplay
from signal import signal, SIGINT
from pynput.keyboard import Key, Controller
import sys
import pychrome
import subprocess
import io

keyboard = Controller()
url = "https://buzzin.live/play"
browserbin = "chromium-browser"

def run_js(tab, code):
    return tab.call_method("Runtime.evaluate", expression=code)

def stop_browser():
    print("Closing the browser...")
    subprocess.Popen(['pkill', '--oldest', 'chromium*'], stderr=subprocess.STDOUT)

def main():
    print("Trivia Buzzer")
    # stop_browser() # close Chromium if it's already open
    print("Opening Buzzin.live...")
    cp = subprocess.Popen([browserbin, '--remote-debugging-port=9222', '--app=' + url], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in io.TextIOWrapper(cp.stdout, encoding="utf-8"): # wait for Chromium to open
        if ("DevTools listening on ws://127.0.0.1" in line):
            break
    print("Browser ready")
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    tab = browser.list_tab()[0]
    tab.start()
    subprocess.Popen(["mplayer", "start.mp3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    with Board() as board:
        print('Press the button when you have joined the game')
        print('LED is ON while button is pressed (Ctrl-C for exit).')
        board.button.wait_for_press()
        run_js(tab, "document.getElementById('mute').checked = true") # turn buzzin sound on
        board.led.state = Led.PULSE_SLOW
        while True:
            board.button.wait_for_press()
            board.led.state = Led.ON
            print('Pressed')
            keyboard.press('b') # alternative: run_js(tab, 'document.getElementById("buzzer").click()')
            #board.led.state = Led.DECAY
            board.button.wait_for_release()
            keyboard.release('b')
            board.led.state = Led.PULSE_SLOW
            print('Released')
            

def stop_program():
  print('stopping program...')
  stop_browser()
  with Board() as board:
       board.led.state = Led.OFF
  sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, Exception) as err:
        print(err)
        stop_program()
