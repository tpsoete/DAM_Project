var btn = document.getElementById('pick_list');
var btn2 = document.getElementById('followers_list');
var btn3 = document.getElementById('edit');
var div = document.getElementById('background');
var div2 = document.getElementById('background2');
var div3 = document.getElementById('background3');
var close = document.getElementById('close-button');
var close2 = document.getElementById('close-button2');

var followers = document.getElementById('followerList');

btn.onclick = function show() {
	div.style.display = "block";
}
btn2.onclick = function show() {
	div2.style.display = "block";
	var followerRequest = new XMLHttpRequest();
	followerRequest.open('GET', '');
	followerRequest.onload = function () {
		var followerList = JSON.parse(followerRequest.responseText);
		renderHTML(followerList);
    };
	followerRequest.send();
}

function renderHTML(data) {
	var htmlString = "test string!";
	followers.insertAdjacentHTML('beforeend', htmlString);
}

btn3.onclick = function show() {
	div3.style.display = "block";
}

close.onclick = function close() {
	div.style.display = "none";
}
close2.onclick = function close(){
	div2.style.display = "none";
}

window.onclick = function close(e) {
	if (e.target == div) {
		div.style.display = "none";
	}
	else if(e.target == div2){
		div2.style.display = "none";
	}
    else if(e.target == div3){
    	div3.style.display = "none";
	}
}