$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-medical").modal("show");
      },
      success: function (data) {
        $("#modal-medical .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#medical-table tbody").html(data.html_medical_list);
          $("#modal-medical").modal("hide");
        }
        else {
          $("#modal-medical .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create medical
  $(".js-create-medical").click(loadForm);
  $("#modal-medical").on("submit", ".js-medical-create-form", saveForm);

  // Update medical
  $("#medical-table").on("click", ".js-update-medical", loadForm);
  $("#modal-medical").on("submit", ".js-medical-update-form", saveForm);

  // Delete medical
  $("#medical-table").on("click", ".js-delete-medical", loadForm);
  $("#modal-medical").on("submit", ".js-medical-delete-form", saveForm);

});
