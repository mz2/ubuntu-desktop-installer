screen = Screen()

opts = OCR.Options()
opts.textHeight(22)
# textHeight(Offset(76, 25)

# screen.findText("Resize to").click()

click("1674910578664.png")
doubleClick(Pattern("1674911309091.png").targetOffset(48,0))
type("1920")
doubleClick(Pattern("1674910635006.png").targetOffset(49,1))
type("1080")

click("1674913542390.png")

#screen.findText("Options").click()
click("1675065478360.png")

screen.findText("Options").click()
click("1675065666811.png")

#wait(3600)
# screen.findText("Scale display").click()
#screen.findText("Resize guest to match window size").click()
