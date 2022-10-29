$(function(){

    console.log(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");

    $(".dynamic-table")?.on("submit", function(e){
        e.preventDefault()
        var formElem = e.currentTarget
        var form_data = new FormData(formElem)

        if(form_data.getAll("columns").length && form_data.get("action") !== "none"){
            var alert_title  = $(formElem).attr("alert_title")
            var alert_text  = $(formElem).attr("alert-text")
            var alert_type  = $(formElem).attr("alert-type")
            swal({
                title: alert_title || "Confirm",
                text: alert_text || "Are you sure?",
                icon: alert_type || "warning",
                buttons: true,
                dangerMode: true,
            })
            .then(async (willDelete) => {
                if (willDelete) {

                   await swal("Information!", "Poof! Your have confirmed!,", "info", {
                        icon: "success",
                    });
                    
                    formElem.submit()

                } else {
                    swal("Information!", "Your data file is safe!,", "info");
                }
            });
            
        }

    })

    
})