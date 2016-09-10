#!/usr/bin/env python3

import pyphen
import sys
import re

hyphenator = pyphen.Pyphen(filename='../patterns/hyph_la_liturgical.dic',left=1,right=1)

def comparenoncompletehyphens(original, obtained):
	i = 0
	for c in obtained:
		if c == '-':
			if original[i] == '-':
				i = i + 1
		else:
			if original[i] == '-':
				return False
			else:
				i = i + 1
	return True

def dotest(filename, allhyphens=True):
	global hyphenator
	print('differences in '+filename+':\nproofread result / result obtained by patterns')
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			line = re.sub('\s*\%.*', '', line)
			base = line.replace('-', '')
			new = hyphenator.inserted(base)
			if allhyphens:
				if not line == new:
					print(line+' / '+new)
			else:
				if not comparenoncompletehyphens(line, new):
					print(line+' / '+new)	

dotest('proofreading-Claudio-2.txt')
print('\n')
dotest('proofreading-Solesmes-1.txt')
print('\n')
dotest('proofreading-Solesmes-2.txt')
print('\n')
dotest('proofreading-Solesmes-3.txt')
print('\n')
dotest('proofreading-Flavigny-text-1.txt')
print('\n')
dotest('orberg.txt', False)
