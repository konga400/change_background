import ctypes
import os
from random import randrange

dir_name = "Pictures"
pathname = os.getcwd()
pathname_pic = pathname + "/{}".format(dir_name)
if not os.path.exists(pathname_pic):
    os.mkdir(pathname_pic)
    print("Created directory called \"{}\". Place pictures inside new directory".format(dir_name))


files_in_dir = []

# r=>root, d=>directories, f=>files
# this grabs all of the images in the directory
for r, d, f in os.walk(pathname_pic):
   for item in f:
      if '.jpg' in item:
         files_in_dir.append(os.path.join(r, item))
      if '.png' in item:
         files_in_dir.append(os.path.join(r, item))


def change_pic():
   if len(files_in_dir) == 0:
      print("You don't have any pictures in your directory")
   else:
      x = randrange(len(files_in_dir))
      print("Picture chosen: {}".format(files_in_dir[x]))
      pathToJpg = files_in_dir[x]
      SPI_SETDESKWALLPAPER = 20
      ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToJpg, 0)
      x = x - 1


if __name__ == "__main__":
   change_pic()




