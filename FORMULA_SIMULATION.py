import pygame
import Menu
import RandomEvents
import PitstopTimeLost
import Track
import Bolide

#tworzy menu ... zaczyna symulacje jakos tak
menu = Menu

#doRandomEvents
rainChance = 0.39
safetyCarChance = 0.56
RandomEventsObject = RandomEvents.RandomEvents(rainChance,safetyCarChance) #tworze obiekt żeby co jakis czas losoac deszcz jak bedzie for

#doPitstopTimeLost
#example values
normalLost = 19.1
rainLost = 18.5
scLost = 14.2
PitstopTimeLostObject = PitstopTimeLost.TimeLostPitstop(normalLost, rainLost, scLost)

#global
isRain = RandomEventsObject.isRain()
isSC = RandomEventsObject.isSafetyCar(isRain)

#Track
screen_width = 900
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))


track_width = 400
track_height = 300
margin = 100  #marigin of the track

TrackObject = Track.Track(screen_width, screen_height, screen, track_width, track_height, margin)

#Bolide
bolide_width = 20
bolide_height = 20




