from PIL import Image
import os
import zoom_out_img

def rotate_img():

    def rotate_img(img_path, rt_degr):
        img = Image.open(img_path)
        return img.rotate(rt_degr, expand=1)

    i = 0
    for f in os.listdir('extracted_grains'):
        i = i + 1
        img_rt_90 = Image.open('extracted_grains/' + f)
        a, b = img_rt_90.size
        if a > b:
            img_rt_90 = rotate_img('extracted_grains/' + f, 90)
            img_rt_90.save('extracted_grains/'+f)

    fd = zoom_out_img.zoom_out()
    return fd
