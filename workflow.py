class Workflow:

  r_session = None
  file_reader = None
  debug = False

  def __init__(self, r_session, file_reader, debug = False):
    self.r_session = r_session
    self.file_reader = file_reader
    self.debug = debug
    self.r_session.run_code('rm(list=ls(all=TRUE))')

  def add_variables_to_scope(self, var_names, var_values):
    for var in var_names:
      new_variable_expr = '%s = "%s"' % (var, var_values[var])
      if self.debug: print("Adding new variable to scope: %s" % new_variable_expr)
      self.r_session.run_code(new_variable_expr)

  def run(self, steps, selectable_step_options, args):
    step_sources = []

    for step in steps:
      step_source_file = step
      is_selectable_step = step[0] == '$'
      if is_selectable_step:
        step = step[1:]
        step_source_file = selectable_step_options[step][args[step]]
      if self.debug: print("Reading %s" % step_source_file)
      step_sources.append(self.file_reader.read(step_source_file))

    for step_src in step_sources:
      self.r_session.run_code(step_src)

  def results(self, output_config):
    return {
      "files": ["%s/%s" % (working_directory, output_file) for output_file in output_config.get('files',[])],
      "values": dict((var, self.r_session.get_variable(var)) for var in output_config.get('vars',[]))
    }
