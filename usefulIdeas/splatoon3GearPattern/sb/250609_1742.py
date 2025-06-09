from itertools import product

#main_gears

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

# 2744
#sub_gear_pattern = list(product(normal_gears,repeat=3))

#sub_gear_pattern = set(list(map(sorted, product(normal_gears,repeat=3))))

#sub_gear_pattern = list(set([tuple(sg) for sg in map(sorted, product(normal_gears,repeat=3))]))

sub_gear_pattern = list(
  map(list, set(map(tuple, map(sorted, product(normal_gears, repeat=3))))))

print(len(sub_gear_pattern))

