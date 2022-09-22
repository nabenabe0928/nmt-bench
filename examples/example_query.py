from typing import Dict

from bench.api import NMTBench

import numpy as np

from utils.constants import SEARCH_SPACE


def get_random_config(seed: int) -> Dict[str, float]:
    rng = np.random.RandomState(seed)
    config: Dict[str, float] = {}
    for k, choices in SEARCH_SPACE.items():
        config[k] = choices[rng.randint(len(choices))]

    return config


if __name__ == "__main__":
    n_checks = 10
    api = NMTBench()
    for i in range(n_checks):
        config = get_random_config(seed=i)
        print(f"config: {config}, results: {api(config)}")
