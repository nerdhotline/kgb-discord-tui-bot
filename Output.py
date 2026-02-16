import re
class Output:
  def __init__(self):
    self.id = 0
  
  def outPrint(self, txt:str):
    ## Check for bolding
    txt = txt.replace('**', '')
    txt = f'\033[1m{txt}\033[0m'
    print(txt)