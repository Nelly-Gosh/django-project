// document.addEventListener("DOMContentLoaded", () => {
//   const form = document.querySelector("form");
//   const firstNameInput = document.querySelector(".first input");
//   const lastNameInput = document.querySelector(".last input");
//   const countryInput = document.querySelector(".country input");
//   const phoneInput = document.querySelector(".phone input");
//   const emailInput = document.querySelector(".email input");
//   const usernameInput = document.querySelector(".user input");
//   const passwordInput = document.querySelector(".password input");
//   const confirmPasswordInput = document.querySelector(".confirm input");
//   const termsCheckbox = document.querySelector(".check input");

//   form.addEventListener("submit", (event) => {
//     event.preventDefault(); // Prevent the form from submitting

//     // Basic validation
//     if (!firstNameInput.value) {
//       alert("First Name is required");
//       return;
//     }
//     if (!lastNameInput.value) {
//       alert("Last Name is required");
//       return;
//     }
//     if (!countryInput.value) {
//       alert("Country is required");
//       return;
//     }
//     if (!phoneInput.value) {
//       alert("Phone Number is required");
//       return;
//     }
//     if (!emailInput.value || !validateEmail(emailInput.value)) {
//       alert("Valid Email Address is required");
//       return;
//     }
//     if (!usernameInput.value) {
//       alert("Username is required");
//       return;
//     }
//     if (!passwordInput.value) {
//       alert("Password is required");
//       return;
//     }
//     if (passwordInput.value !== confirmPasswordInput.value) {
//       alert("Passwords do not match");
//       return;
//     }
//     if (!termsCheckbox.checked) {
//       alert("You must agree to the Privacy & Policy, Terms & Condition");
//       return;
//     }

//     // Store user data in local storage
//     const userData = {
//       firstName: firstNameInput.value,
//       lastName: lastNameInput.value,
//       country: countryInput.value,
//       phone: phoneInput.value,
//       email: emailInput.value,
//       username: usernameInput.value,
//       password: passwordInput.value,
//     };
//     localStorage.setItem("userData", JSON.stringify(userData));

//     // Redirect to the dashboard page
//     window.location.href = "dashboard.html";
//   });

//   function validateEmail(email) {
//     const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//     return re.test(String(email).toLowerCase());
//   }
// });
