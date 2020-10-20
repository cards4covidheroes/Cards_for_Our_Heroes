from PIL import Image
import glob, os

size = 300, 300

<<<<<<< HEAD

for infile in glob.glob("images/*.*"):
=======
for infile in glob.glob("./input/*.jpg" or "./input/*.png"):
>>>>>>> 0d68eb1792672f40aed02c4875e34cf0aa088de6
    file, ext = os.path.splitext(infile)
    if ext == ".pdf":
        continue
    im = Image.open(infile)
    im.thumbnail(size)
<<<<<<< HEAD
    outfile = file.replace("images", "output")
    outfile = outfile + "_t"+ext
    if ext == ".jpg":
        im.save(outfile, "JPEG")
    if ext == ".png":
        im.save(outfile, "PNG")
=======
    file.replace("input", "output")
    if ext == ".jpg":
        outfile = outfile + "_t.jpg"
        im.save(outfile, "JPEG")
    elif ext == ".png":
        outfile = outfile +"_t.png"
        im.save(outfile, "PNG")
>>>>>>> 0d68eb1792672f40aed02c4875e34cf0aa088de6
