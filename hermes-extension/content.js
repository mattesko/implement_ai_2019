// Input: List of booleans values in the natural order of the web page.
// Output: If the value is True, then hide.

// Get all paragraphs and images in a webpage
let paragraphs = document.getElementsByTagName('p');
let images = document.getElementsByTagName('img');

// Create a request to send to the backend
var requestURL = 'http://127.0.0.1:5000/filter';
var xhr = new XMLHttpRequest();

// TODO Once the input works, get the output to remove the correct number of paragraphs/images
let censorListParagraphs; 
let censorListImages = [];
let pList = [];
let imgList = [];

for (i = 0; i < paragraphs.length; i++){
    pList.push(paragraphs[i].innerHTML)
}

xhr.onload = do_crazy_shit;

function do_crazy_shit() {
    censorListParagraphs = xhr.response;
    console.log(censorListParagraphs);

    for (var i = 0; i < pList.length; i++) {
        if(censorListParagraphs[i]) {
            blurr(paragraphs[i]);
        }
    }

};


xhr.open('POST', requestURL, true);
xhr.responseType = 'json';
xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr.send(JSON.stringify(pList));


function hide(elt) {
    elt.style['background-color'] = '#000000';
}

function blurr(elt) {
    elt.style['text-decoration'] = 'none';
    elt.style['color'] = 'transparent';
    elt.style['text-shadow'] = '0 0 5px rgba(0,0,0,0.5)';
    let anchors = elt.getElementsByTagName('a');
    for(a of anchors) {
        a.style['color'] = 'transparent';
    }
}

function blurrImage(elt) {
    elt.style['filter'] = 'blur(8px)';
    elt.style['-webkit-filter'] = 'blur(8px)';
}
