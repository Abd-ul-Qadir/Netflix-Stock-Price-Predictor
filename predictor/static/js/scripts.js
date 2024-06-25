document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('prediction-form');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        loading.style.display = 'block';
        result.textContent = '';

        setTimeout(() => {
            loading.style.display = 'none';
            const prediction = (Math.random() * 100).toFixed(2);
            result.textContent = `Predicted Stock Price: $${prediction}`;
        }, 2000);
    });
});

// Get the current URL path
var currentPath = window.location.pathname;

// Get the anchor element of the active tab
var predictionTab = document.getElementById('predictionTab');
var aboutTab = document.getElementById('aboutTab');

// Check if the current path matches the href attribute of each tab
if (currentPath === '/index.html') {
    predictionTab.classList.add('active');
} else if (currentPath === '/about.html') {
    aboutTab.classList.add('active');
}

