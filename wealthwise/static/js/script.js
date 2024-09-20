document.addEventListener("DOMContentLoaded", function () {
  const servicesLink = document.getElementById("services-link");
  const dropDown = document.getElementById("drop-down");

  servicesLink.addEventListener("click", function (event) {
    event.preventDefault();
    dropDown.style.display =
      dropDown.style.display === "block" ? "none" : "block";
  });

  document.addEventListener("click", function (event) {
    if (
      !servicesLink.contains(event.target) &&
      !dropDown.contains(event.target)
    ) {
      dropDown.style.display = "none";
    }
  });
});
// 
document.addEventListener("DOMContentLoaded", () => {
  const menuIcon = document.querySelector(".menu-icon");
  const closeIcon = document.querySelector(".close-icon");
  const navLinks = document.querySelector(".links");

  menuIcon.addEventListener("click", () => {
    navLinks.classList.toggle("show");
    menuIcon.style.display = "none";
    closeIcon.style.display = "block";
    console.log("hi it is i");
  });

  closeIcon.addEventListener("click", () => {
    navLinks.classList.toggle("show");
    menuIcon.style.display = "block";
    closeIcon.style.display = "none";
  });
});
const first = document.querySelector(".first-section");
const btn = document.querySelector(".btn");
btn.addEventListener("click", () => {
  window.location.href="./login.html"
});



document.addEventListener("DOMContentLoaded", function() {
  const sections = document.querySelectorAll('.section-content');

  const options = {
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('slide-in');
        observer.unobserve(entry.target);
      }
    });
  }, options);

  sections.forEach(section => {
    section.classList.add('hidden');
    observer.observe(section);
  });
});




