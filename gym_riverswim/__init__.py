from gym.envs.registration import register

register(
    id='riverswim-v0',
    entry_point='gym_riverswim.envs:RiverSwimEnv',
    max_episode_steps=20,
)
