# Syllabifier script

This directory contains a small Python script you can use to add hyphens in a text.

It has many options, but an interesting feature is that it can add `()` automatically in a text, making it ready for use in Gregorio.

## Dependencies

The script depends on Python 3, and [pyphen](http://pyphen.org/). Note that you must have generated the patterns for libhyphen in order for the script to work. See [../patterns/README.md](documentation).

## Installation

Fetch the entire repository (`git clone https://github.com/gregorio-project/hyphen-la.git`) and use it directly, no need to install. You can also adapt it to suit your needs, it is less than 50 lines long!

## Usage

See `./syllabify.py -h` for all options.