import gym
import sys

sys.path.append('gym-fightingice')
from gym_fightingice.envs.Machete import Machete

def main():
    env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="", port=4242)
    # env = gym.make("FightingiceDataNoFrameskip-v0", java_env_path="")
    env.reset(p2=Machete)
    
    for i in range(3000):
        env.step(31)

if __name__ == "__main__":
    main()
