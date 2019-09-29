// Input: List of booleans values in the natural order of the web page.
// Output: If the value is True, then hide.

// Get all paragraphs and images in a webpage
let paragraphs = document.getElementsByTagName('p');
let images = document.getElementsByTagName('img');

// Create a request to send to the backend
let xhr = new XMLHttpRequest();
var requestURL = 'http://127.0.0.1:5000/filter';

// TODO Once the input works, get the output to remove the correct number of paragraphs/images
let censorListParagraphs = []; 
let censorListImages = [];
let pList = [];
let imgList = [];

for (i = 0; i < paragraphs.length; i++){
    pList.push(paragraphs[i].innerHTML)
}

xhr = new XMLHttpRequest();
xhr.open('POST', requestURL);
xhr.responseType = 'json';
xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr.send(JSON.stringify(pList));
xhr.onload = function() {
    censorListParagraphs.push(xhr.response['Do-Censor']);
};

console.log(censorListParagraphs);

// for (i=0; i < paragraphs.length; i++) {
//     if(i < paragraphs.length/2) {
//         censorListParagraphs.push(true);
//     } else {
//         censorListParagraphs.push(false);
//     }
    
// }

let j=0; //Decide whether to hide or not
for (elt of paragraphs) {
    // console.log(elt);
    
    if(censorListParagraphs[j++]) {
        blurr(elt);
    }
    
}

for(k=0; k<3;k++) {
    blurrImage(images[k]);
}

function hide(elt) {
    elt.style['background-color'] = '#000000';
}

function blurr(elt) {
    let anchors = document.getElementsByTagName('a');
    for(a of anchors) {
        a.style['color'] = 'transparent';
    }
    // TODO: Style multiple elements at once
    elt.style['text-decoration'] = 'none';
    elt.style['color'] = 'transparent';
    elt.style['text-shadow'] = '0 0 5px rgba(0,0,0,0.5)';
}

function blurrImage(elt) {
    elt.style['filter'] = 'blur(8px)';
    elt.style['-webkit-filter'] = 'blur(8px)';
}

function censor() {
    // Take all elements
    // Create request
    // Get response
    // Modify data
}