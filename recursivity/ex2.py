import sys
sys.setrecursionlimit(2000)

def syracuse(un):
	if un == 1:
	   return None
	if un % 2 == 0:
	   syracuse(un//2)
	else:
	   syracuse(un*3+1)
syracuse(10)
