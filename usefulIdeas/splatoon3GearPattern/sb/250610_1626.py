from itertools import product

normal_gears = [  # 通常ギアパワー
  'メ',  # インク効率アップ(メイン)
  'サ',  # インク効率アップ(サブ)
  '回',  # インク回復力アップ
  '人',  # ヒト移動速度アップ
  'ダ',  # イカダッシュ速度アップ
  '増',  # スペシャル増加量アップ
  '減',  # スペシャル減少量ダウン
  '能',  # スペシャル性能アップ
  '復',  # 復活時間短縮
  'ジ',  # スーパージャンプ時間短縮
  '性',  # サブ性能アップ
  '安',  # 相手インク影響軽減
  '影',  # サブ影響軽減
  'ア',  # アクション強化
]

head_gears = [  # アタマ専用ギアパワー
  'ス',  # スタートダッシュ
  'ラ',  # ラストスパート
  '逆',  # 逆境強化
  'カ',  # カムバック
]

wear_gears = [  # フク専用ギアパワー
  '忍',  # イカニンジャ
  'リ',  # リベンジ
  'マ',  # サーマルインク
  'ぺ',  # 復活ペナルティアップ
]

shoes_gears = [  # クツ専用ギアパワー
  'テ',  # ステルスジャンプ
  '対',  # 対物攻撃力アップ
  '受',  # 受け身術
]


def create_pattern(
  main_gears: list[str], sub_gear_patterns: list[list[str, str, str, ]]
) -> list[list[str, list[str, str, str, ]]]:
  product_iter = product(main_gears, sub_gear_patterns)
  pattern_list = list(map(list, product_iter))
  return pattern_list


def create_sub_gear_patterns(
    sub_gears: list[str]) -> list[list[str, str, str, ]]:
  gears_add_num = [f'{n:02}{g}' for n, g in enumerate(sub_gears)]
  product_map = map(list, product(gears_add_num, repeat=3))
  sorted_map = map(tuple, (map(sorted, product_map)))
  set_map = map(list, set(list(sorted_map)))
  items_sorted = sorted(list(set_map))
  gears_remove_num = [[item[-1] for item in items] for items in items_sorted]
  return gears_remove_num


if __name__ == '__main__':
  from pprint import pprint

  sub_patterns = create_sub_gear_patterns(normal_gears)

  # head
  _main_head_gears = head_gears + normal_gears
  head_gearpower_pattern = create_pattern(_main_head_gears, sub_patterns)

  # wear
  _main_wear_gears = wear_gears + normal_gears
  wear_gearpower_pattern = create_pattern(_main_wear_gears, sub_patterns)

  # shoes
  _main_shoes_gears = shoes_gears + normal_gears
  shoes_gearpower_pattern = create_pattern(_main_shoes_gears, sub_patterns)

  print(f'アタマ\t: {len(head_gearpower_pattern)}')
  print(f'フク\t: {len(wear_gearpower_pattern)}')
  print(f'クツ\t: {len(shoes_gearpower_pattern)}')

