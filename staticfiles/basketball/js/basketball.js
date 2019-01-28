document.addEventListener("DOMContentLoaded", function() {
  $( "a[href='"+ window.location.pathname + "']").parent().addClass('active');
});
