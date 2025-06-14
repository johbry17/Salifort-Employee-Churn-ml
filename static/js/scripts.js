/*!
 * Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
 */

// header scroll effect
window.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.querySelector(".navbar-toggler");
  const navMenu = document.querySelector("#navbarResponsive");

  toggleButton.addEventListener("click", function () {
    navMenu.classList.toggle("show");
  });

  let scrollPos = 0;
  const mainNav = document.getElementById("mainNav");
  const headerHeight = mainNav.clientHeight;
  window.addEventListener("scroll", function () {
    const currentTop = document.body.getBoundingClientRect().top * -1;
    if (currentTop < scrollPos) {
      // Scrolling Up
      if (currentTop > 0 && mainNav.classList.contains("is-fixed")) {
        mainNav.classList.add("is-visible");
      } else {
        console.log(123);
        mainNav.classList.remove("is-visible", "is-fixed");
      }
    } else {
      // Scrolling Down
      mainNav.classList.remove(["is-visible"]);
      if (
        currentTop > headerHeight &&
        !mainNav.classList.contains("is-fixed")
      ) {
        mainNav.classList.add("is-fixed");
      }
    }
    scrollPos = currentTop;
  });
});

// insert the circle separator at a specific element or selector
function insertCircleSeparator(targetSelector) {
  const separatorHTML = `
    <p class="center-icons">
      <i class="fa fa-circle spacer-icons small-circle"></i>
      <i class="fa fa-circle spacer-icons"></i>
      <i class="fa fa-globe globe-icon"></i>
      <i class="fa fa-circle spacer-icons"></i>
      <i class="fa fa-circle spacer-icons small-circle"></i>
    </p>
  `;
  if (targetSelector) {
    document.querySelectorAll(targetSelector).forEach((el) => {
      el.insertAdjacentHTML("beforeend", separatorHTML);
    });
  } else {
    // If no selector is given, append to body (or you can change this)
    document.body.insertAdjacentHTML("beforeend", separatorHTML);
  }
}
