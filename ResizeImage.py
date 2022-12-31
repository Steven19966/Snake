from PIL import ImageTk,Image

def ResizeIMG(filename, width, height):
    im = Image.open(filename).resize((width, height))
    im = ImageTk.PhotoImage(im)
    return im