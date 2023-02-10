import pyautogui as pt
import csv
from time import sleep
sleep(3)   # Delay time given to open whatsapp app

def addpeople():


    pt.click(700, 125, duration=0.5) # Used to click on the whatsapp group name
    pt.moveTo(1500, 200, duration=0.5)  # Moves to right column where you have to scroll
    pt.scroll(-1200)   # Scrolls the column
    pt.click(1600, 550, duration=0.5) # Clicks on "add participant"
    sleep(1) # Delay



    # Now Adding Participants
    # Reading CSV file
    count=0
    l = []
    y=433
    with open('check.csv', 'rt') as f:  # Opens the csv file where all the contacts with their name is already added
         data = csv.reader(f)
         for row in data:
             if row[1] != "Given Name":
                 l.append(row[1]) 

    for i in l:
        sleep(0.2)
        pt.typewrite(i)    # Type the name of participant in blank
        sleep(1)   # Delay after writing the name
        pt.click(743,y,duration=0.5)# Select the participant
        count += 1
        if count==1:
            y += 30
        if count==4:
            y+=30
        if count==7:
            y+=30
        if count==10:
            y+=30



        pt.click(1196, 261, duration=0.5) # Select the cross on the participant blank
                                        # Loop ends after adding all the participants
    pt.click(1175, 886, duration=0.5)  # checks the tick button
    pt.click(1091, 582, duration=1)  # clicks "Add Participant" button
    # All the participants are added

addpeople()
#program ends




