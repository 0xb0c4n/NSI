class Chrono:
	heure_max = 24
	def __init__(self,h,m,s):
		self._temps = 3600*h+60*m+s

	def avance(self,s):
		self._temps += s

	def _conversion(self):
		s = self._temps()
		return (s // 3600, (s // 60) % 60, s % 60)
	
	def __str__(self):
		h,m,s = self._conversion()
		return (str(h) + "h " + str(m) + "m " + str(s) + "s ")
	 
	def clone(self, h, m, s):
		u = Chrono(h,m,s)
		return u

	def __eq__(self, u):
		return (self.h == u.h and self.m == u.m and self.s == u.s)