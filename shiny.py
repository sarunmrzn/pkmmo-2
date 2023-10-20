import keyboard
from pyautogui import (
    locateOnScreen,
    press,
    locateCenterOnScreen,
)


def find_and_press(image_path, action_key, confidence=0.5):
    location = locateCenterOnScreen(image_path, grayscale=True, confidence=confidence)
    if location:
        print(f"{image_path} found")
        for _ in range(3):
            press(action_key)


start_key = "n"
stop_key = " "
action_key = "z"
scent_key = "4"

bot_running = False

while True:
    if bot_running:
        if not locateOnScreen("battle.png", grayscale=True, confidence=0.5):
            press(scent_key)
            find_and_press("leppa.png", action_key, confidence=0.8)
        else:
            find_and_press("run.png", action_key, confidence=0.9)
    if keyboard.is_pressed(stop_key):
        bot_running = False
        print("Bot stopped")
    if keyboard.is_pressed(start_key):
        bot_running = True
        print("Bot started")
