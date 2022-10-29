
 $(document).ready(function(){

              $(".sweet-alert-basic").click(function(){
                  swal("Hello world!");
              });

              $(".sweet-alert-title").click(function(){
                  swal("Here's the title!", "...and here's the text!");
              });

              $(".sweet-alert-success").click(function(){
                  swal("Good job!", "You clicked the button!,", "success");
              });

              $(".sweet-alert-error").click(function(){
                  swal("Somthing Wrong!", "You clicked the button!,", "error");
              });

              $(".sweet-alert-info").click(function(){
                  swal("Information!", "You clicked the button!,", "info");
              });

              $(".sweet-alert-warning").click(function(){
                  swal("Warning!", "You clicked the button!,", "warning");
              });
              
              $(".delete-alert-confirm").click(function(e){
                swal({
                  title: "Are you sure?",
                  text: "Once deleted, you will not be able to recover data!",
                  icon: "warning",
                  buttons: true,
                  dangerMode: true,
                })
                .then((willDelete) => {
                  if (willDelete) {

                    swal("Poof! Your data has been deleted!", {
                      icon: "success",
                    });
                    e.currentTarget.form.submit()

                  } else {
                    swal("Your data file is safe!");
                  }
                });

              });

             

          });