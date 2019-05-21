function updateIcon() 
{
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() 
	{
		//Execute only when the request is completed
		if(xhttp.readyState == 4)
		{
			var response = this.responseText.split(",")
			
			for (var i = 0; i < response.length; i++) 
			{
				chrome.browserAction.setBadgeText({text: response[i]});
				sleep(1000)
			}	
		}
	};
	xhttp.open("GET", "http://localhost:5000/", true);
	xhttp.send();
};

chrome.browserAction.onClicked.addListener(updateIcon);

function sleep(milliseconds) 
{
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) 
  {
    if ((new Date().getTime() - start) > milliseconds)
	{
      break;
    }
  }
}