#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas do site v2 do Instituto Gaia Soul a partir do Institucional (PDF).
Cabeçalho e rodapé compartilhados. Rodar: python3 _build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
IMG = "assets/images/v2"
LOGO = "assets/images/logos"
WA = "https://wa.me/557199972427"
MAIL = "contato@institutogaiasoul.ong.br"
IG = "https://instagram.com/institutogaiasoul"

SOCIAL = [
    ("https://instagram.com/institutogaiasoul", "fab fa-instagram", "Instagram"),
    ("https://www.facebook.com/p/Instituto-Gaia-Soul-61552657763845/", "fab fa-facebook-f", "Facebook"),
    ("https://www.youtube.com/@InstitutoGaiaSoul", "fab fa-youtube", "YouTube"),
    ("https://www.tiktok.com/@institutogaiasoul", "fab fa-tiktok", "TikTok"),
    ("https://www.linkedin.com/company/instituto-gaia-soul/", "fab fa-linkedin-in", "LinkedIn"),
    ("https://br.pinterest.com/institutogaiasoul/", "fab fa-pinterest-p", "Pinterest"),
    ("https://share.google/oN9QCGZIFGdvhcymP", "fab fa-google", "Google"),
]


def social_html(cls):
    return "".join(f'<a href="{u}" target="_blank" rel="noopener" class="{cls}" aria-label="{n}" title="{n}"><i class="{i}"></i></a>' for u, i, n in SOCIAL)


NAV = [("index.html", "Início"), ("sobre.html", "Sobre"), ("projetos.html", "Projetos"),
       ("acoes-sociais.html", "Ações Sociais"), ("contato.html", "Contato")]


def head(title, desc, page):
    links = "\n".join(
        f'                        <li><a href="{h}" class="nav-link{" active" if h == page else ""}">{t}</a></li>'
        for h, t in NAV)
    dark = "" if page == "index.html" else " header-dark"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="{IMG}/hf-01-hero-baia.webp">
    <meta property="og:locale" content="pt_BR">
    <link rel="icon" type="image/png" href="{LOGO}/gaia-soul-oficial.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Allura&family=Urbanist:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/styles.css">
    <link rel="stylesheet" href="assets/css/pages.css">
    <link rel="stylesheet" href="assets/css/v2.css">
</head>
<body>
    <header class="header{dark}" id="header">
        <div class="container">
            <nav class="nav">
                <a href="index.html" class="logo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
                <div class="nav-menu" id="nav-menu">
                    <ul class="nav-list">
{links}
                    </ul>
                </div>
                <div class="nav-actions">
                    <div class="social-icons">
                        {social_html("social-icon")}
                    </div>
                    <button class="nav-toggle" id="nav-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
                </div>
            </nav>
        </div>
    </header>
"""


def page_hero(img, script, main, crumb):
    return f"""
    <section class="page-hero">
        <div class="bg" style="background-image:url('{IMG}/{img}.webp')"></div>
        <div class="veil"></div>
        <div class="container" data-aos="fade-up">
            <h1 class="v2-title light"><span class="script">{script}</span><span class="main">{main}</span></h1>
            <p class="crumb"><a href="index.html">Início</a> / {crumb}</p>
        </div>
    </section>
"""


FOOTER = f"""
    <footer class="footer wave">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <a href="index.html" class="footer-logo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
                    <p>Informar, sensibilizar e engajar as pessoas para a Cultura Oceânica e a difusão da OceanoTerapia. Só cuidamos do que conhecemos.</p>
                    <div class="footer-social">{social_html("")}</div>
                </div>
                <div class="footer-links">
                    <h4>Navegação</h4>
                    <ul>
                        <li><a href="index.html">Início</a></li>
                        <li><a href="sobre.html">Sobre</a></li>
                        <li><a href="projetos.html">Projetos</a></li>
                        <li><a href="acoes-sociais.html">Ações Sociais</a></li>
                        <li><a href="contato.html">Contato</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Contato</h4>
                    <ul>
                        <li><i class="fab fa-whatsapp"></i> <a href="{WA}" target="_blank" rel="noopener">(71) 9997-2427</a></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:{MAIL}">{MAIL}</a></li>
                        <li><i class="fab fa-instagram"></i> <a href="{IG}" target="_blank" rel="noopener">@institutogaiasoul</a></li>
                        <li><i class="fas fa-map-marker-alt"></i> Bahia · Salvador e Baía do Iguape</li>
                    </ul>
                </div>
                <div class="footer-newsletter">
                    <h4>Apoio institucional</h4>
                    <p>UNESCO · Década do Oceano 2021-2030 · Fundação Aleixo Belov · Associação Brasileira de Oceanografia · Escola Azul Brasil</p>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                <p>&copy; 2026 Gaia Soul Instituto de Proteção e Educação Ambiental · CNPJ 34.941.993/0001-18</p>
            </div>
        </div>
    </footer>

    <a href="#" class="back-to-top" id="back-to-top" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></a>
    <a href="{WA}" class="whatsapp-button" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fab fa-whatsapp"></i></a>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>
"""

# ---------- blocos reutilizados ----------
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

SVG_ESTRELA = '<svg viewBox="0 0 64 64"><path d="M22 10l4 9 10 1-7 7 2 10-9-5-9 5 2-10-7-7 10-1z"/><path d="M40 30c6-8 18-6 18 4s-8 16-18 18"/><path d="M44 36l6-2M46 42l7 1M44 47l5 4"/><path d="M36 50l3 7 7 1-5 5"/></svg>'
SVG_ONDA = '<svg viewBox="0 0 64 64"><path d="M6 40c8 0 10-6 16-6s8 6 16 6 10-6 16-6"/><path d="M6 50c8 0 10-6 16-6s8 6 16 6 10-6 16-6"/><path d="M20 30c0-10 8-18 18-18 6 0 10 4 10 9 0 4-3 7-7 7-3 0-5-2-5-5"/></svg>'
SVG_BARCO = '<svg viewBox="0 0 64 64"><path d="M32 8v36"/><path d="M32 10l18 30H32"/><path d="M30 16L16 40h14"/><path d="M10 46h44l-6 8H16z"/><path d="M6 58c6 0 7-3 13-3s7 3 13 3 7-3 13-3 7 3 13 3"/></svg>'

MVV = f"""
                <div class="mvv">
                    <div class="mvv-item" data-aos="fade-left">
                        <div class="ico">{SVG_ESTRELA}</div>
                        <div><h3>Missão</h3><p>Informar, sensibilizar e engajar as pessoas para a Cultura Oceânica e a difusão da OceanoTerapia!</p></div>
                    </div>
                    <div class="mvv-item" data-aos="fade-left" data-aos-delay="100">
                        <div class="ico">{SVG_ONDA}</div>
                        <div><h3>Visão</h3><p>Sensibilizar, até 2030, a consciência ecológica de pelo menos 100 mil pessoas, através de nossos conteúdos, projetos e iniciativas sociais.</p></div>
                    </div>
                    <div class="mvv-item" data-aos="fade-left" data-aos-delay="200">
                        <div class="ico">{SVG_BARCO}</div>
                        <div><h3>Valores</h3><ul><li>Ética</li><li>Respeito</li><li>Transparência</li><li>Conscientização</li><li>Preservação</li></ul></div>
                    </div>
                </div>"""

def next_page(href, img, script, main):
    return f"""
    <section class="v2-section wave" style="padding-top:60px">
        <div class="container">
            <a href="{href}" class="next-page" data-aos="fade-up">
                <div class="bg" style="background-image:url('{IMG}/{img}.webp')"></div>
                <div><span class="eyebrow">Próxima página</span><h2 class="v2-title light"><span class="script">{script}</span><span class="main">{main}</span></h2></div>
                <span class="arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
        </div>
    </section>
"""


PROJETOS = [
    ("imersao-azul", "hf-04-imersao-azul-vr", "Cultura oceânica nas escolas", "Imersão Azul",
     "Plataforma educacional com 11 livros didáticos, realidade virtual e jornada gamificada, alinhada à BNCC e à Década do Oceano."),
    ("submarino-imersivo", "submarino-1", "Uma viagem ao fundo do mar", "Submarino Imersivo",
     "Uma expedição pelas profundezas do oceano por meio da realidade virtual, dentro de uma estrutura que simula um submarino."),
    ("imersao-polar", "hf-06-polar-geleira", "Uma missão congelante", "Imersão Polar",
     "Expedição científica ao Ártico que transforma imagens terrestres e subaquáticas em conteúdos didáticos sobre as mudanças climáticas."),
    ("mundo-submarino-360", "hf-09-360-aeroporto", "Uma viagem ao fundo do mar", "Mundo Submarino 360°",
     "Experiências educacionais imersivas em aeroportos e shopping centers, com recursos audiovisuais de ponta."),
    ("oceanoterapia", "hf-12-oceanoterapia", "Conectar pessoas ao oceano", "OceanoTerapia®",
     "A conexão consciente com o oceano como ferramenta para promover bem-estar, saúde integral e consciência ambiental."),
    ("mare-de-campeoes", "mare-time", "Esporte e transformação social", "Maré de Campeões",
     "O esporte como ferramenta de inclusão social e porta de entrada para a Cultura Oceânica na Baía do Iguape e em Salvador."),
]
CARDS = "\n".join(f"""                <a href="projetos.html#{slug}" class="proj-card" data-aos="fade-up" data-aos-delay="{(i % 3) * 80}">
                    <div class="ph"><img src="{IMG}/{img}.webp" alt="{nome}" loading="lazy"></div>
                    <div class="bd"><span class="tag">projeto</span><h3>{nome}</h3><p>{txt}</p><span class="more">Conhecer o projeto <i class="fas fa-arrow-right"></i></span></div>
                </a>""" for i, (slug, img, _, nome, txt) in enumerate(PROJETOS))

PARCEIROS = f"""
            <div class="partners-v2">
                <div class="partner-box" data-aos="zoom-in"><img src="{LOGO}/unesco.png" alt="UNESCO"></div>
                <div class="partner-box" data-aos="zoom-in" data-aos-delay="80"><img src="{LOGO}/aleixo-belov.png" alt="Fundação Aleixo Belov"></div>
                <div class="partner-box" data-aos="zoom-in" data-aos-delay="160"><img src="{LOGO}/aoceano.png" alt="Associação Brasileira de Oceanografia"></div>
                <div class="partner-box" data-aos="zoom-in" data-aos-delay="240"><img src="{LOGO}/escola-azul.png" alt="Escola Azul Brasil"></div>
            </div>"""

CONTATO_BOX = f"""
                    <div class="contact-box">
                        <a href="https://institutogaiasoul.ong.br"><i class="fas fa-globe"></i> www.institutogaiasoul.ong.br</a>
                        <a href="{IG}" target="_blank" rel="noopener"><i class="fab fa-instagram"></i> @institutogaiasoul</a>
                        <a href="mailto:{MAIL}"><i class="far fa-envelope"></i> {MAIL}</a>
                        <a href="{WA}" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i> (71) 9997-2427</a>
                        <div class="soc-row">{social_html("")}</div>
                    </div>"""

# ================= HOME =================
index = head("Instituto Gaia Soul | Cultura Oceânica e OceanoTerapia",
             "O Instituto Gaia Soul aproxima pessoas do oceano por meio da educação, ciência, inovação e experiências transformadoras. Projetos Imersão Azul, Submarino Imersivo, OceanoTerapia e ações sociais na Baía do Iguape (BA).",
             "index.html") + f"""
    <section class="v2-hero" id="home">
        <div class="bg" style="background-image:url('{IMG}/hf-01-hero-baia.webp')"></div>
        <div class="veil"></div>
        <span class="bubble b1"></span><span class="bubble b2"></span><span class="bubble b3"></span>
        <a href="#sobre" class="scroll-hint" aria-label="Rolar"><i class="fas fa-chevron-down"></i></a>
        <div class="inner" data-aos="fade-up" data-aos-duration="1100">
            <img class="hero-logo" src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul">
            <h1>Informar, Sensibilizar e Engajar as pessoas para a Cultura Oceânica e difusão da OceanoTerapia!</h1>
            <span class="motto">Só cuidamos do que conhecemos</span>
            <div class="hero-buttons">
                <a href="projetos.html" class="btn btn-light">Conheça os projetos</a>
                <a href="contato.html" class="btn btn-outline">Fale conosco</a>
            </div>
        </div>
    </section>

    <section class="numbers-float">
        <div class="container">
            <div class="numbers">
                <div class="num-card" data-aos="fade-up"><b>11</b><span>livros didáticos autorais de Cultura Oceânica</span></div>
                <div class="num-card" data-aos="fade-up" data-aos-delay="80"><b>14</b><span>comunidades quilombolas na Baía do Iguape</span></div>
                <div class="num-card" data-aos="fade-up" data-aos-delay="160"><b>60</b><span>jovens de 12 a 17 anos no Real São Francisco</span></div>
                <div class="num-card" data-aos="fade-up" data-aos-delay="240"><b>650</b><span>famílias de pescadores e marisqueiras apoiadas</span></div>
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
                        <img class="tall" src="{LOGO}/decada-oceano.png" alt="Década das Nações Unidas da Ciência Oceânica para o Desenvolvimento Sustentável 2021-2030">
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

    <section class="v2-section wave deco" id="sobre">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="eyebrow">Desde 2019</span>
                    <h2 class="v2-title"><span class="script">quem</span><span class="main">somos</span></h2>
                    <p class="v2-lead">O Instituto Gaia Soul nasceu em 2019 com o propósito de <strong>aproximar pessoas ao oceano</strong> por meio da <strong>educação, ciência, inovação e experiências transformadoras</strong>.</p>
                    <p class="v2-lead">Acreditamos que só cuidamos do que conhecemos.</p>
                    <a href="sobre.html" class="btn btn-primary">Conheça nossa história</a>
                </div>
                <div class="rimg" style="aspect-ratio:4/3" data-aos="fade-left"><img src="{IMG}/loja-gaia-soul.webp" alt="Espaço do Instituto Gaia Soul" loading="lazy"></div>
            </div>
        </div>
    </section>


    <section class="v2-section wave" id="projetos">
        <div class="container">
            <div class="center" data-aos="fade-up">
                <span class="eyebrow">O que fazemos</span>
                <h2 class="v2-title"><span class="script">nossos</span><span class="main">projetos</span></h2>
                <p class="v2-lead">Um ecossistema integrado, onde cada projeto se conecta para amplificar nosso impacto na sociedade e no meio ambiente.</p>
            </div>
            <div class="proj-grid bento">
{CARDS}
            </div>
        </div>
    </section>

    <section class="v2-section wave mist">
        <div class="container">
            <div class="grid-2 wide-left">
                <div class="video-card" data-aos="fade-right">
                    <iframe src="https://www.youtube-nocookie.com/embed/axZOpjMf4V8?rel=0" title="O oceano regula o clima" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                </div>
                <div data-aos="fade-left">
                    <span class="eyebrow">Assista</span>
                    <h2 class="v2-title"><span class="script">por que</span><span class="main">o oceano</span></h2>
                    <p class="v2-lead">O oceano regula o clima, produz boa parte do oxigênio que respiramos e sustenta comunidades inteiras. Conhecer é o primeiro passo para cuidar.</p>
                    <a href="https://www.youtube.com/watch?v=axZOpjMf4V8" target="_blank" rel="noopener" class="btn btn-ghost"><i class="fab fa-youtube"></i> Assistir no YouTube</a>
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave flip deco left">
        <div class="container">
            <div class="social-band">
                <div class="circle-img" data-aos="zoom-in"><img src="{IMG}/baia-iguape-aerea.webp" alt="Reserva Extrativista Marinha Baía do Iguape" loading="lazy"></div>
                <div data-aos="fade-left">
                    <span class="pill">Conectando pessoas. Transformando comunidades.</span>
                    <h2 class="v2-title" style="margin-top:1.4rem"><span class="script">ações sociais</span><span class="main">baía do iguape</span></h2>
                    <p class="v2-lead">Na Reserva Extrativista Marinha Baía do Iguape, cerca de <strong>14 comunidades quilombolas</strong> vivem da pesca, da mariscagem e do cultivo de ostras. É lá que o Instituto atua com esporte, educação e apoio às famílias.</p>
                    <div class="selo">
                        <img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública">
                        <div class="t"><small>Reconhecimento de</small><b>Utilidade pública</b><small>Prefeitura de Cachoeira - BA</small></div>
                    </div>
                    <a href="acoes-sociais.html" class="btn btn-primary" style="margin-top:1.6rem">Ver as ações sociais</a>
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mata">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <img class="logo-mq" src="{LOGO}/mata-quantica-clara.png" alt="Mata Quântica">
                    <h2 class="v2-title"><span class="script">conheça também</span><span class="main">Mata Quântica</span></h2>
                    <p class="v2-lead">Um refúgio na Mata Atlântica para quem busca reconexão com a natureza. Um projeto irmão do Instituto Gaia Soul, com a mesma essência de cuidado com o meio ambiente.</p>
                    <a href="https://mataquantica.com.br" target="_blank" rel="noopener" class="btn btn-light">Conhecer a Mata Quântica</a>
                </div>
                <div class="rimg" style="aspect-ratio:4/3" data-aos="fade-left"><img src="{IMG}/mata-floresta.webp" alt="Mata Quântica na Mata Atlântica" loading="lazy"></div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist" id="ods">
        <div class="container">
            <div class="center" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">compromisso</span><span class="main">global</span></h2>
                <p class="v2-lead">Nossas ações contribuem para os Objetivos de Desenvolvimento Sustentável da ONU.</p>
            </div>
            <div class="ods-grid">
                <div class="ods-card" style="background:#4c9f38" data-aos="fade-up"><b>3</b><h4>Saúde e Bem-Estar</h4><p>A OceanoTerapia promove saúde integral pela conexão consciente com o mar.</p></div>
                <div class="ods-card" style="background:#c5192d" data-aos="fade-up" data-aos-delay="80"><b>4</b><h4>Educação de Qualidade</h4><p>A Cultura Oceânica chega às escolas com livros, realidade virtual e plataforma digital.</p></div>
                <div class="ods-card" style="background:#3f7e44" data-aos="fade-up" data-aos-delay="160"><b>13</b><h4>Ação Climática</h4><p>A Imersão Polar sensibiliza sobre as mudanças climáticas em curso.</p></div>
                <div class="ods-card" style="background:#0a97d9" data-aos="fade-up" data-aos-delay="240"><b>14</b><h4>Vida na Água</h4><p>Educação e engajamento pela conservação dos ecossistemas marinhos e costeiros.</p></div>
            </div>
        </div>
    </section>

    <section class="v2-section wave" id="parceiros">
        <div class="container">
            <div class="center" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">apoio</span><span class="main">institucional</span></h2>
            </div>
{PARCEIROS}
        </div>
    </section>

    <section class="v2-section wave mist" id="contato">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <h2 class="v2-title"><span class="script">proteger nossos oceanos</span><span class="main">para o futuro</span></h2>
                    <p class="v2-lead">O Instituto Gaia Soul atua como um ecossistema integrado, onde cada projeto se conecta para amplificar nosso impacto na sociedade e no meio ambiente.</p>
                    <p class="v2-lead"><strong>Junte-se a esse movimento.</strong></p>
                    <p class="v2-lead">Vamos conectar pessoas ao oceano, transformar comunidades e construir um futuro mais sustentável.</p>
{CONTATO_BOX}
                </div>
                <div data-aos="fade-left">
                    <div class="rimg" style="aspect-ratio:3/4"><img src="{IMG}/veleiro-gaia.webp" alt="Veleiro GAIA no mar" loading="lazy"></div>
                    <div class="cnpj">GAIA SOUL INSTITUTO DE PROTEÇÃO E EDUCAÇÃO AMBIENTAL · CNPJ 34.941.993/0001-18</div>
                </div>
            </div>
        </div>
    </section>
""" + FOOTER

# ================= SOBRE =================
sobre = head("Sobre | Instituto Gaia Soul",
             "Conheça o Instituto Gaia Soul: nascido em 2019 para aproximar pessoas ao oceano. Missão, visão, valores e os 7 princípios da Cultura Oceânica.",
             "sobre.html") + page_hero("hf-03-mar-aereo", "quem", "somos", "Sobre") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <h2 class="v2-title"><span class="script">nossa</span><span class="main">história</span></h2>
                    <p class="v2-lead">O Instituto Gaia Soul nasceu em 2019 com o propósito de <strong>aproximar pessoas ao oceano</strong> por meio da <strong>educação, ciência, inovação e experiências transformadoras</strong>.</p>
                    <p class="v2-lead">Acreditamos que só cuidamos do que conhecemos.</p>
                    <div class="rimg" style="aspect-ratio:4/3;margin-top:2rem"><img src="{IMG}/loja-gaia-soul.webp" alt="Espaço do Instituto Gaia Soul" loading="lazy"></div>
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
                    <h2 class="v2-title light"><span class="script">princípios</span><span class="main">cultura oceânica</span></h2>
                    <div class="big">70%</div>
                    <div class="big-sub">da superfície da Terra é <span>Oceano</span></div>
                    <div class="seals">
                        <div><p style="color:#cfe3ec;margin-bottom:.5rem">Apoio da</p><img src="{LOGO}/unesco.png" alt="UNESCO"></div>
                        <img class="tall" src="{LOGO}/decada-oceano.png" alt="Década das Nações Unidas da Ciência Oceânica 2021-2030">
                    </div>
                </div>
                <div data-aos="fade-left">
                    <ul class="principles">
{PRINC_HTML}
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="v2-section wave mist">
        <div class="container">
            <div class="grid-2 wide-left">
                <div class="video-card" data-aos="fade-right">
                    <iframe src="https://www.youtube-nocookie.com/embed/axZOpjMf4V8?rel=0" title="O oceano regula o clima" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                </div>
                <div data-aos="fade-left">
                    <h2 class="v2-title"><span class="script">apoio</span><span class="main">institucional</span></h2>
                    <p class="v2-lead">Trabalhamos ao lado de instituições que compartilham o compromisso com o oceano.</p>
                    <a href="projetos.html" class="btn btn-primary">Conheça os projetos</a>
                </div>
            </div>
            <div style="margin-top:3rem">{PARCEIROS}
            </div>
        </div>
    </section>
""" + next_page("projetos.html", "hf-09-360-aeroporto", "conheça os", "nossos projetos") + FOOTER

# ================= PROJETOS =================
def gal(items, cls="g3"):
    out = []
    for it in items:
        img, alt = it[0], it[1]
        extra = f" {it[2]}" if len(it) > 2 else ""
        out.append(f'<div class="rimg{extra}"><img src="{IMG}/{img}.webp" alt="{alt}" loading="lazy"></div>')
    return f'<div class="gallery {cls}" data-aos="fade-up">' + "".join(out) + "</div>"


projetos = head("Projetos | Instituto Gaia Soul",
                "Imersão Azul, Submarino Imersivo, Imersão Polar, Mundo Submarino 360°, OceanoTerapia e Maré de Campeões: os projetos do Instituto Gaia Soul.",
                "projetos.html") + page_hero("hf-05-submarino-vr", "nossos", "projetos", "Projetos") + f"""
    <nav class="proj-nav"><div class="container"><a href="#imersao-azul">Imersão Azul</a><a href="#submarino-imersivo">Submarino Imersivo</a><a href="#imersao-polar">Imersão Polar</a><a href="#mundo-submarino-360">Mundo Submarino 360°</a><a href="#oceanoterapia">OceanoTerapia®</a><a href="#mare-de-campeoes">Maré de Campeões</a></div></nav>

    <section class="project-block wave alt" id="imersao-azul">
        <span class="idx">01</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">imersão azul</span></h2>
                <div><span class="pill">Cultura oceânica nas escolas</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <img class="brand" src="{LOGO}/imersao-azul.png" alt="Imersão Azul" style="height:120px;margin-bottom:1.2rem">
                    <p class="v2-lead">O Imersão Azul é uma <strong>plataforma educacional que leva a Cultura Oceânica para as escolas</strong>, alinhada à BNCC e à Década do Oceano.</p>
                    <p class="v2-lead">Por meio de um ecossistema de aprendizagem que integra <strong>11 livros didáticos autorais</strong>, <strong>realidade virtual</strong>, plataforma digital e jornada gamificada, <strong>transforma conceitos científicos em experiências envolventes</strong>.</p>
                    <p class="v2-lead">Ao conectar estudantes ao oceano, o programa fortalece a <strong>consciência ambiental</strong>, <strong>estimula o protagonismo</strong> das novas gerações e <strong>prepara escolas para formar cidadãos comprometidos com a sustentabilidade e a Economia Azul Regenerativa.</strong></p>
                </div>
                <div class="stack" data-aos="fade-left">
                    <div class="rimg" style="aspect-ratio:16/10"><img src="{IMG}/hf-04-imersao-azul-vr.webp" alt="Estudantes com óculos de realidade virtual em sala de aula" loading="lazy"></div>
                    <div class="books">
                        <img src="{IMG}/livros-1.webp" alt="Livros Imersão Azul, 1º ao 5º ano" loading="lazy">
                        <img src="{IMG}/livros-2.webp" alt="Livros Imersão Azul, Ensino Médio" loading="lazy">
                        <img src="{IMG}/livros-3.webp" alt="Livros Imersão Azul, 3º ao 7º ano" loading="lazy">
                        <img src="{IMG}/livros-4.webp" alt="Livros Imersão Azul, 8º e 9º ano" loading="lazy">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="project-block wave rev" id="submarino-imersivo">
        <span class="idx">02</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">submarino imersivo</span></h2>
                <div><span class="pill">Uma viagem ao fundo do mar</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <p class="v2-lead">O Submarino Imersivo leva o público <strong>a uma expedição pelas profundezas do oceano por meio da realidade virtual</strong>.</p>
                    <p class="v2-lead">Em uma <strong>estrutura que simula um submarino</strong>, os visitantes exploram ecossistemas marinhos, conhecem espécies e compreendem a importância do oceano para a vida no planeta.</p>
                    <p class="v2-lead">De forma envolvente, acessível e memorável, <strong>a experiência fortalece a Cultura Oceânica, desperta a consciência ambiental e inspira atitudes em favor da conservação dos ecossistemas marinhos.</strong></p>
                </div>
                <div class="rimg" style="aspect-ratio:16/10" data-aos="fade-left"><img src="{IMG}/hf-05-submarino-vr.webp" alt="Crianças com realidade virtual no fundo do mar" loading="lazy"></div>
            </div>
            <div style="margin-top:28px">{gal([("submarino-1", "Submarino inflável com escotilhas"), ("submarino-2", "Submarino imersivo visto de lado"), ("submarino-3", "Entrada do Submarino 360")])}</div>
        </div>
    </section>

    <section class="project-block wave alt" id="imersao-polar">
        <span class="idx">03</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">imersão polar</span></h2>
                <div><span class="pill">Uma missão congelante</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <p class="v2-lead">Expedição científica ao Ártico para a curadoria de imagens terrestres e subaquáticas. O projeto transforma esse acervo exclusivo em <strong>conteúdos didáticos</strong> para a plataforma Imersão Azul e materiais impressos, <strong>promovendo uma experiência educativa baseada em evidências.</strong></p>
                    <p class="v2-lead">Seu principal objetivo é <strong>sensibilizar crianças, jovens e adultos sobre as mudanças climáticas em curso</strong> e a importância da conservação dos oceanos e das regiões polares.</p>
                </div>
                <div class="rimg" style="aspect-ratio:16/10" data-aos="fade-left"><img src="{IMG}/hf-06-polar-geleira.webp" alt="Geleira e montanhas nevadas" loading="lazy"></div>
            </div>
            <div style="margin-top:28px">{gal([("hf-07-polar-pinguins", "Pinguins e navio de expedição"), ("hf-08-polar-urso", "Urso polar sobre o gelo")], "g2")}</div>
        </div>
    </section>

    <section class="project-block wave rev" id="mundo-submarino-360">
        <span class="idx">04</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">mundo submarino 360°</span></h2>
                <div><span class="pill">Uma viagem ao fundo do mar</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <p class="v2-lead">Leva experiências educacionais transformadoras para aeroportos e shopping centers.</p>
                    <p class="v2-lead">Proporciona <strong>uma verdadeira viagem ao fundo do mar utilizando recursos audiovisuais de ponta e experiências sensoriais memoráveis.</strong></p>
                    <div class="pill-row"><span class="pill soft">Experiência inédita</span><span class="pill soft">Impacto visual e sensorial</span><span class="pill soft">Conteúdo educativo</span></div>
                </div>
                <div class="rimg" style="aspect-ratio:16/10" data-aos="fade-left"><img src="{IMG}/hf-09-360-aeroporto.webp" alt="Estande Mundo Submarino 360 no aeroporto" loading="lazy"></div>
            </div>
            <div style="margin-top:28px">{gal([("hf-10-360-frente", "Estande Mundo Submarino 360 visto de frente"), ("hf-11-360-interior", "Interior do Mundo Submarino 360")], "g2")}</div>
        </div>
    </section>

    <section class="project-block wave alt" id="oceanoterapia">
        <span class="idx">05</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">OceanoTerapia®</span></h2>
                <div><span class="pill">Conectar pessoas ao oceano para transformar vidas</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <img class="brand" src="{LOGO}/oceanoterapia.png" alt="OceanoTerapia" style="height:110px;margin-bottom:1.2rem">
                    <p class="v2-lead">A OceanoTerapia® utiliza a <strong>conexão consciente com o oceano como ferramenta para promover bem-estar, saúde integral e consciência ambiental.</strong></p>
                    <p class="v2-lead">Por meio de <strong>experiências imersivas no oceano</strong>, práticas contemplativas e vivências sensoriais, <strong>fortalece a relação entre pessoas e ambiente marinho</strong>, despertando pertencimento, equilíbrio e atitudes em favor da conservação do oceano.</p>
                </div>
                <div class="stack" data-aos="fade-left">
                    <div class="rimg" style="aspect-ratio:16/10"><img src="{IMG}/hf-12-oceanoterapia.webp" alt="Pessoa boiando no mar em estado contemplativo" loading="lazy"></div>
                    <div class="quote-box"><h3>O oceano educa de um jeito diferente</h3><p>Ele ensina ritmo, pausa, escuta, pertencimento e conexão. Quando a pessoa se conecta com o mar, ela também começa a perceber melhor o próprio corpo e o ambiente ao redor.</p></div>
                </div>
            </div>
            <div class="congresso" data-aos="fade-up">
                <div class="rimg" style="aspect-ratio:16/10"><img src="{IMG}/hf-13-congresso.webp" alt="Congresso OceanoTerapia" loading="lazy"></div>
                <div>
                    <h3 class="v2-title"><span class="script">congresso</span><span class="main">OceanoTerapia</span></h3>
                    <p class="v2-lead">Em breve, mais informações sobre o Congresso OceanoTerapia. Deixe seu contato para ser avisado.</p>
                    <a href="contato.html" class="btn btn-primary">Quero saber mais</a>
                </div>
            </div>
        </div>
    </section>

    <section class="project-block wave rev" id="mare-de-campeoes">
        <span class="idx">06</span>
        <div class="container">
            <div class="project-head" data-aos="fade-up">
                <h2 class="v2-title"><span class="script">projeto</span><span class="main">maré de campeões</span></h2>
                <div><span class="pill">Esporte, Cultura Oceânica e Transformação Social</span></div>
            </div>
            <div class="grid-2">
                <div data-aos="fade-right">
                    <p class="v2-lead">O Maré de Campeões utiliza o <strong>esporte como ferramenta de inclusão social</strong> e <strong>porta de entrada para a Cultura Oceânica</strong>, promovendo educação ambiental em comunidades da Baía do Iguape e Salvador (BA).</p>
                    <p class="v2-lead">Integrando <strong>modalidades esportivas, vivências na natureza e atividades educativas</strong>, o projeto visa desenvolver crianças e adolescentes de forma integral, <strong>formando não apenas atletas, mas cidadãos conscientes do papel do oceano para a vida</strong> e <strong>comprometidos com a conservação dos ecossistemas costeiros</strong>.</p>
                    <div class="pill-row"><span class="pill soft"><i class="fas fa-medal"></i> Campeãs baianas do jiu-jitsu: irmãs gêmeas Larissa e Stella</span></div>
                </div>
                <div class="rimg" style="aspect-ratio:16/10" data-aos="fade-left"><img src="{IMG}/mare-time.webp" alt="Time Real São Francisco 2026" loading="lazy"></div>
            </div>
            <div style="margin-top:28px">{gal([("mare-gemeas", "Campeãs baianas do jiu-jitsu, Larissa e Stella", "tall"), ("mare-vela", "Escolinha de Vela", "tall"), ("rsf-2", "Time Real São Francisco com a bandeira do Instituto", "tall")])}</div>
        </div>
    </section>

    <section class="v2-section wave navy">
        <div class="container center" data-aos="fade-up">
            <h2 class="v2-title light"><span class="script">quer apoiar</span><span class="main">nossos projetos?</span></h2>
            <p class="v2-lead" style="color:#cfe3ec">Escolas, empresas e parceiros podem levar a Cultura Oceânica a mais pessoas.</p>
            <a href="contato.html" class="btn btn-light">Fale com o Instituto</a>
        </div>
    </section>
""" + next_page("acoes-sociais.html", "baia-iguape-aerea", "veja as", "ações sociais") + FOOTER

# ================= AÇÕES SOCIAIS =================
_ACAO_N = [0]


def acao(titulo, texto, fotos, cls=None, extra_head=""):
    _ACAO_N[0] += 1
    alt = _ACAO_N[0] % 2 == 1
    n = len(fotos)
    fotos = [f[:2] for f in fotos]
    if n == 5:
        fotos[0] = fotos[0] + ("wide",)
    cls = {2: "g2", 3: "g3", 4: "g4", 5: "g3"}.get(n, "g3")
    return f"""
    <section class="action wave{' alt' if alt else ''}">
        <div class="container">
            <div class="head" data-aos="fade-up"><div><h3>{titulo}</h3>{f'<p class="v2-lead" style="margin:.6rem 0 0">{texto}</p>' if texto else ''}</div>{extra_head}</div>
            {gal(fotos, cls)}
        </div>
    </section>"""


acoes = head("Ações Sociais na Baía do Iguape | Instituto Gaia Soul",
             "Ações sociais do Instituto Gaia Soul na Reserva Extrativista Marinha Baía do Iguape (BA): esporte, regatas, apoio a 650 famílias de pescadores e marisqueiras. Utilidade Pública pela Prefeitura de Cachoeira.",
             "acoes-sociais.html") + page_hero("hf-14-costa-bahia", "ações sociais", "baía do iguape", "Ações Sociais") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <span class="pill">Conectando pessoas. Transformando comunidades.</span>
                    <h2 class="v2-title" style="margin-top:1.4rem"><span class="script">reserva marinha</span><span class="main">baía do iguape</span></h2>
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
""" + acao("Time Real São Francisco",
           "<strong>O time Real São Francisco conta com 60 jovens de 12 a 17 anos.</strong> Contribuímos com treinador, uniformes para os jogos, bolas, lanche dos atletas, entre outras ações. <strong>Chegamos ao vice-campeonato em 2025.</strong>",
           [("rsf-1", "Time Real São Francisco no Campeonato Cachoeirano 2026"), ("rsf-2", "Time com a bandeira do Instituto Gaia Soul"), ("rsf-4", "Times perfilados antes do jogo"), ("rsf-3", "Treino do time Real São Francisco")],
           f'<img class="crest" src="{LOGO}/real-sao-francisco.png" alt="Esporte Clube Real São Francisco">') \
    + acao("Bordejos e regatas de canoas", "",
           [("bordejo-3", "Canoas a vela na praia"), ("bordejo-premiacao", "Premiação do Grande Bordejo"), ("bordejo-1", "Regata de canoas na baía"), ("bordejo-2", "Canoa a vela ao pôr do sol")])  \
    + acao("650 famílias de pescadores e marisqueiras",
           "Contribuímos em datas festivas: Natal, Dia das Mães, Dia dos Pais e Dia das Crianças. No Dia das Crianças, levamos <strong>educação ambiental e doação de chocolates</strong> para as escolas.",
           [("escola-1", "Dia das Crianças com educação ambiental na escola"), ("escola-2", "Doações preparadas para o Dia das Crianças", "tall"), ("escola-3", "Crianças da escola com a equipe do Instituto")])  \
    + acao("Dia das Mães", "",
           [("maes-3", "Entrega de presentes no Dia das Mães"), ("maes-4", "Presentes para as mães"), ("maes-2", "Mesa de presentes"), ("maes-1", "Mães reunidas na comemoração"), ("maes-5", "Mesa do Instituto Gaia Soul")])  \
    + acao("Convênio com a Associação dos Pescadores e Marisqueiras de Cachoeira",
           "Convênio de Cooperação com a Associação dos Pescadores e Marisqueiras de Cachoeira.",
           [("pescadores-3", "Confraternização das marisqueiras na praia"), ("pescadores-4", "Entrega de kits no Sindicato de Pescadores"), ("pescadores-1", "Pescadores e marisqueiras com as doações"), ("pescadores-5", "Presentes para as famílias"), ("pescadores-2", "Mesa de lanche do Instituto")])  \
    + acao("Dia das Crianças",
           "Entrega de brinquedos para as crianças das comunidades.",
           [("brinquedos-1", "Crianças com os brinquedos recebidos"), ("brinquedos-2", "Crianças escolhendo brinquedos"), ("brinquedos-4", "Criança com brinquedo novo"), ("brinquedos-3", "Brinquedos arrecadados para a doação")])  \
    + acao("Apresentação do projeto à Prefeitura de Cachoeira - BA", "",
           [("prefeitura-1", "Apresentação com óculos de realidade virtual na Prefeitura"), ("prefeitura-2", "Experiência de realidade virtual na Prefeitura")], "g2") + f"""

    <section class="v2-section wave navy">
        <div class="container center" data-aos="fade-up">
            <h2 class="v2-title light"><span class="script">junte-se</span><span class="main">a esse movimento</span></h2>
            <p class="v2-lead" style="color:#cfe3ec">Vamos conectar pessoas ao oceano, transformar comunidades e construir um futuro mais sustentável.</p>
            <a href="contato.html" class="btn btn-light">Quero apoiar</a>
        </div>
    </section>
""" + next_page("contato.html", "veleiro-gaia", "fale", "conosco") + FOOTER

# ================= CONTATO =================
contato = head("Contato | Instituto Gaia Soul",
               "Fale com o Instituto Gaia Soul pelo WhatsApp (71) 9997-2427, e-mail contato@institutogaiasoul.ong.br ou Instagram @institutogaiasoul.",
               "contato.html") + page_hero("hf-14-costa-bahia", "fale", "conosco", "Contato") + f"""
    <section class="v2-section wave">
        <div class="container">
            <div class="grid-2">
                <div data-aos="fade-right">
                    <h2 class="v2-title"><span class="script">proteger nossos oceanos</span><span class="main">para o futuro</span></h2>
                    <p class="v2-lead">Escolas, empresas, prefeituras e parceiros: conte para a gente como quer levar a Cultura Oceânica a mais pessoas.</p>
{CONTATO_BOX}
                    <div class="cnpj">GAIA SOUL INSTITUTO DE PROTEÇÃO E EDUCAÇÃO AMBIENTAL · CNPJ 34.941.993/0001-18</div>
                </div>
                <form class="form-v2" id="form-contato" data-aos="fade-left">
                    <div class="row">
                        <div><label for="f-nome">Nome</label><input id="f-nome" name="nome" required></div>
                        <div><label for="f-tel">WhatsApp</label><input id="f-tel" name="telefone" type="tel" required></div>
                    </div>
                    <div><label for="f-email">E-mail</label><input id="f-email" name="email" type="email"></div>
                    <div><label for="f-assunto">Assunto</label>
                        <select id="f-assunto" name="assunto">
                            <option>Imersão Azul nas escolas</option>
                            <option>Submarino Imersivo / Mundo Submarino 360°</option>
                            <option>OceanoTerapia</option>
                            <option>Parceria ou patrocínio</option>
                            <option>Ações sociais</option>
                            <option>Outro assunto</option>
                        </select>
                    </div>
                    <div><label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem"></textarea></div>
                    <button type="submit" class="btn btn-primary"><i class="fab fa-whatsapp"></i> Enviar pelo WhatsApp</button>
                    <div class="form-ok" id="form-ok">Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar.</div>
                </form>
            </div>
        </div>
    </section>
    <script>
    document.getElementById('form-contato').addEventListener('submit', function (e) {{
        e.preventDefault();
        var f = this, v = function (n) {{ return (f.elements[n].value || '').trim(); }};
        var t = 'Olá! Vim pelo site do Instituto Gaia Soul.\\n' + 'Nome: ' + v('nome') + '\\nWhatsApp: ' + v('telefone') +
            (v('email') ? '\\nE-mail: ' + v('email') : '') + '\\nAssunto: ' + v('assunto') + (v('mensagem') ? '\\n\\n' + v('mensagem') : '');
        window.open('{WA}?text=' + encodeURIComponent(t), '_blank');
        document.getElementById('form-ok').style.display = 'block';
    }});
    </script>
""" + FOOTER

for nome, html in [("index.html", index), ("sobre.html", sobre), ("projetos.html", projetos),
                   ("acoes-sociais.html", acoes), ("contato.html", contato)]:
    (ROOT / nome).write_text(html, encoding="utf-8")
    print("ok", nome, len(html))
