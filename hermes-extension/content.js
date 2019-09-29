// Input: List of booleans values in the natural order of the web page.
// Output: If the value is True, then hide.

// Get all paragraphs and images in a webpage
let paragraphs = document.getElementsByTagName('p');
let images = document.getElementsByTagName('img');

// Create a request to send to the backend
var requestURL = 'http://127.0.0.1:5000/filter';
var requestURL_fking_imgs = 'http://127.0.0.1:5000/img';
var xhr = new XMLHttpRequest();
var xhr_img = new XMLHttpRequest();

// TODO Once the input works, get the output to remove the correct number of paragraphs/images
let censorListParagraphs;
let censorListImages = [];
let pList = [];
let imgList = [];

for (i = 0; i < paragraphs.length; i++){
    pList.push(paragraphs[i].innerHTML);
}

for (i = 0; i < images.length; i++){
    console.log(images[i].src);
    imgList.push(images[i].src.replace("&", "%26"));
}
console.log(imgList);

xhr.onload = do_crazy_shit;
xhr_img.onload = do_some_more_crazy_shit_with_photos_this_time;

for (var i = 0; i < pList.length; i++) {
    blurr(paragraphs[i]);
}

function do_crazy_shit() {
  // AI on content
    censorListParagraphs = xhr.response;
  // Unblur necessary
    for (var i = 0; i < pList.length; i++) {
        if(! censorListParagraphs[i]) {
            un_blurr(paragraphs[i]);
        }
    }
};

for (var i = 0; i < imgList.length; i++) {
        blurrImage(images[i]);
}

function do_some_more_crazy_shit_with_photos_this_time() {
    censorListImages = xhr_img.response;

    for (var i = 0; i < imgList.length; i++) {
        if(! censorListImages[i]) {
            un_blurrImage(images[i]);
        }
    }

};

xhr_img.open('POST', requestURL_fking_imgs, true);
xhr_img.responseType = 'json';
xhr_img.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr_img.send(JSON.stringify(imgList));

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

function un_blurr(elt) {
    elt.style['text-decoration'] = '';
    elt.style['color'] = '';
    let anchors = elt.getElementsByTagName('a');
    for(a of anchors) {
        a.style['color'] = '';
    }
}

function un_blurrImage(elt) {
    elt.style['filter'] = '';
    elt.style['-webkit-filter'] = '';
}
