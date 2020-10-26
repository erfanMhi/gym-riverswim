import gym
import numpy as np

from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.toy_text import discrete


LEFT = 0
RIGHT = 1


class RiverSwimEnv(discrete.DiscreteEnv):
    metadata = {'render.modes': ['human']}

    def __init__(self, nS=5):
        
        # Defining the number of actions
        nA = 2
        
        # Defining the reward system and dynamics of RiverSwim environment
        P, isd = self.__init_dynamics(nS, nA)
        
        super(RiverSwimEnv, self).__init__(nS, nA, P, isd)

    def __init_dynamics(self, nS, nA):
        
        # P[s][a] == [(probability, nextstate, reward, done), ...]
        P = {}
        for s in range(nS):
            P[s] = {a: [] for a in range(nA)}

        # Rewarded Transitions
        P[0][LEFT] = [(1., 0, 5/1000, 0)]
        P[nS-1][RIGHT] = [(0.9, nS-1, 1, 0), (0.1, nS-2, 1, 0)]

        # Left Transitions
        for s in range(1, nS):
            P[s][LEFT] = [(1., max(0, s-1), 0, 0)]

        # RIGHT Transitions
        for s in range(1, nS - 1):
            P[s][RIGHT] = [(0.3, min(nS - 1, s + 1), 0, 0), (0.6, s, 0, 0), (0.1, max(0, s-1), 0, 0)]
        P[0][RIGHT] = [(0.3, 0, 0, 0), (0.7, 1, 0, 0)]

        # Starting State Distribution
        isd = np.zeros(nS)
        isd[0] = 1.

        return P, isd

    def render(self, mode='human'):
        pass

    def close(self):
        pass
