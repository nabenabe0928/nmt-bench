from typing import Dict, Tuple

from utils.constants import SEARCH_SPACE


def get_config_id_from_dict(config: Dict[str, float]) -> str:
    config_id = ""
    for hp, (hp_name, choices) in zip(config.values(), SEARCH_SPACE.items()):
        idx = choices.index(hp)
        config_id += str(idx)

    return config_id


def get_config_id_from_tuple(config: Tuple[float]) -> str:
    config_id = ""
    for hp, (hp_name, choices) in zip(config, SEARCH_SPACE.items()):
        idx = choices.index(hp)
        config_id += str(idx)

    return config_id
