import os
import shutil
import time

defualt_extention_path = 'C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data'

shutil.rmtree(defualt_extention_path)

print('wait for a minute')

time.sleep(50)

print('END')
