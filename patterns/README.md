# Latin Hyphenation patterns

This directory contains two sets of Latin hyphenation patterns:

- `hyph.la.liturgical.txt` contains the patterns for hyphenation of liturgical Latin (used by recent Solesmes books), it is the most tested set of patterns
- `hyph.la.etymology.txt` contains the patterns for medieval hyphenation considering etymology
- `hyph.la.phonetic.txt` contains the patterns for "modern" (or ancient) hyphenation considering phonetic

See [doc](../doc/) folder for more on the differences, and how to choose between the two.

## Format conversion

The patterns are in the patgen format used by TeX. You can download them in other forms on the [webpage](http://gregorio-project.github.io/hyphen-la/), but if you want to convert them yourself:

### libhyphen (LibreOffice, Adobe, etc.)

The patterns can be converted to [libhyphen](https://github.com/hunspell/hyphen) format (from the [Hunspell](https://hunspell.github.io/) sofware), in order to be usable in LibreOffice/OpenOffice, Mozilla products, Adobe products, etc. 

##### Converting to libhyphen format

Run `make` in this directory to do the conversion. Note that you must have `perl` and `git` in order to do so.

### Javascript

The patterns can be converted to the format used by [Hyphenator](http://mnater.github.io/Hyphenator/) and [hypher](https://github.com/bramstein/hypher) by using the [conversion page from Hyphenator](http://mnater.github.io/Hyphenator/compressor.html), after replacing new lines by space in the pattern files.

## License

The patterns used to be under the [LPPL](https://latex-project.org/lppl/), but the author allows their distribution under [MIT](https://opensource.org/licenses/MIT) licence, which is what we do here.
