# reiyua, rei@reiyua.lol, 2023
# This is a simple python script which copies the images from the Microsoft Lockscreen Wallpaper Directory in AppData, append them with ".jpg" and place them in a directory of the user's choosing.

# Import modules

import os
import shutil
from PIL import Image

# Set the source and destination directories (Replace \ with / before imputting)
source = 'C:/Users/USER/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/' #Replace "USER" with your username
destination = '' # Replace with the directory you want to copy the files to, swapping "\" with "/" Example: 'C:/Users/User/Desktop/Wallapapers
dir_list = os.listdir(source)
# Print message stating code has started
print ("Task started, please wait...")


#Main loop
for file in dir_list:
    img = Image.open(source+file)
    if img.width > img.height: # Image is Landscape and not Portrait 
        shutil.copyfile(source+file,destination+file+".jpg")




