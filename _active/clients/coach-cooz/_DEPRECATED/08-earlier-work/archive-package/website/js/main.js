/**
 * The Resurrection Coach — Main JavaScript
 * Handles: Navigation, Scroll Reveal, Smooth Scroll, Active States
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initScrollReveal();
  initSmoothScroll();
  initNavShrink();
});

// ─── NAVIGATION ───────────────────────────────────────────
function initNavigation() {
  const toggle = document.getElementById('nav-toggle');
  const links = document.getElementById('nav-links');
  const nav = document.getElementById('main-nav');

  if (!toggle || !links) return;

  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', !isOpen);
    links.classList.toggle('nav__links--open');
    document.body.classList.toggle('nav-open');
  });

  // Close mobile nav on link click
  links.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      links.classList.remove('nav__links--open');
      document.body.classList.remove('nav-open');
    });
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && links.classList.contains('nav__links--open')) {
      toggle.setAttribute('aria-expanded', 'false');
      links.classList.remove('nav__links--open');
      document.body.classList.remove('nav-open');
    }
  });
}

// ─── NAV SHRINK ON SCROLL ─────────────────────────────────
function initNavShrink() {
  const nav = document.getElementById('main-nav');
  if (!nav) return;

  let lastScroll = 0;
  const threshold = 80;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    if (currentScroll > threshold) {
      nav.classList.add('nav--scrolled');
    } else {
      nav.classList.remove('nav--scrolled');
    }

    // Hide nav on scroll down, show on scroll up (after hero)
    if (currentScroll > window.innerHeight) {
      if (currentScroll > lastScroll && currentScroll - lastScroll > 10) {
        nav.classList.add('nav--hidden');
      } else if (lastScroll - currentScroll > 10) {
        nav.classList.remove('nav--hidden');
      }
    } else {
      nav.classList.remove('nav--hidden');
    }

    lastScroll = currentScroll;
  }, { passive: true });
}

// ─── SCROLL REVEAL ────────────────────────────────────────
function initScrollReveal() {
  const revealElements = document.querySelectorAll('[data-reveal]');
  if (!revealElements.length) return;

  // Set initial state
  revealElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger the animation for sibling elements
        const siblings = entry.target.parentElement.querySelectorAll('[data-reveal]');
        let delay = 0;
        siblings.forEach((sibling, i) => {
          if (sibling === entry.target) {
            delay = i * 120; // 120ms stagger
          }
        });

        setTimeout(() => {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }, delay);

        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -60px 0px'
  });

  revealElements.forEach(el => observer.observe(el));
}

// ─── SMOOTH SCROLL ────────────────────────────────────────
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      
      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();
      const navHeight = document.getElementById('main-nav')?.offsetHeight || 0;

      window.scrollTo({
        top: target.offsetTop - navHeight - 20,
        behavior: 'smooth'
      });
    });
  });
}
