from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self):
        self.sim = Simulator()

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.
        """
        self.assertIsInstance(self.sim.update(), World)

    def test_update_rule(self):
        """
        Tests the update rules, the core of Game of Life
        """
        world = World(4)
        self.sim.set_world(world)
        world.set(0, 1, 1)
        world.set(1, 1, 1)
        world.set(2, 1, 1)
        next_world = self.sim.update()
        expected = np.array([
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
        ])
        self.assertEqual(expected.tolist(), next_world.world.tolist())

    def test_different_ruleset(self):
        """
        Tests different rule-sets for different cellular automata
        """
        world = World(7, 5)
        sim = Simulator(world, {3, 5, 8}, {2, 3, 7})    # rule-set B358/S237
        world.world = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ])
        next_world = sim.update()
        expected = np.array([
            [0, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ])
        self.assertEqual(expected.tolist(), next_world.world.tolist())

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)
