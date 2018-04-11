#from executor import Executor
import pddlsim.planner as planner
from pddlsim.executors.executor import Executor

class PlanDispatcher(Executor):
	"""docstring for PlanDispatcher."""
	def __init__(self):
		super(PlanDispatcher, self).__init__()
		self.steps = []

	def initialize(self,services):
		self.steps = planner.make_plan(services.pddl.domain_path, services.pddl.problem_path)

	def next_action(self):
		if len(self.steps)>0:
			return self.steps.pop(0).lower()
		return None


from pddlsim.local_simulator import LocalSimulator
from pddlsim.executors.plan_dispatch import PlanDispatcher

domain_path = "domain.pddl"
problem_path = "problem.pddl"
print LocalSimulator().run(domain_path, problem_path, PlanDispatcher())