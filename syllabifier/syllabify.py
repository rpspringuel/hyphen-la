#!/usr/bin/env python3

import pyphen
import argparse
import sys
import re

parser = argparse.ArgumentParser(
    				description='A script to "syllabify" (insert a character between all syllables) a file.',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-t', '--text-type',
                    help='text type (chant or prose)',
                    default='prose', dest='type')
parser.add_argument('-m', '--hyphen-mode',
                    help='Hyphenation mode (phonetic or etymology)',
                    default='phonetic', dest='mode')
parser.add_argument('-i', '--input', nargs='?', type = argparse.FileType('r'),
					default=sys.stdin, dest='inputfile')
parser.add_argument('-o', '--output-file', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout, dest='outputfile')
parser.add_argument('-c', '--hyphen-char', nargs='?',
                    default='-', dest='hyphenchar')

args = parser.parse_args()

righthyphenmin = 2
lefthyphenmin = 2
cutvowels = False
if (args.type == 'chant'):
	righthyphenmin=1
	lefthyphenmin=1
	cutvowels = True

hyphenator = pyphen.Pyphen(filename='../patterns/hyph_la_'+args.mode+'.dic',left=lefthyphenmin,right=righthyphenmin)

def hyphenate_one_word(word):
	global hyphenator,args
	return hyphenator.inserted(word,args.hyphenchar)

wordregex = re.compile(r'\b[^\W\d_]+\b')

for line in args.inputfile:
	line = line.strip()
	hyphenline = wordregex.sub(lambda match: hyphenate_one_word(match.group(0)), line)
	args.outputfile.write(hyphenline+'\n')

args.inputfile.close()
args.outputfile.close()