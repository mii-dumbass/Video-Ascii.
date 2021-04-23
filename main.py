import sys
import os
import time
import cv2
from PIL import Image
#cv2 needs to be manually installed if using pycharm
#keep pygame after os.environ part, IMPORTANT
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

audio = input("What song do you want to play? (for path use the C:/Users/entername/filename.filetype) ")
video = input("What video do you want to play? (make sure you also use path for the video too)")
#inputs you should make your own command to stop it :) 

sys.tracebacklimit = 0

cap = cv2.VideoCapture(video)

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[91mUse fullscreen console for better experience. | Made for Windows command line.\033[37m')

try:
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    print('\033[32mSong found.\033[37m')
except Exception as e:
    print('\033[93mNot using song.\033[37m')
    print(e)

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "i", " "]

size = 220
# make sure you change size throughout, I recommend atleast 200+

pygame.mixer.music.play()


def resized_gray_image(image, new_width=size):
    width, height = image.size
    width = width * 2
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height), Image.BICUBIC).convert('L')
    return resized_image


def pix2chars(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def generate_frame(image, new_width=size):
    new_image_data = pix2chars(resized_gray_image(image))
    total_pixels = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, total_pixels, new_width)])
    sys.stdout.write("\n" * 20 + ascii_image + '\n')


waitkey = 20
videoframe = False

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if cv2.waitKey(1) & 0xFF == ord('q'): #not functional
            break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

if videoframe:
    try:
        while True:
            ret, frame = cap.read()
            cv2.imshow("Real time video frame", frame)
            generate_frame(Image.fromarray(frame))
            cv2.waitKey(waitkey)
    except Exception as a:
        print('\n\033[32mEND\033[37m\n')
        print(a)

if not videoframe:
    try:
        while True:
            ret, frame = cap.read()
            if ret:
                generate_frame(Image.fromarray(frame))
                cv2.waitKey(waitkey)
    except Exception as b:
        print('\n\033[32mEND\033[37m\n')
        print(b)
        sys.exit()

time.sleep(10)
