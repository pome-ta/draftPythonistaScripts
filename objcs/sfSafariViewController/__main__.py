from objc_util import ObjCClass, UIApplication, on_main_thread, nsurl

import pdbg

path = 'file:///private/var/mobile/Containers/Shared/AppGroup/A2F05B95-E190-4D22-B466-3FDBABAAFCE1/File%20Provider%20Storage/Repositories/soundShader4twigl/public/index.html'

SFSafariViewController = ObjCClass('SFSafariViewController')


@on_main_thread
def open_in_safari_vc(url):
  #pdbg.state(nsurl(url))
  #vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))
  vc = SFSafariViewController.alloc().initWithURL_(nsurl(url))

  app = UIApplication.sharedApplication()
  root_vc = app.keyWindow().rootViewController()
  root_vc.presentViewController_animated_completion_(vc, True, None)
  vc.release()


if __name__ == '__main__':
  open_in_safari_vc('http://localhost:8000')
  #print(nsurl(path))

