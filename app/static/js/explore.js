var user_update = function() {
    var data = JSON.stringify({
        type: "recommend",
        username: username,
    })
    $.ajax({
        data: data,
        dataType: "json",
        type: "POST",
        success: function(result) {
            var users = eval(result);
            var i = 0;
            $(".user_detail").each(function(){
                if(users[i] == undefined) return false;
                $(this).find('img').attr('src', users[i].portrait);
                $(this).find('img').attr('href', "/explore?username=" + users[i].username)
                $(this).find('.nickname').html(users[i].nickname)
                $(this).find('.uid').html(users[i].username)
                i++;
            });
        }
    })
}

var thumb_update = function() {
    var data = JSON.stringify({
        type: "explore",
        username: username
    })
    $.ajax({
        data: data,
        dataType: "json",
        type: "POST",
        success: function(result) {
            var images = eval(result)//返回的随机图片组
            var i = 0;
            $(".thumb").each(function(){
                if(images[i] == undefined) return false;
                $(this).find('a').attr('href', images[i].img)
                $(this).find('h1').html(images[i].nickname+"<em>’s photo</em>")
                $(this).find('img').attr('src', images[i].img)
                i++;
            });
        }
    })
}

user_update();
thumb_update();

$(function(){

    $("#change-button").click(function(){
        user_update();
        thumb_update();
    })

    $("#search-form").submit(function(){
        var e = $("#explorer").val();
        if(e == "") return false
        window.location.href="homepage?"+"username="+encodeURI(e)+"&explorer="+encodeURI(username);//change after merge
        return false
    })

    $("#homepage").click(function(){
        window.location.href="homepage?"+"username="+encodeURI(username)+"&explorer="+encodeURI(username);//change after merge

    })

    $("#explore").click(function(){
        window.location.href="explore?"+"username="+encodeURI(username);//change after merge

    })

    $(".view-button").click(function(){
        var target = $(this).parents().find(".uid").html()

        window.location.href="homepage?username="+encodeURI(target)+"&explorer="+encodeURI(username);//change after merge
    })

})