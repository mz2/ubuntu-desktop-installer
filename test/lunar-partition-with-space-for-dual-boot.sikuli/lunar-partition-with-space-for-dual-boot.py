from ../installer partitioner import Partitioner

import shlib

try:
    click("something_else.png")
    click("1675149621593.png")
    wait("allocate_disk_space.png")
    click(Pattern("device_for_boot_loader_installation.png").targetOffset(-10,41))
    click("dev_vda.png")


    # Add / partition
    click("free_space.png")
    click("plus.png")
    click(Pattern("size.png").targetOffset(117,1))
    type("10000")
    click(Pattern("mount_point.png").targetOffset(106,-2))
    click("slash.png")
    click("ok.png")


    # Add /boot partition
    click("free_space.png")
    click("plus.png")
    click(Pattern("size.png").targetOffset(117,1))
    type("1024")
    click(Pattern("mount_point.png").targetOffset(101,-3))
    click("slash_boot.png")
    click("ok.png")


    # Add swap partition
    click("free_space.png")
    click("plus.png")
    click(Pattern("size.png").targetOffset(117,1))
    type("4096")
    click(Pattern("used_as.png").similar(0.66).targetOffset(69,0))
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    click("swap_area.png")
    click("ok.png")
    click("1675149621593.png")

except:
screen = Screen()

    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
