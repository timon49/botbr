#pip install pyautogui
#pip install opencv-python
#pip3 install keyboard
#pip3 install pydirectinput
#pip3 install pynput


from imports import *

i = 0

current_time = datetime.now().time()

timeStart = datetime.now()

timeFinish = timeStart + timedelta(seconds=1)

pydirectinput.FAILSAFE = False

pyautogui.FAILSAFE = False

#  ======== settings ========
resume_key = Key.space
pause_key = Key.f2
exit_key = Key.f1
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Продолжение]")
    elif key == pause_key:
        pause = True
        print("[Пауза]")
    elif key == exit_key:
        running = False
        print("[Выход]")

def display_controls():
    print("Авто-Драк")
    print("\t Пробел = Старт/Продолжение")
    print("\t f2 = Пауза")
    print("\t f1 = Выход")
    print("-----------------------------------------------------")
    print('Нажмите Пробел, чтобы начать ...')
    

def loop1():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            heal = pyautogui.locateOnScreen("BUTTON/heal.png", confidence = 0.93)
            heal2 = pyautogui.locateOnScreen("BUTTON/heal2.png", confidence = 0.82)
            check = pyautogui.locateOnScreen("BUTTON/check.png", confidence = 0.93)
            raund1 = pyautogui.locateOnScreen("BUTTON/raund1.png", confidence = 0.82)
            raund21 = pyautogui.locateOnScreen("BUTTON/raund21.png", confidence = 0.75)







            if check:
                if heal:
                    print("отхилился")
                    pydirectinput.keyDown('r')
                    time.sleep(random.uniform(0.4,0.8))
                    pydirectinput.keyUp('r') 
                    time.sleep(random.uniform(1,1.5))                            
                     
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.4,0.8))
            

            if check:
                if heal2:
                    print("afk")
                    keyboard.send("ctrl")
                    time.sleep(random.uniform(4.1,8.2))
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(4.1,8.2))
        
            
            
        


            

            
            if check == None:
                if heal == None:
                    if raund21 == None:
                        print("отхил unlock")
                        pyautogui.sleep((random.uniform(0.9,1.3)))
                        keyboard.send("r")
                        pyautogui.sleep((random.uniform(0.9,1.3))) 
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.5,0.9))
            
            
            if raund1:
                print("бой! 1 раунд")
                logging.debug('бой! 1 раунд котэ')
                pydirectinput.keyDown('1')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('1')
                time.sleep(random.uniform(1,1.5))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(0.3,0.8)) 
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
            
        
        
def loop2():
    while running:
        if not pause:
            button3 = pyautogui.locateOnScreen("BUTTON/close.png", confidence = 0.82)
            check = pyautogui.locateOnScreen("BUTTON/check.png", confidence = 0.85)
            raund1 = pyautogui.locateOnScreen("BUTTON/raund1.png", confidence = 0.82)
            raund11 = pyautogui.locateOnScreen("BUTTON/raund11.png", confidence = 0.98)
            raund2 = pyautogui.locateOnScreen("BUTTON/raund22.png", confidence = 0.98)
            raund21 = pyautogui.locateOnScreen("BUTTON/raund21.png", confidence = 0.75)
            raund3 = pyautogui.locateOnScreen("BUTTON/raund33.png", confidence = 0.98)     
            orc2 = pyautogui.locateOnScreen("BUTTON/utop2.png", confidence = 0.85)
            null = pyautogui.locateOnScreen("BUTTON/ivmcheck.png", confidence = 0.85)
            orc22 = pyautogui.locateOnScreen("BUTTON/olencheck.png", confidence = 0.96)
            orc33 = pyautogui.locateOnScreen("BUTTON/angcheck.png", confidence = 0.96)
            orc = pyautogui.locateOnScreen("BUTTON/5ang23.png", region=(0,60,500,850), confidence = 0.98)
            orc4 = pyautogui.locateOnScreen("BUTTON/4ang23.png", region=(0,60,500,850), confidence = 0.98)
            orc1 = pyautogui.locateOnScreen("BUTTON/olen.png", region=(0,60,500,850), confidence = 0.95)
            logging.basicConfig(filename='output.txt', level=logging.DEBUG, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')




            

            
            
            if raund1 == None:
                if raund11 == None:
                    if raund2 == None:
                        if raund21:
                            if raund3 == None:
                                print("бой! 4+ раунд")
                                pydirectinput.keyDown('f9')
                                time.sleep(random.uniform(0.3,0.8))
                                pydirectinput.keyUp('f9')
                                time.sleep(random.uniform(0.3,0.8))

                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
         
             
            if check:               
                if orc2:
                    if orc22 == None:
                        if orc33 == None:
                            print("закрываю окно")
                            time.sleep(random.uniform(1,1.4))
                            keyboard.send("esc")  
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
        
            
        
        
            if check:
                if null == None:
                    if orc:
                        print("атакую горного орка")
                        pyautogui.moveTo(orc, duration=0.5)
                        time.sleep(random.uniform(0.3,0.8))
                        pyautogui.moveTo(orc, duration=0.3)
                        pyautogui.click(button='left')
                        time.sleep(random.uniform(0.8,1.5))   
                    if orc == None:                    
                        if orc1:
                            print("атакую горного орка")
                            pyautogui.moveTo(orc, duration=0.5)
                            time.sleep(random.uniform(0.3,0.8))
                            pyautogui.moveTo(orc1, duration=0.3)
                            pyautogui.click(button='left')
                            time.sleep(random.uniform(1.3,1.7))    
                    if orc == None:                    
                        if orc1 == None:
                            if orc4:
                                print("атакую горного орка")
                                pyautogui.moveTo(orc, duration=0.5)
                                time.sleep(random.uniform(0.3,0.8))
                                pyautogui.moveTo(orc4, duration=0.3)
                                pyautogui.click(button='left')
                                time.sleep(random.uniform(1.3,1.7))                             
                    if orc == None:
                        if orc1 == None:
                            if orc2 == None:
                                if orc4 == None:
                                    if raund1 == None:
                                        if raund2 == None:
                                            print("ищу орка")
                                            pyautogui.moveTo(116, 207, duration=0.58)
                                            keyboard.send("n")
                                            time.sleep(random.uniform(1.3,1.8)) 
                                            pyautogui.moveRel(30, 33, duration=0.4)
                                            pyautogui.vscroll(-3070)
                                            time.sleep(random.uniform(1.3,1.8))  
                if orc2:
                    if null == None:
                        if orc22:
                            time.sleep(random.uniform(0.3,0.6)) 
                            if null:
                                print("закрываю окно")
                                time.sleep(random.uniform(1,1.4))
                                keyboard.send("esc") 
                            print("бой с орком")
                            pyautogui.moveTo(orc2, duration=0.4)
                            pyautogui.moveRel(0, 3, duration=0.4)
                            pyautogui.click(button='left')
                        if orc33:
                            time.sleep(random.uniform(0.3,0.6)) 
                            if null:
                                print("закрываю окно4")
                                time.sleep(random.uniform(1,1.4))
                                keyboard.send("esc") 
                            print("бой с орком")
                            pyautogui.moveTo(orc2, duration=0.4)
                            pyautogui.moveRel(0, 3, duration=0.4)
                            pyautogui.click(button='left')
                        if orc22 == None:
                            if orc33 == None:
                                print("закрываю окно5")
                                time.sleep(random.uniform(1,1.4))
                                keyboard.send("esc")  
                                     
            
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.4,0.7))
            
            
            if raund1:
                print("бой! 1 раунд")
                logging.debug('бой! 1 раунд котэ')
                pydirectinput.keyDown('1')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('1')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(0.3,0.8)) 
            if raund2:
                print("бой! 2 раунд")
                pydirectinput.keyDown('2')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('2')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(1.4,2.5))
            if raund3:
                print("бой! 3 раунд")
                pydirectinput.keyDown('2')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('2')
                time.sleep(random.uniform(0.4,0.6))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.6))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(1.4,2.5))


                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
            
            
            if button3:
                if orc22 == None:
                    if orc33 == None:
                        print("закрываю окно")
                        time.sleep(random.uniform(1,1.4))
                        keyboard.send("esc")  
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
            
            if null:
                print("закрываю окно")
                time.sleep(random.uniform(1,1.4))
                keyboard.send("esc")  
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
     
     
    
def loop3():
    while running:
        if not pause:
            heal = pyautogui.locateOnScreen("BUTTON/heal.png", confidence = 0.93)
            heal2 = pyautogui.locateOnScreen("BUTTON/heal2.png", confidence = 0.82)
            check = pyautogui.locateOnScreen("BUTTON/check.png", confidence = 0.93)
            raund1 = pyautogui.locateOnScreen("BUTTON/raund1.png", confidence = 0.82)







            if check:
                if heal:
                    print("отхилился")
                    pydirectinput.keyDown('r')
                    time.sleep(random.uniform(0.4,0.8))
                    pydirectinput.keyUp('r') 
                    time.sleep(random.uniform(1,1.5))                            
                     
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.4,0.8))
            

            if check:
                if heal2:
                    print("afk")
                    keyboard.send("ctrl")
                    time.sleep(random.uniform(4.1,8.2))
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(4.1,8.2))
        
            
            
        


            

            

            
            
            if raund1:
                print("бой! 1 раунд")
                logging.debug('бой! 1 раунд котэ')
                pydirectinput.keyDown('1')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('1')
                time.sleep(random.uniform(1,1.5))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(0.3,0.8)) 
                
                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
            
            
            
            
def loop4():
    while running:
        if not pause:
            raund1 = pyautogui.locateOnScreen("BUTTON/raund1.png", confidence = 0.82)





            

            
        
            
            
            if raund1:
                print("бой! 11 раунд")
                pydirectinput.keyDown('1')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('1')
                time.sleep(random.uniform(1,1.5))
                pydirectinput.keyDown('f9')
                time.sleep(random.uniform(0.3,0.8))
                pydirectinput.keyUp('f9')
                time.sleep(random.uniform(0.3,0.8)) 



                
            timeStart = datetime.now()
            
            time.sleep(random.uniform(0.1,0.2))
            





Thread(target=loop1).start()
Thread(target=loop2).start()
Thread(target=loop3).start()
Thread(target=loop4).start()

