from World import *
import copy


class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world=None, birth_condition=None, survive_condition=None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world is None:
            self.world = World(20)
        else:
            self.world = world
        if birth_condition is None:
            self.birth_condition = {3}
        else:
            self.birth_condition = birth_condition
        if survive_condition is None:
            self.survive_condition = {2, 3}
        else:
            self.survive_condition = survive_condition

    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1
        world_copy = copy.deepcopy(self.world)

        for y in range(world_copy.height):
            for x in range(world_copy.width):
                neighbors = np.array(world_copy.get_neighbours(x, y))

                # rule 1
                if np.count_nonzero(neighbors) < 2:
                    self.world.set(x, y, 0)
                # rule 2
                elif np.count_nonzero(neighbors) > 3:
                    self.world.set(x, y, 0)
                # rule 4
                elif np.count_nonzero(neighbors) == 3:
                    self.world.set(x, y, 1)
                # rule 3 nothing changes

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
