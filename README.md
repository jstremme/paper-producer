# paper-producer

Produces new papers from old papers

### About

Produces new papers from old papers by applying rules or ML models.

### Disclaimer

For now, all derivative papers belong to the authors of the original paper.  Do not pass off derivative papers as your own.

### Environment

To build the `paper-producer` Python 3.8 environment, create a Python 3.8 virtual environment and install the dependencies in `requirements.txt`.  We recommend using [Anaconda](https://www.anaconda.com/products/individual) to create your environment.

```
git clone https://github.com/jstremme/paper-producer
conda create --name=paper=producer python=3.8
source activate paper-producer
pip install -r requirements.txt
```

### Run Paper Producer

To run `paper-producer`, follow these steps to activate your conda environment and run `paper_producer.py` with an arxiv paper ID provided as the only required argument.

```
source activate paper-producer
python paper_producer --arxiv_id=<arxiv-paper-id-here>
```

### Contributing

To contribute features, bug fixes, tests, examples, or documentation, please submit a pull request with a description of your proposed changes or additions.

Please include a brief description of your pull request when submitting code and ensure that your code follows the [Pep 8](https://www.python.org/dev/peps/pep-0008/) style guide.  To do this run `pip install black` and `black paper-producer` to reformat files within your copy of the code using the [black code formatter](https://github.com/psf/black).  The black code formatter is a PEP 8 compliant, opinionated formatter that reformats entire files in place.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
