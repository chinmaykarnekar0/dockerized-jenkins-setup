import os
import subprocess
import sys

VENV_NAME = "venv"

REQUIRED_FOLDERS = [
    "jenkins_home",
    "screenshots",
    "pipelines"
]

def create_required_folders():

    print("\nChecking project folders...")

    for folder in REQUIRED_FOLDERS:

        if not os.path.exists(folder):

            os.makedirs(folder)
            print(f"Created folder: {folder}")

        else:
            print(f"Folder already exists: {folder}")

def create_venv():

    print("\nChecking virtual environment...")

    if not os.path.exists(VENV_NAME):

        subprocess.run(
            ["python", "-m", "venv", VENV_NAME],
            check=True
        )

        print("Virtual environment created successfully.")

    else:
        print("Virtual environment already exists.")

def install_requirements():

    print("\nInstalling project dependencies...")

    pip_path = os.path.join(
        VENV_NAME,
        "Scripts",
        "pip.exe"
    )

    subprocess.run(
        [pip_path, "install", "-r", "requirements.txt"],
        check=True
    )

    print("Dependencies installed successfully.")

def check_docker():

    print("\nChecking Docker installation...")

    try:

        subprocess.run(
            ["docker", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print("Docker is installed.")

    except Exception:

        print("Docker is not installed or not running.")
        sys.exit(1)

def build_jenkins_image():

    print("\nBuilding Jenkins Docker image...")

    try:

        subprocess.run(
            ["docker", "compose", "build"],
            check=True
        )

        print("Jenkins image built successfully.")

    except subprocess.CalledProcessError:

        print("Failed to build Jenkins image.")
        sys.exit(1)

def start_jenkins():

    print("\nStarting Jenkins services...")

    try:

        subprocess.run(
            ["docker", "compose", "up", "-d"],
            check=True
        )

        print("\nJenkins services started successfully.")

    except subprocess.CalledProcessError:

        print("\nFailed to start Jenkins services.")
        sys.exit(1)

def show_container_status():

    print("\nFetching container status...\n")

    subprocess.run(["docker", "ps"])

if __name__ == "__main__":

    print("=" * 60)
    print("Dockerized Jenkins Local Environment Startup")
    print("=" * 60)

    create_required_folders()
    create_venv()
    install_requirements()
    check_docker()
    build_jenkins_image()
    start_jenkins()
    show_container_status()

    print("\nEnvironment setup completed successfully.")