import keyboard
from pyautogui import locateOnScreen, click, locateCenterOnScreen, keyUp, keyDown
import time


def find_and_press(image_path, confidence=0.5):
    runaway_location = locateCenterOnScreen(
        image_path, grayscale=True, confidence=confidence
    )

    if (
        runaway_location
        and hasattr(runaway_location, "x")
        and hasattr(runaway_location, "y")
    ):
        print("Runaway found")
        click(runaway_location.x, runaway_location.y)
        click(runaway_location.x, runaway_location.y)
        click(runaway_location.x, runaway_location.y)


start_key = "n"
stop_key = " "
move_keys = ["j", "k"]

bot_running = False

while True:
    if bot_running:
        start_time = time.time()
        found = locateOnScreen("battle_single.png", grayscale=True, confidence=0.5)
        if found:
            find_and_press("run_2.png", confidence=0.9)
        else:
            if time.time() % 1 < 0.5:
                keyDown("j")
                time.sleep(0.3)
                keyUp("j")
                time.sleep(0.3)
                keyDown("k")
                time.sleep(0.3)
                keyUp("j")
                time.sleep(0.3)

    if keyboard.is_pressed(stop_key):
        bot_running = False
        print("Bot stopped")
    if keyboard.is_pressed(start_key):
        bot_running = True
        print("Bot started")
