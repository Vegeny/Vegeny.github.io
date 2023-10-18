function calculatePrice(event) {
  event.preventDefault();
  let selectedProduct = document.getElementById("selection").value;
  let amount = document.getElementById("amount").value;

  let isDecimal = /^-?\d+\.\d+$/.test(amount);
  let isZero = amount.trim()[0] == "0" ? 1 : 0;
  let isNegative = parseFloat(amount) < 0 ? 1 : 0;
  let isString = isNaN(amount) ? 1 : 0;

  if (isNegative || isString || isZero || isDecimal) {
    document.getElementById("result").textContent =
      "Введите корректное количество товара.";
  } else {
    let price = getProductPrice(selectedProduct);
    let parsedAmount = parseFloat(amount);
    let totalCost = price * parsedAmount;
    document.getElementById("result").textContent =
      "ИТОГО: " + totalCost.toFixed(2) + " руб";
  }
}

window.addEventListener("DOMContentLoaded", function (event) {
  let payButton = document.getElementById("pay-button");
  payButton.addEventListener("click", calculatePrice);
});

function getProductPrice(productName) {
  switch (productName) {
    case "Вид1":
      return 4199.0;
    case "Вид2":
      return 	16299.0;
    case "Вид3":
      return 16299.0;
    case "Вид4":
      return 23999.0;
    case "Вид5":
      return 	26199.0;
    case "Вид6":
      return 27999.0;
    case "Вид7":
      return 34499.0;

    default:
      return 0.0;
  }
}
