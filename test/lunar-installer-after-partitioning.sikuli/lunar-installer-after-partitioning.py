import shutil

try:
    wait("where_are_you.png")
    click("continue.png")

    wait("disabled_continue.png")
    click("1676326058165.png")
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
    click("continue.png")
    wait("light-mode.png")
    click("light-mode.png")
    click("continue.png")

    wait("installation_complete.png", 1800)
    # wait("is-installed-and-ready-to-use.png", 1800)

    click(Pattern("shut_down.png").similar(0.53))

    # findText("Please remove the installation medium, then press ENTER")
    wait("remove_installation_medium.png", 60)
    type(Key.ENTER)

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
