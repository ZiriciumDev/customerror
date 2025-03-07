import time
class customerror(Exception):
    def __init__(self, message=''):
        pass
def error(MainMessage:str, ReturnMessage:str):
    def keyint():
        time.sleep(0.8)
        customerror.__init__(str(ReturnMessage))
        customerror.__name__ = MainMessage
        raise customerror(ReturnMessage) from None
    t = keyint()
    return t
def trye(errorname:str, code:str):
    try:
        exec(code)
    except customerror:
        if customerror.__name__ == errorname:
            return True
def checkerr(errorname:str):
    if customerror.__name__ == errorname:
        return True