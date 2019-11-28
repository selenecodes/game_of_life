from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None, A=1, S=[2, 3], B=[3, 6]):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        :param A: (optional) Max age of cell.
        """

        self.B = B
        self.S = S
        self.A = A
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        world = self.world

        # Create the next evolution of the world
        next_generation = World(world.width, world.height)

        # Lefthand is B3/S23 game of life, righthand is custom options
        B = [3] if self.A == 1 else self.B # Birth neighbours
        S = [2, 3] if self.A == 1 else self.S # Survival neighbours

        # Birth condition set (only used with custom game of life)
        Bc = set(range(2, self.A - 1))

        # Loop through every grid cell
        for y in range(0, world.height):
            for x in range(0, world.width):
                hp = world.get(x,y)
                neighbours = world.get_neighbours(x,y)
                neighbours_count = len([n for n in neighbours if n > 0])

                # Rules for decreasing or preserving a cell
                if (hp > 0 and not neighbours_count in S):
                    next_generation.set(x,y, hp - 1)
                else:
                    next_generation.set(x,y, hp)

                # Rules for creating a cell
                meetsBc = list(set(neighbours) & Bc)
                if (not hp and neighbours_count in B):
                    if (self.A > 1 and len(meetsBc) > 0):
                        # We're playing custom GOL so our age = self.A
                        next_generation.set(x, y, self.A)
                    else:
                        # We're playing the default GOL so our age = 1
                        next_generation.set(x, y, 1)

        # Change our world to be the next generation
        self.set_world(next_generation)

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world
