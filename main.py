import pyautogui
from PIL import Image, ImageGrab
# from numpy import asfarray
import time


# below func is made such that it will ake the action once we press down arrow key
def hit(key):
    pyautogui.press(key)


def isCollide(data):

    # draw for the rectangle for birds
    for i in range(370, 400):
        for j in range(450, 500):
            if data[i, j] < 100:
                hit('down')
                return True  # wil stop the execution of later statements if ret is true
    # draw the rectangle for cactus
    for i in range(370, 430):
        for j in range(210, 450):
            if data[i, j] < 100:
                hit('down')
                return True

    return False


if __name__ == "__main__":
    print('dino game will start in 3 sec be ready!')
    time.sleep(3)
    # hit('up')  # this is used to start(init) the game
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(nparray(image))
        if isCollide(data):
            hit('up')
        '''    
        # draw for the rectangle for birds
        for i in range(370, 400):
            for j in range(450, 500):
                data[i, j] = 171
        image.show()

        # draw the rectangle for cactus
        for i in range(370, 430):
            for j in range(210, 450):
                data[i, j] = 0
        image.show()
        break
        '''
