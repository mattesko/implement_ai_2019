var doneStyle = document.getElementById('done');
var loadStyle = document.getElementById('loading');
var previousStyleDone = doneStyle.style['display'];
var previousLoadDone = loadStyle.style['display'];
doneStyle.style['display'] = 'none';

var port = chrome.runtime.connect({name: "knockknock"});
port.postMessage({joke: "status"});
port.onMessage.addListener(function(msg) {
    console.log(msg.question);
  if (msg.isCompleted == "true") {
    doneStyle.style['display'] = previousStyleDone;
    loadStyle.style['display'] = 'none';
  }
  else {
    doneStyle.style['display'] = 'none';
    loadStyle.style['display'] = previousLoadDone;
  }
});