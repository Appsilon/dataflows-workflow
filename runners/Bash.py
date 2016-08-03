import subprocess

class Bash:

  process = None
  needed_variables = []

  def __init__(self, working_directory):
    self.process = subprocess.Popen("/bin/bash", shell=True, \
      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.append_code('cd %s' % working_directory)

  def append_code(self, code):
    self.process.stdin.write(bytes('%s\n' % code, 'utf8'))

  def execute(self):
    self.process.stdin.flush()
    stdout, stderr = self.process.communicate()
    variables = dict((name, self.extract_variable(stdout, name)) for name in self.needed_variables)
    return stdout, stderr, variables

  def variable_tag_open(self, variable):
    return "<var-%s>" % variable

  def variable_tag_close(self, variable):
    return "</var-%s>" % variable

  def extract_variable(self, stdout, variable):
    tag_open = bytes(self.variable_tag_open(variable), 'utf8')
    tag_close = bytes(self.variable_tag_close(variable), 'utf8')
    if tag_open in stdout:
      stdout = stdout.split(tag_open)[1]
      if tag_close in stdout:
        value = stdout.split(tag_close)[0]
        return value
    return ""

  def need_variable(self, variable):
    """TODO: We need clever method for retrieving process variables"""
    self.needed_variables.append(variable)
    tag_open = self.variable_tag_open(variable)
    tag_close = self.variable_tag_close(variable)
    self.append_code('echo "%s$%s%s"' % (tag_open, variable, tag_close))
