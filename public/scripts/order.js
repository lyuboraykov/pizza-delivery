let button = document.getElementById("order-pizza");

button.addEventListener("click", function() {
  let name = document.getElementById("name").value,
      address = document.getElementById("address").value,
      phone = document.getElementById("phone").value,
      pizzaId = window.localStorage.pizzaId;

  let order = {
      name,
      address,
      phone,
      pizzaId
  };

  $.ajax({
      url: "/order",
      method: "POST",
      data: order,
      dataType: "json",
      statusCode: {
          200: function() {
              // window.location.href = "/order";
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

  section.fadeOut(100);
  $(parent.children()[indexOfThis + 1]).fadeIn({ "duration": 100, done: function() {
    this.style.display = "flex";
  }});

});