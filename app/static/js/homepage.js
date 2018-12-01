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

        }
    })
}

$(function () {
    getInfo();

    $("#buttonAdd").on("change", function () {
        var formData = new FormData($("#buttonAdd")[0]);
        formData.append("type","file");
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
                console.log(json_data)
            }
        });
    });
})

