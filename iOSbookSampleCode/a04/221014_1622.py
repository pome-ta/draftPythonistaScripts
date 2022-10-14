from pathlib import Path
import time

from objc_util import ObjCClass, NSURL

import pdbg

AVAudioSession = ObjCClass('AVAudioSession')
AVAudioRecorder = ObjCClass('AVAudioRecorder')

# xxx: `objc_util` では、設定済み？
# NSURL = ObjCClass('NSURL')
'''  todo: enum.Enum だと落ちる
``` .log
*** -[__NSDictionaryM setObject:forKey:]: object cannot be nil (key: AVFormatIDKey)
```
import enum
class AVAudioQuality(enum.Enum):
  AVAudioQualityMin = 0
  AVAudioQualityLow = 32
  AVAudioQualityMedium = 64
  AVAudioQualityHigh = 96
  AVAudioQualityMax = 127

class AVFormatIDKey(enum.Enum):  #UInt32
  kAudioFormatLinearPCM      = 1819304813
  kAudioFormatAppleIMA4      = 1768775988
  kAudioFormatMPEG4AAC       = 1633772320
  kAudioFormatMACE3          = 1296122675
  kAudioFormatMACE6          = 1296122678
  kAudioFormatULaw           = 1970037111
  kAudioFormatALaw           = 1634492791
  kAudioFormatMPEGLayer1     = 778924081
  kAudioFormatMPEGLayer2     = 778924082
  kAudioFormatMPEGLayer3     = 778924083
  kAudioFormatAppleLossless  = 1634492771
'''


class AVAudioQuality:
  AVAudioQualityMin = 0
  AVAudioQualityLow = 32
  AVAudioQualityMedium = 64
  AVAudioQualityHigh = 96
  AVAudioQualityMax = 127


class AVFormatIDKey:
  kAudioFormatLinearPCM = 1819304813
  kAudioFormatAppleIMA4 = 1768775988
  kAudioFormatMPEG4AAC = 1633772320
  kAudioFormatMACE3 = 1296122675
  kAudioFormatMACE6 = 1296122678
  kAudioFormatULaw = 1970037111
  kAudioFormatALaw = 1634492791
  kAudioFormatMPEGLayer1 = 778924081
  kAudioFormatMPEGLayer2 = 778924082
  kAudioFormatMPEGLayer3 = 778924083
  kAudioFormatAppleLossless = 1634492771


def prepare_file_path(target_str: str, save_dir: str='./out') -> Path:
  target_path = Path(save_dir if save_dir else '') / target_str
  # todo: 保存先ディレクトリツリーが存在しない場合作成
  parent_path = target_path.parent
  if not (parent_path.exists()):
    parent_path.mkdir(parents=True)
  # todo: 保存ファイルが存在しない場合作成
  if not (target_path.exists()):
    target_path.touch()
  return target_path


def avaudio_recorder_record(
    file_name,
    duration,
    save_dir='./out',
    avFormatIDKey=AVFormatIDKey.kAudioFormatLinearPCM,
    avSampleRateKey=44100.00,
    avNumberOfChannelsKey=2,
    avEncoderAudioQualityKey=AVAudioQuality.AVAudioQualityMedium):
  file_path = prepare_file_path(file_name, save_dir)
  record_file_url = NSURL.fileURLWithPath_(f'{file_path.absolute()}')

  shared_avaudio_session = AVAudioSession.sharedInstance()
  category_set = shared_avaudio_session.setCategory_error_(
    'AVAudioSessionCategoryPlayAndRecord', None)

  settings = {
    'AVFormatIDKey': avFormatIDKey,
    'AVSampleRateKey': avSampleRateKey,
    'AVNumberOfChannelsKey': avNumberOfChannelsKey,
    'AVEncoderAudioQualityKey': avEncoderAudioQualityKey
  }

  AVAudioRecorder_ = AVAudioRecorder.alloc().initWithURL_settings_error_(
    record_file_url, settings, None)

  AVAudioRecorder_.recordForDuration_(duration)
  #started_recording = AVAudioRecorder_.record()

  time.sleep(duration + 0.1)  # `0.1`: time buffer

  AVAudioRecorder_.stop()
  AVAudioRecorder_.release()


if __name__ == '__main__':
  avaudio_recorder_record(file_name='record.wav', duration=3)

