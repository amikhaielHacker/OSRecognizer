import platform

def recognize():
    if platform.system() == "Darwin" and platform.release() >= 16.0:
        print ("MacOS")

    elif platform.system() == "Darwin" and platform.release() < 16.0:
        print ("OS X")

    elif platform.system() == "Windows" or platform.system() == "win32":
        print ("Windows")

    elif platform.system() == "linux" or platform.system() == "linux2":
        print ("Linux")

    else:
        print ("I can't recognize this OS, sorry.")

recognize()        
