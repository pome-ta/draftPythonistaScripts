import DomFactory from './utils/domFactory.js';



const owner = 'pome-ta';
const repo = 'p5SketchBook'

const endPoint = 'https://api.github.com/repos';
const kind = 'contents'



async function getRepoContents() {
  const res = await fetch([endPoint, owner, repo, kind].join('/'));
  const data = await res.json();
  console.log(data);
}

getRepoContents();
