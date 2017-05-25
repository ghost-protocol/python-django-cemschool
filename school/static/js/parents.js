$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-parent").modal("show");
      },
      success: function (data) {
        $("#modal-parent .modal-content").html(data.html_form);
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
          $("#parent-table tbody").html(data.html_parent_list);
          $("#modal-parent").modal("hide");
        }
        else {
          $("#modal-parent .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create parent
  $(".js-create-parent").click(loadForm);
  $("#modal-parent").on("submit", ".js-parent-create-form", saveForm);

  // Update parent
  $("#parent-table").on("click", ".js-update-parent", loadForm);
  $("#modal-parent").on("submit", ".js-parent-update-form", saveForm);

  // Delete parent
  $("#parent-table").on("click", ".js-delete-parent", loadForm);
  $("#modal-parent").on("submit", ".js-parent-delete-form", saveForm);

});
