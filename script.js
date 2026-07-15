const button = document.querySelector('.menu-button');
const nav = document.querySelector('#site-nav');
button.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  button.setAttribute('aria-expanded', open);
});
document.querySelectorAll('#site-nav a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open'); button.setAttribute('aria-expanded', 'false');
}));
document.querySelector('#year').textContent = new Date().getFullYear();
