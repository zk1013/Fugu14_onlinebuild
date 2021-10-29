from os.path import exists
import time
while not exists('./DONE'):
    print("not done")
    time.sleep(5)