import numpy as np


HYPS_HEADER = ["bpe", "n_layers", "n_embed", "n_hidden", "n_heads", "initial_lr"]
EVALS_HEADER = ["bleu", "decoding_time", "perplexity", "n_updates", "gpu_memory", "n_params"]
SEARCH_SPACE = {
    "bpe": [1000, 2000, 4000, 8000, 16000, 32000],
    "n_layers": [1, 2, 4],
    "n_embed": [256, 512, 1024],
    "n_hidden": [1024, 2048],
    "n_heads": [8, 16],
    "initial_lr": [0.0003, 0.0006, 0.001],
}
CRASH_VALS = {
    "bleu": 0.0,
    "decoding_time": 1500.0,
}
N_CONFIGS = np.prod([len(choices) for choices in SEARCH_SPACE.values()])
