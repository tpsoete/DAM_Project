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
    nickName.innerHTML = info.nickname;

    var realName = document.getElementById("realname");
    realName.innerHTML = info.realname;

    var userAge = document.getElementById("age");
    userAge.innerHTML = info.age;

    var userGender = document.getElementById("gender");
    userGender.innerHTML = info.gender;

    var userSign = document.getElementById("signment");
    userSign .innerHTML = info.signature;
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

    $("#homepage").click(function(){
        window.location.href="homepage?"+"username="+encodeURI(explorer)+"&explorer="+encodeURI(explorer);//change after merge

    })

    $("#explore").click(function(){
        window.location.href="explore?"+"username="+encodeURI(explorer);//change after merge

    })
})

