from operator import itemgetter

from appex import get_web_page_info, finish
import clipboard

import webbrowser

web_info = get_web_page_info()
title, url = itemgetter('title', 'url')(web_info)
clipboard.set(f'[{title}]({url})')

webbrowser.open('pythonista://')
finish()

