import time
import subprocess


def start_conversation():
    print("\033[H\033[J")
    print("Welcome to the Christoperus Photobooth! We are happy you are here!")

    response = input("Do you want to take a picture? [yes, y, no, n]\n")
    return response


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
        if n == 0:
            return


def take_picture():
    subprocess.call("image.sh")
