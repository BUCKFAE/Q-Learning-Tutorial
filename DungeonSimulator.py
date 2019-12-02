from enums import *
import random


class DungeonSimulator:
    def __init__(self, length = 5, slip = 0.1, small_reward = 2, large_reward = 10):
        self.length = length  # Length of the dungeon
        self.slip = slip  # probability of 'slipping' (changing) an action
        self.small = small_reward  # Payout for BACKWARDS action
        self.large_reward = large_reward  # Payout at end of chain for FORWARD action
        self.state = 0  # Start at beginning of the dungeon

    def take_action(self, action):
        if random.random() < self.slip:  # Agent slipped, reverse action taken
            action = not action
        if action == BACKWARD:  # Go back to the beginning, get small reward
            reward = self.small
            self.state = 0
        elif action == FORWARD:  # Go one step further in the dungeon
            if self.state < self.length - 1:  # If we did not reach the end yet
                self.state += 1
                reward = 0
            else:  # We did reach the end
                reward = self.large_reward
        return self.state, reward

    def reset(self):
        # Reset state to zero, the beginning of the dungeon
        self.state = 0
        return self.state
