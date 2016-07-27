from readers.FileReader import FileReader

class Workflow:

  r_session = None # runner.R object
  debug = False
  workflow_args = dict()
  workflow_steps = list()

  def __init__(self, workflow_name, config, args, r_session):
    self.r_session = r_session
    self.debug = args.debug_mode()
    self.prepare_args(workflow_name, config, args)
    self.prepare_steps(workflow_name, config, args)
    self.r_session.run_code('rm(list=ls(all=TRUE))')

  def prepare_args(self, workflow_name, config, args):
    for arg_name in config.get_workflow_args(workflow_name):
      self.workflow_args[arg_name] = args.get(arg_name, "")

  def prepare_steps(self, workflow_name, config, args):
    selectable_step_options = config.get_workflow_steps_options(workflow_name)
    for step in config.get_workflow_steps(workflow_name):
      step_source_file = step
      is_selectable_step = step[0] == '$'
      if is_selectable_step:
        step = step[1:]
        step_source_file = selectable_step_options[step][args.get(step)]
      self.workflow_steps.append(step_source_file)

  def add_variables_to_scope(self):
    for var_name, var_value in self.workflow_args.items():
      new_variable_expr = '%s = "%s"' % (var_name, var_value)
      if self.debug: print("Adding new variable to scope: %s" % new_variable_expr)
      self.r_session.run_code(new_variable_expr)

  def run_steps(self):
    step_sources = []
    file_reader = FileReader()
    for step_source_file in self.workflow_steps:
      if self.debug: print("Reading %s" % step_source_file)
      step_sources.append(file_reader.read(step_source_file))
    for step_src in step_sources:
      self.r_session.run_code(step_src)

  def run(self):
    self.add_variables_to_scope()
    self.run_steps()

  def results(self, output_config):
    return {
      "files": ["%s/%s" % (working_directory, output_file) for output_file in output_config.get('files',[])],
      "values": dict((var, self.r_session.get_variable(var)) for var in output_config.get('vars',[]))
    }
