/* Instituto Gaia Soul · v3: modal "Embarque com a gente", submenu mobile,
   contadores, Marujada (valores e perfil pessoa/empresa) e formulários. */
(function () {
    var CFG = window.GAIA || {};
    var $ = function (s, c) { return (c || document).querySelector(s); };
    var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

    // ---------- Modal "Embarque com a gente" ----------
    var modal = $('#embarque-modal');
    var lastFocus = null;
    function openModal() {
        if (!modal) return;
        lastFocus = document.activeElement;
        modal.hidden = false;
        document.body.classList.add('modal-open');
        var first = $('.em-opt', modal); if (first) first.focus();
    }
    function closeModal() {
        if (!modal || modal.hidden) return;
        modal.hidden = true;
        document.body.classList.remove('modal-open');
        if (lastFocus) lastFocus.focus();
    }
    $$('[data-embarque]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); openModal(); }); });
    $$('[data-close]', modal || document).forEach(function (b) { b.addEventListener('click', closeModal); });
    $$('.em-opt').forEach(function (a) { a.addEventListener('click', closeModal); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeModal(); });

    // ---------- Vídeo do hero: só carrega depois da página, poupa dados ----------
    var hv = $('.hero-video');
    if (hv) {
        var poupar = (navigator.connection && navigator.connection.saveData) ||
            (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
        var liga = function () {
            if (poupar) return;
            hv.src = window.innerWidth < 768 ? hv.getAttribute('data-src-mobile') : hv.getAttribute('data-src');
            hv.addEventListener('playing', function () { hv.classList.add('on'); }, { once: true });
            var pr = hv.play(); if (pr && pr.catch) pr.catch(function () { });
        };
        if (document.readyState === 'complete') setTimeout(liga, 300); else window.addEventListener('load', function () { setTimeout(liga, 300); });
    }

    // ---------- Submenu no mobile ----------
    $$('.sub-toggle').forEach(function (b) {
        b.addEventListener('click', function (e) { e.stopPropagation(); b.parentElement.classList.toggle('open'); });
    });
    $$('.has-sub .sub a').forEach(function (a) {
        a.addEventListener('click', function () {
            var m = $('#nav-menu'); if (m) m.classList.remove('active');
            var i = $('#nav-toggle i'); if (i) { i.classList.remove('fa-times'); i.classList.add('fa-bars'); }
        });
    });

    // ---------- Contadores animados ----------
    var counters = $$('.count');
    function run(el) {
        var to = parseInt(el.getAttribute('data-to'), 10) || 0, t0 = null, dur = 1600;
        function step(ts) {
            if (!t0) t0 = ts;
            var p = Math.min((ts - t0) / dur, 1), v = Math.round(to * (1 - Math.pow(1 - p, 3)));
            el.textContent = v.toLocaleString('pt-BR');
            if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (ents) {
            ents.forEach(function (en) { if (en.isIntersecting) { run(en.target); io.unobserve(en.target); } });
        }, { threshold: .4 });
        counters.forEach(function (c) { io.observe(c); });
    } else {
        counters.forEach(function (c) { c.textContent = parseInt(c.getAttribute('data-to'), 10).toLocaleString('pt-BR'); });
    }

    // ---------- Marujada: valores mensais ----------
    $$('.tiers').forEach(function (box) {
        var form = box.closest('form');
        var hidden = form && form.elements.valor;
        var outro = form && $('.outro-valor', form);
        $$('.tier', box).forEach(function (t) {
            t.addEventListener('click', function () {
                $$('.tier', box).forEach(function (x) { x.classList.remove('on'); });
                t.classList.add('on');
                var v = t.getAttribute('data-valor');
                if (hidden) hidden.value = v;
                if (outro) { outro.hidden = v !== 'outro'; if (v === 'outro') $('input', outro).focus(); }
            });
        });
    });

    // ---------- Pessoa x empresa (muda o botão dos projetos em captação) ----------
    var perfil = 'pf';
    $$('.perfil-toggle button').forEach(function (b) {
        b.addEventListener('click', function () {
            perfil = b.getAttribute('data-perfil');
            $$('.perfil-toggle button').forEach(function (x) { x.classList.toggle('on', x === b); });
            $$('.js-apoiar').forEach(function (a) { a.textContent = a.getAttribute('data-' + perfil); });
        });
    });
    $$('.js-apoiar').forEach(function (a) {
        a.addEventListener('click', function (e) {
            e.preventDefault();
            var quem = perfil === 'pj' ? 'Represento uma empresa e quero patrocinar' : 'Quero apoiar';
            abrirWhats(quem + ' o projeto ' + a.getAttribute('data-projeto') + '.');
        });
    });

    // ---------- Formulários: WhatsApp (+ webhook do CRM, se configurado) ----------
    function abrirWhats(texto) {
        var msg = 'Olá! Vim pelo site do Instituto Gaia Soul.\n' + texto;
        window.open('https://wa.me/' + (CFG.wa || '557199972427') + '?text=' + encodeURIComponent(msg), '_blank');
    }
    var ROTULOS = { nome: 'Nome', telefone: 'WhatsApp', email: 'E-mail', assunto: 'Assunto', forma: 'Forma', valor: 'Valor', outro: 'Outro valor', mensagem: 'Mensagem' };
    $$('form.js-lead').forEach(function (f) {
        f.addEventListener('submit', function (e) {
            e.preventDefault();
            var dados = {}, linhas = [];
            var assunto = f.getAttribute('data-assunto');
            if (assunto) { dados.assunto = assunto; linhas.push('Assunto: ' + assunto); }
            Object.keys(ROTULOS).forEach(function (k) {
                var el = f.elements[k]; if (!el) return;
                var v = (el.value || '').trim(); if (!v) return;
                if (k === 'valor' && v === 'outro') return;
                if (k === 'valor' && /^\d+$/.test(v) && f.classList.contains('marujada-form')) v = 'R$ ' + v + ' por mês';
                if (k === 'outro') v = 'R$ ' + v + ' por mês';
                dados[k] = v;
                if (k !== 'assunto' || !assunto) linhas.push(ROTULOS[k] + ': ' + v);
            });
            if (CFG.webhook) {
                dados.origem = 'site-institutogaiasoul'; dados.pagina = location.pathname;
                try { fetch(CFG.webhook, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dados), keepalive: true }); } catch (err) { }
            }
            abrirWhats(linhas.join('\n'));
            var ok = $('.form-ok', f);
            if (ok) { ok.textContent = f.getAttribute('data-ok') || 'Mensagem pronta no WhatsApp.'; ok.style.display = 'block'; }
        });
    });

    // ---------- Contato: assunto por botão ou pela URL (?assunto=) ----------
    var sel = $('#f-assunto');
    function marcar(a) {
        if (!sel) return;
        $$('.assunto').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-assunto') === a); });
        $$('option', sel).forEach(function (o) { if (o.value === a) sel.value = a; });
    }
    $$('.assunto').forEach(function (b) {
        b.addEventListener('click', function () { marcar(b.getAttribute('data-assunto')); var n = $('#f-nome'); if (n) n.focus(); });
    });
    var q = new URLSearchParams(location.search).get('assunto');
    if (q) marcar(q);
})();
