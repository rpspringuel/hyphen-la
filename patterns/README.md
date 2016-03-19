# Latin Hyphenation patterns

This directory contains two sets of Latin hyphenation patterns:

- `hyph_la-etymology.dic` contains the patterns for medieval hyphenation considering etymology (as found in most liturgical books)
- `hyph_la-phonetic.dic` contains the patterns for "modern" (or ancient) hyphenation considering phonetic (used by recent Solesmes books)

See [doc](../doc/) folder for more on the differences, and how to choose between the two.

## Format

The patterns are in the format of [libhyphen](https://github.com/hunspell/hyphen) from the [Hunspell](https://hunspell.github.io/) sofware, and thus should be usable as is in:

- LibreOffice/OpenOffice
- Adobe products (InDesign, etc.)

Adaptation to TeX is straightforward and can be achieved with a script (TODO!).

## License

The patterns are currently under the [LPPL](https://latex-project.org/lppl/).
