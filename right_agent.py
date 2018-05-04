#!/usr/bin/env python

import retro

env = retro.make(game='SonicTheHedgehog2-Genesis', state='AquaticRuinZone.Act1', record='.')
env.reset()
while True:
    env.render()
    action = env.action_space.sample()
    action[7] = 1
    _obs, _rew, done, _info = env.step(env.action_space.sample())
    ob, reward, done, _ = env.step(action)
    if done:
        print('episode complete')
        env.reset()
