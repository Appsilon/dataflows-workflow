import yaml
from Reader import Reader

class YamlReader(Reader):
  def read(self, file_path):
    return "YAML"