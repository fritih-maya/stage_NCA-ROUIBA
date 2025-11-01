const container = document.querySelector('.container');
const loginBtn = document.querySelector('.btn'); // Sélectionne le bouton "Login"

if (loginBtn) {
    loginBtn.addEventListener('click', () => {
        container.classList.remove('active');
    });
}