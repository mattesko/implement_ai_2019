var done;

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      console.log(sender.tab ?
                  "from a content script:" + sender.tab.url :
                  "from the extension");
        done = request.status;
        sendResponse({farewell: "Value set to: " + done});
    });

chrome.runtime.onConnect.addListener(function(port) {
    console.assert(port.name == "knockknock");
    port.onMessage.addListener(function(msg) {
        console.log(msg.answer);
      if (msg.joke == "status")
        port.postMessage({isCompleted: done});
    });
  });