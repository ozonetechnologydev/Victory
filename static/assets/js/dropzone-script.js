

$(function(){
  const camelize = (str) => str.replace(/[\-_](\w)/g, (match) => match.charAt(1).toUpperCase());
  
  $(".dropzone").toArray().forEach(dropzoneElement => {
    
    
    var thisDropzoneTrigger = $($(dropzoneElement).attr("dz-trigger"))
    Dropzone.options[camelize(dropzoneElement.getAttribute("id"))] = {

      url: $(dropzoneElement).attr("dz-post") || null,
      acceptedFiles:$(dropzoneElement).attr("dz-accepted-file") || null,
      dictDefaultMessage:$(dropzoneElement).attr("dz-title") || "Drop files here to upload",
      maxFiles:$(dropzoneElement).attr("dz-max-file") || null,
      parallelUploads: 1,
      autoProcessQueue:!Boolean($($(dropzoneElement).attr("dz-trigger")).length),
      addRemoveLinks:true,
      renameFilename: null,
      headers: {'X-CSRFToken': $("input[name='csrfmiddlewaretoken']").val()},
      
      init: function(){
        var myDropzone = this;

        myDropzone.on("addedfiles", function(file){
          console.log(file);
        });

        myDropzone.on("success", async function(file, response){
          console.log(response);
          if(response.success){
            if (Boolean(response.file_delete_url)){
              $(file._removeLink).attr("href",response.file_delete_url)
            } else {
              $(file._removeLink).hide();
            }
            if (Boolean(response.file_view_url)){

              const file_view_link = $("<a></a>").attr("href",response.file_view_url).attr("target", "newtab").text(response.file_name)
              console.log(file_view_link);
              $(file.previewElement.querySelector(".dz-filename span")).html(file_view_link)
            }
            await myDropzone.processQueue()
          } else{
            myDropzone.removeFile(file)
          }
          
        });
        myDropzone.on("error",  async function(file, response){
          myDropzone.removeFile(file)
        });

        if (thisDropzoneTrigger.length){
          thisDropzoneTrigger.on("click", async function(e){
            e.preventDefault()
            await myDropzone.processQueue()
            
          });
        }
          
        myDropzone.on("removedfile", function(file){
          console.log(file.status);
          if(file.status !== "error" && file._removeLink.href !== "javascript:undefined;"){
            $.ajax({
              url: file._removeLink.href,
              success: function (data) {
                  console.log(data);
              }
            });
          }
        });
      },

    };

    
  });

});
