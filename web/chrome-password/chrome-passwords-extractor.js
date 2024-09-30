function extract(){

	var txt_result = "";
	var html_result = "";

	arr_login = document.frames[0].getElementsByClassName("name");
	arr_url = document.getElementsByClassName("favicon-cell weakrtl url");

	for (i = 0; i < arr_login.length; i++){
		txt_result += 'Link: ' + arr_url[i].innerHTML + '\n'
				+ 'Login: ' + arr_login[i].innerHTML + '\n'
				+ "Password: " + "\n\n";

		html_result += 'Link: ' + arr_url[i].innerHTML + '<br>'
				+ 'Login: ' + arr_login[i].innerHTML + '<br>'
				+ "Password: " + "<br><br>";
	}

	try{
		document.getElementById("content").innerHTML = html_result;
	} catch(err){
		document.getElementById("password-list-headers").innerHTML = '<div>' + html_result + '</div>';
	}

	alert(txt_result);
}

extract();
