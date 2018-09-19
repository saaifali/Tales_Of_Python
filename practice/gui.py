import pyautogui as pya

s = pya.size()

for i in s:
    print(i)

pya.moveTo(100,100, duration=1)