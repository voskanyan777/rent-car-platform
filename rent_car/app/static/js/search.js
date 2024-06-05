document.addEventListener('DOMContentLoaded', function(){
    const inputSearch = document.getElementById('input-search');
    const cards = document.querySelectorAll('.card');

    inputSearch.addEventListener('input', function(){
        const filter = inputSearch.value.toLowerCase();
        cards.forEach(card => {
            const model = card.querySelector('h3').textContent.toLowerCase();
            if (model.includes(filter)){
                card.style.display = '';
            }
            else{
                card.style.display = 'none'
            }
        })
    })
})