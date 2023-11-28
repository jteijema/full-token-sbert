# Template for extending ASReview with a full text sbert classifier

This repository contains a template for extending ASReview with a full text
sbert classifier.

## Getting started

To get started, install the package with

```bash
pip install git+https://github.com/jteijema/full-token-sbert.git
```

## Usage

The new classifier `ft_sbert` is defined in
[`asreviewcontrib/models/ft_sbert.py`](asreviewcontrib/models/ft_sbert.py) and can be used in a simulation.

```bash
asreview simulate example_data_file.csv -m ft_sbert
```

## License

MIT license
