## Tabular benchmarks for Hyperparameter optimization of Neural machine translation systems

The source is available [here](https://github.com/Este1le/hpo_nmt)
and the title of the original paper is [`Reproducible and Efficient Benchmarks for Hyperparameter Optimization of Neural Machine Translation Systems`](https://aclanthology.org/2020.tacl-1.26/).

As the raw datasets are not easy to handle directly, this repository provides:
1. Preprocessing of the raw datasets
2. Easy-to-use API.

The processed datasets are available in [datasets/](https://github.com/nabenabe0928/nmt-bench/tree/main/datasets/).

To obtain the datasets from the raw datasets, run the following:

```shell
$ python -m data_gen.raw_to_json
```

A simple example is available in [examples/](https://github.com/nabenabe0928/nmt-bench/tree/main/examples/).

To test the script, run the following:

```shell
$ python -m examples.example_query
```
