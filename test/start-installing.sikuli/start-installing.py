import shlib

try:
    click("start_installing.png")
except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
