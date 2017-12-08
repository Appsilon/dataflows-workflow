import os
import json

from readers.DataflowsConfigReader import DataflowsConfigReader
from readers.ArgsReader import ArgsReader
from runners.R import R
from version import dataflows_version
from workflow import Workflow

config = DataflowsConfigReader()
args = ArgsReader(config)

def print_in_dataflows_tag(data):
  print("<dataflows>%s</dataflows>" % data)

if args.show_version():
  print("Dataflows version: %s\n" % dataflows_version)
  exit(0)

if args.show_config():
  print_in_dataflows_tag(config.get_json())
  exit(0)

if args.show_release():
  print("Project release: %s" % config.get_release())
  exit(0)

if not args.workflow():
  print("No workflow chosen. Type `dataflows -h` to view available workflows")
  exit(0)
else:
  working_directory = os.path.realpath('.')
  session = R(working_directory)
  workflow = Workflow(args.workflow(), config, args, session)
  workflow.run()
  results = workflow.results()
  print_in_dataflows_tag(json.dumps(results, sort_keys=True, indent=4, separators=(',', ': ')))
