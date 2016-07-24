import yaml
import os

from readers.FileReader import FileReader

class DataflowsConfigReader(FileReader):

  name = 'dataflows.yml'

  def __init__(self):
    FileReader.__init__(self)

  def get_config(self):
    try:
      raw_yml = self.read(self.name)
      return yaml.load(raw_yml)
    except:
      return {}
