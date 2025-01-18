import subprocess
import psutil
import time
import os

username = os.getlogin()

def is_spotify_running():
    """Check if Spotify is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Spotify.exe':
            return True
    return False

def close_spotify():
    """Close Spotify if it's running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Spotify.exe':
            process.kill()
            print("closed spotify")

def open_spotify():
    """Open Spotify."""
    subprocess.Popen([f'C:\\Users\\{username}\\AppData\\Roaming\\Spotify\\Spotify.exe'])
    print("opened spotify")

powershell_command = "iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex"

if is_spotify_running():
    close_spotify()

try:
    result = subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-Command', powershell_command], 
                            capture_output=True, text=True, check=True)
    print("output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("error:\n", e.stderr)

time.sleep(2)

open_spotify()