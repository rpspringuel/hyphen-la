# Latin Hyphenation patterns

This directory contains two sets of Latin hyphenation patterns:

- `hyph.la.etymology.txt` contains the patterns for medieval hyphenation considering etymology (as found in most liturgical books)
- `hyph.la.phonetic.txt` contains the patterns for "modern" (or ancient) hyphenation considering phonetic (used by recent Solesmes books)

See [doc](../doc/) folder for more on the differences, and how to choose between the two.

## Format conversion

The patterns are in the TeX format.

The patterns can be converted to [libhyphen](https://github.com/hunspell/hyphen) format (from the [Hunspell](https://hunspell.github.io/) sofware), in order to be usable in LibreOffice/OpenOffice, Mozilla products, Adobe products, etc. Run `make` to do the conversion. Note that you must have `perl` and `git` in order to do so.

## License

The patterns used to be under the [LPPL](https://latex-project.org/lppl/), but the author allows their distribution under BSD-3 licence, which is what we do here.
