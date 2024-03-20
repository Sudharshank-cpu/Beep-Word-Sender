from random import choice
import pyautogui as pa
import time
hate=["donkey","cow","sheep","pig","horse"]  #Add which kind of words you need to add in this list
val=int(input("How many times you needed to send them?= "))
print("\nGo to the Message Box that you need to send.(Time Limits 10 seconds)\n")
time.sleep(10)                               #Waiting for 10 seconds
for i in range(val):
   a=choice(hate)
   pa.write("You are "+a+"\n")
   time.sleep(0.1)
   pa.press('enter')
print("Program Ended")