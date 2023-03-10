#7
from shutil import copyfile
copyfile('D.txt', 'A.txt')

#8
import os
if os.path.exists('C:\\Users\\asus\\Desktop\\pp2\\week6\\filetodelete.txt'):
    os.remove('C:\\Users\\asus\\Desktop\\pp2\\week6\\filetodelete.txt')
else:
    print("Such file does not exist!")
