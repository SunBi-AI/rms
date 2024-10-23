window.addEventListener("DOMContentLoaded", (event) => {
  const parent = document.querySelector(".carousel");
  const prev = parent.querySelector(".prev");
  const next = parent.querySelector(".next");

  next.addEventListener("click", (e) => {
    e.preventDefault();
    let active = parent.querySelector(".active").nextElementSibling;
    parent.querySelector(".active").classList.remove("active");
    if (active) {
      scroll(active);
    } else {
      scroll(parent.querySelector(".image-container").firstElementChild);
    }
  });
  prev.addEventListener("click", (e) => {
    e.preventDefault();
    let active = parent.querySelector(".active").previousElementSibling;
    parent.querySelector(".active").classList.remove("active");
    if (active) {
      scroll(active);
    } else {
      scroll(parent.querySelector(".image-container").lastElementChild);
    }
  });

  const scroll = (elem) => {
    elem.scrollIntoView({
      behavior: "smooth",
      block: "center",
      inline: "start",
    });
    elem.classList.add("active");
  };
});
