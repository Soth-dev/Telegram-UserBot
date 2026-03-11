import os
import random


def randimg():
    img_dir = "./tgubot/assets/images/background"
    if os.path.exists(img_dir):
        files = os.listdir(img_dir)
        if files == []:
            return None
        return f"{img_dir}/{random.choice(files)}"
    return None
