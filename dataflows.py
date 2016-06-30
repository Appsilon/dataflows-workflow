import os
import json

from readers.FileReader import FileReader
from readers.DataflowsConfigReader import DataflowsConfigReader
from readers.ArgsReader import ArgsReader
from runners.R import R
from version import dataflows_version


config = DataflowsConfigReader().get_config()
args = ArgsReader(config['run']['args'], config['steps_options']).parse_args()

DEBUG = args['debug']

if args['version']:
  print "Dataflows version: %s" % dataflows_version
  print
  exit(0)
if args['config']:
  print "<dataflows>%s</dataflows>" % json.dumps(config)
  exit(0)

reader = FileReader()

working_directory = os.path.realpath('.')
r = R(working_directory)

# Initialization.

r.run_code('setwd("%s")' % working_directory)
r.run_code('rm(list=ls(all=TRUE))')

# Adding arguments to scope.

for argument in config['run']['args']:
  new_variable_expr = '%s = "%s"' % (argument, args[argument])
  if DEBUG: print "Adding new variable to scope: %s" % new_variable_expr
  r.run_code(new_variable_expr)

# Executing workflow steps.

step_sources = []
for step in config['run']['steps']:
  step_source_file = step
  is_selectable_step = step[0] == '$'
  if is_selectable_step:
    step = step[1:]
    step_source_file = config['steps_options'][step][args[step]]
  if DEBUG: print "Reading %s" % step_source_file
  step_sources.append(reader.read(step_source_file))

for step_src in step_sources:
  r.run_code(step_src)

# Reading results

results = {
  "files": ["%s/%s" % (working_directory, output_file) for output_file in config['run']['output']['files']],
  "values": dict((var, r.get_variable(var)) for var in config['run']['output']['vars'])
}

print "<dataflows>%s</dataflows>" % json.dumps(results)
