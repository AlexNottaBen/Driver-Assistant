
#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

def Wait():
    input("Press any key to continue... ")

def SimpleInstall(RootPassword,ProgrammeName):
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt install " + ProgrammeName + " --yes"))

def DoThis(RootPassword,Command):
    os.system('echo %s|sudo -S %s' % (RootPassword,Command))

def WhatItIs(About):
    print("====================" + About + " ====================")

def UpdatePackege(RootPassword):
    print("==================== Update ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt update"))

def UpgradePackege(RootPassword):
    print("==================== Upgrade ====================")
    os.system('echo %s|sudo -S %s' % (RootPassword, "sudo apt upgrade --yes"))
    
def Logo():
    print("######################################")
    print("#        Ubuntu Driver Assistant     #")
    print("######################################")
    print("By AlexNottaBen")
    print("Support: Ubuntu 20.04+")

def ClearScreen():
    os.system("clear")
    
#Begin

ClearScreen()
Logo()
RootPassword = input("Input Root Password > ")

while True:
    
    ClearScreen()
    Logo()

    print("0 - Exit")
    print("1 - NVIDIA Driver")
    print("2 - AMD / Intel Driver Only")
    print("3 - Install Vulkan Libraryes Only")
    print("4 - Install All Driveres (1 - 2)")
    print("5 - Delete NVIDIA Driver")
    Answer = input("Answer > ")


    print("================= Start =================")

    if Answer == "0":
        exit(0)

    elif Answer == "1":
        Version = input("Version > ")
        DoThis(RootPassword,"sudo add-apt-repository ppa:graphics-drivers/ppa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt install -y nvidia-driver-" + Version + " libvulkan1 libvulkan1:i386 --yes")

    elif Answer == "2":
        DoThis(RootPassword,"sudo add-apt-repository ppa:kisak/kisak-mesa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386 --yes")

    elif Answer == "3":
        DoThis(RootPassword,"sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libvulkan1 libvulkan1:i386 --yes")
    
    elif Answer == "4":
        Version = input("Version > ")
        DoThis(RootPassword,"sudo add-apt-repository ppa:graphics-drivers/ppa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt install -y nvidia-driver-" + Version + " libvulkan1 libvulkan1:i386 --yes")
        DoThis(RootPassword,"sudo add-apt-repository ppa:kisak/kisak-mesa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386 --yes")

    elif Answer == "5":
        Version = input("Version > ")
        DoThis(RootPassword,"sudo apt purge nvidia-driver-" + Version + " --yes")

    print("================= Finish =================")
    Wait()
