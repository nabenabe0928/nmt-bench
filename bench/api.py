from enum import Enum
from typing import Dict
import json

from utils.constants import EVALS_HEADER
from utils.utils import get_config_id_from_dict


class DatasetChoices(Enum):
    so_en = "so-en.json"
    sw_en = "sw-en.json"
    tl_en = "tl-en.json"


class NMTBench:
    def __init__(self, dataset: DatasetChoices = DatasetChoices.so_en):
        self._data = json.load(open(f"datasets/{dataset.value}"))
        self._metric_names = EVALS_HEADER[:2]

    def __call__(self, config: Dict[str, float]) -> Dict[str, float]:
        config_id = get_config_id_from_dict(config)
        idx = self._data["config_id_to_idx"][config_id]
        return {name: self._data[name][idx] for name in self._metric_names}
