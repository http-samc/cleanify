# cleanify [![PyPI version](https://badge.fury.io/py/cleanify.svg)](https://badge.fury.io/py/cleanify) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ea4c058a4f684790a4e1e8aa31845e7e)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=http-samc/cleanify&amp;utm_campaign=Badge_Grade)
CLI utility to remove remove newlines, tabs from a file and copy it to your clipboard
- Pure 🐍 with only [klembord](https://pypi.org/project/klembord/) used in the Tech Stack as a clipboard API

## Installation
1. From PyPI (requires Python and PIP)
`pip install cleanify`

2. From source (requires Python)
   1. Clone this repository
   2. Start a terminal in the repository's folder
      1. Run `python setup.py install`

## Use
1. In your terminal, type `cleanify --file {your filepath - relative OR absolute}`
2. The cleanified string will be copied to your clipboard

Supported Flags:
|Flag|Required|Description|
|---|---|---|
|`-file`, `-f`|`true`|The path {relative or absolute} to the target file|
|`--repQuotes`, `--rq`|`false`|Whether you want to replace double quotes with single ones (useful for HTML stored as JSON). Defaults to `false`|