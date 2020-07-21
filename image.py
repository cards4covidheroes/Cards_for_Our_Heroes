from PIL import Image
import glob, os

size = 300, 300

for infile in glob.glob("./input/*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    outfile = file.replace("input", "output")
    outfile = outfile + "_t.jpg"
    im.save(outfile, "JPEG")