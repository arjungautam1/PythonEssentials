import datetime
import os
from pathlib import Path

currentDate = datetime.datetime.today()

log_path = os.path.join("/Users/arjuncodes/Desktop/" + currentDate.strftime("%Y%m%d") + "/data.py")

if os.path.exists(log_path):
    log_path = log_path
    print("File already exists")
else:
    log_path = Path("/Users/arjuncodes/Desktop/" + currentDate.strftime("%Y%m%d") + "/data.py")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    f = open(log_path, "a+")

# if os.path.exists(log_path):
#     log_path=log_path
# else:
#     log_path=Path("/Users/arjuncodes/Desktop/"+currentDate.strftime("%Y%m%d")+"/data1.py")
#     log_path.touch(exist_ok=True)
#     f=open(log_path)
