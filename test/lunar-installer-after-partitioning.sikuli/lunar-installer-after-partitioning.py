import shutil

try:
    wait("select_your_timezone.png")

    sleep(2)
    click("next.png")

    
    click(Pattern("your_name.png").targetOffset(0,15))
    type("Dustin Henderson")
    click(Pattern("1676326082146.png").targetOffset(-11, 19))
    type("a", Key.CTRL)

    type("Falkor")

    click(Pattern("1676326124343.png").targetOffset(-8, 17))
    type("a", Key.CTRL)
    type("dustin")

    click("1676326150218.png")
    type("herptyderp")

    click("1676326159422.png")
    type("herptyderp")

    click("require-my-password-to-login.png")
    click("next.png")
    wait("light-mode.png")
    click("light-mode.png")
    click("next.png")

    wait("restart_now.png", 3800)

    click("restart_now.png")

    # findText("Please remove the installation medium, then press ENTER")
    wait("remove_installation_medium.png", 60)
    type(Key.ENTER)

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
