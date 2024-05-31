import pygame
import Menu
import RandomEvents
import PitstopTimeLost

#tworzy menu ... zaczyna symulacje jakos tak
menu = Menu

#doRandomEvents
rainChance = 0.39
safetyCarChance = 0.56
RandomEventsObject = RandomEvents(rainChance,safetyCarChance) #tworze obiekt żeby co jakis czas losoac deszcz jak bedzie for

#doPitstopTimeLost
# przykładowe współczynniki na strate czasu przy pitstopie
normalLost = 19.1
rainLost = 18.5
safetyCarLost = 14.2
PitstopTimeLostObject = PitstopTimeLost(normalLost, rainLost, safetyCarLost)

#global
isRain = RandomEventsObject.isRain()
isSafetyCar = RandomEventsObject.isSafetyCar(isRain)