from pathlib import Path

dash = '---\n'
tags = 'tags: Pythonista3 Python3\n'
author = 'author: pome-ta\n'
slide = 'slide: false\n'


def create_article(day, path):
  day_count = f'{day+1:02}'
  body = [
    dash,
    f'title: {day_count}日目の記事(メモ欄)\n',
    tags,
    author,
    slide,
    dash,
    f'この記事は、[Pythonista3 Advent Calendar 2022](https://qiita.com/advent-calendar/2022/pythonista3) の{day_count}日目の記事です。\n',
  ]
  article = Path(path, f'day{day_count}.md')
  with article.open(mode='w', encoding='utf-8') as f:
    f.writelines(body)


def setup_folder_path(dir_name):
  target_path = Path('./', dir_name)
  if (target_path.exists() or target_path.is_dir()):
    [file.unlink() for file in target_path.iterdir() if file.is_file()]
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


