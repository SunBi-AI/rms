window.addEventListener("DOMContentLoaded", (event) => {
  // pizza draw
  const pizzaLeftSelect = document.getElementById("firsthalf");
  const pizzaLeft = document.getElementById("pizza--left");
  const pizzaRightSelect = document.getElementById("secondhalf");
  const pizzaRight = document.getElementById("pizza--right");

  pizzaLeftSelect.addEventListener("change", (e) => {
    let src = e.currentTarget.selectedOptions[0].getAttribute("data-src");
    // console.log(src);
    pizzaLeft.setAttribute("src", src);
  });
  pizzaRightSelect.addEventListener("change", (e) => {
    let src = e.currentTarget.selectedOptions[0].getAttribute("data-src");
    // console.log(src);
    pizzaRight.setAttribute("src", src);
  });

  // everything for the shake of prize
  // init all input
  const pizzaSize = document.getElementById("size");
  const primaryDip = document.getElementById("primarydip");
  const itemCount = document.getElementById("itemCount");

  // init price variable
  let priceSize = parseFloat(
      parseFloat(
        pizzaSize.selectedOptions[0].getAttribute("data-price")
      ).toFixed(2)
    ),
    pricePrimaryDip = 0,
    priceExtraDip = 0,
    priceTotal = 0,
    count = 1;

  // setting price size;
  pizzaSize.addEventListener("change", (e) => {
    priceSize = e.currentTarget.selectedOptions[0].getAttribute("data-price");
    priceSize = parseFloat(priceSize);
    getTotalPrice();
  });

  // setting pricePrimaryDip;
  primaryDip.addEventListener("change", (e) => {
    pricePrimaryDip =
      e.currentTarget.selectedOptions[0].getAttribute("data-price");
    pricePrimaryDip = parseFloat(pricePrimaryDip).toFixed(2);
    pricePrimaryDip = parseFloat(pricePrimaryDip);
    getTotalPrice();
  });

  //setting  total cart number
  itemCount.addEventListener("change", (e) => {
    count = parseInt(e.currentTarget.value);
    getTotalPrice();
  });

  //   addind dipboxes
  const extraTop = document.getElementById("extraTopping");
  let myModal = new bootstrap.Modal(extraTop);
  extraTop.addEventListener("submit", (e) => {
    let elem = document.querySelector(".dips .item").cloneNode(true);
    elem.classList.remove("d-none");
    [...document.querySelectorAll(".dips .item")].forEach((elem) => {
      elem.remove();
    });

    e.preventDefault();
    let listTop = extraTop.querySelectorAll("input[name='extra']:checked");
    listTop = [...listTop];
    myModal.hide();
    priceExtraDip = 0;
    listTop.forEach((item) => {
      document.querySelector(".dips").innerHTML += elem.outerHTML;
      priceExtraDip += parseFloat(
        item.nextElementSibling.getAttribute("price")
      );
    });
    priceExtraDip = parseFloat(priceExtraDip.toFixed(2));
    getTotalPrice();
  });

  const getTotalPrice = () => {
    debugger;
    priceTotal = (priceSize + pricePrimaryDip + priceExtraDip) * count;
    priceTotal = parseFloat(priceTotal.toFixed(2));
    console.log("priceSize", priceSize);
    console.log("pricePrimaryDip", pricePrimaryDip);
    console.log("count ", count);
    console.log("priceExtraDip ", priceExtraDip);
    console.log("priceTotal", priceTotal);
    document.getElementById("totalPrice").innerText = priceTotal;
  };
});
