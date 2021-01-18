import os
subpath = "EA Games\\Dead Space 2\\settings.txt"

from fileinput import FileInput

with FileInput(files=[os.path.join(os.getenv("LOCALAPPDATA"), subpath)], inplace=True) as file:
    for line in file:
        line = line.rstrip()
        param = line.split(" ")
        if "Controls.AcL.X" in line or "Controls.AcL.Y" in line:
            param[2] = '0'
            line = " ".join(str(x) for x in param)
        print(line)
            