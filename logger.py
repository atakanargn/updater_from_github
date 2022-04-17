from os import mkdir
from datetime import datetime
from traceback import format_exc

line_limit=20

def log_exception(func):
    global line_limit
    def trycatch(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            try:
                mkdir("./logs")
            except:
                pass
            
            error = format_exc()
            
            now = datetime.now()
            log = "[ ERROR ][ {} ]\n{}\n".format(now.strftime("%H:%M:%S"),error)
            print(log)
            try:
                with open("./logs/LOG_{}.txt".format(now.strftime("%d-%m-%Y")),"r+") as file:
                    lines = file.readlines()
                    lines = lines[line_limit-len(lines)+len(log.split("\n")):] if len(lines)+len(log.split("\n"))>line_limit else lines
                    log   = "".join(lines) + log
            except:
                pass

            with open("./logs/LOG_{}.txt".format(now.strftime("%d-%m-%Y")),"w+") as file:
                file.write(log)
    return trycatch