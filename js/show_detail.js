$(function(){

	var rootPath = 'wikiwomanstats/'
	var ajax_call = function(){
		var countTotal = 1;
		console.log(1);
		$('#articleData').find('tr').remove();
		$('#userData').find('tr').remove();

		$.getJSON(rootPath+'useredit.json', function(json, textStatus) {
			var count = 1;
			for (key in json.user){
				val = json.user[key];
				name = key.replace(/\ /g,'_');
				var href = "https://ml.wikipedia.org/wiki/User:" + name;
				userData = "<tr><td> " + count + " </td> <td><a target = '_blank' href="+ href +">" + key+ "</a></td> <td>" + val + "</td> </tr>";
				$('#userData').append(userData);
				count = count + 1;
			}
		});

		$.getJSON(rootPath+'articleedit.json', function(json, textStatus) {
			for (key in json){
				val = json[key];
				name = key.replace(/\ /g,'_');
				var href = "https://ml.wikipedia.org/wiki/" + name;
				articleData = "<tr><td> " + countTotal + " </td> <td><a target = '_blank' href="+ href +">" + key+ "</a></td> <td>" + val + "</td> </tr>";
				$('#articleData').append(articleData);
				countTotal = countTotal + 1;
			}
		});

		$.getJSON(rootPath+'generalstats.json', function(json, textStatus) {
			$('#totalArticleCount').text(countTotal-1);
			$('#totalEditCount').text(json.totalEdit);
			$('#totalUserCount').text(json.userCount);
		});
	}

	ajax_call();
	setInterval(ajax_call, 1000*60*3);

})
