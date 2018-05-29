#!/bin/env python
import sys

prints = []
normalized_output = True
MAX_DOT_NOTATION_LEN = 50

def convert(lvl, d_lvl, lvls, c):
	if c == '*':
		s = ''
		for i in range(lvl - 1):
			s += str(lvls[i]) + "."
		s += str(lvls[lvl - 1])
		return s
	else:
		return "-"

def count(s, c):
	count = 0
	while count < len(s) and s[count] == c:
		count += 1
	return count

def print_tabs(lvl, d_lvl, lvls, line, c):
	prefix =  ''
	if c != '*' or not normalized_output:
                prefix = '\t' * (d_lvl if normalized_output else lvl + d_lvl)
	prefix += convert(lvl, d_lvl, lvls, c)
	prints.append(prefix + line[count(line, c):])

def print_section():
	if len(prints) == 0:
		return

	for i in range(len(prints) - 1):
		line = prints[i]
		next_line = prints[i + 1]
		if line.strip().startswith('-') and next_line.strip().startswith('-'):
			if count(prints[i + 1], '\t') > count(prints[i], '\t'):
				idx = line.find('-')
				prints[i] = line[:idx] + '+' + line[idx + 1:]
		print(prints[i])
	print(prints[-1])

	# Clear the prints list.
	prints[:] = []

# Tail recursion example
def parse_tail_recursive(lines, idx, curr_lvl, dot_lvl, lvls):
	if lines is None:
		line = sys.stdin.readline()
		if not line:
			print_section()
			return
	else:
		if len(lines) == idx:
			print_section()
			return
		line = lines[idx]

	line = line.strip()
	if not line:
		parse_tail_recursive(lines, idx + 1, curr_lvl, dot_lvl, lvls)
	elif line.startswith('.'):
		x = count(line, '.')
		print_tabs(curr_lvl, x, lvls, line, '.')

		parse_tail_recursive(lines, idx + 1, curr_lvl, x, lvls)
	elif line.startswith('*'):
		print_section()

		x = count(line, '*')
		if curr_lvl < x:
			lvls[x - 1] = 1
		else:
			lvls[x - 1] += 1

		print_tabs(x, 0, lvls, line, '*')
		parse_tail_recursive(lines, idx + 1, x, 0, lvls)
	else:
		subs = prints[-1][:count(prints[-1], '\t')]
		prints[-1] += "\n" + subs + "  " + line
		parse_tail_recursive(lines, idx + 1, curr_lvl, dot_lvl, lvls)

# The iterative approach
def parse_and_build_list():
	lvls = [0 for i in range(MAX_DOT_NOTATION_LEN)]
	curr_level = dot_level = 0
	for line in sys.stdin:
		line = line.strip()
		# Skip over plain white space..
		if len(line) == 0:
			continue

		if line.startswith('.'):
			dot_level = count(line, '.')
			print_tabs(curr_level, dot_level, lvls, line, '.')
		elif line.startswith('*'):
			print_section()

			x = count(line, '*')
			if curr_level < x:
				lvls[x - 1] = 1
			else:
				lvls[x - 1] += 1

			curr_level  = x
			dot_level = 0

			print_tabs(curr_level, dot_level, lvls, line, '*')
		else:
			s = prints[-1]
			prints[-1] += "\n" + s[:count(s, '\t')] + "  " + line
	print_section()

if __name__ == "__main__":
	sections = [0 for i in range(MAX_DOT_NOTATION_LEN)]
	#parse_tail_recursive(open('input2.txt').readlines(), 0, 0, 0, sections)
	parse_tail_recursive(None, 0, 0, 0, sections)

	#parse_and_build_list()
