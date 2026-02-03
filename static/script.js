// static/script.js

// Auto-hide alerts after 5 seconds
document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");

  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 300);
    }, 5000);
  });
});

// Confirm before delete
function confirmDelete(studentName) {
  return confirm(
    `Are you sure you want to delete ${studentName}'s record?\n\nThis action cannot be undone.`,
  );
}
