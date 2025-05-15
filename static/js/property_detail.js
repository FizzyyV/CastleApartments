document.addEventListener('DOMContentLoaded', () => {
    const slideshow = document.querySelector('.image-slideshow');
    if (!slideshow) return;

    const slides = slideshow.querySelectorAll('.property-image');
    const dots = slideshow.querySelectorAll('.dot');
    const leftArrow = slideshow.querySelector('.left-arrow');
    const rightArrow = slideshow.querySelector('.right-arrow');

    let slideIndex = 0;

    function showSlide(n) {
        slideIndex = (n + slides.length) % slides.length; // Wrap around

        slides.forEach(slide => slide.classList.remove('active'));
        slides[slideIndex].classList.add('active');

        dots.forEach(dot => dot.classList.remove('active'));
        dots[slideIndex].classList.add('active');
    }

    // Arrow controls
    leftArrow.addEventListener('click', () => showSlide(slideIndex - 1));
    rightArrow.addEventListener('click', () => showSlide(slideIndex + 1));

    // Dot controls
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => showSlide(index));
    });

    // Auto-advance (optional)
    setInterval(() => showSlide(slideIndex + 1), 5000);
});