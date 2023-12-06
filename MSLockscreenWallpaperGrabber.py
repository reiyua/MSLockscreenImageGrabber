# reiyua, rei@reiyua.lol, 2023

import os
import shutil

#Set the source and destination directories (Replace \ with / before imputting)
source = 'C:/Users/User/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets' #Replace "User" with your username
destination = '*INSERT USER DIRECTORY HERE* (Example: C:/Users/User/Pictures/Wallpapers/)'

#Copy files from the system directory to a directory of the user's choice
for file_name in os.listdir(source):
    if file_name.endswith(''):
        shutil.copy(os.path.join(source, file_name), destination)

# Append .jpg to end of file name (Windows doesn't do this automatically)
for filename in os.listdir(destination):
    os.rename(destination + filename, destination + filename + '.jpg')

