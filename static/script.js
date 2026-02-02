// static/script.js
// Auto-hide alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});

// Confirm before delete
function confirmDelete(studentName) {
    return confirm(`Are you sure you want to delete ${studentName}'s record? This action cannot be undone.`);
}
```

Keep the same `student.py` and `database.py` from before.

Now create a `requirements.txt`:
```
Flask==3.0.0