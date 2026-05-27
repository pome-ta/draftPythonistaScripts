(function () {
  'use strict';

  if (typeof p5 === 'undefined') {
    console.error(
      'p5.js is not loaded. Please make sure to include p5.js before refreshSoundContext.js.'
    );
    return;
  }

  if (!p5.prototype.getAudioContext) {
    console.error(
      'p5.sound.js is not loaded. Please make sure to include p5.sound.js before refreshSoundContext.js.'
    );
    return;
  }

  p5.prototype.refreshSoundContext = function () {
    if (!this.getAudioContext) {
      return;
    }

    // wip: クリップノイズ対策
    this.disposeSound();

    const soundArray = this.soundOut.soundArray;
    for (let soundIdx = soundArray.length - 1; soundIdx >= 0; soundIdx--) {
      const sound = soundArray[soundIdx];
      // todo: 過剰処理?
      sound?.stop && sound.stop();
      sound?.dispose && sound.dispose();
      sound?.disconnect && sound.disconnect();
      soundArray.splice(soundIdx, 1);
    }

    const parts = this.soundOut.parts;
    for (let partIdx = parts.length - 1; partIdx >= 0; partIdx--) {
      const phrases = parts[partIdx].phrases;
      for (let phraseIdx = phrases.length - 1; phraseIdx >= 0; phraseIdx--) {
        phrases.splice(phraseIdx, 1);
      }
      parts.splice(partIdx, 1);
    }

    this.soundOut.soundArray = [];
    this.soundOut.parts = [];
    this.soundOut.extensions = []; // todo: 対応必要?

    this.userStartAudio();
  };

  // wip: 直接書いてもいいかも？
  p5.prototype.registerMethod(
    'beforePreload',
    p5.prototype.refreshSoundContext
  );
})();
