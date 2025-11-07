import subprocess
import time


def responseServer(ip):
    commandPing = ["ping", "-c", "4", ip]

    try:
        resultPing = subprocess.Popen(commandPing)
        #print("Output command: Ping")
        if resultPing.returncode == 0:
            print(f"Output command: Ping {resultPing.pid}")
        

    except subprocess.CalledProcessError as cPe:
        print(f"Error executing command: {' '.join(cPe.cmd)}")
        print(f"Error of return: {cPe.returncode}")
        print(f"Output Error: {cPe.stderr}")
    except FileNotFoundError:
        print(f"Error: The command 'nmap' wasn't found. Check if it's in your PATH.")

def mappingServer(ip):
    commandNmap = ["nmap", "p", "21", "80", "445", ip]

    try:
        resultNmap = subprocess.run(commandNmap, capture_output=True, text=True, check=True)
        print("Output command: Nmap")
        print(resultNmap.stdout)
        print(f"Return of code: {resultNmap.returncode}")
    except subprocess.CalledProcessError as cPe:
        print(f"Error executing command: {' '.join(cPe.cmd)}")
        print(f"Error of return: {cPe.returncode}")
        print(f"Output Error: {cPe.stderr}")
    except FileNotFoundError:
        print(f"Error: The command 'nmap' wasn't found. Check if it's in your PATH.")
    