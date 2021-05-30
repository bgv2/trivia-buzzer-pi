# trivia-buzzer-pi
Use your Raspberry Pi + AIY Project Voice Kit as a trivia buzzer. Code can be adapted to almost any buzzer website that can be keyboard operated. Currently designed for [buzzin.live](https://buzzin.live).
## What you need
1. Raspberry Pi with Raspbian installed (this includes Chromium)
2. AIY Voice Kit (this is designed for V1, with some Python knowledge you could probably adapt this for any hardware button)
3. An mp3 file called `start.mp3` in the same directory as these files (you can try a tone from [here](https://theinteractivist.com/free-ringtones-iringpro/)—make sure to download the Android versions)
## How it works
You need to install the dependencies first, `pychrome` and `pynput` (both available with Pip) and [`aiy`](https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/HACKING.md#install-aiy-software-on-an-existing-raspbian-system) (most of the steps in the article aren't needed for the Voice Kit V1) or whatever your button needs.
1. You run the Python script.
2. In the Chromium window that opens, you enter the code for your Buzzin game, then push your hardware button.
3. After the script runs some code to unmute the buzzer, you can then use your hardware button to operate the buzzer, since it basically pushes the <kbd>B</kbd> key. You can unplug the monitor at this point.
4. When you're done with the game, you press <kbd>Ctrl</kbd> + <kbd>C</kbd> in the terminal to stop the program and close the browser.
