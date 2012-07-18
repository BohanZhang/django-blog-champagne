if (window.webkitNotifications)
{
    (function()
    {
        window.webkitNotifications.originalCreateNotification = window.webkitNotifications.createNotification;
        window.webkitNotifications.createNotification = function(iconUrl, title, body)
        {
            if( window.webkitNotifications.checkPermission() == 0 )
            {
                var n = window.webkitNotifications.originalCreateNotification(iconUrl, title, body);
                n.original_show = n.show;
                n.show = function()
                {
                    console.log("Get notified!");
                    var chromifyOSDComEvent = document.createEvent("Event");
                    chromifyOSDComEvent.initEvent("chromifyOSDComEvent", true, true);

                    if (iconUrl.match('^http') == null) {
                        if (iconUrl.match('^/') == null) {
                            iconUrl = window.location.origin + window.location.pathname.replace(/\\/g,'/').replace(/\/[^\/]*$/, '/') + iconUrl;
                            console.log("Icon url isn't start with http and /, rebuild it to: " + iconUrl);
                        } else {
                            iconUrl = window.location.origin + iconUrl;
                            console.log("Icon url isn't start with http, rebuild it to: " + iconUrl);
                        }
                    }
                    
                    // Please use JSON object serialization soon.
                    var container = document.createElement("div");
                    var c1 = document.createElement("div");
                    c1.innerHTML = title;
                    var c2 = document.createElement("div");
                    c2.innerHTML = body;
                    var c3 = document.createElement("div");
                    c3.innerHTML = iconUrl;
                    var c4 = document.createElement("div");
                    c4.innerHTML = "text";
                    container.appendChild(c1);
                    container.appendChild(c2);
                    container.appendChild(c3);
                    container.appendChild(c4);
                    container.id = "chromifyOSDComObject";
                    container.style.display = "none !important";
                    document.body.appendChild(container);
                    
                    // GTFO.
                    document.dispatchEvent(chromifyOSDComEvent);
                    console.log("Dispatched!", title, body, iconUrl);
                }
                
                return n;
            }
            else
            {
                return false;
            }
        }
    })();
}
$(function() {
	$("#submit").bind("click",function(e) {
		post_id = $("#comment_post_ID").attr("value");
		author = $("#author").attr("value");
		email = $("#email").attr("value");
		url = $("#url").attr("value");
		comment = $("#comment").attr("value");
		$.post("/comment/post/", {
				post_id: post_id,
				author : author,
				email : email,
				url : url,
				comment : comment
		} , function(data) {
			if(data == 'SUCCESS') {
				window.location.reload();
			} else {
				alert(data);
			}	
		});
	});
	$(".comment-reply-link").bind("click", function(){
		reply = "@" + $(this).attr("author") + ": ";
		$("#comment").attr("value", reply);
	});
});
