#!/usr/bin/python

import wifi_qrcode_generator
import webbrowser
from PIL import Image
import pathlib
import stdiomask
import getpass
import warnings
import os
from termcolor2 import c
from colorama import init, Fore, deinit, Style
import time

def input_password():
    vis_pass = False
    try:
        password = stdiomask.getpass("Password: " + Fore.GREEN)
        print(Style.RESET_ALL, end="")
    except:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                'error',
                category=getpass.GetPassWarning,
                module='getpass'
            )
            try:
                password = getpass.getpass("Password: " + Fore.GREEN)
                print(Style.RESET_ALL, end="")
            except getpass.GetPassWarning:
                vis_pass = True
                password = cinput("")

    if vis_pass == False:
        while True:
            show_password = cinput("Show password? (Yes/No): ").lower()
            if show_password == "no":
                return password
            elif show_password == "yes":
                print(c(password).green, end="")
                time.sleep(3)
                print("\r", end="")
                print("*"*len(password))
                while True:
                    accept_password = cinput("Is the password correct? (Yes/No): ").lower()
                    if accept_password == "yes":
                        return password
                    elif accept_password == "no":
                        return input_password()
                    print(c("Wrong Type").red)
            print(c("Wrong Type").red)
    return password


def override(image_name):
    if os.path.exists(image_name):
        print(c("File or directory \"" + image_name + "\" already exists.").red)
        while True:
            override_file = cinput(c("Override (Yes/No): ").red).lower()
            if override_file == "yes":
                return True
            elif override_file == "no":
                return False
            else:
                print(c("Wrong Type").red)
    else:
        return True


def cinput(promt):
    input_str = input(promt + Fore.GREEN)
    print(Style.RESET_ALL, end="")
    return input_str


def main():
    print(c("This program will generate QRCODE for auto WIFI connection").green.bold)
    ssid = ""
    while True:
        ssid = cinput("1) Wifi (SSID) ssid: ")

        if ssid == "":
            print(c("Wrong Type").red)
        else:
            break

    while True:
        hidden = cinput("2) Is Wifi Network SSID Hidden (Yes/No): ").lower()
        if hidden == "yes":
            hidden = True
            break
        elif hidden == "no":
            hidden = False
            break
        else:
            print(c("Wrong Type").red)

    while True:
        security = cinput("3) Security Type (WPA/WEP/None): ").upper()
        if security == "WPA" or security == "WEP" or security == "NONE":
            if security == "NONE":
                security = "nopass"
            break
        else:
            print(c("Wrong Type").red)

    password = ""
    if security != "nopass":
        while True:
            password = input_password()
            if password == "":
                print(c("Wrong Type").red)
            else:
                break
    else:
        password = None

    default_image_name = ssid + ".png"
    i = 0
    while True:
        if os.path.exists(default_image_name):
            i += 1
            default_image_name = ssid + "_" + str(i) + ".png"
        else:
            break

    while True:
        image_name = cinput(
            "4) Enter file name for QRCODE Image.\nOr hit enter for default name - " + c(
                default_image_name).green + ": ").strip().split(
            ".")[0]
        if image_name == "":
            image_name = default_image_name
            break
        else:
            image_name += ".png"
            if override(image_name):
                break

    print("File name: " + c(image_name).green)
    print("File path: " + c(str(pathlib.Path().resolve()) + "/" + image_name).green)

    qrcodeim = wifi_qrcode_generator.wifi_qrcode(ssid, hidden, security, password)
    qrcodeim.save(image_name, "PNG")

    try:
        im = Image.open(image_name)
        im.show()
    except:
        webbrowser.open(image_name)
    return 0


if __name__ == "__main__":
    init(autoreset=True)
    main()
    deinit()
