all: hyph_la_etymology.dic hyph_la_phonetic.dic hyph_la_ecclesiastic.dic

hyphen/substrings.pl:
	git submodule update --init

hyph_la_etymology.dic: hyphen/substrings.pl hyph.la.etymology.txt
	perl hyphen/substrings.pl hyph.la.etymology.txt hyph_la_etymology.dic UTF-8 2 2 > /dev/null

hyph_la_phonetic.dic: hyphen/substrings.pl hyph.la.phonetic.txt
	perl hyphen/substrings.pl hyph.la.phonetic.txt hyph_la_phonetic.dic UTF-8 2 2 > /dev/null

hyph_la_ecclesiastic.dic: hyphen/substrings.pl hyph.la.ecclesiastic.txt
	perl hyphen/substrings.pl hyph.la.ecclesiastic.txt hyph_la_ecclesiastic.dic UTF-8 2 2 > /dev/null

clean:
	rm hyph_la_etymology.dic hyph_la_phonetic.dic hyph_la_ecclesiastic.dic