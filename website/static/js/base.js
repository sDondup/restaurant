/* =========================
   MOBILE NAV TOGGLE
========================= */
function toggleMenu() {
  const nav = document.getElementById("nav-links");
  nav.classList.toggle("show");
}

/* =========================
   CLOSE MENU AFTER CLICK (MOBILE)
========================= */
document.addEventListener("DOMContentLoaded", function () {
  const links = document.querySelectorAll("#nav-links a");
  const nav = document.getElementById("nav-links");

  links.forEach(link => {
    link.addEventListener("click", () => {
      nav.classList.remove("show");
    });
  });
});

/* =========================
   SMOOTH SCROLL (OPTIONAL)
========================= */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();

    const target = document.querySelector(this.getAttribute("href"));
    if (target) {
      target.scrollIntoView({
        behavior: "smooth"
      });
    }
  });
});