

class TacTac:

	board = [
		"-|-|-",
		"-|-|-",
		"-|-|-",
		
	]

	def repr(self):
		print(self.board)

	def addToken(self, point, loc):
		#'X' or 'O' point
		# (x, y) loc

		for row in self.board:
			r = row.split("|")
			print(r)


tt = TacTac()

tt.addToken('X', (0, 0))
tt.repr()
