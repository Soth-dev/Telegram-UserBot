from subprocess import Popen as SSSU, PIPE, STDOUT
def SSU(C, **kw):
    return SSSU([SHELL_PATH, '-c', C], stdout=PIPE, stderr=STDOUT, text=True, **kw)