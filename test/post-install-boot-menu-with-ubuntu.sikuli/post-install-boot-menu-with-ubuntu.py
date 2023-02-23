import shutil

try:
    wait("1675167311690.png", 60)
    click("1675167311690.png")
    type(Key.ENTER)
except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
