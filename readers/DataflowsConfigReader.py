import yaml
import os
import json

from readers.FileReader import FileReader

class DataflowsConfigReader(FileReader):

  name = "dataflows.yml"
  config = {}

  def __init__(self):
    FileReader.__init__(self)
    try:
      raw_yml = self.read(self.name)
      self.config = yaml.load(raw_yml)
    except:
      self.config = {}

  def get_json(self):
    return json.dumps(self.config)

  def get_release(self):
    return self.config.get("release", "")

  def get_workflow_names(self):
    return list(self.config.get("workflows", {}).keys())

  def get_workflow_config(self, workflow_name):
    return self.config.get("workflows", {}).get(workflow_name, {})

  def get_workflow_steps(self, workflow_name):
    workflow_config = self.get_workflow_config(workflow_name)
    return workflow_config.get("steps", [])

  def get_workflow_steps_options(self, workflow_name):
    workflow_config = self.get_workflow_config(workflow_name)
    return workflow_config.get("steps_options", {})

  def get_workflow_args(self, workflow_name):
    workflow_config = self.get_workflow_config(workflow_name)
    return workflow_config.get("args", [])
