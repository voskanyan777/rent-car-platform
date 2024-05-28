const authForm = document.getElementById('main-form');
const errorMessage = document.getElementById('error-message');
const formsField = document.getElementsByTagName('input')
authForm.addEventListener('submit', function (event) {
    event.preventDefault();
    let allFieldsFilled = true;
    Array.from(formsField).forEach((field) => {
        if (!field.value){
            allFieldsFilled = false;
        }
    });
    if (!allFieldsFilled){
        errorMessage.style.display = 'flex';
    }
    else{
        errorMessage.style.display = 'none';
    }
})