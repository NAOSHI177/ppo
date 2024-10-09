import subprocess
def install_packages():
    packages = [
        "opencv-python==4.6.0.66",
        "imutils==0.5.4",
        "mediapipe==0.8.10.1"
    ]
    
    for package in packages:
        subprocess.check_call(["pacman", "-S", package, "--noconfirm"])

if __name__ == "__main__":
    install_packages()
