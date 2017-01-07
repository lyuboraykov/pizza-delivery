function updateStatusPeriodically() {
  var orderId = $(".progress_container").attr("data-order-id");
  $.ajax({
    url: '/update_status/' + orderId,
    method: "GET",
    success: function(statusIndex) {
      changeStatus(statusIndex);
    },
    complete: function() {
      setTimeout(updateStatusPeriodically, 3000);
    }
  });
}

function changeStatus(statusIndex) {
  $(".progress_container div").each(function (index) {
    if (index < statusIndex) {
      $(this).removeClass("active");
      $(this).addClass("done");
    } else if (index == statusIndex) {
      $(this).removeClass("active");
      $(this).addClass("active");
    } else {
      $(this).removeClass("active");
      $(this).removeClass("done");
    }
  });
}

// perform the initial invocation
updateStatusPeriodically();

// schedule the second invocation
setTimeout(myPeriodicMethod, 3000);