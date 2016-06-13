class Reader:

  working_directory = ""

  def __init__(self, working_directory):
    self.working_directory = working_directory

  def abs_path(self, rel_path):
    return "%s/%s" % (self.working_directory, rel_path)

  def read(self, relative_file_path):
    with open(self.abs_path(relative_file_path), 'r') as f:
      return f.read()
