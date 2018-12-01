var uName;
var uAge;
var uGender;
var uNick;
var uSign;

function addImg(imgsrc) {
    var post = document.getElementById("post");
    var img = document.createElement("img");
    img.src = imgsrc;
    post.appendChild(img);
}

function setHead(imgsrc){
    var head = document.getElementById("head");
    head.src = imgsrc
}

function setInformation(info) {
    setHead(info.portrait);
    var nickName = document.getElementById("nickname");
    uNick = info.nickname;
    nickName.innerHTML = uNick;

    var realName = document.getElementById("realname");
    uName = info.realname;
    realName.innerHTML = uName;

    var userAge = document.getElementById("age");
    uAge = info.age;
    userAge.innerHTML = uAge;

    var userGender = document.getElementById("gender");
    uGender = info.gender;
    userGender.innerHTML = uGender;

    var userSign = document.getElementById("signment");
    uSign = info.signature;
    userSign .innerHTML = uSign;
}

function getInfo(){
    var data = JSON.stringify({
        type: "homepage",
        username: username,
        explorer:explorer
    })
    $.ajax({
        data:data,
        type:"POST",
        dataType:"json",
        success:function (result) {
            if (username===explorer) {
                document.getElementById("followers_list").style.visibility="visible";
                document.getElementById("pick_list").style.visibility="visible";
                document.getElementById("buttonAdd").style.visibility="visible";
                document.getElementById("edit").style.visibility="visible";
                setInformation(result)
            }
            else {
                document.getElementById("followers_list").style.visibility="hidden";
                document.getElementById("pick_list").style.visibility="hidden";
                document.getElementById("buttonAdd").style.visibility="hidden";
                document.getElementById("edit").style.visibility="hidden";
                setInformation(result)
            }
        }
    })
}

function getPic(){
    var data = JSON.stringify({
        type: "photo",
        username: username,
        explorer:explorer
    })
    $.ajax({
        data:data,
        type:"POST",
        dataType:"json",
        success:function (result) {
            var count = result.count;
            for(var i=0;i<count;i++)
            {
                addImg(result.album[i]);
            }

        }
    })
}

$(function () {
    getInfo();

    getPic();

    $("#buttonAdd").on("change", function () {
        var formData = new FormData($("#buttonAdd")[0]);
        formData.append("type","file");
        formData.append("username", username);
        $.ajax({
            url:"/upload",
            type:"POST",
            data:formData,
            dataType:"json",
            async:true,
            cache:false,
            contentType:false,
            processData:false,
            success:function (json_data) {
                alert("upload succeed!")
                addImg(json_data.path)
            },
            error:function (json_data) {
                alert(json_data)
            }
        });
    });

    $("#headFile").on("change", function () {
        var formData = new FormData($("#headFile")[0]);
        formData.append("type","head");
        formData.append("username",username);
        $.ajax({
            url:"/upload",
            type:"POST",
            data:formData,
            dataType:"json",
            async:true,
            cache:false,
            contentType:false,
            processData:false,
            success:function (json_data) {
                alert("upload succeed!")
                setHead(json_data.path )
            },
            error:function (json_data) {
                alert(json_data)
            }
        });
    });

    $("#submit").click(function () {
        var newNick = $("#unick").val();
        var newSign = $("#usign").val();
        var data = JSON.stringify({
            type:"information",
            username:username,
            newNick:newNick,
            newSign:newSign
        })
        $.ajax({
            data:data,
            type:"POST",
            dataType:"json",
            success:function (result) {
                div3.style.display = "none";
                getInfo();
            }
        })
    })

    $("#homepage").click(function(){
        window.location.href="homepage?"+"username="+encodeURI(explorer)+"&explorer="+encodeURI(explorer);//change after merge
    })

    $("#explore").click(function(){
        window.location.href="explore?"+"username="+encodeURI(explorer);//change after merge
    })

    var btn = document.getElementById('pick_list');
    var btn2 = document.getElementById('followers_list');
    var btn3 = document.getElementById('edit');
    var div = document.getElementById('background');
    var div2 = document.getElementById('background2');
    var div3 = document.getElementById('background3');
    var close = document.getElementById('close-button');
    var close2 = document.getElementById('close-button2');

    var followers = document.getElementById('followerList');

    btn.onclick = function show() {
        div.style.display = "block";
    }
    btn2.onclick = function show() {
        div2.style.display = "block";
        var followerRequest = new XMLHttpRequest();
        followerRequest.open('GET', '');
        followerRequest.onload = function () {
            var followerList = JSON.parse(followerRequest.responseText);
            renderHTML(followerList);
        };
        followerRequest.send();
    }

    function renderHTML(data) {
        var htmlString = "test string!";
        followers.insertAdjacentHTML('beforeend', htmlString);
    }

    btn3.onclick = function show() {
        div3.style.display = "block";
        document.getElementById("uid").innerHTML = username;
        document.getElementById("uname").innerHTML = uName;
        document.getElementById("uage").innerHTML = uAge;
        document.getElementById("ugender").innerHTML = uGender;
        document.getElementById("unick").setAttribute("placeholder", uNick);
        document.getElementById("usign").setAttribute("placeholder", uSign);
    }

    close.onclick = function close() {
        div.style.display = "none";
    }
    close2.onclick = function close(){
        div2.style.display = "none";
    }

    window.onclick = function close(e) {
        if (e.target == div) {
            div.style.display = "none";
        }
        else if(e.target == div2){
            div2.style.display = "none";
        }
        else if(e.target == div3){
            div3.style.display = "none";
        }
    }


})

