# If any of the width or height is less than L, the photo is rejected and ---> print “UPLOAD ANOTHER”.
# If both, width and height, are larger than LxL and If the photo is already square --> Print “ACCEPTED”. Otherwise --->  Print “CROP IT”

from PIL import Image


def checkimage(Leng):
    img = Image.open('test.png')

    width, height = img.size
    
    print(width, height)

    if width < Leng or height < Leng:
        print("UPLOAD ANOTHER")
        return
    elif width == Leng and height == Leng:
        print("ACCEPTED")
        return
    elif width >= Leng and height >= Leng and width == height:
        print("ACCEPTED")
        return
    elif width >= Leng or height >= Leng and width != height:
        print("Crop It!")
        return


if __name__ == '__main__':

    L = int(input("L = ").strip())

    checkimage(L)
