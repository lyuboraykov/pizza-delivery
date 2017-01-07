var statuses = [
  "Accepting",
  "In Progress",
  "Quality Checking",
  "On the way",
  "Delivered"
];

function myPeriodicMethod() {
  $.ajax({
    url: '/update_status/1',
    method: "GET",
    success: function(statusIndex) {
      // update the ui
      // 
      console.log("success");
    },
    complete: function() {
      setTimeout(myPeriodicMethod, 3000);
    }
  });
}

// schedule the first invocation:
setTimeout(myPeriodicMethod, 3000);