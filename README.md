# Unmanned Ariel Vehicle
This project involved the development of an autonomous drone system to deliver packages across a city. A custom AI was created with a combination of various machine learning algorithms, to tackle multifaceted problems, some of which are described below. A patent was successfully published as an Intellectual property in India under the name "Unmanned Aerial Vehicle (UAV) and Navigation Method Thereof"  (IN Application No.: 202221010717).

## PID Control System
A PID control system was developed to maneuver the aircraft along the roll, pitch, and yaw axes that analyzed the target's location, and determined the craft's safe acceleration and deceleration. Another layer of the system would proportionate latitude and longitudinal accelerations to roll and pitch such that the drone always travels in a straight line rather than a curved path. A regression model accounted for external influences like pressure change and wind resistance. 

## Locating Landing Pad
The destination's general location is determined by the QR code on the package. The onboard camera uses the Haar Cascade model to locate the landing pad and then translate the camera's coordinates to its precise location in terms of latitude and longitude.

## Navigation System
Conventional navigation systems use A* and Dijkstra's algorithms, which require knowledge of the map, on a 2D terrain, to determine an efficient path. Since the UAV can move in all three dimensions, a custom navigation algorithm was developed to find an almost efficient way in a labyrinth of an uncharted environment. 

## Traveling Salesman Problem
To determine an expeditious order of delivery and pickup locations, the infamous traveling salesman problem had to be solved. The genetic algorithm approach was used to tackle this issue. 

## Watchdog Timer
A watchdog timer algorithm was used in the flight controller, inspired by the Mars Exploration Rover. It predicts an estimated time needed to perform each task with error tolerance.  If a task is not flagged as complete within the allotted time, the UAV will abandon that task and return to base for an error inspection.

## Video
https://www.youtube.com/watch?v=DJb2M16Uxo4&list=TLGG5oEL1KpnWucyMDA0MjAyNA&t=69s
