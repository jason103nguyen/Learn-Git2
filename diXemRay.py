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

print("Flycam is running ...")
setLichTrinh(1000, "Tan Nghia")
autoTakingOff()


