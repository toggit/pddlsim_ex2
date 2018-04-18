#from executor import Executor
import sys
import pddlsim.planner as planner
from pddlsim.executors.executor import Executor

class SmartReplanner(Executor):
	"""docstring for SmartReplanner."""
	def __init__(self):
		super(SmartReplanner, self).__init__()
		self.steps = []
		self.plan = []

	def initialize(self, services):
		self.services = services

	def next_action(self):
		if self.services.goal_tracking.reached_all_goals():
			return None
			
		self.steps = self.services.valid_actions.get()
		if len(self.steps) == 0: return None
		if len(self.steps) == 1: return self.steps[0]
		
		if self.plan == []:
			problem_path = self.services.problem_generator.generate_problem(self.services.goal_tracking.uncompleted_goals[0], self.services.perception.get_state())
			self.plan = self.services.planner(self.services.pddl.domain_path, problem_path)
		if len(self.plan) > 0: 
			return self.plan.pop(0)
		return None


from pddlsim.local_simulator import LocalSimulator

domain_path = sys.argv[1]
problem_path = sys.argv[2]
print LocalSimulator().run(domain_path, problem_path, SmartReplanner())