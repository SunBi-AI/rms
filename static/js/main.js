"use strict";
(function () {
  console.log("Have a good day :balloon:");
  //Checkbox style toggle on check
  const checkchecked = (a) => {
    if (a.checked === true) {
      a.classList.add("check");
    } else {
      a.classList.remove("check");
    }
  };
  let allcheckbox = document.querySelectorAll(".filter");
  if (allcheckbox !== null) {
    allcheckbox.forEach((a) => {
      a.addEventListener("click", () => {
        checkchecked(a);
      });
    });
  }
  //Set Price
  const checkchecked2 = (a) => {
    // let thisone = document.getElementById(a.getAttribute("for"));
    let thisone = a.previousElementSibling;
    if (thisone.checked === true) {
      console.log("checked");
      thisone.classList.add("check");
    } else {
      thisone.classList.remove("check");
    }
  };
  const setprice = (a, b) => {
    let tar = "target-" + a;
    document.getElementById(tar).innerHTML = b;
  };
  let alloptionsize = document.querySelectorAll(".size-item label");
  if (alloptionsize !== null) {
    alloptionsize.forEach((a) => {
      a.addEventListener("mouseover", () => {
        setprice(a.getAttribute("data-name"), a.getAttribute("data-price"));
      });
      a.addEventListener("click", () => {
        checkchecked2(a);
      });
    });
  }
  //Toggle The Text SeeAll
  let seall = document.getElementById("seeall");
  var seaclick = 0;
  if (seall !== null) {
    seall.addEventListener("click", () => {
      if (seaclick % 2 === 0) {
        seall.innerHTML = "Close";
      } else {
        seall.innerHTML = "See All";
      }
      seaclick++;
    });
  }
  // cart check tag
  const dec = document.querySelectorAll(".cart__wrapper .dec");
  const inc = document.querySelectorAll(".cart__wrapper .inc");
  [...dec].map((dec) => {
    dec.addEventListener("click", (e) => {
      e.preventDefault();
      let value = dec.nextElementSibling.value;
      if (value > 1) dec.nextElementSibling.value = --value;
      let event = new Event("change");
      dec.nextElementSibling.dispatchEvent(event);
      priceInc(e, value);
    });
  });
  [...inc].map((inc) => {
    inc.addEventListener("click", (e) => {
      e.preventDefault();
      let elem = inc.previousElementSibling;
      let max = elem.getAttribute("max");
      max = parseInt(max);
      let value = elem.value;
      if (value < max) {
        elem.value = ++value;
        priceInc(e, value);
        let event = new Event("change");
        elem.dispatchEvent(event);
      }
    });
  });

  // increse price
  const priceInc = (e, value) => {
    let priceElem =
      e.currentTarget.parentNode.nextElementSibling.querySelector("b");
    if (priceElem) {
      let price = priceElem.getAttribute("price");
      price = (parseFloat(price) * value).toFixed(2);
      priceElem.innerText = price;
    }
  };

  //Veg Check
  let raditems = document.querySelectorAll(".radio-item label");
  if (raditems !== null) {
    raditems.forEach((a) => {
      a.addEventListener("click", () => {
        a.classList.toggle("check");
      });
    });
  }

  //Click event for the branches
  let maindroppe = document.querySelector(".droppe");
  if (maindroppe !== null) {
    maindroppe.addEventListener("mouseover", () => {
      maindroppe.classList.add("show");
    });
    maindroppe.addEventListener("mouseleave", () => {
      maindroppe.classList.remove("show");
    });
  }
  let allsub = document.querySelectorAll(".subdroppe");
  if (allsub !== null) {
    allsub.forEach((a) => {
      a.addEventListener("mouseover", () => {
        a.classList.add("show");
      });
      a.addEventListener("mouseleave", () => {
        a.classList.remove("show");
      });
    });
  }

  //Signup Login toging
  let logmod = document.querySelector(".login");
  let signmod = document.querySelector(".signup");
  let tologin = document.querySelector("#loginbtn");
  let tosign = document.querySelector("#signbtn");
  if (tosign !== null) {
    tosign.addEventListener("click", () => {
      logmod.classList.remove("active");
      signmod.classList.add("active");
    });
  }
  if (tologin !== null) {
    tologin.addEventListener("click", () => {
      signmod.classList.remove("active");
      logmod.classList.add("active");
    });
  }

  //Hamburger actions
  let hamburger = document.getElementById("ham");
  let sidebar = document.querySelector(".nav--left");
  hamburger.addEventListener("click", () => {
    sidebar.classList.add("show");
  });
  document.addEventListener("click", (e) => {
    var checkit = sidebar.contains(e.target);
    var checkit2 = hamburger.contains(e.target);
    if (!checkit && !checkit2) {
      sidebar.classList.remove("show");
    }
  });
})();
