import {Fragmen} from './fragmen.js';
import {Onomat} from './onomat.js';


console.log('start');




(() => {
let canvas = null;            // スクリーン
let fragmen = null;           // fragmen.js のインスタンス
let onomat = null;            // onomat.js のインスタンス
let currentSource = '';       // 直近のソースコード
let currentAudioSource = '';  // 直近の Sound Shader のソースコード

let wrap = null; // html の一番ガワ


// fragmen.js 用のオプションの雛形
const FRAGMEN_OPTION = {
  target: null,
  eventTarget: null,
  mouse: true,
  resize: true,
  escape: false
}


window.addEventListener('DOMContentLoaded', () => {
  console.log('DOMContentLoaded');
  // DOM への参照
  canvas = document.querySelector('#webgl');
  wrap = document.querySelector('#wrap');

  // fragmen からデフォルトのソース一覧を取得
  const fragmenDefaultSource = Fragmen.DEFAULT_SOURCE;
  // xxx: 無意味な渡し
  currentSource = fragmenDefaultSource;
  //currentSource = glShader;
  
  // audioToggle が checked ではないかサウンドシェーダのソースが空の場合既定のソースを利用する
  // xxx: `audioToggle` は設定してない
  if(currentAudioSource === ''){
    currentAudioSource = Onomat.FRAGMENT_SHADER_SOURCE_DEFAULT;
  }
  
  // todo: ユーザーアクションをしていないと（タップとか）音は出ない
  onomatSetting(true);
  //update(currentSource);
  //counter.textContent = `${editor.getValue().length}`;
  //audioCounter.textContent = `${audioEditor.getValue().length}`;


/*
  // ウィンドウのリサイズ時
  window.addEventListener('resize', () => {
    //console.log('resize');
    resize();
  }, false);
  // 最初に一回リサイズ相当の処理を行っておく
  resize();
*/


  // メインとなる fragmen のインスタンス
  const option = Object.assign(FRAGMEN_OPTION, {
    target: canvas,
    eventTarget: window,
  });
  fragmen = new Fragmen(option);
  fragmen.render(currentSource);
  
  console.log(currentAudioSource);
  //updateAudio(currentAudioSource, true);
  //updateAudio(currentAudioSource);
  
  // 着火のおまじない
  // xxx: 事前準備してるコードを走らせるので簡単に
  const eventName = typeof document.ontouchend !== 'undefined' ? 'touchend' : 'mouseup';
  document.addEventListener(eventName, initAudioContext);
  function initAudioContext(){
    document.removeEventListener(eventName, initAudioContext);
    // wake up AudioContext
    onomat.audioCtx.resume();
  }
  
  // サウンドシェーダ関連
  /*
  wrap.addEventListener('change', () => {
    onomatSetting();
  }, false);
  */
  wrap.addEventListener('click', () => {
    /*
    if(audioToggle.checked !== true || latestAudioStatus !== 'success'){return;}
    ++soundPlay;
    */
    console.log(onomat.isPlay);
    //updateAudio(currentAudioSource, true);
    
    /*
    // 配信中はステータスとは無関係に状態を送る
    if(currentChannelId != null && (broadcastMode === 'owner' || broadcastMode === 'friend')){
      // グラフィックスを編集する立場かどうか
      if(
        (broadcastMode === 'owner' && directionMode !== BROADCAST_DIRECTION.GRAPHICS) ||
        (broadcastMode === 'friend' && directionMode === BROADCAST_DIRECTION.GRAPHICS)
      ){
        updateSoundData(currentDirectorId, currentChannelId, soundPlay);
      }
    }*/
  }, false);
  
  wrap.addEventListener('click', () => {
    /*
    if(musician != null){musician.stop();}
    if(audioToggle.checked !== true){return;}
    */
    //if(!onomat.isPlay){onomat.stop();}
  }, false);
  
  
}, false);



/**
 * ウィンドウリサイズ時の処理
 */
function resize(){
  const canvas = document.querySelector('#webgl');
  const bound = canvas.parentElement.getBoundingClientRect();
  canvas.width = bound.width;
  canvas.height = bound.height;
  /*
console.log('resize');
console.log(canvas.width);
console.log(canvas.height);
*/
}


/**
 * シェーダのソースを更新
 */
function update(source){
  if(fragmen == null){return;}
  fragmen.render(source);
}


/**
 * シェーダのソースを更新
 */
function updateAudio(source, force){
  if(onomat == null){return;}
  onomat.render(source, force);
}

/**
 * audioToggle の状態によりエディタの表示・非表示を切り替え、場合により Onomat の初期化を行う
 * @param {boolean} [play=true] - そのまま再生まで行うかどうかのフラグ
 */
function onomatSetting(play = true){
  // onomat のインスタンスが既に存在するかどうか
  if(onomat == null){
    // 存在しない場合生成を試みる
    onomat = new Onomat();
    
    // ビルド時のイベントを登録
    
    //onomat.on('build', (res) => {
      /*
      latestAudioStatus = res.status;
      audioLineout.classList.remove('warn');
      audioLineout.classList.remove('error');
      audioLineout.classList.add(res.status);
      audioMessage.textContent = res.message;
      if(latestStatus === 'success' && latestAudioStatus === 'success'){
        link.classList.remove('disabled');
      }else{
        link.classList.add('disabled');
      }
      */
    //});
    
    // 再生まで行うよう引数で指定されている場合は再生処理をタイマーで登録
    
    if(play === true){
      setTimeout(() => {
        //updateAudio(audioEditor.getValue(), true);
        updateAudio(currentAudioSource, true);
      }, 500);
    }
    
  }
  /*
  // 表示・非表示の切り替え
  if(audioToggle.checked === true){
    audioWrap.classList.remove('invisible');
    audioPlayIcon.classList.remove('disabled');
    audioStopIcon.classList.remove('disabled');
  }else{
    audioWrap.classList.add('invisible');
    audioPlayIcon.classList.add('disabled');
    audioStopIcon.classList.add('disabled');
  }
  
  // エディタのスクロールがおかしくならないようにリサイズ処理を呼んでおく
  editor.resize();
  audioEditor.resize();
  */
}

})();
console.log('end');

