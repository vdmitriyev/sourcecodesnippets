var globalJSOPNFeedsInHTML = '';
var paddingFromLeft = '&nbsp;&nbsp;&nbsp;&nbsp;';
var documentIDsArray = new Array();
var INDEX_LIMIT = 3;

function buildHTMLLink(link, value){
	value = typeof value !== 'undefined' ? a : link;
	htmlLink = '<a href=' + link + '>' + value + '</a>'
	return htmlLink
}

function builHTMLBoldBlock(txtValue){
	return '<span style="font-weight:bold;">' + txtValue + '</span>';
}

function foldera77a564c(data){
	try{
		globalJSOPNFeedsInHTML += data.title + '<br>';
		globalJSOPNFeedsInHTML += data.description + '<br>';
		globalJSOPNFeedsInHTML += buildHTMLLink(data.link) + '<br>';
		globalJSOPNFeedsInHTML += '<br>';
		for (var index in data.items) {

			if (index >= INDEX_LIMIT)
				break;

			globalJSOPNFeedsInHTML += paddingFromLeft + data.items[index].title + '<br>';
			globalJSOPNFeedsInHTML += paddingFromLeft + data.items[index].description + '<br>';
			globalJSOPNFeedsInHTML += paddingFromLeft + buildHTMLLink(data.items[index].link) + '<br>';
			for (var innerIndex in data.items[index].fields){
				if (data.items[index].fields[innerIndex].name == "documentId"){
					documentIDsArray.push(data.items[index].fields[innerIndex].value);
				}
				globalJSOPNFeedsInHTML += paddingFromLeft+paddingFromLeft
										+ builHTMLBoldBlock(data.items[index].fields[innerIndex].name)	 + ': '
										+ data.items[index].fields[innerIndex].value + '<br>';
			}
			globalJSOPNFeedsInHTML += '<hr>';
		}
	} catch (err){
			alert('Error while dealing with JSONP: ' + err);
	}
}

function displayJSONPFeeds(){
	document.getElementById("feedsJSONPContent").innerHTML = globalJSOPNFeedsInHTML;
	alertDocumentIDs();
}

function alertDocumentIDs(){

	var alertText = '';
	for (var index in documentIDsArray){
		alertText += documentIDsArray[index] + '\n';
	}

	alert(alertText);
}
