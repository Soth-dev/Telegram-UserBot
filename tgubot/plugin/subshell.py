from subprocess import Popen as SSSU, PIPE, STDOUT
import os

SHELL_PATH = os.getenv("SHELL_PATH")
if not SHELL_PATH:
    SHELL_PATH = "/bin/bash"


def SSU(C, **kw):
    return SSSU([SHELL_PATH, "-c", C], stdout=PIPE, stderr=STDOUT, text=True, **kw)


def SU(C):
    o = SSU(C).stdout
    if o:
        return o.read()
    return ""
