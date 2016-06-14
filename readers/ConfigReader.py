import yaml
import os
from FileReader import FileReader

class ConfigReader(FileReader):

  name = 'dataflows.yml'

  def __init__(self):
    FileReader.__init__(self)

  def get_config(self):
    if not os.path.exists(self.name):
      print "This is not Dataflows project. No dataflows.yml found!"
      print
      exit(1)
    raw_yml = self.read(self.name)
    return yaml.load(raw_yml)
