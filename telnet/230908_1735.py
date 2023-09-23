from telnetlib import Telnet

import console

console.clear()
console.set_font('Ubuntu Mono', 13)

h = 'koukoku.shadan.open.ad.jp'

with Telnet(h, 23, 1) as tn:
  while True:
    print(tn.read_some().decode('shift_jis'), end='')

