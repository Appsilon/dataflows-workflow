import os
import json
import argparse

from readers.FileReader import FileReader
from readers.ConfigReader import ConfigReader
from runners.R import R


config = ConfigReader().get_config()

parser = argparse.ArgumentParser(description="Dataflows | Data Science Workflow")
parser.add_argument("-c", "--config", action="store_true", help="parse dataflows.yml and return config object", required=False)
for step, options in config['config'].items(): # Add steps
  parser.add_argument("-%s" % step, help=step, type=int, choices=range(len(options)), default=0)
for argument in config['run']['args']: # Add variables
  parser.add_argument("-%s" % argument, help=argument, default=None)
args = vars(parser.parse_args())

if args['config']:
  print json.dumps(config)
  exit(0)

reader = FileReader()

working_directory = os.path.realpath('.')
r = R(working_directory)

r.run_code('setwd("%s")' % working_directory)
r.run_code('rm(list=ls(all=TRUE))')

step_sources = []
for step in config['run']['steps']:
  step_source_file = step
  if step[0] == '$':
    step = step.replace('$', '')
    step_source_file = config['config'][step][args[step]]
  print "Reading %s" % step_source_file
  step_sources.append(reader.read(step_source_file))

for step_src in step_sources:
  r.run_code(step_src)

# Read vars and return json obj
