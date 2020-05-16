"""
Day la chuong trinh may bay flycam dung de di tham ray

Feature 2: bay theo lich trinh co san
Feature 3: tu dong ha canh
Feature 4: tu dong cat canh
"""

def setLichTrinh(doCao, diaDiem):
	print("Do cao la: ", doCao)
	print("Dia diem la: ", diaDiem)

def autoTakingOff():
	from time import sleep
	timeTakingOff = 10
	while timeTakingOff > 0:
		print("Flycam is taking off: ", timeTakingOff)
		sleep(1)
		timeTakingOff -= 1

def autoLanding():
	from time import sleep
	timeLanding = 7
	while timeLanding > 0:
		print("Flycam is landing: ", timeLanding)
		sleep(1)
		timeLanding -= 1

print("Flycam is running ...")
levelHigh = input("Nhap do cao: ")
local = input("Nhap dia diem: ")
setLichTrinh(levelHigh,local)
autoTakingOff()
autoLanding()


