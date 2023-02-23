import shutil

try:
    click("1675153496948.png")
    click("use_lvm_with_new_ubuntu_installation.png")
    click("encrypt_new_ubuntu_installation.png")

    click("ok.png")

    click("continue.png")

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
