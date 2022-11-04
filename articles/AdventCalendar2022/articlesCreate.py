from pathlib import Path
from shutil import rmtree

tags = 'tags: Pythonista3 Python3 MobileApp Mobile\n\n'


def create_article(day, path):
  day_count = f'{day+1:02}'
  body = [
    f'title: {day_count}目の記事(メモ欄)\n',
    tags,
    f'この記事は、[Pythonista3 Advent Calendar 2022](https://qiita.com/advent-calendar/2022/pythonista3) の{day_count}日目の記事です。\n\n## \n',
  ]
  article = Path(path, f'day{day_count}', f'day{day_count}.md')
  article.parent.mkdir(parents=True, exist_ok=True)
  with article.open(mode='w', encoding='utf-8') as f:
    f.writelines(body)


def setup_folder_path(dir_name):
  target_path = Path('./', dir_name)
  if (target_path.exists() or target_path.is_dir()):
    rmtree(target_path)
  target_path.mkdir(exist_ok=True)
  return target_path


def main(dir_name, days):
  folder_path = setup_folder_path(dir_name)
  [create_article(day, folder_path) for day in range(days)]
  print('最後まで書くんだぞ☺️')


if __name__ == '__main__':
  folder_name = 'content'
  event_period = 25
  main(folder_name, event_period)

