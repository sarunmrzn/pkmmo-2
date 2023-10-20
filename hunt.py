import keyboard
from pyautogui import locateOnScreen, click, locateCenterOnScreen, keyDown, keyUp
from time import sleep


def find_and_press(image_path, confidence=0.5):
    runaway_location = locateCenterOnScreen(
        image_path, grayscale=True, confidence=confidence
    )
    if runaway_location:
        print("Runaway found")
        for _ in range(3):
            click(runaway_location.x, runaway_location.y)


start_key = "n"
stop_key = " "
bot_running = False

while True:
    if bot_running:
        found = locateOnScreen("battle_org_single.png", grayscale=True, confidence=0.7)
        if found:
            find_and_press("run_org.png", confidence=0.9)
        else:
            keyDown("h")
            sleep(0.3)
            keyUp("h")
            keyDown("l")
            sleep(0.3)
            keyUp("l")

    if keyboard.is_pressed(stop_key):
        bot_running = False
        print("Bot stopped")
    if keyboard.is_pressed(start_key):
        bot_running = True
        print("Bot started")
