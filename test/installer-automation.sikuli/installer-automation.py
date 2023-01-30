# wait("install_ubuntu.png")

wait("english.png", 90)

click("continue.png")
click("1663606007708.png")
click("continue.png")
wait("type_here.png")
click("type_here.png")
type("dogflap")
click("continue.png")

click("1675066734616.png")
click("continue.png")

click("1675066757916.png")
click("continue.png")

click("1675066774477.png")
click("continue.png")
wait("1660739976913.png")
click("start_installing.png")
wait("where_are_you.png")
click("continue.png")

assert "disabled_continue.png"
click("your_name_placeholder.png")
type("Dustin Henderson")
click("1660732897015.png")
type("a", Key.CTRL)

type("Falkor")

click("1660733380533.png")
type("a", Key.CTRL)
type("dustin")

click("1660732634756.png")
type("herptyderp")

click("1660732681771.png")
type("herptyderp")
click("continue.png")

# assert "copying_files.png"
wait("installation_complete.png", 1800)
# click("restart_into_ubuntu.png")
click("1660759005575.png")

# findText("Please remove the installation medium, then press ENTER")
wait("1660758282205.png", 1800)
# wait("please_remove_installation_medium.png", 1800)
# type(Key.ENTER)
