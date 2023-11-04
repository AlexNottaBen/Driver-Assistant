#! /usr/bin/python3
# -*- coding: utf-8 -*-
from os import system as execute

from getpass import getpass as input_password


def wait():
    input("Press any key to continue... ")


def apt_install(root_password="live", program_name="lib"):
    execute(
        "echo %s|sudo -S %s"
        % (root_password, "sudo apt install " + program_name + " --yes")
    )


def execute_as_root(root_password="live", command="echo"):
    execute("echo %s|sudo -S %s" % (root_password, command))


def logo():
    print("######################################")
    print("#          Driver Assistant          #")
    print("######################################")
    print("By Alexander")
    print("Support: Debian 10-12, Ubuntu 20.04+")


def clear():
    execute("clear")


# Begin

clear()
logo()
root_password = input_password("Input Root Password > ")

while True:
    clear()
    logo()

    print("0 - Exit")
    print("For Debian")
    print("1 - [Free] Install Software For Bluetooth")
    print("2 - AMD / Intel Driver Only")
    print("3 - Install Vulkan Libraryes Only")
    print("For Ubuntu")
    print("4 - NVIDIA Driver")
    print("5 - AMD / Intel Driver Only")
    print("6 - Install Vulkan Libraryes Only")
    print("7 - Install All Driveres (1 - 2)")
    print("8 - Delete NVIDIA Driver")
    print("\nr - Open Repositories List")

    answer = input("Answer > ")

    print("================= Start =================")

    if answer == "0":
        exit(0)

    if answer == "1":
        execute_as_root(
            root_password,
            "sudo apt install bluetooth bluez bluez-cups bluez-tools btscanner gnome-bluetooth pulseaudio-module-bluetooth --yes",
        )
        execute_as_root(root_password, "lsmod | grep bluetooth")
        execute_as_root(root_password, "/etc/init.d/bluetooth status")
        execute_as_root(root_password, "/etc/init.d/bluetooth start")
        execute_as_root(root_password, "sudo apt install blueman --yes")

    elif answer == "2":
        execute_as_root(
            root_password,
            "sudo apt install firmware-linux firmware-linux-nonfree libdrm-amdgpu1 xserver-xorg-video-amdgpu --yes",
        )
        execute_as_root(
            root_password,
            "sudo apt install mesa-vulkan-drivers libvulkan1 vulkan-tools  vulkan-validationlayers --yes",
        )
        execute_as_root(root_password, "sudo apt install mesa-opencl-icd --yes")

    elif answer == "3":
        execute_as_root(
            root_password,
            "sudo apt install mesa-vulkan-drivers libvulkan1 vulkan-tools vulkan-utils vulkan-validationlayers --yes",
        )

    # Ubuntu

    elif answer == "4":
        version = input("Version > ")
        execute_as_root(
            root_password,
            "sudo add-apt-repository ppa:graphics-drivers/ppa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt install -y nvidia-driver-"
            + version
            + " libvulkan1 libvulkan1:i386 --yes",
        )

    elif answer == "5":
        execute_as_root(
            root_password,
            "sudo add-apt-repository ppa:kisak/kisak-mesa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386 --yes",
        )

    elif answer == "6":
        execute_as_root(
            root_password,
            "sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libvulkan1 libvulkan1:i386 --yes",
        )

    elif answer == "7":
        version = input("Version > ")
        execute_as_root(
            root_password,
            "sudo add-apt-repository ppa:graphics-drivers/ppa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt install -y nvidia-driver-"
            + version
            + " libvulkan1 libvulkan1:i386 --yes",
        )
        execute_as_root(
            root_password,
            "sudo add-apt-repository ppa:kisak/kisak-mesa && sudo dpkg --add-architecture i386 && sudo apt update && sudo apt upgrade && sudo apt install libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386 --yes",
        )

    elif answer == "8":
        version = input("Version > ")
        execute_as_root(
            root_password, "sudo apt purge nvidia-driver-" + version + " --yes"
        )

    elif answer == "r":
        apt_install(root_password, "mousepad")
        execute_as_root(root_password, "sudo mousepad /etc/apt/sources.list")

    print("================= Finish =================")
    wait()
