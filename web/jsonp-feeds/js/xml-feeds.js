var globalXMLFeedsInHTML = 'Under construction due to "Access-Control-Allow-Origin"';
var paddingFromLeft = '&nbsp;&nbsp;&nbsp;&nbsp;';
var url = "http://feed.issuu.com/folder/36bee7f3-9445-4d25-924a-49baa77a564c/rss20.xml"

function displayXMLFeeds(){
	requesAndParseXML();
	document.getElementById("feedsXMLContent").innerHTML = globalXMLFeedsInHTML;
}

function buildHTMLLink(link, value){
	value = typeof value !== 'undefined' ? a : link;
	htmlLink = '<a href=' + link + '>' + value + '</a>'
	return htmlLink
}

function requesAndParseXML(){

	try{

	} catch (err){
			alert('Error while dealing with JSONP: ' + err)
	}
}
