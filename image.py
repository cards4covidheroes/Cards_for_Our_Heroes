from PIL import Image
import glob, os

size = 300, 300

for infile in glob.glob("./input/*.jpg" or "./input/*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    file.replace("input", "output")
    if ext == ".jpg":
        outfile = outfile + "_t.jpg"
        im.save(outfile, "JPEG")
    elif ext == ".png":
        outfile = outfile +"_t.png"
        im.save(outfile, "PNG")