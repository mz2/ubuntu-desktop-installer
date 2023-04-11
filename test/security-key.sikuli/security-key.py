try:
    click(Pattern("choose-security-key.png").similar(0.78))
    type("very-secure")

    click(Pattern("confirm-the-security-key.png").similar(0.82))
    type("very-secure")

    click("show-security-key.png")

    wait("shown-security-key.png")

    click("next.png")

except:
    screen = Screen()
    screenshot = screen.capture(screen.getBounds())
    screenshot.save("./", "screenshot.png")
    exit(-1)