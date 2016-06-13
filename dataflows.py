from readers.Reader import Reader
from runners.R import R

elements = [
    'Ini.r',
    'config/ustawienia_dane.r',
    'config/ustawienia_parametry.r',
    '20_master_tworz_model.r',
    '21_slave_predict.r',
    'eval.r']

work_dir = '/home/pawel/projects/cenatorium/cenatorium-avm'
reader = Reader(work_dir)
r = R(work_dir)

# What is my working dir?
# Is there dataflows.yml? no -> this is not dataflows project

r.run_code('setwd("%s")' % work_dir)
r.run_code('rm(list=ls(all=TRUE))')

for elem in elements:
  code = reader.read(elem)
  r.run_code(code)
