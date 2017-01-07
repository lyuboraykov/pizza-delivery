let button = document.getElementById("order-pizza");

button.addEventListener("click", function() {
  let name = document.getElementById("name").value,
      deliveryAddress = document.getElementById("address").value,
      phoneNumber = document.getElementById("phone").value,
      pizzaId = window.localStorage.pizzaId;

  let order = {
      name,
      deliveryAddress,
      phoneNumber,
      pizzaId
  };

  $.ajax({
      url: "/order",
      method: "POST",
      data: order,
      dataType: "json",
      statusCode: {
          200: function(orderId) {
              window.location.href = "/orders/" + orderId + "/view";
          },
          403: function() {
              alert("Поръчката не беше успешна!");
          }
      }
  });
});


document.querySelectorAll(".pizza-order button").forEach(function(button) {
  button.addEventListener("click", function() {
    localStorage.pizzaId = this.parentElement.parentElement.getAttribute("id");
  });
});

$('.next-button').click(function(event) {
  let section = $(this).parent(),
    parent = section.parent(),
    indexOfThis = parent.children().index(section);

  section.fadeOut(400);

  setTimeout(function() {
    $(parent.children()[indexOfThis + 1]).fadeIn({ "duration": 400, done: function() {
      this.style.display = "flex";
    }});
  }, 400);
});