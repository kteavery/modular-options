from envs.wrappers.all_toybox_wrapper import (
    ToyboxEnvironment,
    passThroughWrapper,
)
import os
import gym
import json

import numpy as np
from models.random import RandomAgent

from envs.wrappers.paths import (
    get_start_state_path,
    amidar_env_id,
)
from envs.wrappers.amidar.interventions.reset_wrapper import AmidarResetWrapper


def save_trajectory(agent, environment, path, device):

    if environment == "Amidar":
        random_agent = RandomAgent(gym.make(amidar_env_id).action_space)
    else:
        raise ValueError("Unknown environment specified.")

    print(environment)
    env = ToyboxEnvironment(environment + "Toybox", passThroughWrapper, device=device)

    obs = env.reset()
    action, _ = agent.act(obs)

    trajectory = [env.toybox.state_to_json()]
    done = False
    while not done:
        obs = env.step(action)
        done = obs["done"]
        action, _ = agent.act(obs)

        state = env.toybox.state_to_json()

        with open(get_start_state_path(state_num, environment), "w") as f:
            json.dump(state, f)

        trajectory.append(state)