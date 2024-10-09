import subprocess
import sys

def install_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
    except subprocess.CalledProcessError:
        print("Error installing pip")
        sys.exit(1)

def install_packages():
    packages = [
        "opencv",
        "python-imaging",
        "mediapipe"
    ]
    
    for package in packages:
        subprocess.check_call(["sudo", "pacman", "-S", "--noconfirm", package])

if __name__ == "__main__":
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        install_pip()
    install_packages()