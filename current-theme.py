import darkdetect
import time


l = None

while True:
    t = darkdetect.theme()
    if t != l:
       print("theme is:", t)
       l = t
    time.sleep(1)
