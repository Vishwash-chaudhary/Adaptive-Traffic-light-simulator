import time
import threading

start_time = time.time()

road_A, road_B = [], []
arrival_times_A, arrival_times_B = [], []

def calculate_priority(road, arrival_times):
    if not road:
        return 0
    return 2 * len(road) + 0.5 * (time.time() - arrival_times[0])

def serve_green(road, arrival_times, name):
    start = time.time()
    print(f"\n--- Green for Road {name} ---")
    while road and time.time() - start < 10:
        time.sleep(3)                 # one vehicle crossing
        car = road.pop(0)
        arrival_times.pop(0)          # keep both lists in sync
        print(f"Road {name}: {car} crossed")

def controller():
    while thread_A.is_alive() or thread_B.is_alive() or road_A or road_B:
        pA = calculate_priority(road_A, arrival_times_A)
        pB = calculate_priority(road_B, arrival_times_B)
        print(f"Priority A: {pA:.2f} | Priority B: {pB:.2f}")

        if pA == 0 and pB == 0:       # nothing waiting, check again shortly
            time.sleep(0.2)
            continue

        if pA >= pB:
            serve_green(road_A, arrival_times_A, "A")
        else:
            serve_green(road_B, arrival_times_B, "B")

def add_vehicles(road, arrival_times, count, delay, name):
    for i in range(count):
        time.sleep(delay)
        road.append(f"Car{i + 1}")
        arrival_times.append(time.time())
        print(f"Road {name}: Car{i + 1} arrived")

a  = int(input("Number of vehicles on Road A: "))
aT = float(input("Arrival interval on Road A (s): "))
b  = int(input("Number of vehicles on Road B: "))
bT = float(input("Arrival interval on Road B (s): "))

thread_A = threading.Thread(target=add_vehicles, args=(road_A, arrival_times_A, a, aT, "A"))
thread_B = threading.Thread(target=add_vehicles, args=(road_B, arrival_times_B, b, bT, "B"))
thread_C = threading.Thread(target=controller)

thread_A.start()
thread_B.start()
thread_C.start()

thread_A.join()
thread_B.join()
thread_C.join()

end_time = time.time()
print(f"\nTotal simulation time: {end_time - start_time:.2f} seconds")

print("\nSimulation complete. Both roads have been served.")