import rpy2.robjects as ro

class R:
  def __init__(self, working_directory):
    ro.r('setwd("%s")' % working_directory)

  def run_code(self, code):
    """Execute R code"""
    ro.r(code)

  def get_variable(self, variable):
    """Read variable value from the current R scope"""
    pass
