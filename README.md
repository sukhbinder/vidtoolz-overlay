# vidtoolz-overlay

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-overlay.svg)](https://pypi.org/project/vidtoolz-overlay/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-overlay?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-overlay/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-overlay/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-overlay/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-overlay/blob/main/LICENSE)

Add overlay video on a video using moviepy

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-overlay
```
## Usage

type ``vid overlay --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-overlay
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
