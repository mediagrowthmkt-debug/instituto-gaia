/* =====================================================
   Instituto Gaia Soul - JavaScript
   ===================================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate on Scroll)
    AOS.init({
        duration: 950,
        easing: 'ease-out-cubic',
        once: true,
        offset: 75,
        delay: 0,
        anchorPlacement: 'top-bottom'
    });

    // =====================================================
    // COOKIE / LGPD NOTICE
    // =====================================================
    const cookieNotice = document.getElementById('cookie-notice');
    const cookieAccept = document.getElementById('cookie-accept');

    if (cookieNotice && cookieAccept) {
        if (!localStorage.getItem('gaia_cookie_accepted')) {
            setTimeout(() => cookieNotice.classList.remove('hidden'), 800);
        } else {
            cookieNotice.style.display = 'none';
        }
        cookieAccept.addEventListener('click', function () {
            localStorage.setItem('gaia_cookie_accepted', '1');
            cookieNotice.classList.add('hidden');
            setTimeout(() => cookieNotice.style.display = 'none', 600);
        });
    }

    // =====================================================
    // SCROLL PROGRESS BAR
    // =====================================================
    const scrollProgressBar = document.getElementById('scroll-progress');

    function updateScrollProgress() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        if (scrollProgressBar) {
            scrollProgressBar.style.width = progress + '%';
        }
    }

    window.addEventListener('scroll', updateScrollProgress, { passive: true });

    // =====================================================
    // HEADER SCROLL EFFECT
    // =====================================================
    const header = document.getElementById('header');
    
    function handleScroll() {
        if (window.scrollY > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
    
    window.addEventListener('scroll', handleScroll);

    // =====================================================
    // MOBILE NAVIGATION TOGGLE
    // =====================================================
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Toggle icon
            const icon = navToggle.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // Close menu when clicking on a link
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // =====================================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // =====================================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = header.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // =====================================================
    // BACK TO TOP BUTTON
    // =====================================================
    const backToTop = document.getElementById('back-to-top');
    
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 500) {
                backToTop.classList.add('active');
            } else {
                backToTop.classList.remove('active');
            }
        });
        
        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // =====================================================
    // EASING UTILITY + COUNT-UP
    // =====================================================
    function easeOutCubic(t) {
        return 1 - Math.pow(1 - t, 3);
    }

    function countUp(el, target, duration, prefix, suffix) {
        var startTime = null;
        function frame(now) {
            if (!startTime) startTime = now;
            var elapsed  = now - startTime;
            var progress = Math.min(elapsed / duration, 1);
            var eased    = easeOutCubic(progress);
            var value    = Math.floor(eased * target);
            el.textContent = (prefix || '') + value.toLocaleString('pt-BR') + (suffix || '');
            if (progress < 1) {
                requestAnimationFrame(frame);
            } else {
                el.textContent = (prefix || '') + target.toLocaleString('pt-BR') + (suffix || '');
                el.classList.add('counted');
            }
        }
        requestAnimationFrame(frame);
    }

    // =====================================================
    // FOUNDER STATS COUNTERS
    // =====================================================
    var founderStats    = document.querySelectorAll('.founder-stat-num');
    var founderAnimated = false;

    function animateFounderStats() {
        founderStats.forEach(function(el) {
            countUp(el, parseInt(el.getAttribute('data-count')), 1800, '', '');
        });
    }

    var founderSection = document.querySelector('.founder');
    if (founderSection && founderStats.length > 0) {
        var founderObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !founderAnimated) {
                    animateFounderStats();
                    founderAnimated = true;
                }
            });
        }, { threshold: 0.3 });
        founderObserver.observe(founderSection);
    }

    // =====================================================
    // SOCIAL IMPACT COUNTERS
    // =====================================================
    var impactNumbers  = document.querySelectorAll('.impact-number');
    var impactAnimated = false;

    function animateImpactNumbers() {
        impactNumbers.forEach(function(el) {
            var target = parseInt(el.getAttribute('data-count'));
            var startTime = null;
            function frame(now) {
                if (!startTime) startTime = now;
                var progress = Math.min((now - startTime) / 2000, 1);
                var value    = Math.floor(easeOutCubic(progress) * target);
                el.textContent = '+' + value.toLocaleString('pt-BR');
                if (progress < 1) {
                    requestAnimationFrame(frame);
                } else {
                    el.textContent = '+' + target.toLocaleString('pt-BR');
                    el.classList.add('counted');
                }
            }
            requestAnimationFrame(frame);
        });
    }

    var impactSection = document.querySelector('.social-impact');
    if (impactSection && impactNumbers.length > 0) {
        var impactObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !impactAnimated) {
                    animateImpactNumbers();
                    impactAnimated = true;
                }
            });
        }, { threshold: 0.2 });
        impactObserver.observe(impactSection);
    }

    // =====================================================
    // CONTACT FORM — Full form with feedback
    // =====================================================
    const contactForm = document.getElementById('contact-form');
    const contactFeedback = document.getElementById('contact-feedback');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            const btn = contactForm.querySelector('.contact-submit-btn');
            const originalHTML = btn.innerHTML;

            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>&nbsp; Enviando...';
            btn.disabled = true;

            // Monta link mailto como fallback enquanto não há backend
            const nome    = contactForm.querySelector('[name="nome"]').value;
            const email   = contactForm.querySelector('[name="email"]').value;
            const tel     = contactForm.querySelector('[name="telefone"]').value;
            const msg     = contactForm.querySelector('[name="mensagem"]').value;

            const mailBody = encodeURIComponent(
                `Nome: ${nome}\nTelefone: ${tel}\n\n${msg}`
            );
            const mailLink = `mailto:institutogaiasoul@gmail.com?subject=Contato - ${encodeURIComponent(nome)}&body=${mailBody}`;

            setTimeout(() => {
                window.location.href = mailLink;

                contactFeedback.textContent = 'Mensagem preparada! Seu cliente de e-mail será aberto.';
                contactFeedback.className = 'contact-form-feedback success';
                btn.innerHTML = '<i class="fas fa-check"></i>&nbsp; Mensagem preparada!';

                setTimeout(() => {
                    contactForm.reset();
                    btn.innerHTML = originalHTML;
                    btn.disabled = false;
                    contactFeedback.textContent = '';
                    contactFeedback.className = 'contact-form-feedback';
                }, 4000);
            }, 1000);
        });
    }

    // =====================================================
    // COUNTER ANIMATION (original stats) — com easing
    var counters    = document.querySelectorAll('.stat-number');
    var hasAnimated = false;
    
    function animateCounters() {
        counters.forEach(function(el) {
            countUp(el, parseInt(el.getAttribute('data-count')), 2000, '', '+');
        });
    }
    
    // Trigger counter animation when stats section is visible
    var statsSection = document.querySelector('.stats');
    
    if (statsSection && counters.length > 0) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && !hasAnimated) {
                    animateCounters();
                    hasAnimated = true;
                }
            });
        }, { threshold: 0.3 });
        
        observer.observe(statsSection);
    }

    // =====================================================
    // PROGRESS BAR ANIMATION
    // =====================================================
    const progressBars = document.querySelectorAll('.progress-fill');
    
    function animateProgressBars() {
        progressBars.forEach(bar => {
            const width = bar.getAttribute('data-width');
            bar.style.width = width + '%';
        });
    }
    
    // Observe each progress section
    const progressSections = document.querySelectorAll('.progress-section, .campaign-card, .campaigns');
    
    progressSections.forEach(section => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bars = entry.target.querySelectorAll('.progress-fill');
                    bars.forEach(bar => {
                        const width = bar.getAttribute('data-width');
                        setTimeout(() => {
                            bar.style.width = width + '%';
                        }, 200);
                    });
                }
            });
        }, { threshold: 0.3 });
        
        observer.observe(section);
    });

    // =====================================================
    // ACTIVE NAVIGATION LINK ON SCROLL
    // =====================================================
    const sections = document.querySelectorAll('section[id]');
    const navLinksAll = document.querySelectorAll('.nav-link');
    
    function setActiveLink() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 150;
            const sectionHeight = section.offsetHeight;
            
            if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinksAll.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }
    
    window.addEventListener('scroll', setActiveLink);

    // =====================================================
    // FORM HANDLING
    // =====================================================
    const newsletterForm = document.getElementById('newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            
            // Simulate form submission
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Enviando...';
            submitBtn.disabled = true;
            
            setTimeout(() => {
                // Reset form
                this.reset();
                submitBtn.textContent = 'Inscrito!';
                
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                }, 2000);
            }, 1500);
        });
    }
    
    // Footer newsletter form
    const footerForms = document.querySelectorAll('.footer-form');
    
    footerForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const input = this.querySelector('input');
            const btn = this.querySelector('button');
            
            btn.innerHTML = '<i class="fas fa-check"></i>';
            
            setTimeout(() => {
                input.value = '';
                btn.innerHTML = '<i class="fas fa-paper-plane"></i>';
            }, 2000);
        });
    });

    // =====================================================
    // PARALLAX EFFECT (HERO)
    // =====================================================
    const heroBackground = document.querySelector('.hero-background');

    if (heroBackground) {
        // Remove a classe de fallback agora que o parallax JS está ativo
        heroBackground.classList.remove('no-parallax');

        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const speed = 0.4;
            // scale(1.06) garante que não apareçam bordas brancas durante o parallax
            heroBackground.style.transform = `translateY(${scrolled * speed}px) scale(1.06)`;
        }, { passive: true });
    }

    // =====================================================
    // LAZY LOADING IMAGES
    // =====================================================
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window && lazyImages.length > 0) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // =====================================================
    // CARD TILT 3D — efeito tátil premium (desktop only)
    // =====================================================
    function initCardTilt() {
        if (window.innerWidth < 1024) return;

        // Adiciona data-tilt dinamicamente para evitar poluir o HTML
        document.querySelectorAll(
            '.project-card, .blog-card, .impact-card, .team-card, .partner-card'
        ).forEach(function(card) {
            card.setAttribute('data-tilt', '');
        });

        document.querySelectorAll('[data-tilt]').forEach(function(card) {
            card.addEventListener('mouseenter', function() {
                this.style.transition = 'transform 0.12s ease';
            });

            card.addEventListener('mousemove', function(e) {
                var rect = this.getBoundingClientRect();
                var x    = e.clientX - rect.left;
                var y    = e.clientY - rect.top;
                var cx   = rect.width  / 2;
                var cy   = rect.height / 2;
                var rotY = ((x - cx) / cx) * 5.5;
                var rotX = -((y - cy) / cy) * 5.5;
                this.style.transform = 'perspective(900px) rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg) translateY(-6px)';
            });

            card.addEventListener('mouseleave', function() {
                this.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
                this.style.transform  = '';
            });
        });
    }

    // =====================================================
    // HERO MOUSE PARALLAX — movimento leve (desktop only)
    // =====================================================
    function initHeroMouseParallax() {
        var hero        = document.querySelector('.hero');
        var heroContent = document.querySelector('.hero-content');
        if (!hero || !heroContent || window.innerWidth < 1024) return;

        var targetX = 0, targetY = 0;
        var currentX = 0, currentY = 0;

        hero.addEventListener('mousemove', function(e) {
            var rect = hero.getBoundingClientRect();
            targetX  = (e.clientX - rect.width  / 2) / rect.width  * 11;
            targetY  = (e.clientY - rect.height / 2) / rect.height * 7;
        });

        hero.addEventListener('mouseleave', function() {
            targetX = 0;
            targetY = 0;
        });

        (function loop() {
            currentX += (targetX - currentX) * 0.07;
            currentY += (targetY - currentY) * 0.07;
            heroContent.style.transform = 'translate(' + currentX.toFixed(2) + 'px, ' + currentY.toFixed(2) + 'px)';
            requestAnimationFrame(loop);
        })();
    }

    // =====================================================
    // MAGNETIC BUTTONS — efeito sutil nos CTAs do hero
    // =====================================================
    function initMagneticButtons() {
        if (window.innerWidth < 1024) return;

        document.querySelectorAll('.hero-buttons .btn').forEach(function(btn) {
            btn.addEventListener('mousemove', function(e) {
                var rect = this.getBoundingClientRect();
                var x    = e.clientX - rect.left - rect.width  / 2;
                var y    = e.clientY - rect.top  - rect.height / 2;
                this.style.transition = 'transform 0.12s ease';
                this.style.transform  = 'translate(' + (x * 0.15).toFixed(1) + 'px, ' + (y * 0.15).toFixed(1) + 'px) scale(1.04) translateY(-3px)';
            });

            btn.addEventListener('mouseleave', function() {
                this.style.transition = 'transform 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
                this.style.transform  = '';
            });
        });
    }

    // Inicializa todos os efeitos premium
    initCardTilt();
    initHeroMouseParallax();
    initMagneticButtons();

    // =====================================================
    // TYPING EFFECT (OPTIONAL - FOR HERO TITLE)
    // =====================================================
    function typeWriter(element, text, speed = 50) {
        let i = 0;
        element.textContent = '';
        
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }

    // =====================================================
    // PRELOADER (OPTIONAL)
    // =====================================================
    window.addEventListener('load', function() {
        const preloader = document.querySelector('.preloader');
        if (preloader) {
            preloader.classList.add('loaded');
            setTimeout(() => {
                preloader.remove();
            }, 500);
        }
    });
});

// =====================================================
// SERVICE WORKER REGISTRATION (OPTIONAL - FOR PWA)
// =====================================================
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Uncomment to register service worker
        // navigator.serviceWorker.register('/sw.js');
    });
}
