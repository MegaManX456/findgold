qqqqqqqqqqqqqqqqqimport pyautogui, time,keyboard
import numpy as np
A = (612,199)
#yA = a.xA + b
#yC = a.xB + b
#<=>199 = a.612 + b
#   yC  = a.xC  + b
time.sleep(1)
pyautogui.PAUSE = 0.001
def findgold():
    gold = pyautogui.locateCenterOnScreen("gold.png",region =(146,152,1067-146,636-152),confidence = 0.7)
    C = (gold[0],gold[1])
    a = np.array([[612,1],[C[0],1]])
    b = np.array([199,C[1]])
    res = np.linalg.solve(a,b)
    B = (round((208-res[1])/res[0]),208)
    pyautogui.moveTo(B)
    if pyautogui.pixel(B[0],B[1])[0] in range(42,80):
        pyautogui.click(B)
def findbag():
    bag = pyautogui.locateCenterOnScreen("bag.png",region =(146,152,1067-146,636-152),confidence = 0.7)
    C = (bag[0],bag[1])
    a = np.array([[612,1],[C[0],1]])
    b = np.array([199,C[1]])
    res = np.linalg.solve(a,b)
    B = (round((208-res[1])/res[0]),208)
    pyautogui.moveTo(B)
    if pyautogui.pixel(B[0],B[1])[0] in range(42,80):
        pyautogui.click(B)
while keyboard.is_pressed('q') == False:
    try:
        if pyautogui.locateOnScreen("gold.png",region =(146,152,1067-146,636-152),confidence = 0.7) != None:
            findgold()
            #print(B,pyautogui.pixel(B[0],B[1]))
        if pyautogui.locateOnScreen("bag.png",region =(146,152,1067-146,636-152),confidence = 0.7) != None:
            findbag()
    except:
        print('no')
    
    
                 
