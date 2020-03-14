import grain_extract
def hi():
    img = 'image/uploaded_img/input_image.jpg'
    fd = grain_extract.grain_extract(img)
    return fd
