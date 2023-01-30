screen = Screen()

opts = OCR.Options()
opts.textHeight(22)

click("options.png")
# screen.findText("Options").click()
click("scale_display.png")

click("options.png")
# screen.findText("Options").click()
click("resize_guest.png")


# textHeight(Offset(76, 25)

# screen.findText("Resize to").click()

click("resize_to.png")
doubleClick(Pattern("width.png").targetOffset(48, 0))
type("1920")
doubleClick(Pattern("height.png").targetOffset(49, 1))
type("1080")

click("apply.png")

# wait(3600)
# screen.findText("Scale display").click()
# screen.findText("Resize guest to match window size").click()
