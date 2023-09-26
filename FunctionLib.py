from os.path import dirname, abspath

def current_path():
    current_path = abspath(dirname(dirname(__file__)))+"/"
    return current_path

def writetosave(string):
    with open(current_path()+"savefile.txt", 'w') as f:
        f.write(string)

def readfromsave(line):
    f = open(current_path()+"savefile.txt", 'r')
    data = f.readlines()
    return data[line]
        