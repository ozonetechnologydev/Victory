

function deleteFiles(file, callback){
    $.ajax({
        url: file._removeLink.href,
        success: function (data) {
            callback(null, data)
        }
    });
}



function saveBlogToDraft(form_data, url, callback){
        new FormData()
      form_data.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
      $.ajax({
          url: url,
          method: "POST",
          dataType: 'json',
          cache: false,
          processData: false,
          contentType: false,
          data: form_data,
          success:  function (data) {
            callback(data)
          }
      });
}


