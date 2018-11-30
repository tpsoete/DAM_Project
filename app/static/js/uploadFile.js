$("#buttonAdd").on("change", function () {
    var formData = new FormData($("#buttonAdd")[0]);
    formData.append('username',)
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
        },
        error:function (json_data) {
            alert(json_data)
            console.log(json_data)
        }
    });
});