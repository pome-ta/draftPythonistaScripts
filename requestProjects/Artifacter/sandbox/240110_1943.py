from pathlib import Path
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UsrAgn = 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'


class Artifacter:

  def __init__(self, uid):
    self.uid = uid
    ThreadPoolExecutor().submit(self.Initialization).result()

  def Initialization(self):
    # データの表記名データをEnka.Network公式Githubから取得
    #self.locale_jp = ThreadPoolExecutor().submit(self.locale).result()
    # キャラクターデータをEnka.Network公式Githubから取得
    #self.characters_json = ThreadPoolExecutor().submit(self.character_json).result()
    #self.costumes = ThreadPoolExecutor().submit(self.costume_json).result()

    url = f'https://enka.network/api/uid/{self.uid}'
    try:

      req = urllib.request.Request(url, headers={'User-Agent': UsrAgn})
      print('r')
      print(req)
      json_data = urllib.request.urlopen(req).read().decode(errors='ignore')
      self.player_data = json.loads(json_data)
    except:
      pass

  def main(self):
    print('o')


if __name__ == '__main__':
  uid_path = Path('./uid.txt')
  UID = uid_path.read_text()
  artifacter = Artifacter(UID)
  print('h')
  #ThreadPoolExecutor().submit(artifacter.main)

