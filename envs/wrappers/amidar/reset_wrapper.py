from abc import abstractmethod
from envs.wrappers.paths import (
    get_intervention_dir,
    get_start_state_path,
)
from typing import *
import gym, json

from toybox.envs.atari.amidar import AmidarEnv


class AmidarResetWrapper(gym.Wrapper):
    """Resets amidar environment at the start of every episode to an intervened state."""

    def __init__(
        self,
        tbenv: AmidarEnv,
        state_num: int,
        intv: int,
        lives: int,
    ):
        super().__init__(tbenv)
        self.env = tbenv
        self.toybox = (
            tbenv.toybox
        )  # Why does this fail when ToyboxBaseEnv has a toybox attribute?
        self.intv = intv  # Intervention number 0 - ?
        self.state_num = state_num
        self.lives = lives

    def reset(self):
        super().reset()
        return self.on_episode_start()

    @abstractmethod
    def on_episode_start(self):
        """On the start of each episode, set the state to the JSON state according to the intervention."""
        # Get JSON state
        environment = "Amidar"
        if self.intv >= 0:
            with open(
                f"{get_intervention_dir(self.state_num, environment)}/{self.intv}.json",
            ) as f:
                iv_state = json.load(f)

        else:
            with open(get_start_state_path(self.state_num, environment)) as f:
                iv_state = json.load(f)

        iv_state["lives"] = self.lives

        # Set state to the reset state
        self.env.cached_state = iv_state
        self.toybox.write_state_json(iv_state)
        obs = self.env.toybox.get_state()
        return obs


if __name__ == "__main__":
    pass
