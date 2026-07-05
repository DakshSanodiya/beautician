// Pali Goswami Beauty — site interactions

document.addEventListener('DOMContentLoaded', function () {

  // Add a soft shadow to the header once the page is scrolled
  var header = document.querySelector('header');
  function updateHeaderShadow() {
    if (window.scrollY > 8) {
      header.style.boxShadow = '0 4px 16px rgba(92,26,46,0.08)';
    } else {
      header.style.boxShadow = 'none';
    }
  }
  window.addEventListener('scroll', updateHeaderShadow);
  updateHeaderShadow();

  // Fade + rise each service card into view as the visitor scrolls to it
  var cards = document.querySelectorAll('.card');
  cards.forEach(function (card) {
    card.style.opacity = '0';
    card.style.transform = 'translateY(18px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    cards.forEach(function (card) {
      observer.observe(card);
    });
  } else {
    // Fallback: just show everything if IntersectionObserver isn't supported
    cards.forEach(function (card) {
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    });
  }

});
