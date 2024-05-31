const authForm = document.getElementById('main-form');
const errorMessage = document.getElementById('error-message');
const formsField = document.getElementsByTagName('input');
const passwordMismatch = document.getElementById('password-mismatch-message');


authForm.addEventListener('submit', function (event) {
    event.preventDefault();
    let allFieldsFilled = true;
    Array.from(formsField).forEach((field) => {
        if (!field.value) {
            allFieldsFilled = false;
        }
    });
    if (!allFieldsFilled) {
        errorMessage.style.display = 'flex';
        passwordMismatch.style.display = 'none';
    } else if (formsField[2].value != formsField[3].value) {
        errorMessage.style.display = 'none';
        passwordMismatch.style.display = 'flex';
    } else {
        passwordMismatch.style.display = 'none';
        errorMessage.style.display = 'none';
    }
})