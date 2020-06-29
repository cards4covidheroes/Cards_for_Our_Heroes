const slides = document.querySelectorAll('.slide');
const next = document.querySelector('#next');
const prev = document.querySelector('#prev');
const auto = true; // Auto scroll
const intervalTime = 5000;
let slideInterval;

const nextSlide = () => {
  // Get current1 class
  const current1 = document.querySelector('.current1');
  // Remove current1 class
  current1.classList.remove('current1');
  // Check for next slide
  if (current1.nextElementSibling) {
    // Add current1 to next sibling
    current1.nextElementSibling.classList.add('current1');
  } else {
    // Add current1 to start
    slides[0].classList.add('current1');
  }
  setTimeout(() => current1.classList.remove('current1'));
};

const prevSlide = () => {
  // Get current1 class
  const current1 = document.querySelector('.current1');
  // Remove current1 class
  current1.classList.remove('current1');
  // Check for prev slide
  if (current1.previousElementSibling) {
    // Add current1 to prev sibling
    current1.previousElementSibling.classList.add('current1');
  } else {
    // Add current1 to last
    slides[slides.length - 1].classList.add('current1');
  }
  setTimeout(() => current1.classList.remove('current1'));
};

// Button events
next.addEventListener('click', e => {
  nextSlide();
  if (auto) {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, intervalTime);
  }
});

prev.addEventListener('click', e => {
  prevSlide();
  if (auto) {
    clearInterval(slideInterval);
    slideInterval = setInterval(nextSlide, intervalTime);
  }
});

// Auto slide
if (auto) {
  // Run next slide at interval time
  slideInterval = setInterval(nextSlide, intervalTime);
}