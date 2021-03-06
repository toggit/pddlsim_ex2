import random
from pddlsim.local_simulator import LocalSimulator
#from pddlsim.successors.tracked_successor import TrackedSuccessor

class RandomExecutor(object):
	""" RandomExecutor - pick a random valid action each step
	"""
	def __init__(self):
		self.successor = None
		print "__init__"
		print self.successor

	
	def initialize(self, services):
		self.services = services


	def next_action(self):
		if self.services.goal_tracking.reached_all_goals():
			return None
		options = self.services.valid_actions.get()
		print options
		if len(options) == 0: return None
		if len(options) == 1: return options[0]
		return self.pick_from_many(options)

	def pick_from_many(self, options):
		chosen = random.choice(options)
		return chosen


domain_path = "domain.pddl"
problem_path = "problem.pddl"
print LocalSimulator().run(domain_path, problem_path, RandomExecutor())
