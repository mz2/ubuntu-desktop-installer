from sikuli import *

opts = OCR.Options()
opts.textHeight(30)

class Partitioner():
    def partition(self, size_in_mb):
        click("free_space.png")
        click("plus.png")
        click(Pattern("size.png").targetOffset(117,1))
        type(str(size_in_mb))
        click(Pattern("mount_point.png").targetOffset(106,-2))
        click("slash.png")
        click("ok.png")