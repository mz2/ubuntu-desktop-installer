import shlib

try:
    wait("grub.png", 60)
    click("grub.png")
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.ENTER)

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
