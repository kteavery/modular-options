from all.experiments import SlurmExperiment, run_experiment
from all.environments import AtariEnvironment
import argparse
from all.presets.atari import c51, rainbow, a2c, dqn, vsarsa, vqn, ppo, ddqn

from envs.wrappers.all_toybox_wrapper import (
    ToyboxEnvironment,
    customAmidarResetWrapper,
)
from envs.wrappers.amidar import options
import numpy as np
from glob import glob

device = "cuda"
frames = 1e7 + 1
render = False
logdir = "runs"
writer = "tensorboard"
toybox = True
agent_replicate_num = 1
test_episodes = 100
nodelist = ""
loadfile = False  # replace with specific path if continuing from checkpoint
# e.g. loadfile = "/.../snapshots"


def main(env_name, fam):
    all_options = None
    if env_name == "Amidar":
        custom_wrapper = customAmidarResetWrapper(0, -1, 3)
        all_options = options.FillOption()
    else:
        raise ValueError(f"Unrecognized env_name: {env_name}")

    if toybox:
        env = ToyboxEnvironment(
            env_name + "Toybox", device=device, custom_wrapper=custom_wrapper
        )
    else:
        env = AtariEnvironment(env_name, device=device)

    agent = {
        "a2c": a2c,
        "c51": c51,
        "dqn": dqn,
        "ddqn": ddqn,
        "ppo": ppo,
        "vsarsa": vsarsa,
        "vqn": vqn,
        "vqn": vqn,
        "rainbow": rainbow,
    }[fam]
    agents = [agent.device(device)]
    agents = list(np.repeat(agents, agent_replicate_num))

    if loadfile:
        loadfiles = glob(loadfile + "/*/")
        if len(loadfiles) == 1:
            loadfiles = [loadfile]
    else:
        loadfiles = [""]
    for load in loadfiles:
        if device == "cuda":
            SlurmExperiment(
                agents,
                env,
                frames,
                test_episodes=test_episodes,
                logdir=logdir,
                write_loss=True,
                loadfile="" if load == "" else load + "preset10000000.pt",
                sbatch_args={"partition": "gpu", "exclude": "ials-gpu018,ials-gpu026"},
                nodelist=nodelist,
                options=all_options,
            )
        else:
            run_experiment(
                agents,
                env,
                frames,
                render=render,
                logdir=logdir,
                writer=writer,
                test_episodes=test_episodes,
                options=all_options,
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train agent of specified type on environment."
    )
    parser.add_argument(
        "--env",
        nargs=1,
        type=str,
        help="Environment name: SpaceInvaders, Amidar, or Breakout",
    )
    parser.add_argument(
        "--family",
        nargs=1,
        type=str,
        help="Agent family:  a2c,c51, dqn, ddqn, ppo, rainbow, vsarsa, vqn",
    )
    parser.add_argument("--experiment_id", type=int)

    args = parser.parse_args()

    assert args.env is not None, "ENV must be specified"
    assert args.family is not None, "FAMILY must be specified"

    print(f"Training {args.family[0]} on {args.env[0]}")
    main(args.env[0], args.family[0])
