initial_velocity=0
time=int(input("Please insert the amount of time spent on the road: "))
acc=int(input("Please insert the cars acceleration: "))
dist=((initial_velocity*time)+(acc*time*time)/2)
velocity=initial_velocity+(acc*time)
speed=dist/time



if speed>60:
    print("The person went over the speed limit. (Max speed was ", speed ,"m/s")
else:
    print ("The person did not goover the speed limit. (Max speed was ", speed ,"m/s")

print("The person reached the destioantion. (Reached ", dist ,"m")

for i in range(0,time+1):
    print("duration", i)
    speed= acc*i
    distance= 1/2*i*speed
    print("distance :", "*"*int(distance/10))

if distance >= dist :
    print("\nReach Destination")
else:
    print("\nNot reach destination")
