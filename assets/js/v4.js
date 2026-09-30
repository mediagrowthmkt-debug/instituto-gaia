/* Instituto Gaia Soul · site v4 */
(function () {
    'use strict';
    var $ = function (s, c) { return (c || document).querySelector(s); };
    var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
    var G = window.GAIA || {};

    /* Header: fica sólido ao rolar */
    var hdr = $('.hdr');
    var totop = $('.totop');
    function onScroll() {
        var y = window.scrollY;
        if (hdr && !hdr.classList.contains('solid')) hdr.classList.toggle('scrolled', y > 60);
        if (totop) totop.classList.toggle('on', y > 700);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* Menu mobile */
    var burger = $('.burger'), menu = $('.menu');
    if (burger && menu) {
        burger.addEventListener('click', function () {
            var open = menu.classList.toggle('open');
            burger.innerHTML = open ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
            document.body.style.overflow = open ? 'hidden' : '';
        });
        $$('.menu a').forEach(function (a) {
            a.addEventListener('click', function () {
                menu.classList.remove('open'); document.body.style.overflow = '';
                burger.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });
    }

    /* Vídeos de fundo: versão certa por tela + carrega só quando aparece */
    var mobile = window.matchMedia('(max-width: 768px)').matches;
    var vio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
        es.forEach(function (e) {
            var v = e.target;
            if (e.isIntersecting) {
                if (!v.src) { v.src = (mobile && v.dataset.srcMobile) ? v.dataset.srcMobile : v.dataset.src; }
                var p = v.play(); if (p && p.catch) p.catch(function () {});
            } else if (v.src) { v.pause(); }
        });
    }, { rootMargin: '200px' }) : null;
    $$('video[data-src]').forEach(function (v) {
        if (vio) vio.observe(v); else { v.src = v.dataset.src; v.play(); }
    });

    /* Revelar ao rolar + contadores + barras */
    function contar(el) {
        if (el.dataset.plain) { el.textContent = el.dataset.to; return; }
        var to = parseFloat(el.dataset.to), dur = 1600, t0 = null;
        var fmt = function (n) { return el.dataset.plain ? String(Math.round(n)) : Math.round(n).toLocaleString('pt-BR'); };
        function step(ts) {
            if (!t0) t0 = ts;
            var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
            el.textContent = fmt(to * e);
            if (k < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    }
    var rio = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
        es.forEach(function (e) {
            if (!e.isIntersecting) return;
            var el = e.target;
            el.classList.add('in');
            if (el.matches('[data-to]')) contar(el);
            if (el.matches('.progress')) el.classList.add('go');
            if (el.matches('.bar')) { var i = el.querySelector('i'); if (i) i.style.width = (el.dataset.pct || 100) + '%'; }
            rio.unobserve(el);
        });
    }, { threshold: .18 }) : null;
    $$('[data-rv], [data-to], .progress, .bar').forEach(function (el) {
        if (rio) rio.observe(el); else el.classList.add('in', 'go');
    });

    /* Efeitos de rolagem (réplica dos Motion Effects do Elementor do site oficial):
       data-fx-y / data-fx-x = velocidade; data-fx-blur = desfoque máximo (px);
       data-fx-range = "início,fim" (%) do trecho em que a imagem fica nítida (direção out-in). */
    var fxEls = $$('[data-fx-y], [data-fx-x]');
    var calmo = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function fx() {
        var vh = window.innerHeight;
        fxEls.forEach(function (el) {
            var box = (el.parentNode.getBoundingClientRect ? el.parentNode : el).getBoundingClientRect();
            var p = (vh - box.top) / (vh + box.height);
            if (p < -0.2 || p > 1.2) return;
            p = Math.max(0, Math.min(1, p));
            var d = p - 0.5, t = '';
            if (el.dataset.fxY) t += ' translateY(' + (-d * el.dataset.fxY * 60).toFixed(1) + 'px)';
            if (el.dataset.fxX) t += ' translateX(' + (d * el.dataset.fxX * 140).toFixed(1) + 'px)';
            el.style.transform = t;
            var lv = parseFloat(el.dataset.fxBlur || 0), r = (el.dataset.fxRange || '20,80').split(','), a = r[0] / 100, b = r[1] / 100, bl = 0;
            if (lv) { if (p < a) bl = lv * (a - p) / a; else if (p > b) bl = lv * (p - b) / (1 - b); }
            el.style.filter = bl > 0.15 ? 'blur(' + bl.toFixed(1) + 'px)' : 'none';
        });
    }
    if (fxEls.length && !calmo) {
        var tick = false;
        window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { fx(); tick = false; }); } }, { passive: true });
        window.addEventListener('resize', fx); fx();
    }

    /* Indicadores: pontos do carrossel */
    $$('.ind-wrap').forEach(function (w) {
        var tr = $('.ind-track', w), dots = $('.ind-dots', w);
        if (!tr || !dots) return;
        var items = $$('.ind', tr);
        items.forEach(function (it, i) {
            var b = document.createElement('button');
            b.setAttribute('aria-label', 'Indicador ' + (i + 1));
            b.addEventListener('click', function () { tr.scrollTo({ left: it.offsetLeft - tr.offsetLeft, behavior: 'smooth' }); });
            dots.appendChild(b);
        });
        function mark() {
            var i = Math.round(tr.scrollLeft / (items[0].offsetWidth + 16));
            $$('button', dots).forEach(function (b, k) { b.classList.toggle('on', k === i); });
        }
        tr.addEventListener('scroll', mark, { passive: true }); mark();
        if (tr.scrollWidth <= tr.clientWidth + 4) dots.style.display = 'none';
    });

    /* MAPA: o palco de cada nível cobre a moldura sem distorcer (os pinos acompanham a imagem) */
    function fitMapas() {
        $$('.mapa').forEach(function (m) {
            var W = m.clientWidth, H = m.clientHeight;
            $$('.stage', m).forEach(function (st) {
                var ar = parseFloat(st.dataset.ar) || 1, w, h;
                if (W / H > ar) { w = W; h = W / ar; } else { h = H; w = H * ar; }
                st.style.width = w + 'px'; st.style.height = h + 'px';
            });
        });
    }
    fitMapas(); window.addEventListener('resize', fitMapas);

    /* MAPA interativo: 3 níveis de satélite com zoom */
    $$('.mapa').forEach(function (m) {
        var niveis = $$('.nivel', m), trilha = $$('.trilha button', m), tip = $('.tip', m);
        var info = $$('.mapa-info .lv[data-go]');
        var atual = 0, gmaps = $('.gmaps', m);
        function ir(n) {
            if (n === atual || !niveis[n]) return;
            var ant = niveis[atual], nov = niveis[n], frente = n > atual;
            fecharTip();
            ant.classList.add(frente ? 'saindo' : 'voltando');
            nov.classList.add(frente ? 'voltando' : 'saindo');
            nov.classList.add('on');
            requestAnimationFrame(function () { requestAnimationFrame(function () { nov.classList.remove('saindo', 'voltando'); }); });
            setTimeout(function () { ant.classList.remove('on', 'saindo', 'voltando'); }, 750);
            atual = n;
            trilha.forEach(function (b, k) { b.classList.toggle('on', k === n); });
            info.forEach(function (d) { d.classList.toggle('on', +d.dataset.go === n); });
            if (gmaps && nov.dataset.gmaps) gmaps.href = nov.dataset.gmaps;
        }
        function fecharTip() { if (tip) tip.classList.remove('on'); }
        function abrirTip(pin) {
            if (!tip) return;
            var d = pin.dataset;
            tip.innerHTML = '<small>' + d.tipo + '</small><b>' + d.nome + '</b>' + d.txt +
                (d.zoom ? '<br><button class="go" type="button" data-zoom="' + d.zoom + '">' + (d.cta || 'Aproximar') + ' <i class="fas fa-search-plus"></i></button>' : '') +
                (d.link ? '<br><a class="go" href="' + d.link + '"' + (d.ext ? ' target="_blank" rel="noopener"' : '') + '>' + (d.linkTxt || 'Saiba mais') + ' <i class="fas fa-arrow-right"></i></a>' : '');
            var r = m.getBoundingClientRect(), p = pin.getBoundingClientRect();
            var x = p.left - r.left + p.width / 2, y = p.top - r.top;
            tip.classList.add('on');
            var w = tip.offsetWidth, h = tip.offsetHeight;
            var left = Math.min(Math.max(10, x - w / 2), r.width - w - 10);
            var top = y - h - 16; if (top < 56) top = y + p.height + 34;
            tip.style.left = left + 'px'; tip.style.top = Math.min(top, r.height - h - 44) + 'px';
            var go = tip.querySelector('[data-zoom]');
            if (go) go.addEventListener('click', function () { ir(+go.dataset.zoom); });
        }
        $$('.pin', m).forEach(function (p) {
            p.addEventListener('mouseenter', function () { if (window.matchMedia('(hover: hover)').matches) abrirTip(p); });
            p.addEventListener('click', function (ev) {
                ev.stopPropagation();
                if (p.dataset.zoom && tip.classList.contains('on') && tip.dataset.for === p.dataset.nome) { ir(+p.dataset.zoom); return; }
                abrirTip(p); tip.dataset.for = p.dataset.nome;
            });
        });
        $$('.area[data-zoom]', m).forEach(function (a) { a.addEventListener('click', function () { ir(+a.dataset.zoom); }); });
        m.addEventListener('click', function (e) { if (!e.target.closest('.tip') && !e.target.closest('.pin')) fecharTip(); });
        if (tip) tip.addEventListener('mouseleave', fecharTip);
        trilha.forEach(function (b, k) { b.addEventListener('click', function () { ir(k); }); });
        info.forEach(function (d) { d.addEventListener('click', function () { ir(+d.dataset.go); m.scrollIntoView({ behavior: 'smooth', block: 'center' }); }); });
    });

    /* Galeria com lightbox */
    var lb = null, lbImgs = [], lbI = 0;
    function lbShow(i) { lbI = (i + lbImgs.length) % lbImgs.length; lb.querySelector('img').src = lbImgs[lbI].src; lb.querySelector('img').alt = lbImgs[lbI].alt; }
    $$('.galeria, .galeria-imersao').forEach(function (g) {
        $$('.g img', g).forEach(function (img, i, arr) {
            img.parentNode.addEventListener('click', function () {
                if (!lb) {
                    lb = document.createElement('div'); lb.className = 'lb';
                    lb.innerHTML = '<button class="x" aria-label="Fechar">&times;</button><button class="p" aria-label="Anterior">&#8249;</button><img alt=""><button class="n" aria-label="Próxima">&#8250;</button>';
                    document.body.appendChild(lb);
                    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('x')) lb.classList.remove('on'); });
                    lb.querySelector('.p').addEventListener('click', function () { lbShow(lbI - 1); });
                    lb.querySelector('.n').addEventListener('click', function () { lbShow(lbI + 1); });
                    document.addEventListener('keydown', function (e) {
                        if (!lb.classList.contains('on')) return;
                        if (e.key === 'Escape') lb.classList.remove('on');
                        if (e.key === 'ArrowLeft') lbShow(lbI - 1);
                        if (e.key === 'ArrowRight') lbShow(lbI + 1);
                    });
                }
                lbImgs = arr; lbShow(i); lb.classList.add('on');
            });
        });
    });

    /* Copiar (Pix, CNPJ) */
    $$('.copy').forEach(function (b) {
        b.addEventListener('click', function () {
            var t = b.dataset.copy;
            var done = function () { var o = b.textContent; b.textContent = 'Copiado'; b.classList.add('ok'); setTimeout(function () { b.textContent = o; b.classList.remove('ok'); }, 1800); };
            if (navigator.clipboard) navigator.clipboard.writeText(t).then(done); else { var i = document.createElement('input'); i.value = t; document.body.appendChild(i); i.select(); document.execCommand('copy'); i.remove(); done(); }
        });
    });

    /* Valores do Guardião mensal */
    $$('.tiers').forEach(function (t) {
        var form = t.closest('form');
        $$('button', t).forEach(function (b) {
            b.addEventListener('click', function () {
                $$('button', t).forEach(function (x) { x.classList.remove('on'); });
                b.classList.add('on');
                if (form && form.valor) form.valor.value = b.dataset.valor;
                var outro = form && form.querySelector('.outro'); if (outro) outro.hidden = b.dataset.valor !== 'outro';
            });
        });
    });

    /* Assunto do contato por botão e por ?assunto= */
    var fAssunto = $('#f-assunto');
    $$('.assuntos button').forEach(function (b) {
        b.addEventListener('click', function () {
            $$('.assuntos button').forEach(function (x) { x.classList.remove('on'); });
            b.classList.add('on'); if (fAssunto) fAssunto.value = b.dataset.assunto;
        });
    });
    var qa = new URLSearchParams(location.search).get('assunto');
    if (qa && fAssunto) { fAssunto.value = qa; $$('.assuntos button').forEach(function (b) { b.classList.toggle('on', b.dataset.assunto === qa); }); }

    /* Formulário em etapas */
    $$('form.stepper').forEach(function (f) {
        var steps = $$('.step', f), i = 0, bar = $('.st-bar i', f), cnt = $('.st-cnt', f);
        var bk = $('.bk', f), nx = $('.nx', f), send = $('.send', f);
        f.setAttribute('novalidate', '');
        f.addEventListener('input', function (e) { if (e.target.setCustomValidity) { e.target.setCustomValidity(''); var bx = e.target.closest('.fld'); if (bx) bx.classList.remove('err'); } });
        function show(n, voltar) {
            steps.forEach(function (s, k) { s.classList.toggle('on', k === n); s.classList.toggle('back', !!voltar && k === n); });
            i = n;
            if (bar) bar.style.width = ((n + 1) / steps.length * 100) + '%';
            if (cnt) cnt.textContent = 'Etapa ' + (n + 1) + ' de ' + steps.length;
            if (bk) bk.hidden = n === 0;
            var ult = n === steps.length - 1;
            if (nx) nx.hidden = ult; if (send) send.hidden = !ult;
        }
        function valida() {
            var ok = true;
            $$('input,textarea,select', steps[i]).forEach(function (el) {
                var box = el.closest('.fld');
                el.setCustomValidity('');
                if (el.validity.valueMissing) el.setCustomValidity(el.type === 'checkbox' ? 'Marque esta opção para continuar.' : 'Preencha este campo.');
                else if (el.validity.typeMismatch) el.setCustomValidity('Confira este campo.');
                var bom = el.checkValidity();
                if (box) box.classList.toggle('err', !bom);
                if (!bom && ok) { ok = false; el.reportValidity(); }
            });
            var grupo = $('.opts[data-req]', steps[i]);
            if (grupo && !$('input:checked', grupo)) { ok = false; grupo.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(-6px)' }, { transform: 'translateX(6px)' }, { transform: 'translateX(0)' }], { duration: 300 }); }
            return ok;
        }
        function avanca() { if (valida() && i < steps.length - 1) { show(i + 1); var p = $('input:not([type=radio]):not([type=hidden]),textarea', steps[i]); if (p && window.innerWidth > 700) p.focus({ preventScroll: true }); } }
        if (nx) nx.addEventListener('click', avanca);
        if (bk) bk.addEventListener('click', function () { if (i > 0) show(i - 1, true); });
        $$('.opts[data-auto] input', f).forEach(function (r) {
            r.addEventListener('change', function () { var o = f.querySelector('.outro'); if (o) { o.hidden = r.value !== 'outro'; if (r.value === 'outro') return; } setTimeout(avanca, 260); });
        });
        $$('.opts:not([data-auto]) input', f).forEach(function (r) {
            r.addEventListener('change', function () { var o = f.querySelector('.outro'); if (o) o.hidden = r.value !== 'outro'; });
        });
        f.addEventListener('submit', function (e) {
            if (i < steps.length - 1 || !valida()) { e.preventDefault(); e.stopImmediatePropagation(); if (i < steps.length - 1) avanca(); }
        }, true);
        f.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target.tagName === 'INPUT' && i < steps.length - 1) { e.preventDefault(); avanca(); } });
        var qa = new URLSearchParams(location.search).get('assunto');
        if (qa) { var r = f.querySelector('input[name=assunto][value="' + qa + '"]'); if (r) { r.checked = true; show(1); return; } }
        show(0);
    });

    /* Formulários: abrem o WhatsApp com a mensagem pronta (e enviam ao CRM se houver webhook) */
    $$('form.js-lead').forEach(function (f) {
        f.addEventListener('submit', function (e) {
            e.preventDefault();
            var d = {}; new FormData(f).forEach(function (v, k) { d[k] = v; });
            var assunto = f.dataset.assunto || d.assunto || 'Contato pelo site';
            var linhas = ['Olá! Vim pelo site do Instituto Gaia Soul.', 'Assunto: ' + assunto];
            if (d.nome) linhas.push('Nome: ' + d.nome);
            if (d.telefone) linhas.push('WhatsApp: ' + d.telefone);
            if (d.email) linhas.push('E-mail: ' + d.email);
            if (d.valor) linhas.push('Valor: ' + (d.valor === 'outro' ? (d.outro ? 'R$ ' + d.outro : 'a combinar') : 'R$ ' + d.valor + ' por mês'));
            if (d.forma) linhas.push('Forma: ' + d.forma);
            if (d.mensagem) linhas.push('Mensagem: ' + d.mensagem);
            if (G.webhook) { try { fetch(G.webhook, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(Object.assign({ assunto: assunto, origem: location.href }, d)) }); } catch (err) {} }
            window.open('https://wa.me/' + G.wa + '?text=' + encodeURIComponent(linhas.join('\n')), '_blank');
            var msg = f.dataset.ok || 'Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar.';
            if (f.classList.contains('stepper')) {
                f.innerHTML = '<div class="st-ok"><i class="fas fa-circle-check"></i><h3>Mensagem pronta!</h3><p>' + msg + '</p></div>';
                return;
            }
            var ok = f.querySelector('.ok'); if (ok) { ok.textContent = msg; ok.classList.add('on'); }
        });
    });
})();
