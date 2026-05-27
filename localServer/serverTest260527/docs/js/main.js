import DomFactory from './utils/domFactory.js';
import createEditorView from './editor/index.js';

import {EditorSelection} from '@codemirror/state';
import {
  cursorCharLeft,
  cursorCharRight,
  cursorLineDown,
  cursorLineUp,
  redo,
  selectAll,
  selectLine,
  toggleComment,
  undo,
} from '@codemirror/commands';

const IS_TOUCH_DEVICE = window.matchMedia('(hover: none)').matches;

/* --- load Source */
async function insertFetchDoc(filePath) {
  const fetchFilePath = async (path) => {
    const res = await fetch(path);
    return await res.text();
  };
  return await fetchFilePath(filePath);
}

const mainSketch = './sketchBooks/mainSketch.js';
const devSketch = './sketchBooks/devSketch.js';

const codeFilePath =
  `${location.protocol}` === 'file:' ||
  `${location.protocol}` === 'http:' ||
  `${location.hostname}` === 'localhost'
    ? devSketch
    : mainSketch;
// const codeFilePath = 1 ? devSketch : mainSketch;

/* --- editor(View) */
const editorDiv = DomFactory.create('div', {
  setAttrs: {
    id: 'editor-div',
  },
  setStyles: {
    width: '100%',
  },
});

const editor = createEditorView(editorDiv);

// xxx: iframe 生成時と書き換え時と併用
const reloadSketchHandleEvent = function (e) {
  const toStringDoc = this.targetEditor.viewState.state.doc.toString();
  this.targetSandbox = this.targetSandbox ? this.targetSandbox : e.target;
  this.targetSandbox.contentWindow.postMessage(toStringDoc, '*');
};

/* --- iframe */
const sandbox = DomFactory.create('iframe', {
  setAttrs: {
    id: 'sandbox',
    sandbox: 'allow-same-origin allow-scripts',
    allow:
      'accelerometer; ambient-light-sensor; autoplay; bluetooth; camera; encrypted-media; geolocation; gyroscope;  hid; microphone; magnetometer; midi; payment; usb; serial; vr; xr-spatial-tracking',
    loading: 'lazy',
    src: './js/sandboxes/sandbox.html',
  },
  setStyles: {
    width: '100%',
    height: '100dvh',
    'border-width': '0',
    position: 'fixed',
    top: '0',
    left: '0',
    'z-index': '0',
    //'background-color': 'lightgray',
    'background-color': 'darkgray',
  },
  addEventListeners: [
    {
      type: 'load',
      listener: {
        targetEditor: editor,
        targetSandbox: null,
        handleEvent: reloadSketchHandleEvent,
      },
    },
    /*
    {
      type: 'visibilitychange',
      listener: {
        handleEvent: function (e) {
          console.log('visibilitychange');
        },
      },
    },
    */
  ],
});

/* --- accessory */
const callButton = DomFactory.create('button', {
  textContent: '🔄',
  addEventListeners: [
    {
      type: 'click',
      listener: {
        targetSandbox: sandbox,
        targetEditor: editor,
        handleEvent: reloadSketchHandleEvent,
      },
    },
  ],
});

const summaryTextContent = (bool) => `source: ${bool ? 'hide' : 'show'}`;
const initDetailsOpen = false;

const summary = DomFactory.create('summary', {
  setStyles: {
    'font-family':
      'Consolas, Menlo, Monaco, source-code-pro, Courier New, monospace',
    //'font-size': '0.8rem',
    padding: '0.5rem 1rem',
  },
  textContent: summaryTextContent(initDetailsOpen),
});

const wrapSummary = DomFactory.create('div', {
  setStyles: {
    display: 'flex',
    'justify-content': 'space-between',
  },
});

const detailsControl = (isDetailsOpen, summaryElement, divElement) => {
  summaryElement.textContent = summaryTextContent(isDetailsOpen);
  divElement.style.display = isDetailsOpen ? '' : 'none';
};

const details = DomFactory.create('details', {
  setAttrs: {
    id: 'details',
    open: `${initDetailsOpen}`,
  },
  addEventListeners: [
    {
      type: 'toggle',
      listener: {
        targetSummary: summary,
        targetDiv: editorDiv,
        handleEvent: function (e) {
          detailsControl(e.target.open, this.targetSummary, this.targetDiv);
        },
      },
    },
    {
      type: 'build',
      listener: {
        targetSummary: summary,
        targetDiv: editorDiv,
        handleEvent: function (e) {
          detailsControl(e.detail.open, this.targetSummary, this.targetDiv);
        },
      },
    },
  ],
  appendChildren: [summary, wrapSummary],
});

const headerControlWrap = DomFactory.create('div', {
  setStyles: {
    display: 'grid',
    'grid-template-columns': 'auto 1fr',
  },
  appendChildren: [callButton, details],
});

const headerHandleEvent = function () {
  const header = document.querySelector('#header');
  const offsetTop = Math.max(0, window.visualViewport.offsetTop);
  //console.log(offsetTop);
  //header.style.top = `${offsetTop}px`;
  header.style.transform = `translateY(${offsetTop}px)`;
  //header.style.overflow = 'hidden'
};

/* --- accessory-header */
const header = DomFactory.create('header', {
  setAttrs: {
    id: 'header',
  },
  setStyles: {
    background: `var(--accessory-backGround-color-scheme)`,
    'background-blend-mode': `var(--accessory-backGround-background-blend-mode)`,
    //'backdrop-filter': `var(--accessory-backGround-backdrop-filter)`,
    position: 'sticky',
    width: '100%',
    top: '0',
    'z-index': '1',
  },
  targetAddEventListeners: [
    {
      target: window.visualViewport,
      type: 'resize',
      listener: {
        handleEvent: headerHandleEvent,
      },
    },
    {
      target: window.visualViewport,
      type: 'scroll',
      listener: {
        handleEvent: headerHandleEvent,
      },
    },
    /*
    {
      target: sandbox,
      type: 'resize',
      listener: {
        handleEvent: headerHandleEvent,
      },
    },
    {
      target: sandbox,
      type: 'scroll',
      listener: {
        handleEvent: headerHandleEvent,
      },
    },
    */
  ],
  appendChildren: [headerControlWrap],
});

const buttonFactory = (buttonIconChar, actionHandle) => {
  function createFrame(width, height) {
    return DomFactory.create('div', {
      setStyles: {
        'min-width': `${width}`,
        height: `${height}`,
        display: 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        //background: 'rgba(255, 0, 0, 0.5)',
      },
    });
  }

  const num = 2.5;
  const btnW = `${num}rem`;
  const btnH = `${num * 0.8}rem`;
  // const btnRadius = '16%';

  const createActionButton = (iconChar) => {
    const icon = DomFactory.create('span', {
      textContent: `${iconChar}`,
      setStyles: {
        'font-family':
          'Consolas, Menlo, Monaco, source-code-pro, Courier New, monospace',
        'font-size': '1.0rem',
        'font-style': 'normal',
        'font-weight': '400',
        'line-height': '28px',
        color: `var(--accessory-button-color-normal)`,
      },
    });

    const button = DomFactory.create(createFrame('88%', '98%'), {
      setStyles: {
        //'background-color': '#8e8e93', // light gray
        background: `var(--accessory-button-backGround-normal)`,
        'mix-blend-mode': `var(--accessory-button-background-blend-mode-normal)`,
        'box-shadow': `var(--accessory-button-box-shadow)`,
        'border-radius': `var(--accessory-button-border-radius)`,
      },
      appendChildren: [icon],
    });

    return DomFactory.create(createFrame(btnW, btnH), {
      setStyles: {
        cursor: 'pointer',
      },
      appendChildren: [button],
    });
  };

  const actionButton = createActionButton(buttonIconChar);
  actionButton.addEventListener('click', actionHandle);

  return actionButton;
};

// wip: 最大数問題
const buttons = Object.entries({
  '//': {
    targetEditor: editor,
    handleEvent: function () {
      toggleComment(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '▭': {
    targetEditor: editor,
    handleEvent: function () {
      selectLine(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '←': {
    targetEditor: editor,
    handleEvent: function () {
      cursorCharLeft(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '↓': {
    targetEditor: editor,
    handleEvent: function () {
      cursorLineDown(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '↑': {
    targetEditor: editor,
    handleEvent: function () {
      cursorLineUp(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '→': {
    targetEditor: editor,
    handleEvent: function () {
      cursorCharRight(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '⎁': {
    targetEditor: editor,
    handleEvent: function () {
      selectAll(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '⤻': {
    targetEditor: editor,
    handleEvent: function () {
      redo(this.targetEditor);
      this.targetEditor.focus();
    },
  },
  '⤺': {
    targetEditor: editor,
    handleEvent: function () {
      undo(this.targetEditor);
      this.targetEditor.focus();
    },
  },
}).map(([str, fnc]) => {
  return buttonFactory(str, fnc);
});

const buttonsWrap = DomFactory.create('div', {
  setStyles: {
    width: '100%',
    'box-sizing': 'border-box',
    padding: '0.6rem 1rem',
    display: 'flex',
    'justify-content': 'space-between',
  },

  appendChildren: [...buttons],
});

let caret, headLine, endLine;
const divStep = 16;
let swipeAreaWidth, stepValue;
let startX = 0;

const footerHandleEvent = function () {
  const footer = document.querySelector('#footer');
  if (!this.targetEditor.hasFocus && footer) {
    footer.style.display = 'none';
    return;
  }
  if (!IS_TOUCH_DEVICE) {
    return;
  }
  footer.style.display = '';

  const offsetTop = window.visualViewport.offsetTop;
  const offsetBottom =
    window.innerHeight -
    window.visualViewport.height +
    offsetTop -
    window.visualViewport.pageTop;
  const tOffsetTop =
    visualViewport.offsetTop +
    visualViewport.height -
    document.documentElement.clientHeight;
  //footer.style.bottom = `${offsetBottom}px`;
  footer.style.transform = `translateY(${tOffsetTop}px)`;
};

/* --- accessory-footer */
const footer = DomFactory.create('footer', {
  setAttrs: {
    id: 'footer',
  },
  setStyles: {
    background: `var(--accessory-backGround-color-scheme)`,
    'background-blend-mode': `var(--accessory-backGround-background-blend-mode)`,
    'backdrop-filter': `var(--accessory-backGround-backdrop-filter)`,
    position: 'sticky',
    width: '100%',
    bottom: '0',
    display: 'none',
  },
  targetAddEventListeners: [
    {
      target: window.visualViewport,
      type: 'resize',
      listener: {
        targetEditor: editor,
        handleEvent: footerHandleEvent,
      },
    },
    {
      target: window.visualViewport,
      type: 'scroll',
      listener: {
        targetEditor: editor,
        handleEvent: footerHandleEvent,
      },
    },
  ],
  addEventListeners: [
    {
      type: 'touchstart',
      listener: {
        targetEditor: editor,
        handleEvent: function (e) {
          //e.preventDefault(); // xxx: 変化要確認
          if (!this.targetEditor.hasFocus) {
            return;
          }

          const selectionMain = this.targetEditor.state.selection.main;
          caret = selectionMain.anchor;
          headLine = this.targetEditor.moveToLineBoundary(
            selectionMain,
            0
          ).anchor;
          endLine = this.targetEditor.moveToLineBoundary(
            selectionMain,
            1
          ).anchor;

          swipeAreaWidth = document.querySelector('#footer').clientWidth;
          stepValue = swipeAreaWidth / divStep;
          startX = e.changedTouches[0].clientX;
        },
      },
    },

    {
      type: 'touchmove',
      listener: {
        targetEditor: editor,
        handleEvent: function (e) {
          e.preventDefault(); // xxx: 変化要確認
          if (!this.targetEditor.hasFocus) {
            return;
          }

          const swipeX = e.changedTouches[0].clientX;

          const moveDistance = swipeX - startX;
          const moveCache =
            Math.abs(moveDistance) < stepValue
              ? caret
              : caret + Math.round(moveDistance / stepValue);

          if (caret === moveCache) {
            return;
          }

          const moveValue =
            moveCache < headLine
              ? headLine
              : moveCache >= endLine
                ? endLine
                : moveCache;

          this.targetEditor.dispatch({
            selection: EditorSelection.create([
              EditorSelection.cursor(moveValue),
            ]),
          });
          this.targetEditor.focus();
        },
      },
    },
  ],
  appendChildren: [buttonsWrap],
});

const setLayout = () => {
  const rootMain = DomFactory.create('div', {
    setAttrs: {
      id: 'rootMain',
    },
    setStyles: {
      display: 'grid',
      'grid-template-rows': 'auto 1fr auto',
      height: '100%',
      overflow: 'auto',
    },
    appendChildren: [header, editorDiv],
  });

  if (IS_TOUCH_DEVICE) {
    rootMain.appendChild(footer);
  }
  document.body.appendChild(sandbox);
  document.body.appendChild(rootMain);
};

document.addEventListener('DOMContentLoaded', () => {
  setLayout();
  insertFetchDoc(codeFilePath).then((loadedSource) => {
    // todo: 事前に`doc` が存在するなら、`doc` 以降にテキストを挿入
    editor.dispatch({
      changes: {from: editor.state?.doc.length, insert: loadedSource},
    });
  });
});
