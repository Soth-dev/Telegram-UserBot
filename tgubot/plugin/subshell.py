from subprocess import Popen as SSSU, PIPE, STDOUT
from .variable import SHELL_PATH


def SSU(C, **kw):
    return SSSU([SHELL_PATH, "-c", C], stdout=PIPE, stderr=STDOUT, text=True, **kw)


def SU(C):
    o = SSU(C).stdout
    if o:
        return o.read()
    return ""
