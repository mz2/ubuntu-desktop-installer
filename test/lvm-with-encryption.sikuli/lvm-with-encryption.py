import shutil

try:

    click(Pattern("advanced_features.png").similar(0.62))
    click("use_lvm_with_new_ubuntu_installation.png")
    click("encrypt_new_ubuntu_installation.png")

    click("ok.png")

    click("next.png")

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)
