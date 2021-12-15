import sys

def dot():
	"""print graph in dot format

	>>> python3 dot.py <graph-path>
	>>> python3 dot.py <graph-path> <result-path>
	"""

	with open(sys.argv[1]) as file:
		# n = |V|, m = |E|
		n, m = map(int, file.readline().split())

		print('graph{')
		print('concentrate=true')

		# if there is a result 
		if len(sys.argv) > 2:
			print('\n{')
			print('node [style=filled, fillcolor=red]')
			for i, x in enumerate(open(sys.argv[2])):
				if int(x) == 1:
					print(i + 1, end=' ')
			print('\n}\n')

		# edges
		for u in range(1, n + 1):
			print('{} -- {{{}}}'.format(
				u,
				file.readline().rstrip()
			))

		print('}')

if __name__ == '__main__':
	dot()