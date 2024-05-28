const authForm = document.getElementById('main-form');
const errorMessage = document.getElementById('error-message');
authForm.addEventListener('submit', function (event) {
    event.preventDefault();
    errorMessage.style.display = 'flex';
})