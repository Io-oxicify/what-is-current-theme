import darkdetect
import time


last = None

while True:
    current = darkdetect.theme()
    if current != last:
       print("theme is:", current)
       last = current
    time.sleep(1)
