# -*- coding: utf-8 -*-

import gymnasium as gym
env = gym.make("Skiing-v4", render_mode="human") # random player

observation, info = env.reset(seed=42)

from tqdm import tqdm
for _ in tqdm(range(1000)):
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

env.close()
