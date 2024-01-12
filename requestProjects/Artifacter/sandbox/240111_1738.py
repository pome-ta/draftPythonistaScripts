from pathlib import Path
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UsrAgn = 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'

# コスチュームの動的な指定
difference_costume_json = {
  "202901": {
    "iconName": "UI_AvatarIcon_KleeCostumeWitch",
    "sideIconName": "UI_AvatarIcon_Side_KleeCostumeWitch",
    "nameTextMapHash": 2343491290
  },
  "201501": {
    "iconName": "UI_AvatarIcon_KaeyaCostumeDancer",
    "sideIconName": "UI_AvatarIcon_Side_KaeyaCostumeDancer",
    "nameTextMapHash": 177626138
  }
}


class Artifacter:

  def __init__(self, uid):
    self.uid = uid
    ThreadPoolExecutor().submit(self.Initialization).result()

  def __get_req_json_dict(self, target_url: str) -> dict:
    req = urllib.request.Request(target_url, headers={'User-Agent': UsrAgn})
    try:
      with urllib.request.urlopen(req) as res:
        body = res.read().decode(errors='ignore')
        json_dict = json.loads(body)

    except urllib.error.HTTPError as err:
      print(err.code)

    except urllib.error.URLError as err:
      print(err.reason)

    return json_dict

  def Initialization(self):
    # データの表記名データをEnka.Network公式Githubから取得
    self.locale_jp = ThreadPoolExecutor().submit(self.locale).result()
    # キャラクターデータをEnka.Network公式Githubから取得
    self.characters_json = ThreadPoolExecutor().submit(
      self.character_json).result()
    self.costumes = ThreadPoolExecutor().submit(self.costume_json).result()

    player_data: dict = {}
    url = f'https://enka.network/api/uid/{self.uid}'
    player_data = self.__get_req_json_dict(url)

    self.player_data = player_data

  def locale(self):  # 読み込んだデータの日本語化
    url = 'https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/loc.json'
    LJsn = self.__get_req_json_dict(url)

    for percent in [ja for ja in LJsn['ja'] if 'PERCENT' in ja]:
      if '力' in LJsn['ja'][percent]:
        LJsn['ja'][percent] = LJsn['ja'][percent].replace('力', 'パーセンテージ')
      else:
        LJsn['ja'][percent] = LJsn['ja'][percent].replace(
          LJsn['ja'][percent][-1],
          '{}パーセンテージ'.format(LJsn['ja'][percent][-1]))
    return LJsn['ja']

  def character_json(self):  # キャラクター情報の取得
    url = 'https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/characters.json'
    return self.__get_req_json_dict(url)

  def costume_json(self):  # コスチューム情報の動的な抽出
    url = 'https://raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/costumes.json'
    CosJsn = self.__get_req_json_dict(url)

    for key, value in difference_costume_json.items():
      CosJsn[key] = value
    return CosJsn

  def playerinfo(self):  # プレイヤー情報の一部を取得
    # 取得したデータから「playerInfo」を取得
    player_infomation = self.player_data['playerInfo']
    # 取得した「playerInfo」から「showAvatarInfoList」がある場合は以下を実行
    if 'showAvatarInfoList' in player_infomation:
      # 取得したプレイヤーデータからキャラクター名を日本語へ変換
      for avater in player_infomation['showAvatarInfoList']:
        avatarId = avater['avatarId']
        character = self.characters_json[avatarId]
        map_hash = character['NameTextMapHash']
        avater['name'] = self.locale_jp[map_hash]

    return player_infomation

  def main(self):
    print('o')


if __name__ == '__main__':
  uid_path = Path('./uid.txt')
  UID = uid_path.read_text()
  artifacter = Artifacter(UID)
  print('h')
  #ThreadPoolExecutor().submit(artifacter.main)

