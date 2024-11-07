function toggleMobileMenu() {
  const mobileMenu = document.getElementById("mobile-menu");
  mobileMenu.classList.toggle("hidden");
}

// document.addEventListener("DOMContentLoaded", function () {
//   const links = document.querySelectorAll("ul li a");
//   links.forEach((link) => {
//     link.addEventListener("click", function () {
//       // Remove active class from all links
//       links.forEach((link) => link.classList.remove("active-link"));
//       // Add active class to clicked link
//       this.classList.add("active-link");
//     });
//   });
// });
