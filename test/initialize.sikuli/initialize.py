screen = Screen()

opts = OCR.Options()

opts.textHeight(22)
# textHeight(Offset(76, 25)

screen.findText("Resize to").click()

# click("1674910578664.png")
doubleClick(Pattern("1674911309091.png").targetOffset(48,0))
type("1280")
doubleClick(Pattern("1674910635006.png").targetOffset(49,1))
type("1024")

click("1674913542390.png")

screen.findText("Options").click()
screen.findText("Resize guest to match window size").click()