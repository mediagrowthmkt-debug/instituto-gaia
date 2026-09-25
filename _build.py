#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o site do Instituto Gaia Soul (v3) seguindo o documento "Site Gaia Soul.docx".
Arquitetura: Quem somos -> O que fazemos -> Que transformação geramos -> Como fazer parte
-> Por que confiar -> Contato. Visual da v2 (Urbanist + Allura, azul-marinho, ondas).

Tudo que é "editável no CMS" no documento fica nos blocos de DADOS logo abaixo:
números de impacto, projetos, projetos em captação, histórias, diário de bordo, parceiros
e valores da Marujada. Edite aqui e rode:  python3 _build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
IMG = "assets/images/v2"
LOGO = "assets/images/logos"
WA = "https://wa.me/557199972427"
WA_NUM = "557199972427"
MAIL = "contato@institutogaiasoul.ong.br"
IG = "https://instagram.com/institutogaiasoul"
RAZAO = "Gaia Soul Instituto de Proteção e Educação Ambiental"
CNPJ = "34.941.993/0001-18"
ENDERECO = "Av. Tancredo Neves, 620, Caminho das Árvores, Salvador/BA, CEP 41820-020"
TEL = "(71) 9997-2427"
# Quando houver um webhook do CRM (GHL/n8n) pros formulários, cole aqui. Vazio = só WhatsApp.
LEAD_WEBHOOK = ""

SOCIAL = [
    ("https://instagram.com/institutogaiasoul", "fab fa-instagram", "Instagram"),
    ("https://www.linkedin.com/company/instituto-gaia-soul/", "fab fa-linkedin-in", "LinkedIn"),
    ("https://www.youtube.com/@InstitutoGaiaSoul", "fab fa-youtube", "YouTube"),
    ("https://www.facebook.com/p/Instituto-Gaia-Soul-61552657763845/", "fab fa-facebook-f", "Facebook"),
    ("https://www.tiktok.com/@institutogaiasoul", "fab fa-tiktok", "TikTok"),
    ("https://br.pinterest.com/institutogaiasoul/", "fab fa-pinterest-p", "Pinterest"),
]

# =====================================================================
# DADOS (o "CMS" do site)
# =====================================================================

# Números de impacto: publicar SOMENTE dados consolidados e verificáveis.
# Para ativar um indicador do documento, troque None pelo número confirmado.
IMPACTO = [
    (None, "+", "pessoas alcançadas"),
    (None, "+", "estudantes"),
    (None, "", "escolas"),
    (None, "", "experiências realizadas"),
    (None, "", "territórios e municípios"),
    (None, "", "parceiros"),
    # já confirmados no Institucional:
    (11, "", "livros didáticos autorais de Cultura Oceânica"),
    (2, "", "comunidades quilombolas na Baía do Iguape"),
    (60, "", "jovens atletas no Real São Francisco"),
    (650, "", "famílias de pescadores e marisqueiras apoiadas"),
]
IMPACTO_ON = [(n, s, t) for n, s, t in IMPACTO if n is not None]

# slug, imagem, tags, nome, resumo da Home, CTA, eixo
PROJETOS = [
    ("imersao-azul", "hf-04-imersao-azul-vr", "Educação • Cultura Oceânica", "Imersão Azul",
     "Uma jornada educativa que leva a Cultura Oceânica para dentro das escolas por meio de livros, experiências, tecnologia e aprendizagem.",
     "Conheça o projeto"),
    ("mundo-submarino-360", "hf-09-360-aeroporto", "Tecnologia • Experiência Imersiva", "Mundo Submarino 360°",
     "Uma experiência de realidade virtual que transporta o público para o universo subaquático e aproxima as pessoas do oceano.",
     "Mergulhe nessa experiência"),
    ("submarino-imersivo", "submarino-1", "Cultura Oceânica • Realidade Virtual", "Submarino Imersivo",
     "Uma experiência coletiva que combina ambientação, realidade virtual e conteúdos sobre o oceano para criar a sensação de estar em uma verdadeira expedição submarina.",
     "Conheça"),
    ("oceanoterapia", "hf-12-oceanoterapia", "Oceano • Natureza • Bem-estar", "Oceanoterapia",
     "Experiências que exploram a conexão consciente com a água e os ambientes naturais como caminho para presença, bem-estar e reconexão.",
     "Conheça"),
    ("mare-de-campeoes", "mare-time", "Esporte • Educação • Transformação Social", "Maré de Campeões",
     "Esporte e educação como instrumentos de desenvolvimento, pertencimento e transformação social.",
     "Conheça"),
    ("centro-de-cultura-oceanica", "hf-03-mar-aereo", "Educação • Ciência • Cultura", "Centro de Cultura Oceânica",
     "Um espaço dedicado a aproximar Salvador e seus visitantes do oceano por meio da educação, da ciência, da cultura e de experiências imersivas.",
     "Conheça"),
]

# Projetos em captação. Campos opcionais (None = não mostra): modalidade, território, público,
# valor aprovado, valor captado, valor disponível. Só preencher com dado público e confirmado.
CAPTACAO = [
    dict(slug="imersao-azul", nome="Imersão Azul", tags="Educação • Cultura Oceânica", img="hf-04-imersao-azul-vr",
         resumo="Leve o oceano para dentro das escolas.", modalidade="Lei Rouanet", status="Em captação",
         territorio="Bahia", publico="Estudantes e professores", aprovado=None, captado=None, disponivel=None),
    dict(slug="mare-de-campeoes", nome="Maré de Campeões", tags="Esporte • Educação • Impacto Social", img="mare-time",
         resumo="Esporte e Cultura Oceânica para crianças e jovens da Baía do Iguape e de Salvador.", modalidade=None,
         status="Em captação", territorio="Baía do Iguape e Salvador", publico="Crianças e adolescentes",
         aprovado=None, captado=None, disponivel=None),
    dict(slug="centro-de-cultura-oceanica", nome="Centro de Cultura Oceânica", tags="Educação • Ciência • Cultura • Salvador",
         img="hf-03-mar-aereo", resumo="Um espaço permanente para aproximar Salvador e seus visitantes do oceano.",
         modalidade=None, status="Em captação", territorio="Salvador", publico="Estudantes, famílias e visitantes",
         aprovado=None, captado=None, disponivel=None),
]

# Histórias de impacto: somente histórias, imagens e depoimentos reais e autorizados.
HISTORIAS = [
    ("mare-gemeas", "Maré de Campeões · Baía do Iguape", "Campeãs baianas de jiu-jitsu",
     "As irmãs gêmeas Larissa e Stella encontraram no esporte um caminho de disciplina, pertencimento e conquista, e se tornaram campeãs baianas de jiu-jitsu."),
    ("rsf-2", "Time Real São Francisco · Cachoeira (BA)", "60 jovens, um time e um vice-campeonato",
     "Com treinador, uniformes, bolas e lanche garantidos pelo Instituto, o Real São Francisco reúne 60 jovens de 12 a 17 anos e chegou ao vice-campeonato em 2025."),
    ("pescadores-3", "Ações sociais · Baía do Iguape", "650 famílias de pescadores e marisqueiras",
     "Em parceria com a Associação dos Pescadores e Marisqueiras de Cachoeira, o Instituto está presente nas datas que importam para as comunidades tradicionais do território."),
]

# Diário de Bordo: categoria, imagem, título, data (ou ""), link
DIARIO = [
    ("Projetos", "rsf-1", "Real São Francisco em campo no Campeonato Cachoeirano 2026", "2026", "acoes-sociais.html#time-real-sao-francisco"),
    ("Bastidores", "prefeitura-1", "Imersão em realidade virtual apresentada à Prefeitura de Cachoeira", "", "acoes-sociais.html#prefeitura"),
    ("Eventos", "bordejo-premiacao", "Bordejos e regatas de canoas na Baía do Iguape", "", "acoes-sociais.html#bordejos"),
    ("Notícias", "escola-1", "Dia das Crianças com educação ambiental nas escolas", "", "acoes-sociais.html#dia-das-criancas"),
    ("Ciência & Oceano", "hf-02-terra-oceano", "Os 7 princípios da Cultura Oceânica", "", "o-instituto.html#proposito"),
    ("Projetos", "livros-1", "Os 11 livros autorais do Imersão Azul", "", "projetos.html#imersao-azul"),
]

# Valores sugeridos da contribuição mensal da Marujada (confirmar com o Instituto).
MARUJADA_VALORES = [30, 60, 120]

# Parceiros por tipo (não misturar tudo numa parede única de logos). Grupos vazios não aparecem.
PARCEIROS = [
    ("Patrocinadores", []),
    ("Apoiadores", [("unesco.png", "UNESCO"), ("decada-oceano.png", "Década do Oceano 2021-2030")]),
    ("Parceiros institucionais", [("aleixo-belov.png", "Fundação Aleixo Belov")]),
    ("Parceiros técnicos e científicos", [("aoceano.png", "Associação Brasileira de Oceanografia")]),
    ("Redes", [("escola-azul.png", "Escola Azul Brasil")]),
]

# =====================================================================
# MENU
# =====================================================================
NAV = [
    ("o-instituto.html", "O Instituto", [
        ("o-instituto.html#quem-somos", "Quem Somos"), ("o-instituto.html#historia", "Nossa História"),
        ("o-instituto.html#proposito", "Propósito"), ("o-instituto.html#governanca", "Governança & Equipe"),
        ("o-instituto.html#territorio", "Nosso Território"), ("o-instituto.html#parceiros", "Parceiros")]),
    ("projetos.html", "Projetos", [
        ("projetos.html#imersao-azul", "Imersão Azul"), ("projetos.html#mundo-submarino-360", "Mundo Submarino 360°"),
        ("projetos.html#submarino-imersivo", "Submarino Imersivo"), ("projetos.html#oceanoterapia", "Oceanoterapia"),
        ("projetos.html#mare-de-campeoes", "Maré de Campeões"), ("projetos.html#centro-de-cultura-oceanica", "Centro de Cultura Oceânica"),
        ("projetos.html#blue-bank", "Blue Bank")]),
    ("atuacao-e-impacto.html", "Atuação & Impacto", [
        ("atuacao-e-impacto.html#eixos", "Os quatro eixos"), ("atuacao-e-impacto.html#numeros", "Impacto em números"),
        ("atuacao-e-impacto.html#mapa", "Mapa de atuação"), ("atuacao-e-impacto.html#historias", "Histórias de impacto"),
        ("acoes-sociais.html", "Ações na Baía do Iguape")]),
    ("marujada.html", "Marujada Gaia Soul", [
        ("marujada.html#fazer-parte", "Quero fazer parte da Marujada"), ("marujada.html#doacao", "Quero fazer uma doação"),
        ("marujada.html#empresas", "Quero apoiar como empresa"), ("marujada.html#voluntariado", "Quero ser voluntário")]),
    ("transparencia.html", "Transparência", []),
    ("contato.html", "Contato", []),
]

SVG_ONDA_ICO = '<svg viewBox="0 0 64 64"><path d="M6 40c8 0 10-6 16-6s8 6 16 6 10-6 16-6"/><path d="M6 50c8 0 10-6 16-6s8 6 16 6 10-6 16-6"/><path d="M20 30c0-10 8-18 18-18 6 0 10 4 10 9 0 4-3 7-7 7-3 0-5-2-5-5"/></svg>'
SVG_ESTRELA = '<svg viewBox="0 0 64 64"><path d="M22 10l4 9 10 1-7 7 2 10-9-5-9 5 2-10-7-7 10-1z"/><path d="M40 30c6-8 18-6 18 4s-8 16-18 18"/><path d="M44 36l6-2M46 42l7 1M44 47l5 4"/><path d="M36 50l3 7 7 1-5 5"/></svg>'
SVG_BARCO = '<svg viewBox="0 0 64 64"><path d="M32 8v36"/><path d="M32 10l18 30H32"/><path d="M30 16L16 40h14"/><path d="M10 46h44l-6 8H16z"/><path d="M6 58c6 0 7-3 13-3s7 3 13 3 7-3 13-3 7 3 13 3"/></svg>'
ROSA = ('<svg class="rosa" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="92"/><circle cx="100" cy="100" r="70"/>'
        '<path d="M100 4 L112 100 L100 196 L88 100Z"/><path d="M4 100 L100 88 L196 100 L100 112Z"/>'
        '<path d="M32 32 L106 94 L168 168 L94 106Z" opacity=".5"/><path d="M168 32 L106 106 L32 168 L94 94Z" opacity=".5"/></svg>')


def social_html(cls):
    return "".join(f'<a href="{u}" target="_blank" rel="noopener" class="{cls}" aria-label="{n}" title="{n}"><i class="{i}"></i></a>' for u, i, n in SOCIAL)


def nav_html(page):
    out = []
    for href, label, subs in NAV:
        on = " active" if href == page else ""
        if subs:
            items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in subs)
            out.append(f'<li class="has-sub"><a href="{href}" class="nav-link{on}">{label}</a>'
                       f'<button class="sub-toggle" aria-label="Abrir submenu de {label}"><i class="fas fa-chevron-down"></i></button>'
                       f'<ul class="sub">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{href}" class="nav-link{on}">{label}</a></li>')
    return "\n".join("                        " + x for x in out)


def head(title, desc, page, og="hf-01-hero-baia"):
    solid = "" if page in ("index.html",) else " header-dark"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://institutogaiasoul.ong.br/{'' if page == 'index.html' else page}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://institutogaiasoul.ong.br/{IMG}/{og}.webp">
    <meta property="og:locale" content="pt_BR">
    <link rel="icon" type="image/png" href="{LOGO}/gaia-soul-oficial.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Allura&family=Urbanist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="stylesheet" href="assets/css/pages.css">
    <link rel="stylesheet" href="assets/css/v2.css">
    <link rel="stylesheet" href="assets/css/v3.css">
    {'<link rel="preload" as="image" href="' + IMG + '/hero-poster.webp">' if page == "index.html" else ''}
</head>
<body>
    <header class="header{solid}" id="header">
        <div class="container">
            <nav class="nav">
                <a href="index.html" class="logo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
                <div class="nav-menu" id="nav-menu">
                    <ul class="nav-list">
{nav_html(page)}
                    </ul>
                </div>
                <div class="nav-actions">
                    <button class="btn btn-embarque" data-embarque>Embarque com a gente</button>
                    <button class="nav-toggle" id="nav-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
                </div>
            </nav>
        </div>
    </header>
"""


def page_hero(img, eyebrow, h1, texto, crumb):
    return f"""
    <section class="page-hero v3">
        <div class="bg" style="background-image:url('{IMG}/{img}.webp')"></div>
        <div class="veil"></div>
        <div class="container" data-aos="fade-up">
            <span class="eyebrow">{eyebrow}</span>
            <h1 class="h-page">{h1}</h1>
            {f'<p class="page-lead">{texto}</p>' if texto else ''}
            <p class="crumb"><a href="index.html">Início</a> / {crumb}</p>
        </div>
    </section>
"""


def sec_head(eyebrow, h2, texto="", center=True, light=False):
    cls = "sec-head" + (" center" if center else "") + (" light" if light else "")
    return f"""<div class="{cls}" data-aos="fade-up">
                <span class="eyebrow">{eyebrow}</span>
                <h2 class="h-sec">{h2}</h2>
                {f'<p class="v2-lead">{texto}</p>' if texto else ''}
            </div>"""


MODAL = f"""
    <div class="embarque-modal" id="embarque-modal" role="dialog" aria-modal="true" aria-labelledby="embarque-titulo" hidden>
        <div class="em-backdrop" data-close></div>
        <div class="em-box">
            <button class="em-close" data-close aria-label="Fechar"><i class="fas fa-times"></i></button>
            {ROSA}
            <span class="eyebrow">Todo mundo a bordo</span>
            <h2 id="embarque-titulo">Como você quer embarcar?</h2>
            <div class="em-grid">
                <a href="marujada.html#fazer-parte" class="em-opt"><i class="fas fa-anchor"></i><b>Quero fazer parte da Marujada</b><span>Apoio recorrente.</span></a>
                <a href="marujada.html#doacao" class="em-opt"><i class="fas fa-water"></i><b>Quero fazer uma doação</b><span>Contribuição pontual.</span></a>
                <a href="marujada.html#empresas" class="em-opt"><i class="fas fa-ship"></i><b>Quero apoiar como empresa</b><span>Patrocínio, Lei Rouanet, ESG e parcerias.</span></a>
                <a href="marujada.html#voluntariado" class="em-opt"><i class="fas fa-hands-helping"></i><b>Quero ser voluntário</b><span>Doe seu tempo e conhecimento.</span></a>
            </div>
        </div>
    </div>"""

FOOTER = f"""
    <footer class="footer wave v3">
        <div class="container">
            <div class="footer-grid v3">
                <div class="footer-about">
                    <a href="index.html" class="footer-logo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
                    <p class="f-frase">Conectamos pessoas ao oceano.</p>
                    <div class="footer-social">{social_html("")}</div>
                </div>
                <div class="footer-links">
                    <h4>Navegação</h4>
                    <ul>
                        <li><a href="o-instituto.html">O Instituto</a></li>
                        <li><a href="projetos.html">Projetos</a></li>
                        <li><a href="atuacao-e-impacto.html">Atuação & Impacto</a></li>
                        <li><a href="marujada.html">Marujada Gaia Soul</a></li>
                        <li><a href="transparencia.html">Transparência</a></li>
                        <li><a href="contato.html">Contato</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Projetos</h4>
                    <ul>
                        <li><a href="projetos.html#imersao-azul">Imersão Azul</a></li>
                        <li><a href="projetos.html#mundo-submarino-360">Mundo Submarino 360°</a></li>
                        <li><a href="projetos.html#submarino-imersivo">Submarino Imersivo</a></li>
                        <li><a href="projetos.html#oceanoterapia">Oceanoterapia</a></li>
                        <li><a href="projetos.html#mare-de-campeoes">Maré de Campeões</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Marujada</h4>
                    <ul>
                        <li><a href="marujada.html#doacao">Faça uma doação</a></li>
                        <li><a href="marujada.html#fazer-parte">Apoio recorrente</a></li>
                        <li><a href="marujada.html#empresas">Apoie como empresa</a></li>
                        <li><a href="marujada.html#voluntariado">Voluntariado</a></li>
                        <li><a href="marujada.html#captacao">Projetos em captação</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Institucional</h4>
                    <ul>
                        <li><i class="fas fa-id-card"></i> CNPJ {CNPJ}</li>
                        <li><i class="fas fa-map-marker-alt"></i> {ENDERECO}</li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:{MAIL}">{MAIL}</a></li>
                        <li><i class="fab fa-whatsapp"></i> <a href="{WA}" target="_blank" rel="noopener">{TEL}</a></li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container f-bottom">
                <p>&copy; 2026 {RAZAO} · CNPJ {CNPJ}</p>
                <p class="legal"><a href="politica-de-privacidade.html">Política de Privacidade</a> · <a href="politica-de-privacidade.html#cookies">Cookies</a> · <a href="politica-de-privacidade.html#lgpd">LGPD</a> · <a href="termos-de-uso.html">Termos de Uso</a></p>
            </div>
        </div>
    </footer>
{MODAL}
    <a href="#" class="back-to-top" id="back-to-top" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></a>
    <a href="{WA}" class="whatsapp-button" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>

    <script>window.GAIA = {{ wa: "{WA_NUM}", webhook: "{LEAD_WEBHOOK}" }};</script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="assets/js/main.js"></script>
    <script src="assets/js/v3.js"></script>
</body>
</html>
"""

# =====================================================================
# BLOCOS REUTILIZADOS
# =====================================================================
PRINCIPIOS = [
    "A Terra tem um Oceano global e muito diverso",
    "O Oceano e a vida marinha têm uma forte ação na dinâmica da Terra",
    "O Oceano exerce uma influência importante no clima",
    "O Oceano permite que a Terra seja habitável",
    "O Oceano suporta uma imensa diversidade de vida e de ecossistemas",
    "O Oceano e a humanidade estão fortemente interligados",
    "Há muito por descobrir e explorar no Oceano",
]
PRINC_HTML = "\n".join(
    f'                    <li data-aos="fade-left" data-aos-delay="{i*60}"><span class="n">{i+1}</span><span class="t">{t}</span></li>'
    for i, t in enumerate(PRINCIPIOS))

MVV = f"""
                <div class="mvv">
                    <div class="mvv-item" data-aos="fade-left">
                        <div class="ico">{SVG_ESTRELA}</div>
                        <div><h3>Missão</h3><p>Informar, sensibilizar e engajar as pessoas para a Cultura Oceânica e a difusão da Oceanoterapia.</p></div>
                    </div>
                    <div class="mvv-item" data-aos="fade-left" data-aos-delay="100">
                        <div class="ico">{SVG_ONDA_ICO}</div>
                        <div><h3>Visão</h3><p>Sensibilizar, até 2030, a consciência ecológica de pelo menos 100 mil pessoas, através de nossos conteúdos, projetos e iniciativas sociais.</p></div>
                    </div>
                    <div class="mvv-item" data-aos="fade-left" data-aos-delay="200">
                        <div class="ico">{SVG_BARCO}</div>
                        <div><h3>Valores</h3><ul><li>Ética</li><li>Respeito</li><li>Transparência</li><li>Conscientização</li><li>Preservação</li></ul></div>
                    </div>
                </div>"""


def numeros_html():
    return "\n".join(
        f'                <div class="ig-stat" data-aos="fade-up" data-aos-delay="{(i % 4) * 80}"><b><span class="count" data-to="{n}">{n}</span>{s}</b><em>{t}</em></div>'
        for i, (n, s, t) in enumerate(IMPACTO_ON))


def proj_cards(limit=None):
    items = PROJETOS if limit is None else PROJETOS[:limit]
    out = []
    for i, (slug, img, tags, nome, txt, cta) in enumerate(items):
        cls = "p-card feat" if i == 0 else "p-card"
        out.append(f"""                <a href="projetos.html#{slug}" class="{cls}" data-aos="fade-up" data-aos-delay="{(i % 3) * 80}">
                    <div class="ph"><img src="{IMG}/{img}.webp" alt="{nome}" loading="lazy"><span class="num">{i+1:02d}</span></div>
                    <div class="bd"><span class="tags">{tags}</span><h3>{nome}</h3><p>{txt}</p><span class="more">{cta} <i class="fas fa-arrow-right"></i></span></div>
                </a>""")
    return "\n".join(out)


def eixos_html(detalhe=False):
    eixos = [
        ("01", "Conhecer", "Cultura Oceânica & Educação",
         "Traduzimos ciência e conhecimento sobre o oceano em experiências educativas acessíveis e capazes de despertar curiosidade, consciência e pertencimento.",
         [("imersao-azul", "Imersão Azul"), ("centro-de-cultura-oceanica", "Centro de Cultura Oceânica")], "fa-book-open",
         "11 livros didáticos autorais, alinhados à BNCC e à Década do Oceano."),
        ("02", "Experimentar", "Tecnologia & Experiências Imersivas",
         "Utilizamos realidade virtual, audiovisual e experiências sensoriais para permitir que diferentes públicos conheçam e vivenciem o universo oceânico.",
         [("mundo-submarino-360", "Mundo Submarino 360°"), ("submarino-imersivo", "Submarino Imersivo")], "fa-vr-cardboard",
         "Experiências levadas a escolas, aeroportos e shopping centers."),
        ("03", "Conectar", "Oceanoterapia & Bem-estar",
         "Criamos experiências que estimulam a reconexão consciente com a água e a natureza, promovendo presença e bem-estar.",
         [("oceanoterapia", "Oceanoterapia")], "fa-spa",
         "Vivências no mar, práticas contemplativas e experiências sensoriais."),
        ("04", "Transformar", "Territórios & Regeneração",
         "Desenvolvemos iniciativas conectadas às realidades sociais, ambientais e culturais dos territórios e de suas comunidades.",
         [("mare-de-campeoes", "Maré de Campeões")], "fa-seedling",
         "2 comunidades quilombolas e 650 famílias de pescadores e marisqueiras na Baía do Iguape."),
    ]
    out = []
    for i, (n, verbo, eixo, txt, projs, ico, res) in enumerate(eixos):
        links = " ".join(f'<a href="projetos.html#{s}">{nm}</a>' for s, nm in projs)
        if verbo == "Transformar":
            links += ' <a href="acoes-sociais.html">Ações na Baía do Iguape</a>'
        extra = f'<p class="res"><i class="fas fa-check"></i> {res}</p>' if detalhe else ""
        out.append(f"""                <div class="eixo" data-aos="fade-up" data-aos-delay="{i*80}">
                    <div class="eixo-top"><span class="num">{n}</span><i class="fas {ico}"></i></div>
                    <h3>{verbo}</h3><span class="sub">{eixo}</span>
                    <p>{txt}</p>{extra}
                    <div class="rel"><small>Projetos relacionados</small>{links}</div>
                </div>""")
    return "\n".join(out)


PINS = [  # (nome, x%, y%, destaque, rótulo à esquerda)  posições sobre assets/images/v2/mapa-bts.webp
    ("Litoral da Bahia", 74, 22, False, True),
    ("Baía do Iguape", 23, 16, True, False),
    ("Recôncavo Baiano", 11, 50, False, False),
    ("Baía de Todos-os-Santos", 38, 36, False, False),
    ("Salvador", 58, 46, False, False),
]
MAPA = ('<div class="mapa-img"><img src="' + IMG + '/mapa-bts.webp" alt="Mapa ilustrado da Baía de Todos-os-Santos, com Salvador, a Baía do Iguape, o Recôncavo Baiano e o litoral da Bahia" loading="lazy">'
        + "".join(f'<span class="mpin{" hi" if hi else ""}{" esq" if esq else ""}" style="left:{x}%;top:{y}%"><i></i><b>{n}</b></span>' for n, x, y, hi, esq in PINS)
        + '<span class="mar-label">Oceano Atlântico</span></div>')


def historias_html(items):
    return "\n".join(f"""                <article class="historia" data-aos="fade-up" data-aos-delay="{i*80}">
                    <div class="ph"><img src="{IMG}/{img}.webp" alt="{tit}" loading="lazy"></div>
                    <div class="bd"><small>{onde}</small><h3>{tit}</h3><p>{txt}</p></div>
                </article>""" for i, (img, onde, tit, txt) in enumerate(items))


def diario_html(items):
    return "\n".join(f"""                <a href="{link}" class="diario-card" data-aos="fade-up" data-aos-delay="{(i % 3)*80}">
                    <div class="ph"><img src="{IMG}/{img}.webp" alt="{tit}" loading="lazy"><span class="cat">{cat}</span></div>
                    <div class="bd">{f'<time>{data}</time>' if data else ''}<h3>{tit}</h3><span class="more">Ler <i class="fas fa-arrow-right"></i></span></div>
                </a>""" for i, (cat, img, tit, data, link) in enumerate(items))


def captacao_html():
    out = []
    for i, c in enumerate(CAPTACAO):
        metas = [("Modalidade", c["modalidade"]), ("Status", c["status"]), ("Território", c["territorio"]),
                 ("Público", c["publico"]), ("Valor aprovado", c["aprovado"]), ("Valor captado", c["captado"]),
                 ("Valor disponível", c["disponivel"])]
        dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in metas if v)
        out.append(f"""                <article class="capt-card" data-aos="fade-up" data-aos-delay="{i*80}">
                    <div class="ph"><img src="{IMG}/{c['img']}.webp" alt="{c['nome']}" loading="lazy"><span class="status">{c['status']}</span></div>
                    <div class="bd">
                        <span class="tags">{c['tags']}</span>
                        <h3>{c['nome']}</h3>
                        <p>{c['resumo']}</p>
                        <dl>{dl}</dl>
                        <a href="contato.html?assunto=Parcerias%20e%20patroc%C3%ADnios" class="btn btn-primary js-apoiar" data-projeto="{c['nome']}" data-pf="Apoiar este projeto" data-pj="Quero patrocinar este projeto">Apoiar este projeto</a>
                        <a href="projetos.html#{c['slug']}" class="link-more">Quero conhecer esta oportunidade <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>""")
    return "\n".join(out)


def parceiros_html():
    out = []
    for grupo, logos in PARCEIROS:
        if not logos:
            continue
        boxes = "".join(f'<div class="partner-box"><img src="{LOGO}/{f}" alt="{n}" loading="lazy"></div>' for f, n in logos)
        out.append(f'<div class="p-group" data-aos="fade-up"><h4>{grupo}</h4><div class="p-logos">{boxes}</div></div>')
    return '<div class="parceiros-grupos">' + "".join(out) + "</div>"


TRANSP_ATALHOS = """<div class="atalhos">
                    <a href="transparencia.html#governanca"><i class="fas fa-sitemap"></i> Governança <i class="fas fa-arrow-right"></i></a>
                    <a href="transparencia.html#documentos"><i class="fas fa-file-alt"></i> Documentos Institucionais <i class="fas fa-arrow-right"></i></a>
                    <a href="transparencia.html#relatorios"><i class="fas fa-chart-bar"></i> Relatórios <i class="fas fa-arrow-right"></i></a>
                    <a href="transparencia.html#prestacao-de-contas"><i class="fas fa-balance-scale"></i> Prestação de Contas <i class="fas fa-arrow-right"></i></a>
                </div>"""

NEWSLETTER = """
    <section class="v2-section wave mist newsletter" id="newsletter">
        <div class="container">
            <div class="nl-box" data-aos="fade-up">
                <div>
                    <span class="eyebrow">Notícias de Bordo</span>
                    <h2 class="h-sec">Receba nossas Notícias de Bordo.</h2>
                    <p class="v2-lead">Projetos, histórias, oportunidades e conteúdos sobre o oceano diretamente no seu e-mail.</p>
                </div>
                <form class="nl-form js-lead" data-assunto="Notícias de Bordo (newsletter)" data-ok="Pronto! Você vai receber nossas Notícias de Bordo.">
                    <input name="nome" placeholder="Nome" aria-label="Nome" required>
                    <input name="email" type="email" placeholder="E-mail" aria-label="E-mail" required>
                    <label class="chk"><input type="checkbox" name="lgpd" required> <span>Concordo com a <a href="politica-de-privacidade.html" target="_blank">Política de Privacidade</a>.</span></label>
                    <button class="btn btn-primary" type="submit">Quero receber</button>
                    <div class="form-ok"></div>
                </form>
            </div>
        </div>
    </section>
"""


def cta_final(img="veleiro-gaia", h2="Tem lugar para você nessa Marujada.",
              txt="Pessoas, empresas, escolas, comunidades e organizações podem ajudar a construir uma sociedade mais conectada ao oceano.",
              b1=('<button class="btn btn-light" data-embarque>Embarque com a gente</button>'),
              b2=('<a href="projetos.html" class="btn btn-outline-light">Conheça nossos projetos</a>')):
    return f"""
    <section class="cta-final wave">
        <div class="bg" style="background-image:url('{IMG}/{img}.webp')"></div>
        <div class="veil"></div>
        <div class="container center" data-aos="fade-up">
            <h2 class="h-sec light">{h2}</h2>
            <p class="v2-lead">{txt}</p>
            <div class="btns">{b1}{b2}</div>
        </div>
    </section>
"""


# =====================================================================
# HOME
# =====================================================================
index = head("Instituto Gaia Soul | O oceano nos conecta",
             "O Instituto Gaia Soul conecta pessoas ao oceano por meio da educação, cultura, ciência, tecnologia e experiências transformadoras. Cultura Oceânica na Bahia: Imersão Azul, Mundo Submarino 360°, Oceanoterapia e Maré de Campeões.",
             "index.html") + f"""
    <section class="v2-hero v3-hero" id="home">
        <div class="bg" style="background-image:url('{IMG}/hero-poster.webp')"></div>
        <video class="hero-video" muted loop playsinline preload="none" poster="{IMG}/hero-poster.webp"
               data-src="assets/video/hero-gaia.mp4" data-src-mobile="assets/video/hero-gaia-mobile.mp4" aria-hidden="true"></video>
        <div class="veil"></div>
        <div class="inner" data-aos="fade-up" data-aos-duration="1100">
            <img class="hero-logo v3" src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul" width="420">
            <h1>O oceano nos conecta.<br><em>O conhecimento nos transforma.</em></h1>
            <p class="hero-txt">Conectamos pessoas ao oceano por meio da educação, da cultura, da ciência, da tecnologia e de experiências transformadoras.</p>
            <p class="hero-txt">Promovemos a Cultura Oceânica para ampliar conhecimento, despertar pertencimento e inspirar novas formas de cuidar de nós, das comunidades e do planeta.</p>
            <div class="hero-buttons">
                <a href="o-instituto.html" class="btn btn-light">Conheça o Gaia Soul</a>
                <a href="projetos.html" class="btn btn-outline-light">Conheça nossos projetos</a>
            </div>
        </div>
        <a href="#instituto" class="scroll-hint v3" aria-label="Descubra o Gaia Soul"><span>Descubra o Gaia Soul</span><i class="fas fa-chevron-down"></i></a>
    </section>

    <section class="v2-section wave deco" id="instituto">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Quem somos</span>
                    <h2 class="h-sec">Aproximamos pessoas do oceano para transformar futuros.</h2>
                    <p class="v2-lead">O Instituto Gaia Soul é uma organização dedicada à promoção da Cultura Oceânica e à construção de novas formas de conexão entre pessoas, oceano e sociedade.</p>
                    <p class="v2-lead">Unimos educação, ciência, cultura, tecnologia e bem-estar para transformar <strong>conhecimento em consciência e consciência em ação</strong>.</p>
                    <p class="v2-lead">Nossa atuação nasce na Bahia, um território profundamente conectado ao mar, e se expande por meio de projetos capazes de alcançar escolas, comunidades, empresas e diferentes públicos.</p>
                    <a href="o-instituto.html" class="btn btn-primary">Conheça o Instituto <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="rimg" style="aspect-ratio:4/5" data-aos="fade-left"><img src="{IMG}/veleiro-gaia.webp" alt="Veleiro GAIA do Instituto Gaia Soul no mar" loading="lazy"></div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="projetos">
        <div class="container">
            {sec_head("Nossos projetos", "Propósito que vira ação.", "Criamos projetos que aproximam pessoas do oceano por diferentes caminhos: da educação às experiências imersivas, do esporte ao bem-estar.")}
            <div class="p-grid bento6">
{proj_cards()}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="projetos.html" class="btn btn-primary">Ver todos os projetos <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="v2-section wave" id="atuacao">
        <div class="container">
            {sec_head("Como transformamos", "Do propósito ao impacto.", "Nossa atuação conecta Cultura Oceânica, educação, tecnologia, bem-estar e territórios. Diferentes caminhos unidos por um mesmo propósito: aproximar pessoas do oceano e transformar essa conexão em conhecimento, consciência e ação.")}
            <div class="eixos">
{eixos_html()}
            </div>
        </div>
    </section>

    <section class="v2-section wave navy impacto" id="numeros">
        <div class="container">
            {sec_head("Impacto em números", "Nosso impacto começa nas pessoas.", light=True)}
            <div class="ig-stats">
{numeros_html()}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="atuacao-e-impacto.html" class="btn btn-light">Conheça nossa Atuação & Impacto <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="v2-section wave territorio" id="territorio">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Onde estamos</span>
                    <h2 class="h-sec">Da Bahia para o oceano.</h2>
                    <p class="v2-lead">Nossa história nasce em um território profundamente conectado ao mar.</p>
                    <p class="v2-lead">A Bahia reúne biodiversidade, cultura, comunidades, ciência, economia e modos de vida que têm no oceano uma parte fundamental de sua identidade.</p>
                    <p class="v2-lead">É a partir dessa relação entre <strong>pessoas, território e oceano</strong> que construímos nossa atuação.</p>
                    <a href="o-instituto.html#territorio" class="btn btn-primary">Conheça nosso território <i class="fas fa-arrow-right"></i></a>
                </div>
                <div class="mapa-wrap" data-aos="fade-left">
                    {MAPA}
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="historias">
        <div class="container">
            {sec_head("Histórias que movem essa maré", "Por trás de cada número, existem pessoas.")}
            <div class="historias">
{historias_html(HISTORIAS)}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="atuacao-e-impacto.html#historias" class="btn btn-ghost">Conheça mais histórias <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="marujada-sec wave" id="marujada">
        {ROSA}
        <svg class="rotas" viewBox="0 0 1440 600" preserveAspectRatio="none" aria-hidden="true"><path d="M-20 480 C 300 380 520 520 820 400 S 1300 200 1460 260"/><path d="M-20 160 C 260 240 560 80 900 180 S 1300 380 1460 320"/></svg>
        <div class="container">
            <div class="marujada-head" data-aos="fade-up">
                <span class="eyebrow">Todo mundo a bordo</span>
                <span class="script-t">Marujada Gaia Soul</span>
                <h2 class="h-sec light">O oceano é grande.<br>Nossa Marujada também pode ser.</h2>
                <p class="v2-lead">A Marujada Gaia Soul reúne pessoas, empresas e organizações que escolheram navegar com a gente.</p>
                <p class="v2-lead">Cada pessoa que embarca fortalece nossa capacidade de levar Cultura Oceânica, educação e experiências transformadoras para cada vez mais pessoas e territórios.</p>
            </div>
            <div class="blocos-ab">
                <div class="bloco" data-aos="fade-right">
                    <i class="fas fa-anchor"></i>
                    <h3>Quero fazer parte da Marujada</h3>
                    <p>Contribua de forma recorrente ou pontual e ajude nossos projetos a continuarem navegando.</p>
                    <span class="chips">Apoio mensal • Doação • PIX • Voluntariado</span>
                    <button class="btn btn-light" data-embarque>Quero embarcar</button>
                </div>
                <div class="bloco" data-aos="fade-left">
                    <i class="fas fa-ship"></i>
                    <h3>Quero embarcar minha empresa</h3>
                    <p>Sua empresa pode apoiar projetos e construir impacto conosco por meio de diferentes modalidades.</p>
                    <span class="chips">Lei Rouanet • Patrocínio • Investimento Social Privado • ESG • Programas Corporativos</span>
                    <a href="marujada.html#empresas" class="btn btn-light">Quero apoiar como empresa</a>
                </div>
            </div>
            <div class="center" style="margin-top:2rem"><a href="marujada.html" class="link-light">Conheça todas as formas de fazer parte da Marujada <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="v2-section wave" id="captacao">
        <div class="container">
            {sec_head("Oportunidades de impacto", "Projetos esperando novos tripulantes.", "Conheça iniciativas do Instituto Gaia Soul abertas a novos parceiros, patrocinadores e apoiadores.")}
            <div class="capt-grid">
{captacao_html()}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="marujada.html#captacao" class="btn btn-primary">Ver projetos em captação</a></div>
        </div>
    </section>

    <section class="v2-section wave mist" id="a-bordo">
        <div class="container">
            {sec_head("Quem navega com a gente", "Transformações maiores são construídas em conjunto.", "Construímos relações com organizações que compartilham conosco o compromisso de gerar impacto positivo para pessoas, comunidades e oceano.")}
            {parceiros_html()}
            <div class="center" style="margin-top:2.6rem"><a href="marujada.html#empresas" class="btn btn-primary">Seja uma organização a bordo <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="v2-section wave transp" id="transparencia">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Responsabilidade</span>
                    <h2 class="h-sec">Confiança também faz parte do nosso impacto.</h2>
                    <p class="v2-lead">Acreditamos que toda transformação precisa ser construída com responsabilidade, integridade e transparência.</p>
                    <p class="v2-lead">Por isso, disponibilizamos informações sobre nossa governança, documentos institucionais, atividades, resultados e utilização de recursos.</p>
                    <a href="transparencia.html" class="btn btn-primary">Acesse nossa transparência</a>
                </div>
                <div data-aos="fade-left">{TRANSP_ATALHOS}</div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="diario">
        <div class="container">
            {sec_head("Diário de Bordo", "Acompanhe nossa jornada.")}
            <div class="diario-grid">
{diario_html(DIARIO[:3])}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="diario-de-bordo.html" class="btn btn-ghost">Ver todas as novidades</a></div>
        </div>
    </section>
""" + NEWSLETTER + cta_final() + FOOTER

# =====================================================================
# O INSTITUTO
# =====================================================================
instituto = head("O Instituto | Instituto Gaia Soul",
                 "Quem somos, nossa história, propósito (missão, visão e valores), governança e equipe, nosso território na Baía do Iguape e nossos parceiros.",
                 "o-instituto.html", "veleiro-gaia") + page_hero(
    "hf-03-mar-aereo", "O Instituto", "Aproximamos pessoas do oceano para transformar futuros.",
    "Educação, ciência, cultura, tecnologia e bem-estar a serviço da Cultura Oceânica.", "O Instituto") + f"""
    <nav class="proj-nav"><div class="container"><a href="#quem-somos">Quem Somos</a><a href="#historia">Nossa História</a><a href="#proposito">Propósito</a><a href="#governanca">Governança & Equipe</a><a href="#territorio">Nosso Território</a><a href="#parceiros">Parceiros</a></div></nav>

    <section class="v2-section wave" id="quem-somos">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Quem somos</span>
                    <h2 class="h-sec">Uma organização dedicada à Cultura Oceânica.</h2>
                    <p class="v2-lead">O Instituto Gaia Soul é uma organização dedicada à promoção da Cultura Oceânica e à construção de novas formas de conexão entre pessoas, oceano e sociedade.</p>
                    <p class="v2-lead">Unimos educação, ciência, cultura, tecnologia e bem-estar para transformar <strong>conhecimento em consciência e consciência em ação</strong>.</p>
                    <p class="v2-lead">Acreditamos em uma ideia simples: <strong>só cuidamos do que conhecemos</strong>.</p>
                </div>
                <div class="rimg" style="aspect-ratio:4/3" data-aos="fade-left"><img src="{IMG}/loja-gaia-soul.webp" alt="Espaço do Instituto Gaia Soul" loading="lazy"></div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="historia">
        <div class="container">
            {sec_head("Nossa história", "Desde 2019, navegando pela Cultura Oceânica.")}
            <ol class="timeline" data-aos="fade-up">
                <li><b>2019</b><span>Nasce o Instituto Gaia Soul, em Salvador, com o propósito de aproximar pessoas do oceano por meio da educação, da ciência, da inovação e de experiências transformadoras.</span></li>
                <li><b>Cultura Oceânica</b><span>Os projetos passam a se alinhar aos 7 princípios da Cultura Oceânica e à Década das Nações Unidas da Ciência Oceânica para o Desenvolvimento Sustentável (2021-2030), com apoio da UNESCO.</span></li>
                <li><b>Imersão Azul</b><span>A Cultura Oceânica chega às escolas com 11 livros didáticos autorais, realidade virtual, plataforma digital e jornada gamificada.</span></li>
                <li><b>Baía do Iguape</b><span>O Instituto passa a atuar junto a comunidades quilombolas, pescadores e marisqueiras, com esporte, educação ambiental e apoio às famílias, e recebe o reconhecimento de Utilidade Pública da Prefeitura de Cachoeira (BA).</span></li>
                <li><b>Hoje</b><span>Um ecossistema de projetos que une educação, experiências imersivas, Oceanoterapia, esporte e território, aberto a pessoas, escolas e empresas que querem embarcar.</span></li>
            </ol>
        </div>
    </section>

    <section class="v2-section wave" id="proposito">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Propósito</span>
                    <h2 class="h-sec">Missão, visão e valores.</h2>
                    <p class="v2-lead">O que nos move e para onde queremos navegar.</p>
                </div>
                <div>{MVV}
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave ocean70">
        <div class="earth" style="background-image:url('{IMG}/hf-02-terra-oceano.webp')"></div>
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Cultura Oceânica</span>
                    <div class="big">70%</div>
                    <div class="big-sub">da superfície da Terra é <span>Oceano</span></div>
                    <div class="seals">
                        <img src="{LOGO}/unesco.png" alt="UNESCO">
                        <img class="tall" src="{LOGO}/decada-oceano.png" alt="Década das Nações Unidas da Ciência Oceânica 2021-2030">
                    </div>
                </div>
                <div data-aos="fade-left">
                    <h2 class="v2-title light"><span class="script">princípios</span><span class="main">cultura oceânica</span></h2>
                    <ul class="principles">
{PRINC_HTML}
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="governanca">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Governança & Equipe</span>
                    <h2 class="h-sec">Quem conduz essa travessia.</h2>
                    <p class="v2-lead">O Instituto Gaia Soul é uma associação sem fins lucrativos, registrada como <strong>{RAZAO}</strong> (CNPJ {CNPJ}), com sede em Salvador (BA).</p>
                    <p class="v2-lead">Nossa atuação é guiada pelos valores de ética, respeito, transparência, conscientização e preservação.</p>
                    <a href="transparencia.html#governanca" class="btn btn-ghost">Ver governança e documentos</a>
                </div>
                <div class="team" data-aos="fade-left">
                    <div class="member">
                        <div class="av"><i class="fas fa-user"></i></div>
                        <div><b>Marcelo Telles</b><span>Presidente e fundador</span></div>
                    </div>
                    <div class="member soft">
                        <div class="av"><i class="fas fa-users"></i></div>
                        <div><b>Equipe e colaboradores</b><span>Educadores, pesquisadores, voluntários e parceiros técnicos que tornam cada projeto possível.</span></div>
                    </div>
                    <div class="selo">
                        <img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública">
                        <div class="t"><small>Reconhecimento de</small><b>Utilidade pública</b><small>Prefeitura de Cachoeira - BA</small></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave territorio" id="territorio">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Nosso território</span>
                    <h2 class="h-sec">Da sede em Salvador à Baía do Iguape.</h2>
                    <p class="v2-lead">Nossa sede fica em Salvador, cidade que nasceu voltada para a Baía de Todos-os-Santos. É daqui que partem nossos projetos para escolas, espaços públicos e comunidades.</p>
                    <p class="v2-lead">No Recôncavo Baiano, atuamos na <strong>Reserva Extrativista Marinha Baía do Iguape</strong>, unidade de conservação federal criada em 2000 para proteger o ecossistema local e garantir a subsistência de comunidades tradicionais.</p>
                    <p class="v2-lead">Ali vivem cerca de <strong>14 comunidades quilombolas</strong>, em um território tradicional de pesca, mariscagem e cultivo de ostras. É com elas que construímos esporte, educação ambiental e apoio às famílias.</p>
                    <div class="pill-row"><span class="pill teal">Comunidades pesqueiras</span><span class="pill teal">Comunidades quilombolas</span><span class="pill teal">Barra do Paraguaçu</span></div>
                    <a href="acoes-sociais.html" class="btn btn-primary">Ver as ações na Baía do Iguape</a>
                </div>
                <div class="mapa-wrap" data-aos="fade-left">
                    {MAPA}
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="parceiros">
        <div class="container">
            {sec_head("Parceiros", "Quem navega com a gente.")}
            {parceiros_html()}
        </div>
    </section>
""" + cta_final("hf-14-costa-bahia") + FOOTER

# =====================================================================
# PROJETOS
# =====================================================================
def gal(items, cls="g3"):
    out = []
    for it in items:
        img, alt = it[0], it[1]
        extra = f" {it[2]}" if len(it) > 2 else ""
        out.append(f'<div class="rimg{extra}"><img src="{IMG}/{img}.webp" alt="{alt}" loading="lazy"></div>')
    return f'<div class="gallery {cls}" data-aos="fade-up">' + "".join(out) + "</div>"


def bloco_proj(idx, slug, tags, nome, alt, corpo, midia, extra="", cta="Quero levar este projeto"):
    return f"""
    <section class="project-block wave {'alt' if idx % 2 else 'rev'}" id="{slug}">
        <span class="idx">{idx:02d}</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <div><span class="tags-lg">{tags}</span><h2 class="h-sec">{nome}</h2></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
{corpo}
                    <div class="btns-row"><a href="contato.html?assunto=Projetos" class="btn btn-primary">{cta}</a><button class="btn btn-ghost" data-embarque>Apoiar este projeto</button></div>
                </div>
                {midia}
            </div>{extra}
        </div>
    </section>"""


def rimg(img, alt, ratio="16/10"):
    return f'<div class="rimg" style="aspect-ratio:{ratio}" data-aos="fade-left"><img src="{IMG}/{img}.webp" alt="{alt}" loading="lazy"></div>'


projetos = head("Projetos | Instituto Gaia Soul",
                "Imersão Azul, Mundo Submarino 360°, Submarino Imersivo, Oceanoterapia, Maré de Campeões, Centro de Cultura Oceânica e Blue Bank: os projetos do Instituto Gaia Soul.",
                "projetos.html", "hf-05-submarino-vr") + page_hero(
    "hf-05-submarino-vr", "Nossos projetos", "Propósito que vira ação.",
    "Da educação às experiências imersivas, do esporte ao bem-estar: caminhos diferentes para aproximar pessoas do oceano.", "Projetos") + """
    <nav class="proj-nav"><div class="container"><a href="#imersao-azul">Imersão Azul</a><a href="#mundo-submarino-360">Mundo Submarino 360°</a><a href="#submarino-imersivo">Submarino Imersivo</a><a href="#oceanoterapia">Oceanoterapia</a><a href="#mare-de-campeoes">Maré de Campeões</a><a href="#centro-de-cultura-oceanica">Centro de Cultura Oceânica</a><a href="#blue-bank">Blue Bank</a></div></nav>
""" + bloco_proj(1, "imersao-azul", "Educação • Cultura Oceânica", "Imersão Azul", "", f"""                    <img class="brand" src="{LOGO}/imersao-azul.png" alt="Imersão Azul" style="height:110px;margin-bottom:1.2rem">
                    <p class="v2-lead">Uma jornada educativa que <strong>leva a Cultura Oceânica para dentro das escolas</strong>, alinhada à BNCC e à Década do Oceano.</p>
                    <p class="v2-lead">Um ecossistema de aprendizagem que integra <strong>11 livros didáticos autorais</strong>, <strong>realidade virtual</strong>, plataforma digital e jornada gamificada, transformando conceitos científicos em experiências envolventes.</p>
                    <p class="v2-lead">Com a <strong>Imersão Polar</strong>, uma expedição científica ao Ártico, o projeto ganha imagens terrestres e subaquáticas exclusivas que viram conteúdo didático sobre as mudanças climáticas.</p>""",
                     f"""<div class="stack" data-aos="fade-left">
                    <div class="rimg" style="aspect-ratio:16/10"><img src="{IMG}/hf-04-imersao-azul-vr.webp" alt="Estudantes com óculos de realidade virtual em sala de aula" loading="lazy"></div>
                    <div class="books">
                        <img src="{IMG}/livros-1.webp" alt="Livros Imersão Azul, 1º ao 5º ano" loading="lazy">
                        <img src="{IMG}/livros-2.webp" alt="Livros Imersão Azul, Ensino Médio" loading="lazy">
                        <img src="{IMG}/livros-3.webp" alt="Livros Imersão Azul, 3º ao 7º ano" loading="lazy">
                        <img src="{IMG}/livros-4.webp" alt="Livros Imersão Azul, 8º e 9º ano" loading="lazy">
                    </div>
                </div>""", f"""
            <div style="margin-top:28px">{gal([("hf-06-polar-geleira", "Geleira no Ártico"), ("hf-07-polar-pinguins", "Pinguins e navio de expedição"), ("hf-08-polar-urso", "Urso polar sobre o gelo")])}</div>""",
                     "Quero o Imersão Azul na minha escola") \
    + bloco_proj(2, "mundo-submarino-360", "Tecnologia • Experiência Imersiva", "Mundo Submarino 360°", "", """                    <p class="v2-lead">Uma experiência de <strong>realidade virtual que transporta o público para o universo subaquático</strong> e aproxima as pessoas do oceano.</p>
                    <p class="v2-lead">Levamos o Mundo Submarino 360° a <strong>aeroportos, shopping centers e eventos</strong>, com recursos audiovisuais de ponta e experiências sensoriais memoráveis.</p>
                    <div class="pill-row"><span class="pill soft">Experiência inédita</span><span class="pill soft">Impacto visual e sensorial</span><span class="pill soft">Conteúdo educativo</span></div>""",
                     rimg("hf-09-360-aeroporto", "Estande Mundo Submarino 360 no aeroporto"),
                     f"""
            <div style="margin-top:28px">{gal([("hf-10-360-frente", "Estande Mundo Submarino 360 visto de frente"), ("hf-11-360-interior", "Interior do Mundo Submarino 360")], "g2")}</div>""",
                     "Quero levar ao meu espaço") \
    + bloco_proj(3, "submarino-imersivo", "Cultura Oceânica • Realidade Virtual", "Submarino Imersivo", "", """                    <p class="v2-lead">Uma <strong>experiência coletiva</strong> que combina ambientação, realidade virtual e conteúdos sobre o oceano para criar a sensação de estar em uma <strong>verdadeira expedição submarina</strong>.</p>
                    <p class="v2-lead">Dentro de uma estrutura que simula um submarino, os visitantes exploram ecossistemas marinhos, conhecem espécies e compreendem a importância do oceano para a vida no planeta.</p>""",
                     rimg("hf-05-submarino-vr", "Crianças com realidade virtual no fundo do mar"),
                     f"""
            <div style="margin-top:28px">{gal([("submarino-1", "Submarino inflável com escotilhas"), ("submarino-2", "Submarino imersivo visto de lado"), ("submarino-3", "Entrada do Submarino 360")])}</div>""",
                     "Quero levar à minha escola ou evento") \
    + bloco_proj(4, "oceanoterapia", "Oceano • Natureza • Bem-estar", "Oceanoterapia", "", f"""                    <img class="brand" src="{LOGO}/oceanoterapia.png" alt="Oceanoterapia" style="height:100px;margin-bottom:1.2rem">
                    <p class="v2-lead">Experiências que exploram a <strong>conexão consciente com a água e os ambientes naturais</strong> como caminho para presença, bem-estar e reconexão.</p>
                    <p class="v2-lead">Por meio de vivências no mar, práticas contemplativas e experiências sensoriais, a Oceanoterapia fortalece a relação entre pessoas e ambiente marinho, despertando pertencimento, equilíbrio e atitudes em favor da conservação.</p>
                    <div class="quote-box"><h3>O oceano educa de um jeito diferente</h3><p>Ele ensina ritmo, pausa, escuta, pertencimento e conexão.</p></div>""",
                     rimg("hf-12-oceanoterapia", "Pessoa boiando no mar em estado contemplativo"), "",
                     "Quero viver a Oceanoterapia") \
    + bloco_proj(5, "mare-de-campeoes", "Esporte • Educação • Transformação Social", "Maré de Campeões", "", """                    <span class="pill">Projeto em elaboração</span>
                    <p class="v2-lead" style="margin-top:1rem"><strong>Esporte e educação como instrumentos de desenvolvimento, pertencimento e transformação social.</strong></p>
                    <p class="v2-lead">O Maré de Campeões nasce da experiência do Instituto com o esporte na Baía do Iguape e em Salvador: modalidades esportivas, vivências na natureza e atividades educativas para formar não apenas atletas, mas <strong>cidadãos conscientes do papel do oceano para a vida</strong>.</p>
                    <div class="pill-row"><span class="pill soft"><i class="fas fa-medal"></i> Campeãs baianas do jiu-jitsu: Larissa e Stella</span><span class="pill soft"><i class="fas fa-futbol"></i> Real São Francisco: vice-campeão 2025</span></div>""",
                     rimg("mare-time", "Time Real São Francisco 2026"),
                     f"""
            <div style="margin-top:28px">{gal([("mare-gemeas", "Campeãs baianas do jiu-jitsu, Larissa e Stella", "tall"), ("mare-vela", "Escolinha de Vela", "tall"), ("rsf-2", "Time Real São Francisco com a bandeira do Instituto", "tall")])}</div>""",
                     "Quero apoiar o Maré de Campeões") \
    + bloco_proj(6, "centro-de-cultura-oceanica", "Educação • Ciência • Cultura", "Centro de Cultura Oceânica", "", """                    <span class="pill">Em captação</span>
                    <p class="v2-lead" style="margin-top:1rem">Um espaço dedicado a <strong>aproximar Salvador e seus visitantes do oceano</strong> por meio da educação, da ciência, da cultura e de experiências imersivas.</p>
                    <p class="v2-lead">Uma casa permanente para a Cultura Oceânica na Bahia, reunindo em um só lugar o que hoje acontece em escolas, eventos e comunidades.</p>""",
                     rimg("hf-03-mar-aereo", "Mar da Bahia visto do alto"), "", "Quero saber mais") \
    + bloco_proj(7, "blue-bank", "Imagens • Educação • Ciência", "Blue Bank", "", """                    <span class="pill">Em desenvolvimento</span>
                    <p class="v2-lead" style="margin-top:1rem">Um <strong>banco de imagens e vídeos do oceano</strong>, com foco em vídeos 360° e subaquáticos, formado por imagens doadas por fotógrafos, mergulhadores e cinegrafistas.</p>
                    <p class="v2-lead">O acervo passa por curadoria, alimenta os conteúdos educativos do Imersão Azul e fica acessível aos estudantes. Quem doa a imagem também pode vendê-la: <strong>50% para o autor, 30% para a manutenção do banco e 20% para o Instituto</strong>.</p>""",
                     rimg("veleiro-gaia", "Veleiro GAIA no mar"), "", "Quero doar minhas imagens") + f"""

    <section class="v2-section wave navy">
        <div class="container center" data-aos="fade-up">
            <h2 class="h-sec light">Quer apoiar nossos projetos?</h2>
            <p class="v2-lead" style="color:#cfe3ec">Escolas, empresas e parceiros podem levar a Cultura Oceânica a mais pessoas.</p>
            <div class="btns"><a href="marujada.html#captacao" class="btn btn-light">Ver projetos em captação</a><button class="btn btn-outline-light" data-embarque>Embarque com a gente</button></div>
        </div>
    </section>
""" + FOOTER

# =====================================================================
# ATUAÇÃO & IMPACTO
# =====================================================================
atuacao = head("Atuação & Impacto | Instituto Gaia Soul",
               "Conhecer, experimentar, conectar e transformar: os quatro eixos de atuação do Instituto Gaia Soul, nosso impacto em números, mapa de atuação e histórias reais.",
               "atuacao-e-impacto.html", "baia-iguape-aerea") + page_hero(
    "baia-iguape-aerea", "Atuação & Impacto", "Do propósito ao impacto.",
    "Nossa atuação conecta Cultura Oceânica, educação, tecnologia, bem-estar e territórios. Cada iniciativa nasce de um propósito comum: aproximar pessoas do oceano e transformar essa conexão em conhecimento, consciência e ação.",
    "Atuação & Impacto") + f"""
    <section class="v2-section wave" id="eixos">
        <div class="container">
            {sec_head("Os quatro eixos", "Conhecer, experimentar, conectar, transformar.")}
            <div class="eixos">
{eixos_html(detalhe=True)}
            </div>
        </div>
    </section>

    <section class="v2-section wave navy impacto" id="numeros">
        <div class="container">
            {sec_head("Nosso impacto em números", "Nosso impacto começa nas pessoas.", "Publicamos somente dados consolidados e verificáveis.", light=True)}
            <div class="ig-stats">
{numeros_html()}
            </div>
        </div>
    </section>

    <section class="v2-section wave territorio" id="mapa">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Mapa de atuação</span>
                    <h2 class="h-sec">Da Bahia para o oceano.</h2>
                    <ul class="lugares">
                        <li><b>Salvador</b><span>Sede do Instituto e ponto de partida dos projetos em escolas, eventos e espaços públicos.</span></li>
                        <li><b>Baía de Todos-os-Santos</b><span>A baía que conecta Salvador ao Recôncavo e ao mar aberto.</span></li>
                        <li><b>Baía do Iguape</b><span>Reserva Extrativista Marinha, com cerca de 14 comunidades quilombolas, pesca, mariscagem e cultivo de ostras.</span></li>
                        <li><b>Recôncavo Baiano</b><span>Cachoeira e comunidades do entorno, onde está o Time Real São Francisco.</span></li>
                        <li><b>Litoral da Bahia</b><span>Onde levamos experiências imersivas e ações de Cultura Oceânica.</span></li>
                    </ul>
                </div>
                <div class="mapa-wrap" data-aos="fade-left">
                    {MAPA}
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="historias">
        <div class="container">
            {sec_head("Histórias de impacto", "Por trás de cada número, existem pessoas.")}
            <div class="historias">
{historias_html(HISTORIAS)}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="acoes-sociais.html" class="btn btn-primary">Ver as ações na Baía do Iguape <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>
""" + cta_final("rsf-2") + FOOTER

# =====================================================================
# MARUJADA GAIA SOUL
# =====================================================================
valores_html = "".join(
    f'<button type="button" class="tier{" on" if i == 1 else ""}" data-valor="{v}">R$ {v}<small>/ mês</small></button>'
    for i, v in enumerate(MARUJADA_VALORES)) + '<button type="button" class="tier" data-valor="outro">Outro valor</button>'

marujada = head("Marujada Gaia Soul | Todo mundo a bordo por um oceano mais vivo",
                "Faça parte da Marujada Gaia Soul: apoio mensal, doação, apoio de empresas (Lei Rouanet, patrocínio, ESG, investimento social privado) e voluntariado.",
                "marujada.html", "veleiro-gaia") + f"""
    <section class="page-hero v3 marujada-hero">
        <div class="bg" style="background-image:url('{IMG}/veleiro-gaia.webp')"></div>
        <div class="veil"></div>
        {ROSA}
        <div class="container" data-aos="fade-up">
            <span class="eyebrow">Marujada Gaia Soul</span>
            <h1 class="h-page">Todo mundo a bordo por um oceano mais vivo.</h1>
            <p class="page-lead">A Marujada Gaia Soul é formada por pessoas, empresas e organizações que escolheram navegar com a gente.</p>
            <p class="page-lead">Cada contribuição ajuda o Instituto Gaia Soul a ampliar seus projetos, levar a Cultura Oceânica a mais pessoas e criar experiências que aproximam sociedade e oceano.</p>
            <p class="page-lead">Mais do que apoiar uma instituição, fazer parte da Marujada é embarcar em um movimento de conexão, conhecimento e transformação.</p>
            <a href="#embarque" class="btn btn-light">Embarque nessa maré</a>
            <p class="crumb"><a href="index.html">Início</a> / Marujada Gaia Soul</p>
        </div>
    </section>

    <section class="v2-section wave" id="contribuicao">
        <div class="container">
            {sec_head("Sua contribuição nos leva mais longe", "Quando você apoia o Gaia Soul, ajuda a...")}
            <div class="ajuda-grid">
                <div class="ajuda" data-aos="fade-up"><i class="fas fa-child"></i><h3>Levar Cultura Oceânica a crianças e jovens</h3><p>Apoiar ações educativas, materiais e experiências que aproximam estudantes do oceano.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="80"><i class="fas fa-vr-cardboard"></i><h3>Criar experiências transformadoras</h3><p>Viabilizar atividades educativas, culturais, imersivas e de sensibilização.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="160"><i class="fas fa-map-marked-alt"></i><h3>Ampliar nosso impacto</h3><p>Permitir que nossos projetos cheguem a novas escolas, comunidades e territórios.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="240"><i class="fas fa-compass"></i><h3>Manter o Instituto navegando</h3><p>Fortalecer a estrutura necessária para planejar, executar, monitorar e ampliar nossos projetos.</p></div>
            </div>
            <p class="fecho" data-aos="fade-up">Cada contribuição movimenta essa maré.</p>
        </div>
    </section>

    <section class="marujada-sec wave" id="embarque">
        {ROSA}
        <div class="container">
            <div class="marujada-head" data-aos="fade-up">
                <span class="eyebrow">Escolha o seu caminho</span>
                <h2 class="h-sec light">Como você quer embarcar?</h2>
            </div>
            <div class="caminhos">
                <a href="#fazer-parte" class="caminho" data-aos="fade-up"><span class="ic"><i class="fas fa-anchor"></i></span><small>Quero apoiar como pessoa</small><h3>Faça parte da Marujada</h3><p>Contribua de forma recorrente e faça parte da comunidade que mantém nossos projetos navegando.</p><span class="btn btn-light">Quero ser da Marujada</span></a>
                <a href="#doacao" class="caminho" data-aos="fade-up" data-aos-delay="80"><span class="ic"><i class="fas fa-water"></i></span><small>Quero contribuir agora</small><h3>Faça uma doação</h3><p>Uma contribuição pontual também pode fazer muita diferença.</p><span class="chips">PIX • Transferência • Doação online</span><span class="btn btn-light">Quero doar</span></a>
                <a href="#empresas" class="caminho" data-aos="fade-up" data-aos-delay="160"><span class="ic"><i class="fas fa-ship"></i></span><small>Quero apoiar como empresa</small><h3>Sua empresa a bordo</h3><p>Empresas podem navegar conosco por meio de patrocínios, projetos incentivados, investimento social privado, ações ESG e parcerias institucionais.</p><span class="btn btn-light">Embarque sua empresa</span></a>
                <a href="#voluntariado" class="caminho" data-aos="fade-up" data-aos-delay="240"><span class="ic"><i class="fas fa-hands-helping"></i></span><small>Quero ser voluntário</small><h3>Doe seu tempo</h3><p>Conhecimento, experiência e disponibilidade também podem transformar.</p><span class="btn btn-light">Quero ser voluntário</span></a>
            </div>
        </div>
    </section>

    <section class="v2-section wave" id="fazer-parte">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Faça parte da Marujada</span>
                    <h2 class="h-sec">Uma contribuição que mantém essa maré em movimento.</h2>
                    <p class="v2-lead">Ao entrar para a Marujada Gaia Soul, você passa a fazer parte de uma comunidade que acredita no poder do oceano para educar, conectar e transformar.</p>
                    <p class="v2-lead">Escolha uma contribuição mensal e navegue conosco.</p>
                </div>
                <form class="form-v2 marujada-form js-lead" data-assunto="Quero entrar para a Marujada (apoio mensal)" data-ok="Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar e a nossa equipe te passa os próximos passos." data-aos="fade-left">
                    <div class="tiers" role="radiogroup" aria-label="Valor mensal">{valores_html}</div>
                    <input type="hidden" name="valor" value="{MARUJADA_VALORES[1]}">
                    <div class="outro-valor" hidden><label for="m-outro">Outro valor (R$ por mês)</label><input id="m-outro" name="outro" inputmode="numeric" placeholder="Ex.: 50"></div>
                    <div class="row">
                        <div><label for="m-nome">Nome</label><input id="m-nome" name="nome" required></div>
                        <div><label for="m-tel">WhatsApp</label><input id="m-tel" name="telefone" type="tel" required></div>
                    </div>
                    <div><label for="m-email">E-mail</label><input id="m-email" name="email" type="email"></div>
                    <label class="chk"><input type="checkbox" name="lgpd" required> <span>Concordo com a <a href="politica-de-privacidade.html" target="_blank">Política de Privacidade</a>.</span></label>
                    <button type="submit" class="btn btn-primary">Entrar para a Marujada</button>
                    <div class="form-ok"></div>
                </form>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="acompanhe">
        <div class="container">
            {sec_head("Quem está na Marujada acompanha a viagem", "O maior benefício é pertencer.", "Fazer parte da Marujada é acompanhar de perto o impacto que você ajudou a gerar.")}
            <div class="ajuda-grid">
                <div class="ajuda" data-aos="fade-up"><i class="fas fa-bullhorn"></i><h3>Notícias de bordo</h3><p>Receba novidades sobre projetos, conquistas e próximos destinos.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="80"><i class="fas fa-book"></i><h3>Diário de Bordo</h3><p>Acompanhe periodicamente o que estamos realizando e os impactos gerados.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="160"><i class="fas fa-users"></i><h3>Encontros da Marujada</h3><p>Convites para experiências, encontros e atividades especiais promovidas pelo Instituto, quando disponíveis.</p></div>
                <div class="ajuda" data-aos="fade-up" data-aos-delay="240"><i class="fas fa-fish"></i><h3>Conteúdos do oceano</h3><p>Receba conteúdos e histórias que aproximam você ainda mais do universo oceânico.</p></div>
            </div>
        </div>
    </section>

    <section class="v2-section wave" id="doacao">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Faça uma doação</span>
                    <h2 class="h-sec">Quero contribuir agora.</h2>
                    <p class="v2-lead">Uma contribuição pontual também pode fazer muita diferença. Você pode doar por <strong>PIX, transferência ou doação online</strong>.</p>
                    <div class="dados-doacao">
                        <div><small>Favorecido</small><b>{RAZAO}</b></div>
                        <div><small>CNPJ</small><b>{CNPJ}</b></div>
                    </div>
                </div>
                <form class="form-v2 js-lead" data-assunto="Quero fazer uma doação" data-ok="Abrimos o WhatsApp com a sua mensagem. Nossa equipe te envia os dados do PIX ou da transferência." data-aos="fade-left">
                    <div><label for="d-forma">Como você quer doar?</label>
                        <select id="d-forma" name="forma"><option>PIX</option><option>Transferência</option><option>Doação online</option></select></div>
                    <div class="row">
                        <div><label for="d-nome">Nome</label><input id="d-nome" name="nome" required></div>
                        <div><label for="d-tel">WhatsApp</label><input id="d-tel" name="telefone" type="tel" required></div>
                    </div>
                    <div><label for="d-valor">Valor (opcional)</label><input id="d-valor" name="valor" inputmode="numeric" placeholder="R$"></div>
                    <label class="chk"><input type="checkbox" name="lgpd" required> <span>Concordo com a <a href="politica-de-privacidade.html" target="_blank">Política de Privacidade</a>.</span></label>
                    <button type="submit" class="btn btn-primary">Quero doar</button>
                    <div class="form-ok"></div>
                </form>
            </div>
        </div>
    </section>

    <section class="v2-section wave navy empresas" id="empresas">
        <div class="container">
            {sec_head("Empresas a bordo", "Sua empresa pode levar essa transformação ainda mais longe.", "Empresas e organizações são parte importante da nossa Marujada. Construímos parcerias que conectam os objetivos das organizações à atuação do Instituto em Cultura Oceânica, educação, inovação, tecnologia, bem-estar e desenvolvimento socioambiental.", light=True)}
            <p class="sub-light center" data-aos="fade-up">Existem diferentes maneiras de embarcar:</p>
            <div class="modalidades">
                <div class="mod" data-aos="fade-up"><i class="fas fa-landmark"></i><h3>Projetos incentivados / Lei Rouanet</h3><p>Apoie projetos culturais do Gaia Soul por meio dos mecanismos de incentivo aplicáveis.</p></div>
                <div class="mod" data-aos="fade-up" data-aos-delay="60"><i class="fas fa-award"></i><h3>Patrocínio</h3><p>Associe sua marca a projetos e experiências com propósito.</p></div>
                <div class="mod" data-aos="fade-up" data-aos-delay="120"><i class="fas fa-hand-holding-heart"></i><h3>Investimento Social Privado</h3><p>Invista em iniciativas de impacto alinhadas às estratégias sociais e territoriais da organização.</p></div>
                <div class="mod" data-aos="fade-up"><i class="fas fa-leaf"></i><h3>ESG</h3><p>Construa conosco projetos relacionados a oceano, educação, comunidades e sustentabilidade.</p></div>
                <div class="mod" data-aos="fade-up" data-aos-delay="60"><i class="fas fa-briefcase"></i><h3>Programas Corporativos</h3><p>Leve Cultura Oceânica, experiências imersivas, Oceanoterapia e bem-estar para colaboradores e públicos de relacionamento.</p></div>
                <div class="mod" data-aos="fade-up" data-aos-delay="120"><i class="fas fa-hands"></i><h3>Apoio Institucional</h3><p>Contribua diretamente para o fortalecimento e expansão da atuação do Instituto.</p></div>
            </div>
            <div class="btns center" data-aos="fade-up"><a href="#captacao" class="btn btn-light">Conheça os projetos em captação</a><a href="contato.html?assunto=Parcerias e patrocínios" class="btn btn-outline-light">Converse com o Gaia Soul</a></div>
        </div>
    </section>

    <section class="v2-section wave" id="captacao">
        <div class="container">
            {sec_head("Projetos esperando novos tripulantes", "Escolha onde você quer gerar impacto.")}
            <div class="perfil-toggle" role="group" aria-label="Quem vai apoiar" data-aos="fade-up">
                <button type="button" class="on" data-perfil="pf">Sou pessoa</button><button type="button" data-perfil="pj">Sou empresa</button>
            </div>
            <div class="capt-grid">
{captacao_html()}
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="voluntariado">
        <div class="container">
            {sec_head("Outras formas de fazer parte", "Apoio não é só dinheiro.")}
            <div class="ajuda-grid">
                <a href="#voluntario-form" class="ajuda link" data-aos="fade-up"><i class="fas fa-hands-helping"></i><h3>Seja voluntário</h3><p>Doe tempo e conhecimento.</p></a>
                <a href="{IG}" target="_blank" rel="noopener" class="ajuda link" data-aos="fade-up" data-aos-delay="80"><i class="fas fa-share-alt"></i><h3>Compartilhe nossa causa</h3><p>Ajude a Cultura Oceânica a chegar mais longe.</p></a>
                <a href="contato.html?assunto=Outros assuntos" class="ajuda link" data-aos="fade-up" data-aos-delay="160"><i class="fas fa-shopping-bag"></i><h3>Compre com propósito</h3><p>Conheça os produtos Gaia Soul.</p></a>
                <a href="contato.html?assunto=Experiências" class="ajuda link" data-aos="fade-up" data-aos-delay="240"><i class="fas fa-school"></i><h3>Leve nossos projetos até você</h3><p>Escolas, empresas, eventos e instituições podem receber nossas experiências.</p></a>
            </div>
            <form class="form-v2 volunt-form js-lead" id="voluntario-form" data-assunto="Quero ser voluntário" data-ok="Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar." data-aos="fade-up">
                <h3>Quero ser voluntário</h3>
                <div class="row">
                    <div><label for="v-nome">Nome</label><input id="v-nome" name="nome" required></div>
                    <div><label for="v-tel">WhatsApp</label><input id="v-tel" name="telefone" type="tel" required></div>
                </div>
                <div><label for="v-area">Como você pode ajudar?</label><textarea id="v-area" name="mensagem" placeholder="Sua área, experiência e disponibilidade"></textarea></div>
                <label class="chk"><input type="checkbox" name="lgpd" required> <span>Concordo com a <a href="politica-de-privacidade.html" target="_blank">Política de Privacidade</a>.</span></label>
                <button type="submit" class="btn btn-primary">Quero ser voluntário</button>
                <div class="form-ok"></div>
            </form>
        </div>
    </section>

    <section class="v2-section wave transp" id="transparencia">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Transparência</span>
                    <h2 class="h-sec">Sua confiança também importa.</h2>
                    <p class="v2-lead">Acreditamos que cada pessoa ou organização que embarca conosco deve poder acompanhar como o Instituto atua e utiliza seus recursos.</p>
                    <p class="v2-lead">Por isso, disponibilizamos publicamente nossos documentos institucionais, governança, relatórios e prestações de contas.</p>
                    <a href="transparencia.html" class="btn btn-primary">Acesse nossa transparência</a>
                </div>
                <div data-aos="fade-left">{TRANSP_ATALHOS}</div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="a-bordo">
        <div class="container">
            {sec_head("Quem já está a bordo", "Essa Marujada já começou.")}
            {parceiros_html()}
        </div>
    </section>
""" + cta_final("veleiro-gaia", "O oceano é grande.<br>Nossa Marujada também pode ser.",
                "Cada pessoa que embarca fortalece nossa capacidade de levar conhecimento, experiências e Cultura Oceânica cada vez mais longe. Vem com a gente?",
                '<a href="#fazer-parte" class="btn btn-light">Quero fazer parte da Marujada</a>',
                '<a href="#empresas" class="btn btn-outline-light">Quero embarcar minha empresa</a>') + FOOTER

# =====================================================================
# TRANSPARÊNCIA
# =====================================================================
def doc_item(ico, titulo, txt):
    return f"""<div class="doc-item"><i class="fas {ico}"></i><div><b>{titulo}</b><span>{txt}</span></div>
                        <a href="mailto:{MAIL}?subject={titulo.replace(' ', '%20')}%20-%20Instituto%20Gaia%20Soul" class="doc-btn">Solicitar</a></div>"""


transparencia = head("Transparência | Instituto Gaia Soul",
                     "Governança, documentos institucionais, relatórios e prestação de contas do Instituto Gaia Soul.",
                     "transparencia.html") + page_hero(
    "hf-14-costa-bahia", "Responsabilidade", "Confiança também faz parte do nosso impacto.",
    "Acreditamos que toda transformação precisa ser construída com responsabilidade, integridade e transparência.", "Transparência") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="transp-grid">
                <div class="transp-card" id="governanca" data-aos="fade-up">
                    <span class="eyebrow">Governança</span>
                    <h2 class="h-sec sm">Quem somos, formalmente.</h2>
                    <dl class="ficha">
                        <div><dt>Razão social</dt><dd>{RAZAO}</dd></div>
                        <div><dt>CNPJ</dt><dd>{CNPJ}</dd></div>
                        <div><dt>Natureza</dt><dd>Associação sem fins lucrativos</dd></div>
                        <div><dt>Fundação</dt><dd>04/07/2019</dd></div>
                        <div><dt>Sede</dt><dd>{ENDERECO}</dd></div>
                        <div><dt>Presidente</dt><dd>Marcelo Telles</dd></div>
                        <div><dt>Reconhecimento</dt><dd>Utilidade Pública pela Prefeitura de Cachoeira (BA)</dd></div>
                    </dl>
                </div>
                <div class="transp-card" id="documentos" data-aos="fade-up" data-aos-delay="80">
                    <span class="eyebrow">Documentos Institucionais</span>
                    <h2 class="h-sec sm">Documentos da organização.</h2>
                    {doc_item("fa-file-contract", "Estatuto social", "Regras de funcionamento e finalidades do Instituto.")}
                    {doc_item("fa-id-card", "Cartão CNPJ", "Comprovante de inscrição e situação cadastral ativa.")}
                    {doc_item("fa-stamp", "Declaração de Utilidade Pública", "Reconhecimento da Prefeitura de Cachoeira (BA).")}
                </div>
                <div class="transp-card" id="relatorios" data-aos="fade-up">
                    <span class="eyebrow">Relatórios</span>
                    <h2 class="h-sec sm">Atividades e resultados.</h2>
                    {doc_item("fa-chart-line", "Relatório de atividades", "O que realizamos, onde e com quem.")}
                    {doc_item("fa-book-open", "Apresentação institucional", "Projetos, números e parceiros do Instituto.")}
                </div>
                <div class="transp-card" id="prestacao-de-contas" data-aos="fade-up" data-aos-delay="80">
                    <span class="eyebrow">Prestação de Contas</span>
                    <h2 class="h-sec sm">Como os recursos são utilizados.</h2>
                    {doc_item("fa-balance-scale", "Demonstrativos financeiros", "Entradas, saídas e aplicação dos recursos.")}
                    {doc_item("fa-handshake", "Prestação de contas de projetos", "Relatórios de projetos incentivados e parcerias.")}
                </div>
            </div>
            <p class="nota center" data-aos="fade-up">Os documentos são enviados mediante solicitação pelo e-mail <a href="mailto:{MAIL}">{MAIL}</a>. À medida que forem publicados, ficarão disponíveis para download nesta página.</p>
        </div>
    </section>
""" + cta_final("veleiro-gaia") + FOOTER

# =====================================================================
# DIÁRIO DE BORDO
# =====================================================================
diario = head("Diário de Bordo | Instituto Gaia Soul",
              "Projetos, notícias, ciência e oceano, bastidores e eventos do Instituto Gaia Soul.",
              "diario-de-bordo.html") + page_hero(
    "hf-03-mar-aereo", "Diário de Bordo", "Acompanhe nossa jornada.", "", "Diário de Bordo") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="diario-grid">
{diario_html(DIARIO)}
            </div>
            <div class="center" style="margin-top:2.6rem"><a href="{IG}" target="_blank" rel="noopener" class="btn btn-ghost"><i class="fab fa-instagram"></i> Acompanhe no Instagram</a></div>
        </div>
    </section>
""" + NEWSLETTER + FOOTER

# =====================================================================
# AÇÕES SOCIAIS (mantida, agora dentro de Atuação & Impacto)
# =====================================================================
_ACAO_N = [0]


def acao(anchor, titulo, texto, fotos, cls=None, extra_head=""):
    _ACAO_N[0] += 1
    alt = _ACAO_N[0] % 2 == 1
    n = len(fotos)
    fotos = [f[:2] for f in fotos]
    if n == 5:
        fotos[0] = fotos[0] + ("wide",)
    cls = {2: "g2", 3: "g3", 4: "g4", 5: "g3"}.get(n, "g3")
    return f"""
    <section class="action wave{' alt' if alt else ''}" id="{anchor}">
        <div class="container">
            <div class="head" data-aos="fade-up"><div><h3>{titulo}</h3>{f'<p class="v2-lead" style="margin:.6rem 0 0">{texto}</p>' if texto else ''}</div>{extra_head}</div>
            {gal(fotos, cls)}
        </div>
    </section>"""


acoes = head("Ações Sociais na Baía do Iguape | Instituto Gaia Soul",
             "Ações sociais do Instituto Gaia Soul na Reserva Extrativista Marinha Baía do Iguape (BA): esporte, regatas, apoio a 650 famílias de pescadores e marisqueiras. Utilidade Pública pela Prefeitura de Cachoeira.",
             "acoes-sociais.html", "baia-iguape-aerea") + page_hero(
    "hf-14-costa-bahia", "Atuação & Impacto", "Ações na Baía do Iguape.",
    "Conectando pessoas. Transformando comunidades.", '<a href="atuacao-e-impacto.html">Atuação & Impacto</a> / Ações na Baía do Iguape') + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Territórios & Regeneração</span>
                    <h2 class="h-sec">Reserva Extrativista Marinha Baía do Iguape.</h2>
                    <div class="two-cols-text">
                        <p class="v2-lead">Unidade de conservação federal criada em 2000 para <strong>proteger o ecossistema local</strong> e <strong>garantir a subsistência de comunidades tradicionais</strong>.</p>
                        <p class="v2-lead">Cerca de 14 <strong>comunidades quilombolas</strong> formam um <strong>território tradicional de pesca, mariscagem e cultivo de ostras.</strong></p>
                    </div>
                    <div class="selo">
                        <img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública">
                        <div class="t"><small>Reconhecimento de</small><b>Utilidade pública</b><small>Prefeitura de Cachoeira - BA</small></div>
                    </div>
                </div>
                <div data-aos="zoom-in">
                    <div class="circle-img social-hero-img"><img src="{IMG}/baia-iguape-aerea.webp" alt="Vista aérea da Baía do Iguape e Barra do Paraguaçu" loading="lazy"></div>
                    <div class="pill-row" style="justify-content:center"><span class="pill teal">Reserva Extrativista Marinha Baía do Iguape</span><span class="pill teal">Barra do Paraguaçu</span></div>
                </div>
            </div>
        </div>
    </section>
""" + acao("time-real-sao-francisco", "Time Real São Francisco",
           "<strong>O time Real São Francisco conta com 60 jovens de 12 a 17 anos.</strong> Contribuímos com treinador, uniformes para os jogos, bolas, lanche dos atletas, entre outras ações. <strong>Chegamos ao vice-campeonato em 2025.</strong>",
           [("rsf-1", "Time Real São Francisco no Campeonato Cachoeirano 2026"), ("rsf-2", "Time com a bandeira do Instituto Gaia Soul"), ("rsf-4", "Times perfilados antes do jogo"), ("rsf-3", "Treino do time Real São Francisco")],
           extra_head=f'<img class="crest" src="{LOGO}/real-sao-francisco.png" alt="Esporte Clube Real São Francisco">') \
    + acao("bordejos", "Bordejos e regatas de canoas", "",
           [("bordejo-3", "Canoas a vela na praia"), ("bordejo-premiacao", "Premiação do Grande Bordejo"), ("bordejo-1", "Regata de canoas na baía"), ("bordejo-2", "Canoa a vela ao pôr do sol")]) \
    + acao("familias", "650 famílias de pescadores e marisqueiras",
           "Contribuímos em datas festivas: Natal, Dia das Mães, Dia dos Pais e Dia das Crianças. No Dia das Crianças, levamos <strong>educação ambiental e doação de chocolates</strong> para as escolas.",
           [("escola-1", "Dia das Crianças com educação ambiental na escola"), ("escola-2", "Doações preparadas para o Dia das Crianças", "tall"), ("escola-3", "Crianças da escola com a equipe do Instituto")]) \
    + acao("dia-das-maes", "Dia das Mães", "",
           [("maes-3", "Entrega de presentes no Dia das Mães"), ("maes-4", "Presentes para as mães"), ("maes-2", "Mesa de presentes"), ("maes-1", "Mães reunidas na comemoração"), ("maes-5", "Mesa do Instituto Gaia Soul")]) \
    + acao("convenio", "Convênio com a Associação dos Pescadores e Marisqueiras de Cachoeira",
           "Convênio de Cooperação com a Associação dos Pescadores e Marisqueiras de Cachoeira.",
           [("pescadores-3", "Confraternização das marisqueiras na praia"), ("pescadores-4", "Entrega de kits no Sindicato de Pescadores"), ("pescadores-1", "Pescadores e marisqueiras com as doações"), ("pescadores-5", "Presentes para as famílias"), ("pescadores-2", "Mesa de lanche do Instituto")]) \
    + acao("dia-das-criancas", "Dia das Crianças",
           "Entrega de brinquedos para as crianças das comunidades.",
           [("brinquedos-1", "Crianças com os brinquedos recebidos"), ("brinquedos-2", "Crianças escolhendo brinquedos"), ("brinquedos-4", "Criança com brinquedo novo"), ("brinquedos-3", "Brinquedos arrecadados para a doação")]) \
    + acao("prefeitura", "Apresentação do projeto à Prefeitura de Cachoeira - BA", "",
           [("prefeitura-1", "Apresentação com óculos de realidade virtual na Prefeitura"), ("prefeitura-2", "Experiência de realidade virtual na Prefeitura")], "g2") \
    + cta_final("rsf-2", "Junte-se a esse movimento.",
                "Vamos conectar pessoas ao oceano, transformar comunidades e construir um futuro mais sustentável.") + FOOTER

# =====================================================================
# CONTATO
# =====================================================================
ASSUNTOS = ["Parcerias e patrocínios", "Projetos", "Escolas", "Experiências", "Marujada", "Imprensa", "Outros assuntos"]
contato = head("Contato | Instituto Gaia Soul",
               f"Fale com o Instituto Gaia Soul: parcerias e patrocínios, projetos, escolas, experiências, Marujada e imprensa. WhatsApp {TEL}, e-mail {MAIL}.",
               "contato.html") + page_hero(
    "hf-14-costa-bahia", "Contato", "Vamos conversar?", "Conte para a gente como quer navegar com o Instituto Gaia Soul.", "Contato") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Fale com o Gaia Soul</span>
                    <h2 class="h-sec">Sobre o que você quer falar?</h2>
                    <div class="assuntos">{''.join(f'<button type="button" class="assunto" data-assunto="{a}">{a}</button>' for a in ASSUNTOS)}</div>
                    <div class="contact-box">
                        <a href="{WA}" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> {TEL}</a>
                        <a href="mailto:{MAIL}"><i class="far fa-envelope"></i> {MAIL}</a>
                        <a href="{IG}" target="_blank" rel="noopener"><i class="fab fa-instagram"></i> @institutogaiasoul</a>
                        <span><i class="fas fa-map-marker-alt"></i> {ENDERECO}</span>
                        <div class="soc-row">{social_html("")}</div>
                    </div>
                </div>
                <form class="form-v2 js-lead" id="form-contato" data-ok="Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar." data-aos="fade-left">
                    <div class="row">
                        <div><label for="f-nome">Nome</label><input id="f-nome" name="nome" required></div>
                        <div><label for="f-tel">WhatsApp</label><input id="f-tel" name="telefone" type="tel" required></div>
                    </div>
                    <div><label for="f-email">E-mail</label><input id="f-email" name="email" type="email"></div>
                    <div><label for="f-assunto">Assunto</label>
                        <select id="f-assunto" name="assunto">{''.join(f'<option>{a}</option>' for a in ASSUNTOS)}</select>
                    </div>
                    <div><label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem"></textarea></div>
                    <label class="chk"><input type="checkbox" name="lgpd" required> <span>Concordo com a <a href="politica-de-privacidade.html" target="_blank">Política de Privacidade</a>.</span></label>
                    <button type="submit" class="btn btn-primary"><i class="fab fa-whatsapp"></i> Enviar pelo WhatsApp</button>
                    <div class="form-ok"></div>
                </form>
            </div>
        </div>
    </section>
""" + FOOTER

# =====================================================================
# LEGAL
# =====================================================================
def legal_page(fname, title, h1, corpo):
    return head(f"{title} | Instituto Gaia Soul", f"{title} do Instituto Gaia Soul.", fname) + page_hero(
        "hf-03-mar-aereo", "Legal", h1, "", title) + f"""
    <section class="v2-section wave">
        <div class="container legal-txt">
{corpo}
            <p class="nota">Última atualização: setembro de 2026.</p>
        </div>
    </section>
""" + FOOTER


privacidade = legal_page("politica-de-privacidade.html", "Política de Privacidade", "Política de Privacidade.", f"""
            <p>Esta política explica como o <strong>{RAZAO}</strong> (CNPJ {CNPJ}), controlador dos dados, trata as informações pessoais de quem visita este site ou entra em contato conosco, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
            <h2>Quais dados coletamos</h2>
            <p>Somente os dados que você nos informa nos formulários: nome, telefone (WhatsApp), e-mail, valor ou forma de contribuição e a mensagem enviada.</p>
            <h2>Para que usamos</h2>
            <ul><li>Responder ao seu contato e dar andamento à sua contribuição, apoio ou voluntariado;</li><li>Enviar as Notícias de Bordo, quando você pedir para recebê-las;</li><li>Cumprir obrigações legais e de prestação de contas.</li></ul>
            <h2>Com quem compartilhamos</h2>
            <p>Não vendemos nem cedemos seus dados. Eles podem ser processados por ferramentas que usamos para comunicação (como WhatsApp e e-mail), apenas para as finalidades acima.</p>
            <h2 id="cookies">Cookies</h2>
            <p>Este site pode usar cookies técnicos e de medição de audiência para entender como as páginas são visitadas e melhorar a sua experiência. Você pode bloquear ou apagar os cookies nas configurações do seu navegador.</p>
            <h2 id="lgpd">Seus direitos (LGPD)</h2>
            <p>Você pode, a qualquer momento, pedir acesso, correção, anonimização, portabilidade ou exclusão dos seus dados, e revogar o consentimento para o recebimento de comunicações. Basta escrever para <a href="mailto:{MAIL}">{MAIL}</a>.</p>
            <h2>Por quanto tempo guardamos</h2>
            <p>Pelo tempo necessário para as finalidades descritas ou pelo prazo exigido em lei.</p>""")

termos = legal_page("termos-de-uso.html", "Termos de Uso", "Termos de Uso.", f"""
            <p>Ao usar este site, você concorda com estes termos. O site é mantido pelo <strong>{RAZAO}</strong> (CNPJ {CNPJ}).</p>
            <h2>Conteúdo</h2>
            <p>Textos, imagens, vídeos, marcas e materiais deste site pertencem ao Instituto Gaia Soul ou a seus parceiros e não podem ser reproduzidos para fins comerciais sem autorização. O compartilhamento com citação da fonte é bem-vindo.</p>
            <h2>Contribuições</h2>
            <p>As contribuições feitas ao Instituto são destinadas às suas finalidades estatutárias. Os dados para doação são sempre confirmados pela nossa equipe pelos canais oficiais listados neste site.</p>
            <h2>Links externos</h2>
            <p>Este site pode conter links para sites de terceiros, pelos quais o Instituto não se responsabiliza.</p>
            <h2>Contato</h2>
            <p>Dúvidas sobre estes termos: <a href="mailto:{MAIL}">{MAIL}</a>.</p>""")

# sobre.html antigo passa a apontar para O Instituto
REDIRECT = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>O Instituto | Instituto Gaia Soul</title>
<meta http-equiv="refresh" content="0; url=o-instituto.html"><link rel="canonical" href="https://institutogaiasoul.ong.br/o-instituto.html">
<meta name="robots" content="noindex"></head><body><p><a href="o-instituto.html">O Instituto</a></p></body></html>
"""

PAGES = [("index.html", index), ("o-instituto.html", instituto), ("projetos.html", projetos),
         ("atuacao-e-impacto.html", atuacao), ("marujada.html", marujada), ("transparencia.html", transparencia),
         ("diario-de-bordo.html", diario), ("acoes-sociais.html", acoes), ("contato.html", contato),
         ("politica-de-privacidade.html", privacidade), ("termos-de-uso.html", termos), ("sobre.html", REDIRECT)]

for nome, html in PAGES:
    (ROOT / nome).write_text(html, encoding="utf-8")
    print("ok", nome, len(html))
