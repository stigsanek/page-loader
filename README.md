# PageLoader

[![Actions Status](https://github.com/stigsanek/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/stigsanek/python-project-51/actions)

"PageLoader" is a command line utility that downloads pages from the internet and stores them on your computer. Along with
the page it downloads all the resources (images, styles and js) allowing you to open the page without the Internet.

## Install

1. Install [poetry](https://python-poetry.org/).
2. Run `make install` or `poetry install` in the project directory.

## Usage

### From project

```
poetry run page-loader -o /var/tmp https://ru.hexlet.io/courses

INFO:root:requested url: https://ru.hexlet.io/courses
INFO:root:output path: /var/tmp
INFO:root:write html file: /var/tmp/ru-hexlet-io-courses.html
INFO:root:create directory for assets: /var/tmp/ru-hexlet-io-courses_files
Downloading: |████████████████████████████████| 100.0% (eta: 0)
Page was downloaded as '/var/tmp/ru-hexlet-io-courses.html'
```

### Wheel

You can build the wheel for later installation in a separate virtual environment with command `make build`
or `poetry build`. After installing the package in the virtual environment, the games can be launched using the
command:

```
page-loader -o /var/tmp https://ru.hexlet.io/courses
```