import csv
import itertools
import json
import os
from typing import Dict, Iterator, List

from utils.constants import CRASH_VALS, EVALS_HEADER, HYPS_HEADER, SEARCH_SPACE
from utils.utils import get_config_id_from_tuple

import numpy as np


def get_iterator() -> Iterator:
    return itertools.product(*SEARCH_SPACE.values())


def remove_out_of_domain(data: Dict[str, List[float]]) -> Dict[str, List[float]]:
    # n_layers == 6 is out of domain
    mask = ~np.isclose(data["n_layers"], 6.0)
    return {k: np.asarray(v)[mask].tolist() for k, v in data.items()}


def get_dict_from_raw_dataset(file_name: str) -> Dict[str, List[float]]:
    data = {k: [] for k in HYPS_HEADER + EVALS_HEADER[:2]}

    for ext in ["hyps", "evals"]:
        if ext == "hyps":
            header = HYPS_HEADER
        else:
            header = EVALS_HEADER[:2]

        with open(f"raw_datasets/{file_name}.{ext}", "r") as f:
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                for i, k in enumerate(header):
                    data[k].append(float(row[i]))

    return remove_out_of_domain(data)


def get_config_id_list(data: Dict[str, List[float]]) -> List[str]:
    n_configs = len(data[HYPS_HEADER[0]])
    config_id_list = []
    for i in range(n_configs):
        config = (data[hp_name][i] for hp_name in SEARCH_SPACE.keys())
        config_id_list.append(get_config_id_from_tuple(config))

    return config_id_list


def pad_crash_values(data: Dict[str, List[float]]) -> Dict[str, List[float]]:
    config_id_set = set(get_config_id_list(data))
    for config in get_iterator():
        new_config_id = get_config_id_from_tuple(config)
        if new_config_id not in config_id_set:
            for hp_name, val in zip(SEARCH_SPACE, config):
                data[hp_name].append(val)
            for metric_name, val in CRASH_VALS.items():
                data[metric_name].append(val)

    return data


if __name__ == "__main__":
    DIR_NAME = "datasets/"
    for name in ["so-en", "sw-en", "tl-en"]:
        data = get_dict_from_raw_dataset(file_name=name)
        data = pad_crash_values(data)
        order = np.argsort(np.asarray(get_config_id_list(data)))

        data = {k: np.asarray(v)[order].tolist() for k, v in data.items()}
        data["config_id_to_idx"] = {config_id: idx for idx, config_id in enumerate(get_config_id_list(data))}
        os.makedirs(DIR_NAME, exist_ok=True)
        with open(os.path.join(DIR_NAME, f"{name}.json"), "w") as f:
            json.dump(data, f, indent=4)
