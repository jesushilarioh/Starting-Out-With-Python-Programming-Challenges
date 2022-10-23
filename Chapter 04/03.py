from xml.dom.expatbuilder import FragmentBuilder


fastestLapTime = 0.0
slowestLapTime = 0.0
userLapTime    = 0.0
totalLapTime   = 0.0

numberAroundTrack = int(input("How many times around the track? "))

while numberAroundTrack < 0:
    numberAroundTrack = int(input("Error. Enter a postive number: "))

for lapTime in range(numberAroundTrack):

    userLapTime = float(input("Enter lap time for lap #" + format(lapTime + 1) + ": ")) # 0, 1, 2, 3, n-1
    
    while userLapTime < 0:
        userLapTime = float(input("Error. Enter a positive number: "))

    if lapTime == 0:
        fastestLapTime = slowestLapTime = userLapTime
    
    else: 
        if userLapTime > fastestLapTime:
            fastestLapTime = userLapTime

        elif userLapTime < slowestLapTime:
            slowestLapTime = userLapTime
    
    totalLapTime += userLapTime

averageLapTime = totalLapTime / numberAroundTrack

output = "\nFastest lap time = " + format(fastestLapTime) + "\n" \
         "Slowest lap time   = " + format(slowestLapTime) + "\n" \
         "Average lap time   = " + format(averageLapTime) + "\n"

print(output)