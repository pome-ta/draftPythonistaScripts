import wave
import numpy as np
import matplotlib.pyplot as plt


def wavfile_read(path):
  with wave.open(path, 'rb') as w:
    # note: nchannels, sampwidth, framerate, nframes, comptype, compname
    nchannels, _, framerate, nframes, _, _ = w.getparams()
    data_bytes = w.readframes(nframes)
    # xxx: `int16` はとりあえず固定
    # xxx: ステレオ時の分割とか遠回り？
    _data = np.frombuffer(data_bytes, dtype='int16')
    data = _data.reshape([nframes, nchannels], order='C')
    return framerate, data


if __name__ == '__main__':
  file_path = './out/record.wav'

  samplerate, data = wavfile_read(file_path)
  length = data.shape[0] / samplerate

  time = np.linspace(0., length, data.shape[0])
  plt.plot(time, data[:, 0], label='Left channel')
  plt.plot(time, data[:, 1], label='Right channel')
  plt.legend()
  plt.xlabel('Time [s]')
  plt.ylabel('Amplitude')
  plt.show()

