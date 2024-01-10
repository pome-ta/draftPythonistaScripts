import concurrent.futures


class Artifacter:

  def __init__(self, uid):
    self.uid = uid
    
  def Initialization(self):
    pass
    
  def main(self):
    print('o')


if __name__ == '__main__':
  UID = 
  artifacter = Artifacter(0)
  print('h')
  concurrent.futures.ThreadPoolExecutor().submit(artifacter.main)

