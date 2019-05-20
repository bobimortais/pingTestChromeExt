function updateIcon() 
{
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() 
	{
		chrome.browserAction.setBadgeText({text: this.responseText});
	};
	xhttp.open("GET", "http://localhost:5000/", true);
	xhttp.send();
};

chrome.browserAction.onClicked.addListener(updateIcon);
