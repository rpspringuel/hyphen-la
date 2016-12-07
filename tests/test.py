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
	print('differences in '+filename+':\nproofread result (correct) / result obtained by patterns (incorrect)')
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

def deacc(accstr):
	return accstr.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ý', 'y').replace('́', '').replace('ǽ', 'æ')

def dotest_accents(filename):
	global hyphenator
	print('differences in '+filename+':\nresult without accent (correct) / result with accent (incorrect)')
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			line = re.sub('\s*\%.*', '', line)
			baseacc = line.replace('-', '').lower()
			basenoacc = deacc(baseacc)
			resacc = hyphenator.inserted(baseacc)
			resnoacc = hyphenator.inserted(basenoacc)
			if not resnoacc == deacc(resacc):
				print(resnoacc+' / '+resacc)

dotest('proofreading-Claudio-2.txt')
print('\n')
dotest('proofreading-Solesmes-1.txt')
print('\n')
dotest('proofreading-Solesmes-2.txt')
print('\n')
dotest('proofreading-Solesmes-3.txt')
print('\n')
dotest('proofreading-diphtongues.txt')
print('\n')
dotest('proofreading-Flavigny-text-1.txt')
print('\n')
dotest('proofreading-Flavigny-2.txt')
print('\n')
dotest('orberg.txt', False)
print('\n')
dotest_accents('proofreading-Solesmes-2-accents.txt')
print('\n')
dotest_accents('proofreading-Solesmes-3-accents.txt')
print('\n')
