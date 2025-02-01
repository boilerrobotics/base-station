import subprocess

with open("output.txt", "w") as f:
    result = subprocess.run(["ping", "192.168.0.102"], stdout=f, text = True)
