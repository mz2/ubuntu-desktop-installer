import shutil

screen = Screen()

try:
    wait("1677153028211.png", 5)
except:
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
