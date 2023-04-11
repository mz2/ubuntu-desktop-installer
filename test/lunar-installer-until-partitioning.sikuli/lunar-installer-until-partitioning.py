import shutil

try:
    wait("english.png", 90)

    click("next.png")
    click("install-ubuntu.png")
    click("next.png")
    
    click("type-here-to-test-your-keyboard.png")
    type("dogflap")
    click("next.png")

    click("use_wired_connection.png")
    click("next.png")

    click("minimal_installation.png")
    click("next.png")


except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
