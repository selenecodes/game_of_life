from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    width = 110
    w = World(width)
    sim = Simulator(w)

    midX = w.width // 2
    midY = w.height // 2

    w.set(midX, midY,1)
    w.set(midX - 1, midY,1)
    w.set(midX + 1, midY,1)

    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(5)
