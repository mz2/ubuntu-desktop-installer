# findText("Try or install Ubuntu")
#wait("try_or_install_ubuntu.png", 1800)

# assert "ubuntu_safe_graphics.png"
#type(Key.DOWN)
#type(Key.ENTER)

# wait("jammy_jellyfish.png", 1800)
# wait("installer_panel_icon.png", 1800)
# click("installer_panel_icon.png")

wait("install_ubuntu.png", 1800)

click("continue.png")
click("1663606007708.png")
click("continue.png")
wait("type_here.png")
click("type_here.png")
type("dogflap")
click("continue.png")

#assert "use_wired_connection.png"
click("continue.png")

# assert "normal_installation.png"
click("minimal_installation.png")
click("continue.png")

#assert "erase_disk.png"
click("continue.png")

#assert "write_changes_to_disk.png"

wait("1660739976913.png", 1800)
click("start_installing.png")
assert "where_are_you.png"
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

#assert "copying_files.png"
wait("installation_complete.png", 1800)
# click("restart_into_ubuntu.png")
click("1660759005575.png")

# findText("Please remove the installation medium, then press ENTER")
wait("1660758282205.png", 1800)
# wait("please_remove_installation_medium.png", 1800)
type(Key.ENTER)
