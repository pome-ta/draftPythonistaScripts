from pathlib import Path

search_str = 'swift'

frameworks_path = '/System/Library/Frameworks'
frameworks_iter = Path(frameworks_path).iterdir()
frameworks_list = sorted(list(frameworks_iter))

for fw in frameworks_list:
  if search_str in fw.name:
    print(fw)
