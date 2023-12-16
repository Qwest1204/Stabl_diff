import datetime

def write_to_log(promt):
    log_file = open("Log.txt", "a+", encoding="utf-8")
    log_file.write(f"[{datetime.datetime.today()}], {promt}\n")
    log_file.close()

