from kivy.app import App
from kivy.clock import Clock
from laser import Laser
from spaceship import Spaceship
from asteroidsgame import AsteroidsGame


class AsteroidsApp(App):

	def build(self):

		game = AsteroidsGame()

		# Update the game 60 times per second
		Clock.schedule_interval(game.update, 1.0/60.0)
		
		return game