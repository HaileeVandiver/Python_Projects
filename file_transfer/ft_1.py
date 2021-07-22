import shutil
import os

#set where source files are
source = 'C:\Users\haile\Desktop\folderA'

#set the destination
destination = 'C:\Users\haile\Desktop\folderB'
files = os.listdir(source)

for i in files:
	#we are saying move the files represented by i to new place
	shutil.move(source+i, destination)
