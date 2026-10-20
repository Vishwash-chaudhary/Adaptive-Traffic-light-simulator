import time
import threading

road_A = []
road_B = []

def add_vehicles(road, count, delay, road_name):
    for i in range(count):
        time.sleep(delay)
        vehicle = "Car" + str(i + 1)
        road.append(vehicle)
        print(f"Road {road_name}: {vehicle} arrived")

a = int(input("Number of vehicles on Road A: "))
aT = float(input("Arrival interval for each vehicle on Road A (in seconds): "))

b = int(input("Number of vehicles on Road B: "))
bT = float(input("Arrival interval for each vehicle on Road B (in seconds): "))

thread_A = threading.Thread(
    target=add_vehicles,
    args=(road_A, a, aT, "A")
)

thread_B = threading.Thread(
    target=add_vehicles,
    args=(road_B, b, bT, "B")
)

thread_A.start()
thread_B.start()

thread_A.join()
thread_B.join()

print("Road A:", road_A)
print("Road B:", road_B)
