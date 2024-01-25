![GitHub last commit](https://img.shields.io/github/last-commit/alessandrosebastianelli/opensv?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/alessandrosebastianelli/opensv?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/alessandrosebastianelli/opensv?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/alessandrosebastianelli/opensv?style=flat-square)

# Open Satellite Vision

This library comprises a collection of functions and classes tailored to manage satellite based data.

<a class="btn btn-success" href="https://alessandrosebastianelli.github.io/opensv/pyosv.html" target="_blank">Click here to access the documentation</a>

## Installation

You need to create a virtual environment

```bash
conda create -n osv python=3.10 -y
conda activate osv
conda install pip -y
```

This package is stored on [PyPi](https://pypi.org/project/pyosv/), you can easily install it using pip

```bash
pip install --upgrade pyosv
```

Although certain elements of this library draw from Mayavi, these package is not included in the library's prerequisites, and therefore, it will not be automatically installed. To install it run the following command, once your virtual environment is active

```bash
pip install mayavi
```

or 

```bash
conda install mayavi
```
if there are issue with the first command.

## How to contribute

[Click here](https://github.com/alessandrosebastianelli/opensv/issues/2)