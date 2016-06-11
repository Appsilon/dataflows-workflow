import rpy2.robjects as ro

repo = '/home/pawel/projects/cenatorium/cenatorium-avm'

elements = [
    'Ini.r',
    'config/ustawienia_dane.r',
    'config/ustawienia_parametry.r',
    '20_master_tworz_model.r',
    '21_slave_predict.r',
    'eval.r']

source = {}
for elem in elements:
  with open('%s/%s' % (repo, elem), 'r') as f:
    source[elem] = f.read()
    print "Read [%s], size=%s" % (elem, len(source[elem]))

ro.r('setwd("%s")' % repo)
ro.r('args = c(getwd(), "sessionID")')

for elem in elements:
  print "Running [%s]" % elem
  ro.r(source[elem])
