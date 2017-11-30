class R:
  session = None

  def __init__(self, working_directory):
    import rpy2.robjects as ro
    self.session = ro
    self.session.r('setwd("%s")' % working_directory)

  def run_code(self, code):
    """Execute R code"""
    self.session.r(code)

  def get_variable(self, variable):
    """Read variable value from the current R scope"""
    return self.session.globalenv[variable][0]
