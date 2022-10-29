
// $(function () {

//   // if ($('.summernoteEditor')?.length){
//   //     $('.summernoteEditor')?.summernote({
//   //     height: 400,
//   //     tabsize: 2
//   //     });
//   // }
//   // $("#id_password1, #id_password2")?.addClass("form-control")
//   // $("#id_password, #id_username")?.addClass("form-control")
//   // $("#id_old_password, #id_new_password1, #id_new_password2")?.addClass("form-control")

  
//   // const body = $("body")

//   // if (body.hasClass("theme-light")) {
//   //   $("#admin-sidebar-logo")?.attr("src", "/static/assets/images/logolight.png")
//   //   $("#user-navbar-logo")?.attr("src", "/static/assets/images/logolight.png")

//   // } else if (body.hasClass("theme-dark")) {
//   //   $("#admin-sidebar-logo")?.attr("src", "/static/assets/images/logodark.png")
//   //   $("#user-navbar-logo")?.attr("src", "/static/assets/images/logodark.png")

//   // }

//   if ($('.summernoteEditor')?.length){
//     $('.summernoteEditor')?.summernote({
//     height: 400,
//     tabsize: 2
//     });
//   }







//   $(".model-form-for-multyselecter").on("click", (e) => {
//     const button = e.currentTarget
//     $.ajax({
//       url: $(button).attr("getdata-url"),
//       method: "GET",
//       success: function (data) {
//         const select = $($(button).attr("data-target"))[0].querySelector("form select");
//         data.objects.forEach((obj) => {
//           $(select).append($("<option></option>").attr({ "value": obj.id }).text(obj.name))
//         })
//         multi_select_formate(select)

//       }
//     });
//   })




//   $(".sweet-alert-success-before-submit").on("click", (e) => {
//     e.preventDefault();
//     swal("student is added successfully!", "You clicked the button!,", "success");
//     $(e.currentTarget.form).submit()
//   });


//   $(".delete-alert-confirm-link").click(function (e) {
//     e.preventDefault()
//     swal({
//       title: "Are you sure?",
//       text: "Once deleted, you will not be able to recover data!",
//       icon: "warning",
//       buttons: true,
//       dangerMode: true,
//     })
//       .then((willDelete) => {
//         if (willDelete) {

//           const current_link = $(e.currentTarget).attr("href")
//           $.ajax({
//             url: current_link,
//             method: "GET",
//             success: function (response) {
//               if (response.result == "success") {
//                 swal("Poof! Your data has been deleted!", {
//                   icon: "success",
//                 });
//                 data.redirect && window.location.replace(data.redirect);
//               } else {
//                 $(".sweet-alert-error").click(function () {
//                   swal("Somthing Wrong!", response.error, "error");
//                 });
//               }
//             }
//           });


//         } else {
//           swal("Your data file is safe!");
//         }
//       });

//   });


//   $(".confirm-btn-alert").click(function (e) {
//     const select = e.currentTarget.form.getElementsByClassName("confirm-action")[0]
//     const checkboxs = e.currentTarget.form.getElementsByClassName("checkbox")

//     var checkbox_is_checked = false;
//     for (let i = 0; i < checkboxs.length; i++) {
//       if (checkboxs[i].checked) {
//         checkbox_is_checked = true;
//         break
//       }
//     };
//     if (select.value == "delete_selected" && checkbox_is_checked) {
//       swal({
//         title: "Are you sure?",
//         text: "Once deleted, you will not be able to recover data!",
//         icon: "warning",
//         buttons: true,
//         dangerMode: true,
//       })
//         .then((willDelete) => {
//           if (willDelete) {

//             swal("Poof! Your data has been deleted!", {
//               icon: "success",
//             });
//             e.currentTarget.form.submit()

//           } else {
//             swal("Your data file is safe!");
//           }
//         });
//     } else if (select.value != "none" && checkbox_is_checked) {
//       swal({
//         title: "Are you sure?",
//         text: "You want to do this!",
//         icon: "info",
//         buttons: true,
//         dangerMode: true,
//       })
//         .then((willDelete) => {
//           if (willDelete) {

//             swal("Poof! Your has been done!", {
//               icon: "success",
//             });
//             e.currentTarget.form.submit()

//           } else {
//             swal("Your dont't have been done!");
//           }
//         });
//     }

//   });

// });

