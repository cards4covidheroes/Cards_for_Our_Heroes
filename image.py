from PIL import Image
import glob, os

size = 300, 300


for infile in glob.glob("images/*.*"):
    file, ext = os.path.splitext(infile)
    if ext == ".pdf":
        continue
    im = Image.open(infile)
    im.thumbnail(size)
    outfile = file.replace("images", "output")
    outfile = outfile + "_t"+ext
    if ext == ".jpg":
        im.save(outfile, "JPEG")
    if ext == ".png":
        im.save(outfile, "PNG")
