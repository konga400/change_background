        import ctypes
        import os
        import sys
        from random import randrange


        x = randrange(3)

        pathname = os.path.dirname(sys.argv[0])        
        pathname.replace("change_background.py", "")
        pathname = pathname + "/Pictures/"

        def change_pic(image_name):
            pathToJpg = os.path.normpath("{}{}".format(pathname, image_name))
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToJpg, 0)

        if x == 0:
            change_pic("image1.jpg")

        if x == 1:
            change_pic("image2.jpg")

        if x == 2:
            change_pic("image3.jpg")



