// Пример для изменения количества товаров в корзине
const cartIcon = document.querySelector('.cart-icon');
const cartCount = document.querySelector('.cart-count');

cartIcon.addEventListener('click', () => {
 let count = parseInt(cartCount.textContent);
 count++;
 cartCount.textContent = count;
});
