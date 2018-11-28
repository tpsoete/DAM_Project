var userName
var loc = location.href;
var n1 = loc.length;//地址的总长度
var n2 = loc.indexOf("=");//取得=号的位置
userName = decodeURI(loc.substr(n2+1, n1-n2));
var user_update = function() {
    var data = JSON.stringify({
        type: "recommend",
        username: userName
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
                $(this).find('img').attr('href', "/user?id=" + users[i].username)
                $(this).find('p').html(users[i].nickname)
                i++;
            });
        }
    })
}
var thumb_update = function() {
    var data = JSON.stringify({
        type: "explore",
        username: userName
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
    $("#search-button").click(function(){
        var e = document.getElementById("explorer");
        window.location.href="/explorer?"+"username="+encodeURI(userName)+" & explore="+encodeURI(e.value);//change after merge

    })
    $("#homepage").click(function(){
        window.location.href="/homepage?"+"username="+encodeURI(userName);//change after merge

    })
    $("#explore").click(function(){
        window.location.href="/explorer?"+"username="+encodeURI(userName);//change after merge

    })
    $("#view-button").click(function(){
        var data = JSON.stringify({
            nikName : $("#nikName").val(),    //get the corresponding username
        })
        $.ajax({
            data: data,
            dataType: "text",
            type: "POST",
            success: function(result) {
                window.location.href="/explorer?"+"username="+encodeURI(userName)+" & explorer="+encodeURI(result);//change after merge
            }
        })

    })

})