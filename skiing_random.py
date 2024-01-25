# -*- coding: utf-8 -*-

import gymnasium as gym
env = gym.make("Skiing-v4", render_mode="human") # random player

observation, info = env.reset(seed=42)

class A:
    def __init__(self):
        self.old_image = None
        self.old_image_all = None
        self.skip = 0
    
    def new_reward(self, image):
        self.skip = (self.skip + 1) % 2
        
        if self.old_image is not None and (self.old_image != image[10, 50:90]).any():
            self.old_image = image[10, 50:90]
            return 500.
        
        if self.skip == 1:
            if self.old_image_all is not None and (self.old_image_all == image[25:175,8:152]).all():
                self.old_image_all = image[25:175,8:152]
                return -1000.
            
            self.old_image_all = image[25:175,8:152]
        
        self.old_image = image[10, 50:90]
        return -3.

from tqdm import tqdm

a = A()

for _ in range(1000):
    action = env.action_space.sample()  # this is where you would insert your policy
    observation, reward, terminated, truncated, info = env.step(0)

    print(reward)
    print(a.new_reward(observation))

    if terminated or truncated:
        observation, info = env.reset()

env.close()
