window.addEventListener("scroll", () => {
  const navbar = document.getElementsByClassName("navbar-outer")[0];
  const navbarMobile = document.getElementsByClassName("navbar-mobile")[0];
  if (window.scrollY !== 0) {
    navbar.classList.add("active");
    navbarMobile.classList.add("active");
    return;
  };
  navbar.classList.remove("active");
  navbarMobile.classList.remove("active");
});

window.addEventListener("load", () => {
  const navbarIcon = document.getElementById("nav-icon3");
  const dropdownMenu = document.getElementsByClassName("mobile-dropdown-outer")[0];
  navbarIcon.addEventListener("click", () => {
    if (navbarIcon.classList.contains("open")) {
      navbarIcon.classList.remove("open");
      dropdownMenu.classList.remove("open");
    } else {
      navbarIcon.classList.add("open");
      dropdownMenu.classList.add("open");
    };
  });
});
