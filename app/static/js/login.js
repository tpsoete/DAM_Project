$(function(){
    $("#form-main").submit(function(){
        var data = JSON.stringify({
            username : $("#username").val(),
            password : $("#password").val()
        })

        $.ajax({
            data: data,
            dataType: "text",
            type: "POST",
            url: "/login",
            success: function(result) {
                if(result == "1") {
                    var s = document.getElementById("username");
                    window.location.href="explore?"+"username="+encodeURI(s.value);
                }
                else {
                    alert(result)
                }
            }
        })
    })
})