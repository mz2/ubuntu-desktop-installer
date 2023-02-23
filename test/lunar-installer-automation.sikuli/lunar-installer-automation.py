import shutil

try:
    wait("english.png", 90)

    click("continue.png")
    click(Pattern("install_ubuntu_banner.png").similar(0.56))
    click("continue.png")
    wait("type_here.png")
    click("type_here.png")
    type("dogflap")
    click("continue.png")

    click("use_wired_connection.png")
    click("continue.png")

    click("minimal_installation.png")
    click("continue.png")

    click("erase_disk_and_install_ubuntu.png")
    click("continue.png")
    wait("write_changes_to_disk.png")
    click("start_installing.png")
    wait("where_are_you.png")
    click("continue.png")

    wait("disabled_continue.png")
    click("your_name_placeholder.png")
    type("Dustin Henderson")
    click(Pattern("your-computer-name.png").targetOffset(-26, 25))
    type("a", Key.CTRL)

    type("Falkor")

    click("username_dustin_henderson.png")
    type("a", Key.CTRL)
    type("dustin")

    click("choose_password.png")
    type("herptyderp")

    click("confirm_your_password.png")
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
