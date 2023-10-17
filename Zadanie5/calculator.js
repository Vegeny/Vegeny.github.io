function calculatePrice() {
  let selectedProduct = document.getElementById("selection").value;
  let amount = document.getElementById("amount").value;
  let isNumber = /^[0-9]*(\.[0-9]+)?$/.test(amount);
  let price = getProductPrice(selectedProduct);

  if (isNumber) {
    let parsedAmount = parseFloat(amount);
    if (Number.isInteger(parsedAmount)) {
      let totalCost = price * parsedAmount;
      document.getElementById("result").textContent =
        "ИТОГО: " + totalCost.toFixed(2) + " руб";
    }
  } else {
    document.getElementById("result").textContent =
      "Введите корректное количество товара.";
  }
}

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
