document.querySelectorAll(".sidebar a").forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const sectionId = this.getAttribute("data-section");

    document.querySelectorAll(".content section").forEach((section) => {
      if (section.id === sectionId) {
        section.classList.remove("hidden");
      } else {
        section.classList.add("hidden");
      }
    });

    // Hide the sidebar on mobile view when a link is clicked
    if (window.innerWidth <= 1024) {
      document.querySelector(".sidebar").classList.remove("sidebar-visible");
      document.querySelector(".sidebar").classList.add("sidebar-hidden");
    }
  });
});



document.querySelectorAll(".bars-icon").forEach((barsIcon) => {
  barsIcon.addEventListener("click", function () {
    if (window.innerWidth <= 1024) {
      document.querySelector(".sidebar").classList.toggle("sidebar-visible");
      document.querySelector(".sidebar").classList.remove("sidebar-hidden");
    } else {
      document.querySelector(".sidebar").classList.toggle("sidebar-visible");
      document.querySelector(".sidebar").classList.remove("sidebar-hidden");
    }
  });
});



