# Template for extending ASReview with a full text sbert classifier

This repository provides a template for extending ASReview with a full text
SBERT classifier. The software is designed to be used in conjunction with
[ASReview](https://github.com/asreview/asreview).

By splitting the full text into parts the length of the maximum input size of
the SBERT model, the full text can be embedded into a vector space. The
resulting vectors are then averaged to create a single vector representation of
the full text. This vector is then used to train a classifier. Based on the
following paper:

@misc{mulyar2020phenotyping,
      title={Phenotyping of Clinical Notes with Improved Document Classification Models Using Contextualized Neural Language Models}, 
      author={Andriy Mulyar and Elliot Schumacher and Masoud Rouhizadeh and Mark Dredze},
      year={2020},
      eprint={1910.13664},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

Instead of averaging, other options are possible. See the following paper for
more information:

@article{fiok2021text,
  title={Text guide: improving the quality of long text classification by a text selection method based on feature importance},
  author={Fiok, Krzysztof and Karwowski, Waldemar and Gutierrez-Franco, Edgar and Davahli, Mohammad Reza and Wilamowski, Maciej and Ahram, Tareq and Al-Juaid, Awad and Zurada, Jozef},
  journal={IEEE Access},
  volume={9},
  pages={105439--105450},
  year={2021},
  publisher={IEEE}
}

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
