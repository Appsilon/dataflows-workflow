import os
import json

from readers.FileReader import FileReader
from readers.DataflowsConfigReader import DataflowsConfigReader
from readers.ArgsReader import ArgsReader
from runners.R import R
from version import dataflows_version
from workflow import Workflow


config = DataflowsConfigReader().get_config() # TODO get run/steps powinno byc w DataflowsConfigReader
args = ArgsReader(config.get('run', {}).get('args', []), config.get('steps_options', {})).parse_args()

DEBUG = args['debug']

if args['version']:
  print("Dataflows version: %s\n" % dataflows_version)
  exit(0)

if args['config']:
  print("<dataflows>%s</dataflows>" % json.dumps(config))
  exit(0)

working_directory = os.path.realpath('.')
r_session = R(working_directory)

workflow = Workflow(r_session, FileReader(), DEBUG)
workflow.add_variables_to_scope(config['run']['args'], args)
workflow.run(config['run']['steps'], config['steps_options'], args)
results = workflow.results(config['run']['output'])

print("<dataflows>%s</dataflows>" % json.dumps(results))
