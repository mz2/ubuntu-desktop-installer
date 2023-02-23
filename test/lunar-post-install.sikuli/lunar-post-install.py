import shutil

screen = Screen()

try:

    wait("1675119886175.png", 60)
    wait("1675119898202.png", 60)

except:
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
