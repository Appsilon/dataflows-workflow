import argparse

class ArgsReader:

  parser = None
  subparsers = None
  config = None
  restricted_arg_names = {'c','d','v','r','workflow'}
  args = dict()

  def __init__(self, config):
    self.parser = argparse.ArgumentParser(description="Dataflows | Data Science Workflows")
    self.subparsers = self.parser.add_subparsers(help='Available workflows', dest="workflow")
    self.config = config
    self.args = self.__parse_args()

  def __parse_args(self):
    self.parser.add_argument("-c", action="store_true", help="config - parse dataflows.yml and return config object", required=False)
    self.parser.add_argument("-d", action="store_true", help="debug - show debug messages", required=False)
    self.parser.add_argument("-v", action="store_true", help="version - show Dataflows version", required=False)
    self.parser.add_argument("-r", action="store_true", help="release - show project release", required=False)

    for workflow_name in self.config.get_workflow_names():
      subparser = self.subparsers.add_parser(workflow_name, help='%s workflow' % workflow_name)

      for step, options in self.config.get_workflow_steps_options(workflow_name).items():
        if step in self.restricted_arg_names:
          raise Exception("You can't use `%s` for argument name in dataflows.yml" % step)
        subparser.add_argument("--%s" % step, help=step, type=str, choices=options.keys(), required = True)
      
      for argument in self.config.get_workflow_args(workflow_name):
        if argument in self.restricted_arg_names:
          raise Exception("You can't use `%s` for argument name in dataflows.yml" % argument)
        subparser.add_argument("--%s" % argument, help=argument, required = True)
    
    return vars(self.parser.parse_args())

  def get(self, key, default = None):
    if default is None and key not in self.args:
      raise Exception("Missing argument `%s`" % key)
    return self.args.get(key, default)

  def debug_mode(self):
    return self.get('d', False)

  def show_version(self):
    return self.get('v', False)

  def show_config(self):
    return self.get('c', False)

  def show_release(self):
    return self.get('r', False)

  def workflow(self):
    return self.get('workflow', None)
