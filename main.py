import webbot
import time
from webbot import Browser

# Add a way to import the driver
web = Browser()

# After that, go to collabvm. [ link: http://computernewb.com/collab-vm/ ]
print("Went to CollabVM")
web.go_to("http://computernewb.com/collab-vm/")

# Click 'continue' on the nsfw page.
web.click("Continue")

# Click on a VM
web.click("Windows 10 Enterprise 1909 x64 (VM 5)")

# Sleep and wait for the page to load
time.sleep(3)

# Click on "Take Turn" and wait 10 seconds then click on it again.
while True:
  print("Clicked 'Take Turn. Waiting 8s.....")
  web.click("Take Turn")
  time.sleep(8)