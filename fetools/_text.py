from math import radians, sin, cos


def _getchar(c: str) -> tuple:
	'''
	Get the points for a character.
	Returns tuple in the form (paths, width)
	'''
	alphanum = {
		"A": [
			[(-3, -5), (0,5), (3, -5)],
			[(-1.5,0), (1.5,0)]
		],
		"B": [
			[(-3,5), (1,5), (3,4), (3,1), (1,0), (3,-1), (3,-4), (1,-5), (-3,-5), (-3,5)],
			[(-3,0), (1,0)]
		],
		"C": [
			[(3,5), (-1,5), (-3,3), (-3,-3), (-1,-5), (3,-5)]
		],
		"D": [
			[(-3,-5), (-3,5), (1,5), (3,3), (3,-3), (1,-5), (-3,-5)]
		],
		"E": [
			[(3,5), (-3,5), (-3,-5), (3,-5)],
			[(-3,0), (2, 0)]
		],
		"F": [
			[(3,5), (-3,5), (-3,-5)],
			[(-3,0), (3,0)]
		],
		"G": [
			[(3,5), (-1,5), (-3,3), (-3,-3), (-1,-5), (3,-5), (3,0), (0,0)]
		],
		"H": [
			[(-3,5), (-3,-5)],
			[(-3,0), (3,0)],
			[(3,5), (3,-5)]
		],
		"I": [
			[(-3,5), (3,5)],
			[(0,5), (0,-5)],
			[(-3,-5), (3,-5)]
		],
		"J": [
			[(-3,5), (3,5)],
			[(-3,-3), (-2,-5), (0,-5), (1,-3), (1,5)]
		],
		"K": [
			[(-3,5), (-3,-5)],
			[(3,5), (-3,0), (3,-5)]
		],
		"L": [
			[(-3,5), (-3,-5), (3,-5)]
		],
		"M": [
			[(-3,-5), (-3,5), (0,-1), (3,5), (3,-5)]
		],
		"N": [
			[(-3,-5), (-3,5), (3,-5), (3,5)]
		],
		"O": [
			[(-1,-5), (-3,-3), (-3,3), (-1,5), (1,5), (3,3), (3,-3), (1,-5), (-1,-5)]
		],
		"P": [
			[(-3,-5), (-3,5), (2,5), (3,4), (3,1), (2,0), (-3,0)]
		],
		"Q": [
			[(-1,-5), (-3,-3), (-3,3), (-1,5), (1,5), (3,3), (3,-3), (1,-5), (-1,-5)],
			[(0,0), (3,-5)]
		],
		"R": [
			[(-3,-5), (-3,5), (2,5), (3,4), (3,1), (2,0), (-3,0), (3,-5)]
		],
		"S": [
			[(3,5), (-1,5), (-3,3), (-3,2), (-1,0), (1,0), (3,-2), (3,-3), (1,-5), (-3,-5)]
		],
		"T": [
			[(-3,5), (3,5)],
			[(0,5), (0,-5)]
		],
		"U": [
			[(-3,5), (-3,-3), (-1,-5), (1,-5), (3,-3), (3,5)]
		],
		"V": [
			[(-3,5), (0,-5), (3,5)]
		],
		"W": [  
			[(-3,5), (-2,-5), (0,1), (2,-5), (3,5)]
		],
		"X": [
			[(-3,5), (3,-5)],
			[(-3,-5), (3,5)]
		],
		"Y": [
			[(-3,5), (0,0), (3,5)],
			[(0,0), (0,-5)]
		],
		"Z": [
			[(-3,5), (3,5), (-3,-5), (3,-5)]
		],
		"1": [
			[(-2,2), (0,5), (0,-5)],
			[(-3,-5), (3,-5)]
		],
		"2": [
			[(-3,4), (-2,5), (2,5), (3,4), (3,1), (2,0), (-2,-1), (-3,-2), (-3,-5), (3,-5)]
		],
		"3":[
			[(-3,5), (2,5), (3,4), (3,1), (2,0), (3,-1), (3,-4), (2,-5), (-3,-5)],
			[(2,0), (-2,0)]
		],
		"4": [
			[(-3,5), (-3,0), (3,0)],
			[(3,5), (3,-5)]
		],
		"5": [
			[(3,5), (-3,5), (-3,0), (2,0), (3,-1), (3,-4), (2,-5), (-3,-5)]
		],
		"6": [
			[(3,5), (-2,5), (-3,4), (-3,-4), (-2,-5), (2,-5), (3,-4), (3,-1), (2,0), (-3,0)]
		],
		"7": [
			[(-3,5), (3,5), (-2,-5)]
		],
		"8": [
			[(-2,0), (-3,1), (-3,4), (-2,5), (2,5), (3,4), (3,1), (2,0), (3,-1), (3,-4), (2,-5), (-2,-5), (-3,-4), (-3,-1), (-2,0)],
			[(-2,0), (2,0)]
		],
		"9": [
			[(-3,-5), (2,-5), (3,-4), (3,4), (2,5), (-2,5), (-3,4), (-3,1), (-2,0), (3,0)]
		],
		"0": [
			[(-1,-5), (-3,-3), (-3,3), (-1,5), (1,5), (3,3), (3,-3), (1,-5), (-1,-5)],
			[(-3,-3), (3,3)]
		]
	}
	punc4 = {
		".": [
			[(-0.5,-3), (-0.5,-5), (0.5,-5), (0.5,-3), (-0.5,-3)]
			# [(0,-5), (0,-2)]
		],
		",": [
			[(0,-3), (0,-5), (-2,-8)]
		],
		"-": [
			[(-2,0), (2,0)]
		],
		"(": [
			[(1,6), (0,5), (-1,0), (0,-5), (1,-6)]
		],
		")": [
			[(-1,6), (0,5), (1,0), (0,-5), (-1,-6)]
		],
		"!": [
			[(-0.5,-3), (-0.5,-5), (0.5,-5), (0.5,-3), (-0.5,-3)],
			[(0,-1), (0,6)]
		],
		'"': [
			[(-1,5), (-1,1)],
			[(1,5), (1,1)]
		],
		"'": [
			[(0,5), (0,1)]
		],
		"/": [
			[(2,5), (-2,-5)]
		],
		"\\": [
			[(-2,5), (2,-5)]
		],
		"*": [
			[(-2,5), (2,1)],
			[(-2,1), (2,5)],
			[(-2,3), (2,3)],
			[(0,5), (0,1)]
		],
		":": [
			[(0,3), (0,1)],
			[(0,-3), (0,-1)]
		]
	}
	punc6 = {
		"_": [
			[(-3,-5), (3,-5)]
		],
		"#": [
			[(-3,3), (3,3)],
			[(-3,-1), (3,-1)],
			[(-1,5), (-1,-3)],
			[(1,5), (1,-3)]
		],
		"=": [
			[(-3,1), (3,1)],
			[(-3,-1), (3,-1)]
		],
	}
	if c in alphanum:
		return (alphanum[c], 6)
	elif c in punc4:
		return (punc4[c], 4)
	elif c in punc6:
		return (punc6[c], 6)
	else:
		raise ValueError(f"{repr(c)} isn't a recognized character")


def _movept(x, y, angle, xoff, yoff):
	# Rotate the point
	rotx = x*cos(angle) + y*sin(angle)
	roty = -x*sin(angle) + y*cos(angle)
	# Translate the point
	transx = rotx + xoff
	transy = roty + yoff
	return (transx, transy)


def _test(text, height, hdg, startx, starty):
	import turtle

	WIDTH = 800
	angle = radians(hdg)
	x, y = 0, 0
	scl = height / 10

	turtle.setup(WIDTH, 400)
	turtle.tracer(0)
	turtle.penup()
	turtle.goto(x, y)

	for c in text.upper():
		if c == " ":
			x += 10*scl
			continue
		paths, width = _getchar(c)
		for line in paths:
			# x and y for first point of next line
			targx = x + line[0][0]*scl
			targy = y + line[0][1]*scl
			# Transform point
			nextx, nexty = _movept(targx, targy, angle, startx, starty)
			turtle.goto(nextx, nexty)
			turtle.pendown()
			for pt in line[1:]:
				# x and y for next point of line
				targx = x + pt[0]*scl
				targy = y + pt[1]*scl
				# Transform point
				nextx, nexty = _movept(targx, targy, angle, startx, starty)
				turtle.goto(nextx, nexty)
			turtle.penup()
		x += scl*(width + 4)

	# turtle.goto(startx-4*scl, starty-5*scl)
	# turtle.pendown()
	# turtle.goto(startx-4*scl, starty+height-5*scl)
	# turtle.penup()

	turtle.goto(startx, starty)
	turtle.tracer(1)
	turtle.mainloop()


class Text:
	""" Stores text as lat/lon line segments """

	def __init__(self, text, height, lat=0, lon=0, heading=0):
		self.text = text
		self.height = height
		self.lat = lat
		self.lon = lon
		self.heading = heading

	@property
	def heading(self):
		return self._heading

	@heading.setter
	def heading(self, val):
		self._heading = val % 360

	def coords(self):
		angle = radians(self.heading)
		x, y = 0, 0
		scl = self.height / 10  # (desired height / character height)
		# Generate each character
		coords = []
		for c in self.text.upper():
			# Skip spaces
			if c == " ":
				x += 10*scl
				continue
			# Get the offsets for the char
			paths, width = _getchar(c)
			for line in paths:
				# Generate each line segment
				segment = []
				for pt in line:
					# x and y for  point of line
					targx = x + pt[0]*scl
					targy = y + pt[1]*scl
					# Transform point
					nextx, nexty = _movept(targx, targy, angle, self.lat, self.lon)
					segment.append((nextx, nexty))
				coords.append(segment)
			x += scl*(width + 4)
		return coords


if __name__ == "__main__":
	_test("Testing 123", height=25, hdg=0, startx=-300, starty=0)
	text = Text("A", 10)
	print(text.heading)