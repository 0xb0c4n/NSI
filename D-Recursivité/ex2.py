import sys
sys.setrecursionlimit(2000)

def syracuse(un):
	if un % 2 == 0:
		print(syracuse(un)/2)
	else:
		print(syracuse(un)*3+1)
syracuse(10)
