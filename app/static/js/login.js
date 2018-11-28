$(function(){
    $("#login-button").click(function(){
        var data = JSON.stringify({
            username : $("#username").val(),
            password : $("#password").val()
        })

        $.ajax({
            data: data,
            dataType: "text",
            type: "POST",
            success: function(result) {
                if(result == "1") {
                    $("#login-success")[0].click()
                    var s = document.getElementById("username");
                    window.location.href="explore.html?"+"username="+encodeURI(s.value);
                }
                else {
                    alert(result)
                }
            }
        })
    })
})