window.addEventListener("DOMContentLoaded", (event) => {
  let food = document.querySelectorAll(".menu-row .menu-item");
  food = [...food];
  const addFood = document.getElementById("addFood");

  food.map((elem, index) => {
    elem.addEventListener("click", (event) => {
      event.preventDefault();
      let active = event.currentTarget;
      // form card
      let img = active.querySelector("img").getAttribute("src");
      let title = active.querySelector(".menu-infos h3").innerText;
      // assigning
      addFood.querySelector(".image img").setAttribute("src", img);
      addFood.querySelector(".offcanvas-header .section--title--wrapper .section--title.white").innerText = title;
      addFood.classList.add("show");
    });
  });

  addFood.querySelector("button.btn-close").addEventListener("click", (e) => {
    addFood.classList.remove("show");
  });

  // extra dripping
  const extraTop = document.getElementById("extraTopping");
  const extraTopForm = extraTop.querySelector("form");

  extraTop.addEventListener("shown.bs.modal", function () {
    // extraTopForm.reset();
  });

  extraTopForm
    .querySelector(".buttons .btn.btn-secondary")
    .addEventListener("click", (e) => {
      extraTopForm.reset();
    });

  extraTopForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let listTop = extraTopForm.querySelectorAll("input[name='extra']:checked");
    listTop = [...listTop];
    let price = [];

    let totalPrice = parseFloat(
      document.querySelector("#addFood .totalPrice b").getAttribute("price")
    );
    let value = parseInt(
      document.querySelector("#addFood .cart__wrapper input").value
    );

    listTop.map((elem, index) => {
      let tempP = elem.nextElementSibling.getAttribute("price");
      price.push(tempP);
      document.querySelector("#addFood .totalPrice b").innerText = (
        (totalPrice + tempP) *
        value
      ).toFixed(2);
    });

    let myModal = new bootstrap.Modal(extraTop, {
      keyboard: true,
    });
  });
});