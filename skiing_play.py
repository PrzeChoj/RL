# -*- coding: utf-8 -*-

"""#### Play"""
import gymnasium as gym
from gymnasium.utils.play import play
env = gym.make("Skiing-v4", render_mode="rgb_array")

observation, info = env.reset(seed=7824)

play(env)