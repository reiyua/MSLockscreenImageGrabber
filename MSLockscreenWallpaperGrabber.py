# reiyua, rei@reiyua.lol, 2023
# This is a simple python script which copies the images from the Microsoft Lockscreen Wallpaper Directory in AppData, append them with ".jpg" and place them in a directory of the user's choosing.

import os
import shutil
import time

# Set the source and destination directories (Replace \ with / before imputting)
source = 'C:/Users/User/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/' #Replace "User" with your username
destination = 'See Comment next to line for info' # Replace  with the directory you want to copy the files to, swapping "\" with "/" Example: 'C:/Users/User/Username/

# Print message stating code has started
print ("Task started, please wait...")
time.sleep(1)

# Copy files from the system directory to a directory of the user's choice
for file_name in os.listdir(source):
    if file_name.endswith(''):
        shutil.copy(os.path.join(source, file_name), destination)

        
        # UNDER CONSTRUCTION

        # Add handling for existing files by skipping them
     #elif file_name.endswith('.jpg'):
        #continue
            
  
# Append .jpg to end of file name (Windows doesn't do this by default)
for filename in os.listdir(destination):
    os.rename(destination + filename, destination + filename + '.jpg')


# Print message stating code has executed sucsessfully
print ("Task completed succsessfully, please look at destination folder for results.")

# Delay closing of window by 5 seconds
time.sleep(5)

