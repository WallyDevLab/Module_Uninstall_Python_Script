import subprocess
import sys

def get_installed_packages():
    # Get list of installed packages
    installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode("utf-8").split("\n")[2:]
    return installed_packages

def uninstall_package(package_name):
    # Uninstall a specific package
    subprocess.call([sys.executable, "-m", "pip", "uninstall", "-y", package_name])

def uninstall_all_packages():
    installed_packages = get_installed_packages()
    for package in installed_packages:
        package_name = package.split()[0]
        uninstall_package(package_name)

if __name__ == "__main__":
    uninstall_all_packages()