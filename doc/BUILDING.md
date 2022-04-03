# Building Tic Tac Py

# Windows
## Prerequisites
OS: Windows 8.1/10/11 (amd64), Server 2012 R2/2016/2019/2022
Processor¹: Intel Core 2 Duo E4400 @ 2 GHz, AMD Athlon 64 X2 3600+ @ 2 GHz or better amd64-compatible processor
RAM²: 4 GB or more
HDD: 1 GB free space or more

¹ Windows 11 enforces much newer processors for setup
² You must have at least 6 GB when running Windows 11

## Instructions
1. Go to https://www.python.org/downloads
2. Click the download button for the newest version of Python 3.10
3. Scroll down and select "Windows Installer (64-bit)"
4. When the download is complete, run the executable
5. Check "Add Python 3.10 to PATH"
6. Click on "Install Now"
7. After installation, get the source code onto your computer.
8. Open a command prompt in the source code folder and type: py -3.10 -m pip install --upgrade pip PyInstaller requests
9. Then, type: py -3.10 -m PyInstaller --onefile --icon .\ttpicon.ico .\main.py
10. After completion, copy all files from the source code to the dist folder.
11. You should have a running main.exe file.

# Linux
## Prerequisites
Linux kernel: 4.18 or newer
X11 with GUI
Processor: Intel Core 2 Duo E4400 @ 2 GHz, AMD Athlon 64 X2 3600+ @ 2 GHz or better amd64-compatible processor
RAM: 4 GB or more
HDD: 1 GB free space or more

## Instructions
1. Check if you have Python 3 installed: python3 --version
2. Install the tkinter and pip modules. The command depends on the distribution. Here are some examples
   Debian/Ubuntu: sudo apt-get update && sudo apt-get install python3-tk python3-pip
   Fedora/RHEL: sudo dnf install python3-tkinter python3-pip
   SUSE: sudo zypper in python-tk python-pip
   Arch: sudo pacman -S tk python-pip
3. Install the requests and PyInstaller module: python3 -m pip install --upgrade requests PyInstaller
4. Then, type: python3 -m PyInstaller --onefile .\main.py
5. After completion, copy all files from the source code to the dist folder.
6. You should have a running main file.

# BSD
## Prerequisites
BSD: FreeBSD 12.3 or newer
X11 with GUI
Processor: Intel Core 2 Duo E4400 @ 2 GHz, AMD Athlon 64 X2 3600+ @ 2 GHz or better amd64-compatible processor
RAM: 4 GB or more
HDD: 1 GB free space or more

## Instructions
1. Switch to a virtual terminal where you can login as root.
2. Install Python 3.10: pkg install python310
3. Install the tkinter and pip modules: pkg install py310-tkinter py310-pip
4. Install the requests and PyInstaller module: python310 -m pip install --upgrade requests PyInstaller
5. Then, type: python310 -m PyInstaller --onefile .\main.py
6. After completion, copy all files from the source code to the dist folder.
7. You should have a running main file.
