$(".order-item:not(.order-title)").click(function() {
  $(".active-list-item").removeClass("active-list-item");
  $(this).addClass("active-list-item");
  var orderId = $(this).attr("data-order-id");
  window.localStorage.orderId = orderId;
  $.ajax({
    url: '/orders/' + orderId,
    method: "GET",
    success: function(order) {
      var order = JSON.parse(order),
        dom = '<h1>Информация за поръчка</h1>' +
        '<div class="delivery-info-container">' +
        '<img class="pizza-info-logo" src="' + order.pizzaSrc + '" alt="pizza delivery">' +
        '<div class="info-container">' +
        '<span>Клиент: ' + order.name + '</span>' +
        '<span>Адрес: ' + order.deliveryAddress + '</span>' +
        '<span>Телефон: ' + order.phoneNumber + '</span>' +
        '</div>' +
        '</div>' +
        '<hr class="status_separator">' +
        '<div class="progress_container" data-order-id="<%= order.id %>">' +
          '<div class="status">Приемане</div>' +
          '<div class="status">Приготвяне</div>' +
          '<div class="status">Проверка на качеството</div>' +
         ' <div class="status">На път за адрес</div>' +
          '<div class="status">Доставена</div>' +
        '</div>'

      $(".details-view").html(dom);

      changeStatus(order.status);
      attachStatusActions();
    }
  });
});

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

function attachStatusActions() {
  $(".progress_container div").click(function() {
    var statusIndex = $(".progress_container div").index(this);
    $.ajax({
      url: '/orders/' + window.localStorage.orderId,
      method: "PUT",
      data: { statusIndex },
      dataType: "text",
      success: function(order) {
      	changeStatus(statusIndex);
      }
    });
  });
}