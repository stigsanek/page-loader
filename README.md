# Page Loader

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/stigsanek/page-loader/python-ci)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/page-loader)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/page-loader)

## Description

"Page Loader" is a command line utility that downloads pages from the internet and stores them on your computer. Along
with
the page it downloads all the resources (images, styles and js) allowing you to open the page without the Internet.

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

### Package

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/page-loader.git
# clone via SSH:
>> git@github.com:stigsanek/page-loader.git
```

It remains to move to the directory and install the package:

```bash
>> cd page-loader
>> poetry build
>> python -m pip install --user dist/*.whl
```

Finally, we can move on to using the project functionality!

## Usage

```bash
>> page-loader -o /var/tmp https://ru.hexlet.io/courses

2022-11-01 17:28:06 :: INFO :: requested url: https://ru.hexlet.io/courses
2022-11-01 17:28:06 :: INFO :: output path: /var/tmp
2022-11-01 17:28:07 :: INFO :: write html file: /var/tmp/ru-hexlet-io-courses.html
2022-11-01 17:28:07 :: DEBUG :: resourses path: /var/tmp/ru-hexlet-io-courses_files
Downloading: ████████████████████████████████ 100%
2022-11-01 17:28:10 :: DEBUG :: resources are loaded
2022-11-01 17:28:10 :: DEBUG :: page is fully loaded
Page was downloaded as '/var/tmp/ru-hexlet-io-courses.html'
```

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
