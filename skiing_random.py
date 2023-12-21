# -*- coding: utf-8 -*-

import gymnasium as gym
env = gym.make("Skiing-ram-v4", render_mode="human", obs_type="ram") # random player

observation, info = env.reset(seed=42)

from tqdm import tqdm
#for _ in tqdm(range(1000)):
for _ in range(1000):
   action = env.action_space.sample()  # this is where you would insert your policy
   action = 0
   observation, reward, terminated, truncated, info = env.step(action)
   reward = observation[5 * 18 + 7] # this will be big when the point is geted
   print(reward)

   if terminated or truncated:
      observation, info = env.reset()

env.close()
