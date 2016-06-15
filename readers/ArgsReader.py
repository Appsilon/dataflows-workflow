import argparse

class ArgsReader:

  parser = None
  variables = None
  steps = None

  def __init__(self, variables, steps):
    self.parser = argparse.ArgumentParser(description="Dataflows | Data Science Workflow")
    self.variables = variables
    self.steps = steps

  def parse_args(self):
    self.parser.add_argument("-c", "--config", action="store_true", help="parse dataflows.yml and return config object", required=False)
    self.parser.add_argument("-d", "--debug", action="store_true", help="show debug messages", required=False)
    self.parser.add_argument("-v", "--version", action="store_true", help="show Dataflows version", required=False)
    
    for step, options in self.steps.items():
      self.parser.add_argument("--%s" % step, help=step, type=int, choices=range(len(options)), default=0)
    
    for argument in self.variables:
      self.parser.add_argument("--%s" % argument, help=argument, default=None)
    
    return vars(self.parser.parse_args())