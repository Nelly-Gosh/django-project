// document.addEventListener("DOMContentLoaded", () => {
//   const form = document.querySelector("form");
//   const emailInput = document.querySelector(".email input");
//   const passwordInput = document.querySelector(".password input");

//   form.addEventListener("submit", (event) => {
//     event.preventDefault(); // Prevent the form from submitting

//     const storedUserData = JSON.parse(localStorage.getItem("userData"));
//     if (!storedUserData) {
//       alert("No user data found. Please sign up first.");
//       return;
//     }

//     // Validate login data
//     if (emailInput.value !== storedUserData.email) {
//       alert("Invalid email address");
//       return;
//     }
//     if (passwordInput.value !== storedUserData.password) {
//       alert("Invalid password");
//       return;
//     }

//     // Redirect to the dashboard page
//     window.location.href = "dashboaard.html";
//   });
// });
