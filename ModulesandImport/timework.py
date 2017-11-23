import time
from time import time as myTime
import random

input("Press enter to start:  ")
start = myTime()
input("Press enter to stop :  ")
end = myTime()

print("Started at "+time.strftime("%X", time.localtime(start)))
print("Ended at "+time.strftime("%X", time.localtime(end)))

print("Total spent : {}".format(start-end))

