#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Site do Instituto Gaia Soul · v4

Base: ESTRUTURA e DINÂMICA do site antigo (institutogaiasoul.ong.br, WordPress/Elementor),
que o Marcelo e a Milena aprovaram na reunião de 28-09-2026, com a IDENTIDADE VISUAL atual
do Instituto (mesmas fontes e cores do Instagram) e o conteúdo do documento da Milena (v3),
reescrito com mais engajamento.

Mapa do site antigo -> v4
  Home: herói com vídeo submarino + onda  ->  mantido (mesmo vídeo do canal do Instituto)
        faixas verticais de imagem + O Instituto  ->  mantido, com fotos reais dos projetos
        frase-manifesto sobre foto + 4 contadores  ->  mantido, números do Instituto (sem veleiro)
        números 1, 2, 3 com foto dentro  ->  mantido ("por que agir agora")
        card "Caminhando juntos" + barra 100%  ->  mantido
        Missão, Visão, Valores  ->  mantido
        Iniciativas (cards)  ->  Projetos (cards)
        painéis de projeto em tela cheia com fundo fixo  ->  mantido, 1 por projeto, com link
        Indicadores (carrossel com barras)  ->  mantido, números da reunião (803, 65, 2)
        Projetos Especiais  ->  Quem apoiamos (esporte)
        (novo) mapa interativo de satélite: APA BTS -> RESEX Baía do Iguape -> Mata Quântica
        faixa navy Voluntariado/Doações/Blusa  ->  Seja um Guardião
        foto redonda do Marcelo, ODS, faixa de parceiros, rodapé com formulário  ->  mantidos
  Internas (Quem Somos, Projetos, Palestras, Baía do Iguape, Apoie, Fale Conosco): topo com
        faixa + card de imagem, galerias, caixas de texto, botões  ->  mesmo formato

Ajustes da reunião aplicados: menu com Início; vídeo antigo no herói; Veleiro só no histórico
(origem do nome); uma página por projeto; Imersão Polar, Centro de Cultura Oceânica e
Transparência fora; Maré de Campeões vira "Quem apoiamos"; sem foto das gêmeas; números
quebrados (803 famílias, 65 atletas, 2 comunidades); Marujada vira "Seja um Guardião";
Blue Bank existe (convite a fotógrafos); utilidade pública em Atuação & Impacto.

Edite os DADOS abaixo e rode:  python3 _build.py
"""
import math
from pathlib import Path

ROOT = Path(__file__).parent
IMG = "assets/images/v2"      # acervo do v3
IMG4 = "assets/images/v4"     # acervo novo (site antigo, LPs, mapas)
LOGO = "assets/images/logos"
VID = "assets/video/v4"
V = "20261002b"               # versão dos assets (cache)

WA_NUM = "557199972427"
WA = f"https://wa.me/{WA_NUM}"
TEL = "(71) 99997-2427"
MAIL = "contato@institutogaiasoul.ong.br"
IG = "https://instagram.com/institutogaiasoul"
RAZAO = "Gaia Soul Instituto de Proteção e Educação Ambiental"
CNPJ = "34.941.993/0001-18"
ESCRITORIO = "Av. Tancredo Neves, 620, Caminho das Árvores, Salvador/BA"
LEAD_WEBHOOK = ""   # webhook do CRM pros formulários (vazio = só WhatsApp)

# ---- PENDENTES (a Milena vai enviar). None = o site mostra "peça pelo WhatsApp". ----
PIX_CHAVE = None            # ex.: "34.941.993/0001-18" ou e-mail
PIX_TIPO = "CNPJ"           # tipo da chave
BANCO = None                # ex.: dict(banco="Banco do Brasil", agencia="0000-0", conta="00000-0")
BANCO_IMAGENS_URL = None    # link do Blue Bank (banco de imagens)
LOJA_URL = None             # onde comprar a camiseta
GOOGLE_INSTITUTO = "https://share.google/oN9QCGZIFGdvhcymP"   # perfil do Instituto no Google
IMERSAO_AZUL_URL = "https://imersaoazul.com.br"
MATA_URL = "https://mataquantica.com.br"
OCEANO_EBOOK_URL = "https://mediagrowthmkt-debug.github.io/oceanoterapiapages/?utm_source=site&utm_medium=pagina-oceanoterapia&utm_campaign=ebook"

SOCIAL = [
    ("https://www.linkedin.com/company/instituto-gaia-soul/", "fab fa-linkedin-in", "LinkedIn", "in"),
    (IG, "fab fa-instagram", "Instagram", "ig"),
    ("https://www.youtube.com/@InstitutoGaiaSoul", "fab fa-youtube", "YouTube", "yt"),
    ("https://www.facebook.com/p/Instituto-Gaia-Soul-61552657763845/", "fab fa-facebook-f", "Facebook", "fb"),
    ("https://www.tiktok.com/@institutogaiasoul", "fab fa-tiktok", "TikTok", "tt"),
    ("https://br.pinterest.com/institutogaiasoul/", "fab fa-pinterest-p", "Pinterest", "pi"),
]

# =====================================================================
# DADOS
# =====================================================================
# Contadores da frase-manifesto (números do Instituto, todos confirmados)
CONTADORES = [
    (2019, "ano em que o Instituto nasceu", True),
    (11, "livros didáticos autorais de Cultura Oceânica", False),
    (100, "hectares de Mata Atlântica preservados", False),
    (7, "princípios da Cultura Oceânica em cada projeto", False),
]

# Indicadores sociais (reunião 28-09: números quebrados, reais)
INDICADORES = [
    ("fa-people-roof", "Famílias de pescadores e marisqueiras", "Apoio à Associação de Pescadores e Marisqueiras de Cachoeira.", "803 famílias", 100),
    ("fa-futbol", "Jovens atletas", "Time Real São Francisco, de 12 a 17 anos, vice-campeão em 2025.", "65 jovens", 82),
    ("fa-house-flag", "Comunidades quilombolas", "Presença contínua na Reserva Extrativista da Baía do Iguape.", "2 comunidades", 74),
    ("fa-book-open", "Livros autorais", "Coleção do Imersão Azul, alinhada à BNCC e à Década do Oceano.", "11 livros", 78),
]

# Projetos. bg = imagem do painel; video = fundo em vídeo (opcional)
PROJETOS = [
    dict(slug="imersao-azul", nome="Imersão Azul", tags="Educação • Cultura Oceânica", card=f"{IMG4}/imersao-sala.webp",
         bg=f"{IMG4}/imersao-capa.webp", logo=f"{LOGO}/imersao-azul.png",
         resumo="A Cultura Oceânica dentro da sala de aula, com livros, realidade virtual e muita curiosidade.",
         painel="E se o fundo do mar coubesse dentro da sala de aula? O Imersão Azul leva a Cultura Oceânica para as escolas com 11 livros autorais, realidade virtual, plataforma digital e uma jornada gamificada que transforma ciência em encantamento.",
         ext=(IMERSAO_AZUL_URL, "Visite o site do Imersão Azul")),
    dict(slug="mundo-submarino-360", nome="Mundo Submarino 360°", tags="Tecnologia • Experiência imersiva", card=f"{IMG4}/sub-recife.webp",
         bg=f"{IMG}/hf-09-360-aeroporto.webp", video=f"{VID}/mundo-submarino-loop.mp4",
         resumo="Um mergulho em realidade virtual no meio do aeroporto, do shopping ou do seu evento.",
         painel="Você está no aeroporto, coloca os óculos e, em segundos, está nadando entre tartarugas e cardumes. O Mundo Submarino 360° leva o oceano até onde as pessoas estão, com uma experiência sensorial que ninguém esquece."),
    dict(slug="submarino-imersivo", nome="Submarino Imersivo", tags="Cultura Oceânica • Realidade virtual", card=f"{IMG}/submarino-1.webp",
         bg=f"{IMG4}/sub-dentro.webp",
         resumo="Uma expedição coletiva dentro de um submarino, com escotilhas, sons e realidade virtual.",
         painel="Escotilhas, luzes azuis e o som do mar: crianças e adultos entram juntos num submarino e partem numa expedição pelos ecossistemas marinhos. Conhecimento que entra pelos olhos, pelos ouvidos e pelo coração."),
    dict(slug="oceanoterapia", nome="Oceanoterapia", tags="Oceano • Natureza • Bem-estar", card=f"{IMG4}/mata/mata-05324.webp",
         bg=f"{IMG4}/mata/mata-05352.webp", logo=f"{LOGO}/oceanoterapia.png",
         resumo="Vivências no mar e na natureza para desacelerar, respirar e se reconectar.",
         painel="Boiar, respirar no ritmo das ondas, silenciar. A Oceanoterapia usa a água e a natureza como caminho para presença e bem-estar, e quem se reconecta com o mar passa a querer protegê-lo."),
    dict(slug="mata-quantica", nome="Mata Quântica", tags="Mata Atlântica • Sede • Retiros", card=f"{IMG4}/mata/mata-05357.webp",
         bg=f"{IMG4}/mata-aerea.webp", logo=f"{LOGO}/mata-quantica-escura.png",
         resumo="100 hectares de Mata Atlântica preservada na Baía do Iguape, onde funciona a nossa sede.",
         painel="A Mata Atlântica é um dos biomas mais ameaçados do planeta. Às margens da Baía do Iguape, a Mata Quântica protege 100 hectares de floresta, em processo para se tornar uma Reserva Particular do Patrimônio Natural (RPPN), e é a casa do Instituto.",
         ext=(MATA_URL, "Conheça a Mata Quântica")),
    dict(slug="palestras", nome="Palestras com Marcelo Telles", tags="Educação • Empresas • Escolas", card=f"{IMG4}/palestra-1.webp",
         bg=f"{IMG4}/bg-palestra.webp",
         resumo="Histórias de alto mar que viram consciência ambiental em escolas, eventos e empresas.",
         painel="Oceanógrafo com décadas de vida no mar, Marcelo Telles transforma as travessias que viveu em palestras que emocionam e fazem pensar, em congressos, escolas e empresas, inclusive com óculos de realidade virtual."),
]
PMAP = {p["slug"]: p for p in PROJETOS}

# Galerias por projeto
GAL_PALESTRAS = [(f"{IMG4}/palestra-{i}.webp", "Marcelo Telles em palestra") for i in (1, 2, 3, 4, 5, 6, 7, 8, 9)]

PRINCIPIOS = [
    "A Terra tem um Oceano global e muito diverso",
    "O Oceano e a vida marinha têm uma forte ação na dinâmica da Terra",
    "O Oceano exerce uma influência importante no clima",
    "O Oceano permite que a Terra seja habitável",
    "O Oceano suporta uma imensa diversidade de vida e de ecossistemas",
    "O Oceano e a humanidade estão fortemente interligados",
    "Há muito por descobrir e explorar no Oceano",
]

PARCEIROS = [("unesco.png", "UNESCO"), ("decada-oceano.png", "Década do Oceano 2021-2030"),
             ("aleixo-belov.png", "Fundação Aleixo Belov"), ("aoceano.png", "Associação Brasileira de Oceanografia"),
             ("escola-azul.png", "Escola Azul Brasil"), ("real-sao-francisco.png", "Esporte Clube Real São Francisco")]

# =====================================================================
# MAPA (satélite Esri World Imagery em 3 níveis)
# =====================================================================
NIVEIS = [  # nome, arquivo, (norte, oeste, sul, leste), largura, altura, link Google Maps
    ("Baía de Todos-os-Santos", "mapa-n1", (-12.50, -39.02, -13.12, -38.30), 1600, 1413,
     "https://www.google.com/maps/@-12.82,-38.64,62000m/data=!3m1!1e3"),
    ("Baía do Iguape", "mapa-n2", (-12.66, -39.00, -12.93, -38.72), 1600, 1582,
     "https://www.google.com/maps/@-12.78,-38.86,24000m/data=!3m1!1e3"),
    ("Mata Quântica", "mapa-n3", (-12.8015, -38.8660, -12.8175, -38.8450), 1600, 1250,
     "https://www.google.com/maps/@-12.80931,-38.85558,1600m/data=!3m1!1e3"),
]
MATA_LATLNG = (-12.80931, -38.85558)


def _merc(lat):
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))


def mpos(n, lat, lon):
    N, W, S, E = NIVEIS[n][2]
    x = (lon - W) / (E - W) * 100
    y = (_merc(N) - _merc(lat)) / (_merc(N) - _merc(S)) * 100
    return round(x, 2), round(y, 2)


def pin(n, lat, lon, nome, tipo, txt, hi=False, zoom=None, cta=None, link=None, link_txt=None, ext=False, label=True):
    x, y = mpos(n, lat, lon)
    attrs = f'data-nome="{nome}" data-tipo="{tipo}" data-txt="{txt}"'
    if zoom is not None:
        attrs += f' data-zoom="{zoom}" data-cta="{cta or "Aproximar"}"'
    if link:
        attrs += f' data-link="{link}" data-link-txt="{link_txt or "Saiba mais"}"' + (' data-ext="1"' if ext else "")
    lb = f'<span class="pl">{nome}</span>' if label else ""
    return f'<button type="button" class="pin{" hi" if hi else ""}" style="left:{x}%;top:{y}%" {attrs} aria-label="{nome}"><span class="dot"></span>{lb}</button>'


def mapa_html():
    mx, my = mpos(2, *MATA_LATLNG)
    n0 = "".join([
        f'<span class="area" data-zoom="1" style="left:{mpos(0, -12.70, -38.97)[0]}%;top:{mpos(0, -12.70, -38.97)[1]}%;width:17%;height:22%"></span>',
        pin(0, -12.83, -38.63, "APA Baía de Todos-os-Santos", "Área de Proteção Ambiental",
            "A maior baía do Brasil é protegida como Área de Proteção Ambiental. Manguezais, recifes e comunidades tradicionais dividem essas águas, que são a porta de entrada do nosso território."),
        pin(0, -12.975, -38.50, "Salvador", "Escritório administrativo",
            "Nosso escritório administrativo e ponto de partida dos projetos em escolas, eventos e espaços públicos."),
        pin(0, -12.76, -38.88, "Baía do Iguape", "Reserva Extrativista (RESEX)",
            "Dentro da Baía de Todos-os-Santos, a Baía do Iguape é uma Reserva Extrativista: um território onde comunidades quilombolas e pesqueiras vivem do mar e o protegem.",
            hi=True, zoom=1, cta="Aproximar da Baía do Iguape"),
    ])
    n1 = "".join([
        pin(1, -12.735, -38.885, "RESEX Baía do Iguape", "Reserva Extrativista",
            "Unidade de conservação federal criada em 2000 para proteger o ecossistema e garantir o modo de vida das comunidades tradicionais: pesca, mariscagem e cultivo de ostras."),
        pin(1, -12.775, -38.935, "Comunidades tradicionais", "Quilombolas e pescadores",
            "Atuamos junto a 2 comunidades quilombolas e apoiamos a Associação de Pescadores e Marisqueiras de Cachoeira, que reúne 803 famílias.",
            link="baia-do-iguape.html", link_txt="Ver as ações na Baía do Iguape"),
        pin(1, *MATA_LATLNG, "Mata Quântica", "Sede do Instituto",
            "100 hectares de Mata Atlântica preservada às margens da baía, em processo para se tornar RPPN. É aqui que funciona a nossa sede.",
            hi=True, zoom=2, cta="Aproximar da Mata Quântica"),
        pin(1, -12.85, -38.785, "Baía de Todos-os-Santos", "Voltar",
            "A Baía do Iguape deságua na Baía de Todos-os-Santos pela foz do Rio Paraguaçu.", zoom=0, cta="Voltar para a Baía de Todos-os-Santos"),
    ])
    n2 = "".join([
        f'<span class="area sq" style="left:{mx - 3}%;top:20%;width:46%;height:58%"></span>',
        pin(2, *MATA_LATLNG, "Mata Quântica", "Sede do Instituto · RPPN em processo",
            "100 hectares de Mata Atlântica preservada. Aqui ficam a sede do Instituto e as casas onde acontecem retiros, vivências de Oceanoterapia e encontros.",
            hi=True, link="projeto-mata-quantica.html", link_txt="Conheça a Mata Quântica"),
        pin(2, -12.8095, -38.8615, "Baía do Iguape", "Reserva Extrativista",
            "A floresta encontra o mar: a Mata Quântica fica na beira da RESEX Baía do Iguape.", zoom=1, cta="Voltar para a Baía do Iguape"),
        f'<span class="pin" style="left:{mx + 20}%;top:23%;pointer-events:none"><span class="pl" style="position:static;transform:none;background:rgba(255,209,102,.92);color:#0A2E4D">100 hectares preservados</span></span>',
    ])
    niveis = [n0, n1, n2]
    stages = "".join(
        f'<div class="nivel{" on" if i == 0 else ""}" data-gmaps="{nv[5]}"><div class="stage" data-ar="{nv[3] / nv[4]:.4f}">'
        f'<img src="{IMG4}/{nv[1]}.webp" alt="Imagem de satélite: {nv[0]}" loading="lazy">{niveis[i]}</div></div>'
        for i, nv in enumerate(NIVEIS))
    ON = ' class="on"'
    trilha = "".join(f'<button type="button"{ON if i == 0 else ""}>{i + 1}. {nv[0]}</button>' for i, nv in enumerate(NIVEIS))
    return f"""<div class="mapa" data-rv>
                    {stages}
                    <div class="trilha">{trilha}</div>
                    <a class="gmaps" href="{NIVEIS[0][5]}" target="_blank" rel="noopener"><i class="fas fa-map-location-dot"></i> Ver no Google Maps</a>
                    <div class="tip" role="status"></div>
                    <div class="legenda"><span class="hint"><i class="fas fa-hand-pointer"></i> Toque nos pontos para explorar</span><span class="attr">Imagens de satélite: Esri, Maxar, Earthstar Geographics</span></div>
                </div>"""


MAPA_INFO = """<div class="mapa-info">
                    <div class="lv on" data-go="0"><small>1 · Área de Proteção Ambiental</small><b>Baía de Todos-os-Santos</b><p>A maior baía do Brasil, protegida como APA. É daqui que o nosso território começa.</p></div>
                    <div class="lv" data-go="1"><small>2 · Reserva Extrativista</small><b>Baía do Iguape</b><p>RESEX onde vivem comunidades quilombolas e pesqueiras, com quem construímos esporte, educação e apoio às famílias.</p></div>
                    <div class="lv" data-go="2"><small>3 · Sede do Instituto</small><b>Mata Quântica</b><p>100 hectares de Mata Atlântica preservada, em processo para se tornar RPPN.</p></div>
                </div>"""

# =====================================================================
# MENU
# =====================================================================
NAV = [
    ("index.html", "Início", []),
    ("o-instituto.html", "O Instituto", [("o-instituto.html#quem-somos", "Quem somos"), ("o-instituto.html#historia", "Nossa história"),
                                         ("o-instituto.html#proposito", "Propósito"), ("o-instituto.html#governanca", "Governança & Equipe"),
                                         ("o-instituto.html#territorio", "Nosso território"), ("o-instituto.html#parceiros", "Parceiros")]),
    ("projetos.html", "Projetos", [(f"projeto-{p['slug']}.html", p["nome"].replace(" com Marcelo Telles", "")) for p in PROJETOS] + [("projetos.html#blue-bank", "Blue Bank")]),
    ("atuacao-e-impacto.html", "Atuação & Impacto", [("atuacao-e-impacto.html#eixos", "Os quatro eixos"), ("atuacao-e-impacto.html#numeros", "Impacto em números"),
                                                     ("atuacao-e-impacto.html#territorio", "Mapa de atuação"), ("atuacao-e-impacto.html#historias", "Histórias de impacto"),
                                                     ("baia-do-iguape.html", "Ações na Baía do Iguape"), ("atuacao-e-impacto.html#quem-apoiamos", "Quem apoiamos")]),
    ("seja-um-guardiao.html", "Seja um Guardião", [("seja-um-guardiao.html#mensal", "Quero ser um Guardião"), ("seja-um-guardiao.html#doacao", "Quero fazer uma doação"),
                                                   ("seja-um-guardiao.html#empresas", "Quero apoiar como empresa"), ("seja-um-guardiao.html#voluntariado", "Quero ser voluntário")]),
    ("contato.html", "Contato", []),
]


def nav_html(page):
    out = []
    for href, label, subs in NAV:
        on = ' class="on"' if href == page or (page.startswith("projeto-") and href == "projetos.html") or (page == "baia-do-iguape.html" and href == "atuacao-e-impacto.html") else ""
        if subs:
            items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in subs)
            out.append(f'<li><a href="{href}"{on}>{label} <i class="fas fa-caret-down"></i></a><ul class="sub">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{href}"{on}>{label}</a></li>')
    return "".join(out)


def head(title, desc, page, og=f"{IMG4}/hero-oceano.webp"):
    solid = "" if page == "index.html" else " solid"
    canon = "" if page == "index.html" else page
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i></a>' for u, i, n, _ in SOCIAL[:3])
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://institutogaiasoul.ong.br/{canon}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:image" content="https://institutogaiasoul.ong.br/{og}">
    <meta property="og:locale" content="pt_BR">
    <meta name="theme-color" content="#1B3A5C">
    <link rel="icon" type="image/png" href="{LOGO}/gaia-soul-oficial.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Bebas+Neue&family=Caveat:wght@700&family=Fraunces:ital,opsz,wght@1,9..144,400&family=Radley&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="assets/css/v4.css?v={V}">
</head>
<body class="pg-{page.replace('.html', '')}">
    <header class="hdr{solid}">
        <div class="wrap bar">
            <a href="index.html" class="logo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
            <nav aria-label="Menu principal"><ul class="menu">{nav_html(page)}</ul></nav>
            <div class="hdr-social">{soc}</div>
            <button class="burger" aria-label="Abrir menu"><i class="fas fa-bars"></i></button>
        </div>
    </header>
"""


# ---------------------------------------------------------------------
# Formulário em etapas (passo a passo)
# ---------------------------------------------------------------------
LGPD = '<label class="lgpd"><input type="checkbox" required> <span>Concordo com a <a href="politica-de-privacidade.html">Política de Privacidade</a>.</span></label>'


def fld(name, label, tipo="text", req=True, area=False, extra=""):
    r = " required" if req else ""
    if area:
        return f'<div class="fld"><textarea name="{name}" id="f-{name}-{{uid}}" placeholder=" "{r}></textarea><label for="f-{name}-{{uid}}">{label}</label></div>'
    return f'<div class="fld"><input name="{name}" id="f-{name}-{{uid}}" type="{tipo}" placeholder=" "{r}{extra}><label for="f-{name}-{{uid}}">{label}</label></div>'


def opts(name, itens, auto=True):
    """itens: (valor, rótulo, ícone, detalhe)"""
    ops = "".join(f'<label class="opt"><input type="radio" name="{name}" value="{v}"><span>{f"<i class={chr(34)}fas {ic}{chr(34)}></i>" if ic else ""}{r}{f"<small>{d}</small>" if d else ""}</span></label>'
                  for v, r, ic, d in itens)
    return f'<div class="opts" data-req{" data-auto" if auto else ""}>{ops}</div>'


def stepper(uid, etapas, assunto="", ok="", enviar="Enviar pelo WhatsApp", dark=False):
    """etapas: lista de (pergunta, dica, html)"""
    fs = "".join(f'<fieldset class="step"><legend>{q}</legend>{f"<p class={chr(34)}hint{chr(34)}>{h}</p>" if h else ""}{html}</fieldset>'
                 for q, h, html in etapas).replace("{uid}", uid)
    return f"""<form class="stepper js-lead{' dark' if dark else ''}" id="form-{uid}"{f' data-assunto="{assunto}"' if assunto else ''}{f' data-ok="{ok}"' if ok else ''} data-rv>
                    <div class="st-top"><span class="st-cnt">Etapa 1 de {len(etapas)}</span><span class="st-bar"><i></i></span></div>
                    {fs}
                    <div class="st-nav"><button type="button" class="bk" hidden><i class="fas fa-arrow-left"></i> Voltar</button>
                        <button type="button" class="btn btn-navy nx">Continuar <i class="fas fa-arrow-right"></i></button>
                        <button type="submit" class="btn btn-cta send" hidden><i class="fab fa-whatsapp"></i> {enviar}</button></div>
                </form>"""


FOOTER_FORM = stepper("rodape", [
    ("Como podemos te chamar?", "Leva menos de 1 minuto.", '<div class="flds2">' + fld("nome", "Seu nome") + fld("telefone", "Seu WhatsApp", "tel") + '</div>'),
    ("Como podemos ajudar?", "", fld("mensagem", "Escreva sua mensagem", req=False, area=True) + LGPD),
], assunto="Contato pelo rodapé do site", dark=True, enviar="Enviar mensagem")
FOOTER = f"""
    <footer class="ftr">
        <div class="wrap grid">
            <div>
                <a href="index.html" class="flogo"><img src="{LOGO}/gaia-soul-oficial-branca.png" alt="Instituto Gaia Soul"></a>
            </div>
            <div>
                <ul class="fnav">
                    <li><a href="index.html">Início</a></li>
                    <li><a href="o-instituto.html">O Instituto</a></li>
                    <li><a href="projetos.html">Projetos</a></li>
                    <li><a href="atuacao-e-impacto.html">Atuação & Impacto</a></li>
                    <li><a href="seja-um-guardiao.html">Seja um Guardião</a></li>
                    <li><a href="contato.html">Contato</a></li>
                </ul>
                <div class="fsocial">{"".join(f'<a class="{c}" href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i></a>' for u, i, n, c in SOCIAL)}</div>
            </div>
            <div class="fform">
                <h4>Fale Conosco</h4>
                {FOOTER_FORM}
            </div>
        </div>
    </footer>
    <div class="fstrip"><div class="wrap">
        <a href="{WA}" target="_blank" rel="noopener"><i class="fab fa-whatsapp"></i>{TEL}</a>
        <a href="mailto:{MAIL}"><i class="far fa-envelope"></i>{MAIL}</a>
        <a href="{GOOGLE_INSTITUTO}" target="_blank" rel="noopener"><i class="fab fa-google"></i>Avalie o Instituto no Google</a>
    </div></div>
    <div class="fbottom"><div class="wrap">
        <span>© 2026 Instituto Gaia Soul · {RAZAO} · CNPJ {CNPJ}</span>
        <a href="politica-de-privacidade.html">Política de Privacidade</a>
        <a href="termos-de-uso.html">Termos de Uso</a>
    </div></div>
    <a href="#" class="totop" aria-label="Voltar ao topo"><i class="fas fa-chevron-up"></i></a>
    <a href="{WA}" class="wpp" target="_blank" rel="noopener" aria-label="Fale com o Instituto no WhatsApp"><i class="fab fa-whatsapp"></i></a>
    <script>window.GAIA = {{ wa: "{WA_NUM}", webhook: "{LEAD_WEBHOOK}" }};</script>
    <script src="assets/js/v4.js?v={V}"></script>
</body>
</html>
"""


# =====================================================================
# BLOCOS
# =====================================================================
WAVE = '<div class="wave-b"><svg viewBox="0 0 1440 90" preserveAspectRatio="none"><path fill="#fff" d="M0 62c180-30 360-40 560-18s380 44 560 22 250-38 320-40v64H0z"/></svg></div>'


def ptop(faixa, crumb, h1, sub, corpo, img, btns="", logo="", video="", alt=""):
    midia = (f'<video muted loop playsinline autoplay preload="none" poster="{img}" data-src="{video}"></video>' if video
             else f'<img src="{img}" alt="{alt or h1}">')
    return f"""
    <section class="ptop">
        <div class="faixa" style="background-image:url('{faixa}')"></div>
        <div class="wrap">
            <div class="txt" data-rv="l">
                <p class="crumb"><a href="index.html">Início</a> / {crumb}</p>
                {f'<img class="logo-proj" src="{logo}" alt="">' if logo else ''}
                <h1>{h1}</h1>
                {f'<p class="sub">{sub}</p>' if sub else ''}
                {corpo}
                {f'<div class="btns" style="margin-top:1.6rem">{btns}</div>' if btns else ''}
            </div>
            <div class="card-img" data-rv="r">{midia}</div>
        </div>
    </section>
"""


def sec_head(eyebrow, h2, txt="", center=True, script=""):
    return f"""<div class="head{' center' if center else ''}" data-rv>
                {f'<span class="script">{script}</span>' if script else ''}{f'<span class="eyebrow">{eyebrow}</span>' if eyebrow and not script else ''}
                <h2 class="t-sec">{h2}</h2>
                {f'<p class="lead">{txt}</p>' if txt else ''}
            </div>"""


def galeria(items, cls=""):
    g = "".join(f'<figure class="g" style="margin:0"><img src="{s}" alt="{a}" loading="lazy">{f"<figcaption>{a}</figcaption>" if len(it) > 2 and it[2] else ""}</figure>'
                for it in items for s, a in [it[:2]])
    return f'<div class="galeria {cls}" data-rv>{g}</div>'


def card(p):
    return f"""<a class="card" href="projeto-{p['slug']}.html" data-rv>
                    <div class="ph"><img src="{p['card']}" alt="{p['nome']}" loading="lazy"><span class="tag">{p['tags'].split(' • ')[0]}</span></div>
                    <div class="bd"><h3>{p['nome']}</h3><p>{p['resumo']}</p><span class="btn btn-line">Conheça o projeto</span></div>
                </a>"""


def painel(p, i):
    lado = "dir" if i % 2 else ""
    vid = f'<video muted loop playsinline autoplay preload="none" poster="{p["bg"]}" data-src="{p["video"]}" aria-hidden="true"></video>' if p.get("video") else ""
    logo = f'<img class="logo-proj" src="{p["logo"]}" alt="">' if p.get("logo") else ""
    ext = (f'<p style="margin:1rem 0 0"><a class="ext" href="{p["ext"][0]}" target="_blank" rel="noopener">{p["ext"][1]} <i class="fas fa-arrow-up-right-from-square"></i></a></p>'
           if p.get("ext") else "")
    return f"""
    <section class="painel {lado}" id="{p['slug']}" style="background-image:url('{p['bg']}')">
        {vid}
        <div class="wrap">
            <div class="pcard" data-rv="{'r' if lado else 'l'}">
                {logo}<span class="tags">{p['tags']}</span>
                <h2>{p['nome']}</h2>
                <p>{p['painel']}</p>
                <div class="btns"><a href="projeto-{p['slug']}.html" class="btn btn-line">Conheça o projeto <i class="fas fa-arrow-right"></i></a></div>
                {ext}
            </div>
        </div>
    </section>"""


PAINEL_IGUAPE = dict(slug="baia-do-iguape-painel", nome="Ações na Baía do Iguape", tags="Território • Comunidades • Esporte", bg=f"{IMG4}/bg-pescador.webp",
                     painel="Desde 2019 caminhamos ao lado das famílias de pescadores e marisqueiras e das comunidades quilombolas da Baía do Iguape: esporte para os jovens, regatas de canoa, educação ambiental nas escolas e presença nas datas que importam.")


def painel_iguape(i):
    p = PAINEL_IGUAPE
    lado = "dir" if i % 2 else ""
    return f"""
    <section class="painel {lado}" id="baia-do-iguape" style="background-image:url('{p['bg']}')">
        <div class="wrap">
            <div class="pcard" data-rv="{'r' if lado else 'l'}">
                <span class="tags">{p['tags']}</span>
                <h2>{p['nome']}</h2>
                <p>{p['painel']}</p>
                <div class="btns"><a href="baia-do-iguape.html" class="btn btn-line">Conheça as ações <i class="fas fa-arrow-right"></i></a></div>
            </div>
        </div>
    </section>"""


def indicadores():
    its = "".join(f"""<div class="ind" data-rv>
                        <div class="ic"><i class="fas {ic}"></i></div>
                        <h3>{t}</h3><p>{d}</p>
                        <div class="bar" data-pct="{pct}"><i></i><span>{rot}</span></div>
                    </div>""" for ic, t, d, rot, pct in INDICADORES)
    return f'<div class="ind-wrap"><div class="ind-track">{its}</div><div class="ind-dots"></div></div>'


APOIE_LIST = f"""<div class="apoie-list">
                <a class="apoie-it" href="seja-um-guardiao.html#mensal" data-rv><span class="ic"><i class="fas fa-anchor"></i></span><div><h3>Seja um Guardião</h3><p>Uma contribuição mensal que mantém os projetos navegando o ano inteiro.</p></div></a>
                <a class="apoie-it" href="seja-um-guardiao.html#doacao" data-rv><span class="ic"><i class="fas fa-hand-holding-heart"></i></span><div><h3>Doações</h3><p>Pix ou transferência, do jeito e no valor que couber para você.</p></div></a>
                <a class="apoie-it" href="seja-um-guardiao.html#empresas" data-rv><span class="ic"><i class="fas fa-building"></i></span><div><h3>Empresas e incentivo fiscal</h3><p>Patrocínio, Lei Rouanet, ESG e investimento social com propósito.</p></div></a>
                <a class="apoie-it" href="seja-um-guardiao.html#voluntariado" data-rv><span class="ic" style="background:var(--alga)"><i class="fas fa-hands-helping"></i></span><div><h3>Voluntariado</h3><p>Seu tempo e o seu talento também transformam.</p></div></a>
            </div>"""

PARCEIROS_HTML = f"""
    <section class="parceiros">
        <div class="wrap">
            <h2>Quem navega com a gente</h2>
            <div class="logos">{"".join(f'<div class="lg"><img src="{LOGO}/{f}" alt="{n}" loading="lazy"></div>' for f, n in PARCEIROS)}</div>
        </div>
    </section>"""

FUNDADOR = f"""
    <section class="sec espuma" id="fundador">
        <div class="wrap fundador">
            <div class="foto" data-rv><img src="{IMG4}/marcelo.webp" alt="Marcelo Telles, fundador e presidente do Instituto Gaia Soul" loading="lazy"></div>
            <div data-rv="r">
                <span class="script">quem conduz essa travessia</span>
                <h2 class="t-sec">Marcelo Telles</h2>
                <p class="lead"><strong>Oceanógrafo, navegador e fundador do Instituto Gaia Soul.</strong> Foram décadas de vida no mar, em navios e travessias pelo mundo, até entender que o que ele viu lá fora precisava chegar a quem nunca viu o oceano de perto.</p>
                <blockquote>“Só cuidamos do que conhecemos. Por isso a nossa missão é aproximar as pessoas do oceano.”</blockquote>
            </div>
        </div>
    </section>"""

ODS = f"""
    <section class="sec ods center">
        <div class="wrap">
            {sec_head("", "Alinhados aos Objetivos de Desenvolvimento Sustentável", "Nossos projetos conversam com a Agenda 2030 da ONU e com a Década da Ciência Oceânica.", script="um compromisso global")}
            <img src="{IMG4}/ods.webp" alt="Objetivos de Desenvolvimento Sustentável da ONU" loading="lazy" data-rv>
        </div>
    </section>"""


def cta_band(h2, txt, btns):
    return f"""
    <section class="cta-band">
        <div class="wrap" data-rv>
            <h2>{h2}</h2>
            <p class="lead" style="max-width:640px;margin:0 auto 1.6rem">{txt}</p>
            <div class="btns center">{btns}</div>
        </div>
    </section>"""


CTA_GUARDIAO = cta_band("Seja um Guardião do Gaia Soul.",
                        "Cada pessoa que embarca leva a Cultura Oceânica mais longe: para mais escolas, mais comunidades e mais gente que nunca viu o mar de perto.",
                        '<a href="seja-um-guardiao.html" class="btn btn-cta">Quero ser Guardião</a><a href="contato.html" class="btn btn-line">Fale com a gente</a>')

# ---------------------------------------------------------------------
# Blocos da estrutura de copy do v3 (documento da Milena) + reunião 28-09
# ---------------------------------------------------------------------
HISTORIAS = [  # imagem (None = sem foto, por direito de imagem), onde, título, texto
    (f"{IMG}/rsf-2.webp", "Time Real São Francisco · Cachoeira (BA)", "65 jovens, um time e um vice-campeonato",
     "Com treinador, uniformes, bolas e lanche garantidos pelo Instituto, o Real São Francisco reúne 65 jovens de 12 a 17 anos. Em 2025, chegou ao vice-campeonato."),
    (f"{IMG}/pescadores-3.webp", "Ações sociais · Baía do Iguape", "803 famílias de pescadores e marisqueiras",
     "Apoiamos a Associação de Pescadores e Marisqueiras de Cachoeira, que reúne 803 famílias, e estamos presentes nas datas que importam para as comunidades tradicionais do território."),
    (f"{IMG4}/jiujitsu-atletas.webp", "Esporte · Baía do Iguape e Salvador", "Campeãs baianas de jiu-jitsu",
     "As irmãs gêmeas Larissa e Stella encontraram no esporte um caminho de disciplina, pertencimento e conquista, e se tornaram campeãs baianas de jiu-jitsu."),
]


def historias_html(items=HISTORIAS):
    out = []
    for img, onde, tit, txt in items:
        ph = (f'<div class="ph"><img src="{img}" alt="{tit}" loading="lazy"></div>' if img
              else '<div class="ph ph-ic"><i class="fas fa-medal"></i></div>')
        out.append(f'<article class="motivo" data-rv>{ph}<div class="bd"><span class="eyebrow">{onde}</span><h3>{tit}</h3><p>{txt}</p></div></article>')
    return '<div class="motivos">' + "".join(out) + "</div>"


CAPTACAO = [
    dict(nome="Imersão Azul", tags="Educação • Cultura Oceânica", img=f"{IMG4}/imersao-livros-card.webp", link="projeto-imersao-azul.html",
         resumo="Leve o oceano para dentro das escolas.", meta=[("Modalidade", "Lei Rouanet"), ("Status", "Em captação"), ("Território", "Bahia"), ("Público", "Estudantes e professores")]),
    dict(nome="Esporte na Baía do Iguape", tags="Esporte • Educação • Impacto social", img=f"{IMG}/rsf-4.webp", link="baia-do-iguape.html",
         resumo="Mantenha em campo o Real São Francisco e as regatas da Baía do Iguape.", meta=[("Status", "Em captação"), ("Território", "Baía do Iguape (BA)"), ("Público", "Crianças e jovens")]),
    dict(nome="Mundo Submarino 360°", tags="Tecnologia • Experiência imersiva", img=f"{IMG4}/mundo-submarino-estande.webp", link="projeto-mundo-submarino-360.html",
         resumo="Leve o fundo do mar para aeroportos, shoppings e eventos com a sua marca.", meta=[("Modalidade", "Patrocínio"), ("Status", "Aberto a parceiros"), ("Público", "Grande público")]),
]


def captacao_html():
    out = []
    for c in CAPTACAO:
        dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["meta"])
        out.append(f"""<article class="motivo capt" data-rv>
                    <div class="ph"><img src="{c['img']}" alt="{c['nome']}" loading="lazy"></div>
                    <div class="bd"><span class="eyebrow">{c['tags']}</span><h3>{c['nome']}</h3><p>{c['resumo']}</p><dl>{dl}</dl>
                        <div class="btns"><a href="contato.html?assunto=Parcerias%20e%20patroc%C3%ADnios" class="btn btn-cta">Apoiar este projeto</a><a href="{c['link']}" class="more">Conhecer <i class="fas fa-arrow-right"></i></a></div></div>
                </article>""")
    return '<div class="motivos">' + "".join(out) + "</div>"


DIARIO = [  # categoria, imagem, título, link
    ("Projetos", f"{IMG}/rsf-1.webp", "Real São Francisco em campo no Campeonato Cachoeirano 2026", "baia-do-iguape.html"),
    ("Eventos", f"{IMG}/bordejo-premiacao.webp", "Bordejos e regatas de canoa na Baía do Iguape", "baia-do-iguape.html"),
    ("Bastidores", f"{IMG}/prefeitura-1.webp", "Realidade virtual apresentada à Prefeitura de Cachoeira", "projeto-submarino-imersivo.html"),
    ("Notícias", f"{IMG}/escola-1.webp", "Dia das Crianças com educação ambiental nas escolas", "baia-do-iguape.html"),
    ("Ciência & Oceano", f"{IMG4}/tartaruga.webp", "Os 7 princípios da Cultura Oceânica", "o-instituto.html#proposito"),
    ("Projetos", f"{IMG4}/imersao-sala.webp", "Imersão Azul: o oceano dentro da sala de aula", "projeto-imersao-azul.html"),
]


def diario_html(items):
    return '<div class="cards">' + "".join(f"""<a class="card" href="{link}" data-rv>
                    <div class="ph"><img src="{img}" alt="{tit}" loading="lazy"><span class="tag">{cat}</span></div>
                    <div class="bd" style="text-align:left;align-items:flex-start"><h3>{tit}</h3><span class="more">Ler <i class="fas fa-arrow-right"></i></span></div>
                </a>""" for cat, img, tit, link in items) + "</div>"


NEWSLETTER = f"""
    <section class="sec areia" id="noticias">
        <div class="wrap nl">
            <div data-rv="l">
                <span class="script">notícias de bordo</span>
                <h2 class="t-sec">Receba nossas Notícias de Bordo.</h2>
                <p class="lead">Projetos, histórias, oportunidades e conteúdos sobre o oceano direto no seu WhatsApp.</p>
            </div>
            <form class="form js-lead" data-assunto="Quero receber as Notícias de Bordo" data-ok="Pronto! Abrimos o WhatsApp com o seu pedido." data-rv="r">
                <div class="row"><input name="nome" placeholder="Nome" aria-label="Nome" required><input name="telefone" type="tel" placeholder="WhatsApp" aria-label="WhatsApp" required></div>
                <label class="chk"><input type="checkbox" required> <span>Concordo com a <a href="politica-de-privacidade.html">Política de Privacidade</a>.</span></label>
                <button class="btn btn-navy" type="submit">Quero receber</button>
                <div class="ok"></div>
            </form>
        </div>
    </section>"""

EIXOS_HOME = [
    ("01", "Conhecer", "Cultura Oceânica e educação", "Traduzimos a ciência do oceano em experiências educativas acessíveis, capazes de despertar curiosidade, consciência e pertencimento.",
     f"{IMG4}/palestra-7.webp", [("projeto-imersao-azul.html", "Imersão Azul"), ("projeto-palestras.html", "Palestras")]),
    ("02", "Experimentar", "Tecnologia e experiências imersivas", "Realidade virtual, audiovisual e experiências sensoriais para que qualquer pessoa possa conhecer e viver o universo oceânico.",
     f"{IMG4}/sub-familia.webp", [("projeto-mundo-submarino-360.html", "Mundo Submarino 360°"), ("projeto-submarino-imersivo.html", "Submarino Imersivo")]),
    ("03", "Conectar", "Oceanoterapia e bem-estar", "Experiências que estimulam a reconexão consciente com a água e com a natureza, promovendo presença e bem-estar.",
     f"{IMG4}/mata/mata-05314.webp", [("projeto-oceanoterapia.html", "Oceanoterapia"), ("projeto-mata-quantica.html", "Mata Quântica")]),
    ("04", "Transformar", "Territórios e regeneração", "Iniciativas ligadas à realidade social, ambiental e cultural dos territórios e das suas comunidades.",
     f"{IMG}/rsf-2.webp", [("baia-do-iguape.html", "Ações na Baía do Iguape"), ("atuacao-e-impacto.html#quem-apoiamos", "Quem apoiamos")]),
]


def eixos_cards(extra=None):
    out = []
    for i, (n, v, sub, t, img, links) in enumerate(EIXOS_HOME):
        res = f'<p style="margin-top:.6rem"><i class="fas fa-check" style="color:var(--verde-agua)"></i> {extra[i]}</p>' if extra else ""
        lk = " · ".join(f'<a class="more" href="{h}">{nm}</a>' for h, nm in links)
        out.append(f"""<div class="motivo" data-rv>
                    <div class="ph"><img src="{img}" alt="{v}" loading="lazy"></div>
                    <div class="bd"><span class="eyebrow">{n} · {sub}</span><h3 class="t-eixo">{v}</h3><p>{t}</p>{res}<p style="margin-top:.8rem">{lk}</p></div>
                </div>""")
    return '<div class="motivos m2">' + "".join(out) + "</div>"


GUARDIOES_SEC = f"""
    <section class="apoie-sec guardioes" id="guardioes">
        <div class="wrap">
            <div class="head center light" data-rv>
                <span class="script" style="color:var(--piscina)">todo mundo a bordo</span>
                <h2 class="t-sec" style="color:#fff">O oceano é grande.<br>Nossos Guardiões também podem ser.</h2>
                <p class="lead" style="color:#cfe0ea">Os Guardiões Gaia Soul são pessoas, empresas e organizações que escolheram navegar com a gente. Cada pessoa que embarca fortalece a nossa capacidade de levar Cultura Oceânica, educação e experiências transformadoras para mais gente e mais territórios.</p>
            </div>
            <div class="blocos-g">
                <div class="bloco-g" data-rv="l"><i class="fas fa-anchor"></i><h3>Quero ser um Guardião</h3><p>Contribua todo mês ou de forma pontual e ajude os nossos projetos a seguirem navegando.</p><span class="chips">Apoio mensal • Pix • Imposto de Renda • Voluntariado</span><a href="seja-um-guardiao.html" class="btn btn-cta">Quero ser Guardião</a></div>
                <div class="bloco-g" data-rv="r"><i class="fas fa-ship"></i><h3>Quero embarcar minha empresa</h3><p>Sua empresa pode apoiar projetos e construir impacto com a gente de diferentes formas.</p><span class="chips">Lei Rouanet • Patrocínio • Investimento Social Privado • ESG • Programas Corporativos</span><a href="seja-um-guardiao.html#empresas" class="btn btn-white">Quero apoiar como empresa</a></div>
            </div>
            <p class="center" style="margin-top:2rem"><a href="seja-um-guardiao.html" class="more" style="color:#fff">Conheça todas as formas de ser um Guardião <i class="fas fa-arrow-right"></i></a></p>
        </div>
    </section>"""


def cta_final(h2="Tem lugar para você entre os Guardiões.", txt="Pessoas, empresas, escolas, comunidades e organizações podem ajudar a construir uma sociedade mais conectada ao oceano.", img=f"{IMG4}/bg-baleia.webp",
              btns='<a href="seja-um-guardiao.html" class="btn btn-cta">Seja um Guardião</a><a href="projetos.html" class="btn btn-line-white">Conheça nossos projetos</a>'):
    return f"""
    <section class="manifesto cta-final" style="background-image:url('{img}')">
        <div class="wrap center" data-rv>
            <h2 style="margin:0 auto 1rem;max-width:18ch">{h2}</h2>
            <p class="lead" style="color:#dbe9f1;max-width:640px;margin:0 auto 1.8rem">{txt}</p>
            <div class="btns center">{btns}</div>
        </div>
    </section>"""


# =====================================================================
# HOME (estrutura de copy do v3)
# =====================================================================
PLAIN = ' data-plain="1"'
contadores = "".join(
    f'<div class="counter" data-rv><b><span data-to="{n}"{PLAIN if plain else ""}>{n}</span></b><span>{t}</span></div>'
    for n, t, plain in CONTADORES)

index = head("Instituto Gaia Soul | O oceano nos conecta",
             "O Instituto Gaia Soul conecta pessoas ao oceano por meio da educação, cultura, ciência, tecnologia e experiências transformadoras. Imersão Azul, Mundo Submarino 360°, Oceanoterapia, Mata Quântica e ações na Baía do Iguape (BA).",
             "index.html") + f"""
    <section class="hero" style="background-image:url('{IMG4}/hero-oceano.webp')">
        <video muted loop playsinline autoplay preload="none" poster="{IMG4}/hero-oceano.webp" data-src="{VID}/hero-oceano.mp4" data-src-mobile="{VID}/hero-oceano-mobile.mp4" aria-hidden="true"></video>
        <div class="wrap">
            <h1 data-rv>O oceano nos conecta.<em>O conhecimento nos transforma.</em></h1>
            <p data-rv>Conectamos pessoas ao oceano por meio da educação, da cultura, da ciência, da tecnologia e de experiências transformadoras.</p>
            <p data-rv>Promovemos a Cultura Oceânica para ampliar conhecimento, despertar pertencimento e inspirar novas formas de cuidar de nós, das comunidades e do planeta.</p>
            <div class="btns" data-rv>
                <a href="o-instituto.html" class="btn btn-white">Conheça o Gaia Soul</a>
                <a href="projetos.html" class="btn btn-line-white">Conheça nossos projetos</a>
            </div>
        </div>
        <a href="#instituto" class="scroll-cue" aria-label="Descubra o Gaia Soul"><i class="fas fa-chevron-down fa-lg"></i></a>
        {WAVE}
    </section>

    <section class="sec" id="instituto">
        <div class="wrap grid2">
            <div class="strips s5" data-rv="l">
                <div class="s"><img src="{IMG4}/tartaruga.webp" alt="Tartaruga marinha nadando" loading="lazy"></div>
                <div class="s"><img src="{IMG4}/mata/mata-05086.webp" alt="Guardião com a camiseta do Instituto Gaia Soul" loading="lazy"></div>
                <div class="s"><img src="{IMG4}/mergulho-coral.webp" alt="Mergulhador entre corais" loading="lazy"></div>
                <div class="s"><img src="{IMG4}/golfinhos.webp" alt="Golfinhos nadando no mar" loading="lazy"></div>
                <div class="s"><img src="{IMG4}/sub-mergulho.webp" alt="Mergulho entre cardumes" loading="lazy"></div>
            </div>
            <div data-rv="r">
                <span class="script">quem somos</span>
                <h2 class="t-sec">Aproximamos pessoas do oceano para transformar futuros.</h2>
                <p class="lead">O Instituto Gaia Soul é uma organização dedicada à promoção da <strong>Cultura Oceânica</strong> e à construção de novas formas de conexão entre pessoas, oceano e sociedade.</p>
                <p class="lead">Unimos educação, ciência, cultura, tecnologia e bem-estar para transformar <strong>conhecimento em consciência e consciência em ação</strong>.</p>
                <p class="lead">Nossa atuação nasce na Bahia, um território profundamente conectado ao mar, e se expande em projetos que chegam a escolas, comunidades, empresas e a quem ainda nem conhece o oceano de perto.</p>
                <a href="o-instituto.html" class="btn btn-navy">Conheça o Instituto <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </section>

    <section class="ceu" style="background-image:url('{IMG4}/ceu.webp')">
        <img class="gaivota" src="{IMG4}/gaivota.webp" alt="" aria-hidden="true" data-fx-y="4" data-fx-blur="7" data-fx-range="20,80">
        <div class="wrap">
            <h2 data-rv>Informar, sensibilizar e <span>engajar pessoas</span> a protegerem o oceano.</h2>
        </div>
        <div class="horizonte"><img class="veleiro" src="{IMG4}/veleiro.webp" alt="" aria-hidden="true" data-fx-x="2.5" data-fx-blur="7" data-fx-range="20,50"></div>
    </section>
    <section class="mar" style="background-image:url('{IMG4}/mar-mastro.webp')">
        <div class="wrap">
            <div class="counters">{contadores}</div>
        </div>
        <div class="scallop"></div>
    </section>

    <section class="sec espuma inic" id="projetos">
        <img class="folhas" src="{IMG4}/folhas.png" alt="" aria-hidden="true" data-fx-y="4" data-fx-blur="7" data-fx-range="20,52">
        <div class="wrap">
            {sec_head("", "Propósito que vira ação.", "Criamos projetos que aproximam pessoas do oceano por diferentes caminhos: da educação às experiências imersivas, da floresta ao bem-estar. Escolha por onde quer começar.", center=False, script="nossos projetos")}
            <div class="cards">{"".join(card(p) for p in PROJETOS)}</div>
        </div>
    </section>
""" + "".join(painel(p, i) for i, p in enumerate(PROJETOS)) + painel_iguape(len(PROJETOS)) + f"""

    <section class="sec" id="atuacao">
        <div class="wrap">
            {sec_head("", "Do propósito ao impacto.", "Nossa atuação conecta Cultura Oceânica, educação, tecnologia, bem-estar e território. Caminhos diferentes, unidos por um mesmo propósito: aproximar pessoas do oceano e transformar essa conexão em conhecimento, consciência e ação.", script="como transformamos")}
            {eixos_cards()}
        </div>
    </section>

    <section class="sec espuma" id="numeros">
        <div class="wrap">
            {sec_head("", "Nosso impacto começa nas pessoas.", "Números reais do nosso trabalho junto às escolas e às comunidades da Baía do Iguape.", center=False, script="impacto em números")}
            {indicadores()}
            <div class="btns" style="margin-top:2rem"><a href="atuacao-e-impacto.html" class="btn btn-navy">Conheça nossa Atuação & Impacto <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="sec" id="territorio">
        <div class="wrap">
            {sec_head("", "Da Bahia para o oceano.", "Nossa história nasce num território profundamente conectado ao mar. Toque nos pontos do mapa e aproxime, nível por nível: da Baía de Todos-os-Santos até a nossa sede, na Mata Quântica.", script="onde estamos")}
            <div class="grid2 grid-mapa">
                {mapa_html()}
                {MAPA_INFO}
            </div>
        </div>
    </section>

    <section class="sec areia" id="historias">
        <div class="wrap">
            {sec_head("", "Por trás de cada número, existem pessoas.", "", script="histórias que movem essa maré")}
            {historias_html()}
            <div class="btns center" style="margin-top:2.4rem"><a href="atuacao-e-impacto.html#historias" class="btn btn-line">Conheça mais histórias <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>
""" + GUARDIOES_SEC + f"""

    <section class="sec" id="captacao">
        <div class="wrap">
            {sec_head("", "Projetos esperando novos tripulantes.", "Iniciativas do Instituto Gaia Soul abertas a novos parceiros, patrocinadores e apoiadores.", script="oportunidades de impacto")}
            {captacao_html()}
            <div class="btns center" style="margin-top:2.4rem"><a href="seja-um-guardiao.html#captacao" class="btn btn-navy">Ver projetos em captação</a></div>
        </div>
    </section>

    <section class="parceiros">
        <div class="wrap center">
            <span class="script" style="color:var(--piscina)">quem navega com a gente</span>
            <h2 style="margin-bottom:.6rem">Transformações maiores são construídas em conjunto.</h2>
            <p style="color:#dbe9f1;max-width:640px;margin:0 auto 2rem">Construímos relações com organizações que compartilham com a gente o compromisso de gerar impacto positivo para pessoas, comunidades e oceano.</p>
            <div class="logos">{"".join(f'<div class="lg"><img src="{LOGO}/{f}" alt="{n}" loading="lazy"></div>' for f, n in PARCEIROS)}</div>
            <div class="btns center" style="margin-top:2rem"><a href="seja-um-guardiao.html#empresas" class="btn btn-white">Seja uma organização a bordo <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="sec espuma" id="diario">
        <div class="wrap">
            {sec_head("", "Acompanhe nossa jornada.", "", center=False, script="diário de bordo")}
            {diario_html(DIARIO[:3])}
            <div class="btns" style="margin-top:2rem"><a href="diario-de-bordo.html" class="btn btn-line">Ver todas as novidades</a></div>
        </div>
    </section>
""" + NEWSLETTER + cta_final() + FOOTER

GOVERNANCA = f"""
    <section class="sec espuma" id="governanca">
        <div class="wrap grid2">
            <div data-rv="l">
                <span class="script">governança e equipe</span>
                <h2 class="t-sec">Quem conduz essa travessia.</h2>
                <p class="lead">O Instituto Gaia Soul é uma associação sem fins lucrativos, registrada como <strong>{RAZAO}</strong> (CNPJ {CNPJ}). Nossa sede funciona na Mata Quântica, na Baía do Iguape, e o escritório administrativo fica em Salvador.</p>
                <p class="lead">Nossa atuação é guiada pelos valores de ética, respeito, transparência, conscientização e preservação.</p>
                <blockquote class="edit" style="font-size:1.4rem;color:var(--abissal);margin:1.4rem 0 0">“Só cuidamos do que conhecemos. Por isso a nossa missão é aproximar as pessoas do oceano.”</blockquote>
            </div>
            <div class="team" data-rv="r">
                <div class="member"><img src="{IMG4}/marcelo.webp" alt="Marcelo Telles"><div><b>Marcelo Telles</b><span>Presidente e fundador. Oceanógrafo e navegador, com décadas de vida no mar.</span></div></div>
                <div class="member"><span class="av"><i class="fas fa-users"></i></span><div><b>Equipe e colaboradores</b><span>Educadores, pesquisadores, voluntários e parceiros técnicos que tornam cada projeto possível.</span></div></div>
                <div class="selo"><img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública"><div><small>Reconhecimento de</small><b>Utilidade Pública</b><small>Prefeitura de Cachoeira (BA)</small></div></div>
            </div>
        </div>
    </section>"""

# =====================================================================
# O INSTITUTO
# =====================================================================
instituto = head("O Instituto | Instituto Gaia Soul",
                 "Quem somos, nossa história, de onde vem o nome Gaia Soul, missão, visão e valores, os 7 princípios da Cultura Oceânica e quem conduz o Instituto.",
                 "o-instituto.html") + ptop(
    f"{IMG4}/bg-baleia.webp", "O Instituto", "O Instituto", "Aproximamos pessoas do oceano para transformar futuros.",
    """<p>O Instituto Gaia Soul nasceu em 2019, em Salvador, com um propósito simples e enorme: promover a consciência ecológica e levar a <strong>Cultura Oceânica</strong> para toda a sociedade, em especial para crianças e jovens.</p>
                <p>Unimos educação, ciência, cultura, tecnologia e bem-estar para transformar conhecimento em consciência e consciência em ação.</p>""",
    f"assets/images/ocean-gallery.png", '<a href="seja-um-guardiao.html" class="btn btn-navy">Seja um Guardião</a><a href="contato.html" class="btn btn-line">Fale Conosco</a>',
    alt="Atobá olhando para a câmera") + f"""
    <section class="manifesto" style="background-image:url('{IMG4}/mergulho-coral.webp')">
        <div class="wrap">
            <h2 data-rv>Informar, sensibilizar e <span>engajar pessoas</span> a protegerem o oceano.</h2>
            <div class="counters">{contadores}</div>
        </div>
        <div class="scallop"></div>
    </section>

    <section class="sec" id="quem-somos">
        <div class="wrap grid2">
            <div data-rv="l">
                <span class="script">quem somos</span>
                <h2 class="t-sec">Só cuidamos do que conhecemos</h2>
                <p class="lead">O Instituto Gaia Soul é uma organização sem fins lucrativos dedicada à <strong>Cultura Oceânica</strong>: o entendimento de como o oceano influencia a nossa vida e de como nós influenciamos o oceano.</p>
                <p class="lead">Nossa atuação nasce na Bahia, um território profundamente ligado ao mar, e chega a escolas, comunidades, empresas e a qualquer pessoa disposta a olhar o oceano de um jeito novo.</p>
            </div>
            <div class="strips" data-rv="r" style="height:400px">
                <div class="s"><img src="{IMG4}/mata/mata-05086.webp" alt="Guardião com a camiseta do Instituto Gaia Soul" loading="lazy"></div>
                <div class="s"><img src="assets/images/v4/bg-pescador.webp" alt="Marcelo Telles em palestra" loading="lazy"></div>
                <div class="s"><img src="assets/images/v2/baia-iguape-aerea.webp" alt="Marisqueiras da Baía do Iguape" loading="lazy"></div>
                <div class="s"><img src="assets/images/v2/escola-2.webp" alt="Vivência na Mata Quântica" loading="lazy"></div>
            </div>
        </div>
    </section>

    <section class="sec areia" id="historia">
        <div class="wrap grid2" style="align-items:start">
            <div data-rv="l">
                <span class="script">nossa história</span>
                <h2 class="t-sec">Uma travessia que começou no mar</h2>
                <ol class="timeline">
                    <li><b>2019</b>Nasce o Instituto Gaia Soul, em Salvador, para aproximar pessoas do oceano pela educação, pela ciência e por experiências transformadoras.</li>
                    <li><b>Cultura Oceânica</b>Os projetos se alinham aos 7 princípios da Cultura Oceânica e à Década das Nações Unidas da Ciência Oceânica (2021-2030).</li>
                    <li><b>Imersão Azul</b>A Cultura Oceânica chega às escolas com 11 livros autorais, realidade virtual e uma jornada gamificada.</li>
                    <li><b>Baía do Iguape</b>Começa a caminhada junto às comunidades quilombolas e às famílias de pescadores e marisqueiras, e vem o reconhecimento de Utilidade Pública pela Prefeitura de Cachoeira (BA).</li>
                    <li><b>Hoje</b>Um ecossistema de projetos que une educação, experiências imersivas, Oceanoterapia, esporte e a preservação da Mata Quântica.</li>
                </ol>
            </div>
            <div id="nome" data-rv="r">
                <span class="script">de onde vem o nome</span>
                <h2 class="t-sec">Por que Gaia Soul?</h2>
                <p class="lead"><strong>Gaia</strong> era o nome do veleiro que o Marcelo Telles construiu e com o qual fez travessias pelo oceano. Foi a bordo dele que muitas das histórias, imagens e aprendizados que hoje viram conteúdo educativo foram vividos.</p>
                <p class="lead">O barco seguiu outro rumo, mas o nome ficou: <strong>Gaia</strong>, a Terra viva, e <strong>Soul</strong>, a alma que nos liga a ela. Um lembrete de que o planeta e as pessoas são uma coisa só.</p>
            </div>
        </div>
    </section>

    <section class="sec" id="proposito">
        <div class="wrap">
            {sec_head("", "Missão, visão e valores", "O que nos move e para onde queremos navegar.", script="propósito")}
            <div class="mvv">
                <div class="it" data-rv><i class="far fa-circle-dot"></i><h3>Missão</h3><p>Informar, sensibilizar e engajar as pessoas para a Cultura Oceânica e a difusão da Oceanoterapia.</p></div>
                <div class="it" data-rv><i class="far fa-eye"></i><h3>Visão</h3><p>Sensibilizar, até 2030, a consciência ecológica de pelo menos 100 mil pessoas, com nossos conteúdos, projetos e iniciativas sociais.</p></div>
                <div class="it" data-rv><i class="far fa-star"></i><h3>Valores</h3><ul><li>Ética</li><li>Respeito</li><li>Transparência</li><li>Conscientização</li><li>Preservação</li></ul></div>
            </div>
        </div>
    </section>

    <section class="manifesto" style="background-image:url('{IMG}/baia-iguape-aerea.webp')">
        <div class="wrap grid2" style="align-items:center">
            <div data-rv="l">
                <span class="script" style="color:var(--piscina)">cultura oceânica</span>
                <h2 style="margin-bottom:1rem">70% do planeta é oceano.</h2>
                <p style="color:#dbe9f1;font-size:1.1rem">Nossos projetos seguem os 7 princípios da Cultura Oceânica, com apoio da UNESCO e da Década da Ciência Oceânica.</p>
            </div>
            <ol class="principios" data-rv="r">{"".join(f"<li>{t}</li>" for t in PRINCIPIOS)}</ol>
        </div>
        <div class="scallop"></div>
    </section>
""" + GOVERNANCA + f"""
    <section class="sec" id="territorio">
        <div class="wrap">
            {sec_head("", "Nosso território", "Da Baía de Todos-os-Santos à Mata Quântica, onde funciona a nossa sede.", script="onde estamos")}
            <div class="grid2 grid-mapa">{mapa_html()}{MAPA_INFO}</div>
        </div>
    </section>
    <div id="parceiros"></div>
""" + ODS + PARCEIROS_HTML + CTA_GUARDIAO + FOOTER

# =====================================================================
# PROJETOS (lista em painéis, igual à página antiga)
# =====================================================================
BLUE_BANK_BTN = (f'<a href="{BANCO_IMAGENS_URL}" target="_blank" rel="noopener" class="btn btn-cta">Quero doar minhas imagens</a>' if BANCO_IMAGENS_URL
                 else '<a href="contato.html?assunto=Blue%20Bank" class="btn btn-cta">Quero doar minhas imagens</a>')

projetos = head("Projetos | Instituto Gaia Soul",
                "Imersão Azul, Mundo Submarino 360°, Submarino Imersivo, Oceanoterapia, Mata Quântica, Palestras e Blue Bank: os projetos do Instituto Gaia Soul.",
                "projetos.html") + ptop(
    f"{IMG4}/sub-recife.webp", "Projetos", "Propósito que vira ação.", "Nossos projetos",
    """<p>Da educação às experiências imersivas, da floresta ao bem-estar: caminhos diferentes para aproximar pessoas do oceano. Tem livro, tem realidade virtual, tem mata preservada e tem gente.</p>
                <p>Role a página, escolha um projeto e descubra onde a sua história pode se cruzar com a nossa.</p>""",
    f"{IMG4}/tartaruga.webp", '<a href="seja-um-guardiao.html" class="btn btn-navy">Apoie um projeto</a><a href="contato.html?assunto=Projetos" class="btn btn-line">Leve um projeto até você</a>',
    alt="Tartaruga marinha") + "".join(painel(p, i) for i, p in enumerate(PROJETOS)) + painel_iguape(len(PROJETOS)) + f"""

    <section class="painel" id="blue-bank" style="background-image:url('{IMG4}/sub-mergulho.webp')">
        <div class="wrap">
            <div class="pcard" data-rv="l">
                <span class="tags">Imagens • Educação • Ciência</span>
                <h2>Blue Bank</h2>
                <p>O banco de imagens e vídeos do oceano do Instituto Gaia Soul, com foco em imagens subaquáticas e em 360°. Cada foto doada vira material educativo e chega a estudantes de todo o país.</p>
                <p><strong>Você é fotógrafo, mergulhador ou cinegrafista?</strong> Suas imagens podem ensinar muita gente a amar o mar. Colabore com o Blue Bank.</p>
                <div class="btns">{BLUE_BANK_BTN}</div>
            </div>
        </div>
    </section>
""" + cta_final("Quer apoiar nossos projetos?", "Escolas, empresas e parceiros podem levar a Cultura Oceânica a cada vez mais pessoas.", f"{IMG4}/sub-recife.webp", '<a href="seja-um-guardiao.html#captacao" class="btn btn-cta">Ver projetos em captação</a><a href="seja-um-guardiao.html" class="btn btn-line-white">Seja um Guardião</a>') + FOOTER


# =====================================================================
# PÁGINAS DE PROJETO
# =====================================================================
def pagina_projeto(p, faixa, sub, corpo, img, extra, btns=None, video="", title_extra=""):
    if btns is None:
        btns = f'<a href="contato.html?assunto=Projetos" class="btn btn-navy">Quero este projeto</a><a href="seja-um-guardiao.html" class="btn btn-line">Apoiar este projeto</a>'
    return head(f"{p['nome']} | Instituto Gaia Soul", f"{p['resumo']} {title_extra}".strip(), f"projeto-{p['slug']}.html", og=p["card"]) + ptop(
        faixa, f'<a href="projetos.html">Projetos</a> / {p["nome"]}', p["nome"], sub, corpo, img, btns, logo=p.get("logo", ""), video=video) + extra + CTA_GUARDIAO + FOOTER



LIVROS = [  # arquivo em assets/images/v4/livros, legenda
    ("fundamental-1e2-volume-1", "1º e 2º ano", "Volume 1"), ("fundamental-1e2-volume-2", "1º e 2º ano", "Volume 2"),
    ("fundamental-3a5-volume-1", "3º, 4º e 5º ano", "Volume 1"), ("fundamental-3a5-volume-2", "3º, 4º e 5º ano", "Volume 2"),
    ("fundamental-6e7-volume-1", "6º e 7º ano", "Volume 1"), ("fundamental-6e7-volume-2", "6º e 7º ano", "Volume 2"),
    ("fundamental-8e9-volume-1", "8º e 9º ano", "Volume 1"), ("fundamental-8e9-volume-2", "8º e 9º ano", "Volume 2"),
    ("ensino-medio-1serie", "Ensino Médio", "1ª série"), ("ensino-medio-2serie", "Ensino Médio", "2ª série"), ("ensino-medio-3serie", "Ensino Médio", "3ª série"),
]


def marquee_livros():
    um = "".join(f'<a class="livro" href="{IMERSAO_AZUL_URL}" target="_blank" rel="noopener"><img src="{IMG4}/livros/{f}.webp" alt="Livro Imersão Azul, {a}, {v}" loading="lazy"><b>{a}</b><small>{v}</small></a>' for f, a, v in LIVROS)
    return f'<div class="mq" data-rv><div class="mq-track">{um}<span class="mq-dup" aria-hidden="true">{um}</span></div></div>'

IMERSAO_EXT = f'<a href="{IMERSAO_AZUL_URL}" target="_blank" rel="noopener" class="btn btn-cta">Visite o site do Imersão Azul <i class="fas fa-arrow-up-right-from-square"></i></a>'
p_imersao = pagina_projeto(PMAP["imersao-azul"], f"{IMG4}/imersao-capa.webp", "O oceano dentro da sala de aula.",
    """<p>Quantas crianças brasileiras já viram uma baleia de perto? E quantas sabem que metade do oxigênio que respiram vem do mar? O <strong>Imersão Azul</strong> nasceu para mudar essas respostas.</p>
                <p>É uma jornada educativa completa que leva a Cultura Oceânica para dentro das escolas, alinhada à <strong>BNCC</strong> e à <strong>Década do Oceano</strong> da ONU: livros autorais, realidade virtual, plataforma digital, jornada gamificada e formação de professores, do 1º ano ao Ensino Médio.</p>""",
    f"{IMG4}/imersao-vr-menino.webp", f"""
    <section class="sec colecao">
        <div class="wrap">
            {sec_head("", "11 livros. Do 1º ano ao Ensino Médio.", "Uma coleção autoral de Cultura Oceânica, escrita a partir de experiências reais no mar e pensada para cada fase da vida escolar.", script="a coleção cultura oceânica")}
        </div>
        {marquee_livros()}
        <div class="wrap">
            <div class="selos-imersao" data-rv>
                <div><b>11</b><span>livros autorais</span></div>
                <div><b>BNCC</b><span>alinhados à Base Nacional Comum Curricular</span></div>
                <div><b>2021-2030</b><span>Década da Ciência Oceânica da ONU</span></div>
                <div><b>1º ano ao EM</b><span>do Fundamental ao Ensino Médio</span></div>
            </div>
        </div>
    </section>
    <section class="sec espuma">
        <div class="wrap">
            {sec_head("", "Como funciona o Imersão Azul", "Um ecossistema de aprendizagem que transforma ciência em curiosidade e curiosidade em cuidado.", script="a jornada")}
            <div class="formas">
                <div class="forma" data-rv><span class="ic"><i class="fas fa-book-open"></i></span><h3>Livros autorais</h3><p>11 volumes de Cultura Oceânica, do 1º ano ao Ensino Médio, com conteúdo que nasce de vivências reais no mar.</p></div>
                <div class="forma teal" data-rv><span class="ic"><i class="fas fa-vr-cardboard"></i></span><h3>Realidade virtual</h3><p>Com os óculos, os estudantes mergulham em recifes, nadam com tartarugas e visitam ecossistemas que só conheciam por foto.</p></div>
                <div class="forma verde" data-rv><span class="ic"><i class="fas fa-gamepad"></i></span><h3>Plataforma e jornada gamificada</h3><p>Desafios, conteúdos digitais e conquistas que mantêm a turma engajada durante todo o ano letivo.</p></div>
                <div class="forma cta" data-rv><span class="ic"><i class="fas fa-chalkboard-user"></i></span><h3>Formação de professores</h3><p>Educadores recebem material, apoio e certificado para levar o oceano para as suas aulas com segurança.</p></div>
            </div>
        </div>
    </section>
    <section class="sec">
        <div class="wrap">
            {sec_head("", "O Imersão Azul na prática", "", center=False, script="em sala de aula")}
            <div class="galeria-imersao" data-rv>
                <figure class="g big"><img src="{IMG4}/imersao-sala.webp" alt="Turma em aula do Imersão Azul" loading="lazy"><figcaption>Cultura Oceânica em sala de aula</figcaption></figure>
                <figure class="g"><img src="{IMG4}/imersao-vr-menino.webp" alt="Estudante com óculos de realidade virtual" loading="lazy"><figcaption>Mergulho em realidade virtual</figcaption></figure>
                <figure class="g"><img src="{IMG}/prefeitura-2.webp" alt="Realidade virtual apresentada em Cachoeira" loading="lazy"><figcaption>Realidade virtual apresentada em Cachoeira</figcaption></figure>
                <figure class="g wide"><img src="{IMG4}/imersao-capa.webp" alt="Ilustração: sala de aula dentro do oceano" loading="lazy"><figcaption>E se o fundo do mar coubesse na sala de aula?</figcaption></figure>
            </div>
            <div class="btns center" style="margin-top:2.4rem">{IMERSAO_EXT}<a href="contato.html?assunto=Escolas" class="btn btn-line">Quero o Imersão Azul na minha escola</a></div>
        </div>
    </section>""")

p_mundo = pagina_projeto(PMAP["mundo-submarino-360"], f"{IMG4}/sub-recife.webp", "Mergulhe, explore, relaxe.",
    """<p>Imagine estar no saguão de um aeroporto, sentar numa poltrona, colocar os óculos e, de repente, estar a vinte metros de profundidade, rodeado por cardumes.</p>
                <p>O <strong>Mundo Submarino 360°</strong> é uma experiência de realidade virtual que transporta o público para o universo subaquático. Levamos o estande a <strong>aeroportos, shopping centers e eventos</strong>, com audiovisual de ponta e um conteúdo que ensina enquanto encanta.</p>""",
    f"{IMG}/hf-09-360-aeroporto.webp", f"""
    <section class="sec">
        <div class="wrap grid2">
            <div class="video-box" data-rv="l"><video controls playsinline preload="none" poster="{IMG4}/mundo-submarino-estande.webp" src="{VID}/mundo-submarino-estande.mp4"></video></div>
            <div data-rv="r">
                <span class="script">a experiência</span>
                <h2 class="t-sec">O oceano onde as pessoas estão</h2>
                <p class="lead">Em poucos minutos, quem passa pelo estande sai diferente: com vontade de saber mais, de cuidar e de contar para alguém o que viu.</p>
                <ul class="contatos" style="margin-top:1rem"><li><i class="fas fa-check"></i> Experiência inédita e memorável</li><li><i class="fas fa-check"></i> Impacto visual e sensorial</li><li><i class="fas fa-check"></i> Conteúdo educativo sobre o oceano</li><li><i class="fas fa-check"></i> Ideal para ativação de marcas com propósito</li></ul>
            </div>
        </div>
    </section>
    <section class="sec espuma"><div class="wrap">{galeria([(f"{IMG}/hf-10-360-frente.webp", "Estande Mundo Submarino 360° visto de frente"), (f"{IMG}/hf-11-360-interior.webp", "Interior do Mundo Submarino 360°"), (f"{IMG4}/sub-familia.webp", "Família vivendo a experiência"), (f"{IMG4}/sub-recife.webp", "Recife em realidade virtual")], "wide")}</div></section>""",
    btns='<a href="contato.html?assunto=Experiências" class="btn btn-navy">Quero levar ao meu espaço</a><a href="seja-um-guardiao.html#empresas" class="btn btn-line">Patrocinar</a>',
    video=f"{VID}/mundo-submarino-loop.mp4")

p_sub = pagina_projeto(PMAP["submarino-imersivo"], f"{IMG4}/sub-mergulho.webp", "Uma expedição coletiva ao fundo do mar.",
    """<p>Dentro de uma estrutura que simula um submarino de verdade, com escotilhas, luzes e sons do oceano, turmas inteiras partem juntas numa expedição.</p>
                <p>Com a <strong>realidade virtual</strong>, os visitantes exploram ecossistemas marinhos, conhecem espécies e entendem, na prática, por que o oceano é essencial para a vida no planeta. Perfeito para <strong>escolas, feiras e eventos</strong>.</p>""",
    f"{IMG4}/sub-dentro.webp", f"""
    <section class="sec espuma"><div class="wrap">{galeria([(f"{IMG}/submarino-1.webp", "Submarino imersivo com escotilhas"), (f"{IMG}/submarino-2.webp", "Submarino imersivo visto de lado"), (f"{IMG}/submarino-3.webp", "Entrada do submarino"), (f"{IMG4}/sub-dentro.webp", "Interior do submarino")])}</div></section>""",
    btns='<a href="contato.html?assunto=Escolas" class="btn btn-navy">Quero na minha escola ou evento</a><a href="seja-um-guardiao.html" class="btn btn-line">Apoiar este projeto</a>')

p_oceano = pagina_projeto(PMAP["oceanoterapia"], f"{IMG4}/golfinhos.webp", "O oceano educa de um jeito diferente.",
    """<p>Ele ensina ritmo, pausa, escuta e pertencimento. A <strong>Oceanoterapia</strong> usa a conexão consciente com a água e com a natureza como caminho para presença, equilíbrio e bem-estar.</p>
                <p>E tem um efeito colateral bonito: <strong>quem se reconecta com o mar passa a querer protegê-lo</strong>.</p>""",
    f"assets/images/v2/hf-12-oceanoterapia.webp", f"""
    <section class="sec">
        <div class="wrap">
            {sec_head("", "Vivências de Oceanoterapia", "Experiências guiadas no mar e na Mata Quântica, para grupos, empresas e escolas.", script="como acontece")}
            <div class="caixas">
                <div class="caixa" data-rv><h3><i class="fas fa-water" style="color:var(--ciano)"></i> Flutuação consciente</h3><p>Boiar em segurança, sentir o corpo sustentado pela água e desacelerar a mente.</p></div>
                <div class="caixa" data-rv><h3><i class="fas fa-wind" style="color:var(--ciano)"></i> Respiração no ritmo das ondas</h3><p>Práticas de respiração e atenção plena conduzidas à beira-mar.</p></div>
                <div class="caixa" data-rv><h3><i class="fas fa-tree" style="color:var(--ciano)"></i> Banho de floresta</h3><p>Caminhadas contemplativas pela Mata Atlântica preservada da Mata Quântica.</p></div>
                <div class="caixa" data-rv><h3><i class="fas fa-briefcase" style="color:var(--ciano)"></i> Programas corporativos</h3><p>Bem-estar e Cultura Oceânica para equipes, com vivências que viram assunto na empresa por meses.</p></div>
            </div>
        </div>
    </section>
    <section class="sec espuma"><div class="wrap">{galeria([(f"{IMG4}/ia-boiando.webp", "Flutuação consciente no mar"), (f"{IMG4}/aquaterapia.webp", "Banho de cachoeira"), (f"{IMG4}/ia-maos-agua.webp", "Presença e conexão com a água"), (f"{IMG4}/ia-grupo-respiracao.webp", "Respiração no ritmo das ondas")])}</div></section>
    <section class="sec areia" id="ebook">
        <div class="wrap grid2 ebook-oceano">
            <a class="ebook-capa" href="{OCEANO_EBOOK_URL}" target="_blank" rel="noopener" data-rv="l"><img src="{IMG4}/ebook-oceanoterapia-capa.webp" alt="Capa do e-book Oceanoterapia: o poder restaurador da água, de Marcelo Dantas Telles" loading="lazy"></a>
            <div data-rv="r">
                <span class="script">e-book gratuito</span>
                <h2 class="t-sec">Sua mente está cheia demais?</h2>
                <p class="lead">No e-book <strong>Oceanoterapia: o poder restaurador da água</strong>, Marcelo Dantas Telles transforma décadas de vida no mar em um guia prático para desacelerar, respirar e voltar a se sentir presente.</p>
                <p class="lead">Antes de receber, responda a um quiz rápido e descubra o seu <strong>nível de saturação mental</strong>. O diagnóstico e o e-book chegam na hora.</p>
                <ul class="contatos" style="margin:1rem 0 1.6rem"><li><i class="fas fa-check"></i> Diagnóstico do seu nível de saturação mental</li><li><i class="fas fa-check"></i> E-book completo em PDF ou para ler online</li><li><i class="fas fa-check"></i> Gratuito</li></ul>
                <a href="{OCEANO_EBOOK_URL}" target="_blank" rel="noopener" class="btn btn-cta">Fazer o quiz e receber o e-book <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </section>""",
    btns='<a href="contato.html?assunto=Experiências" class="btn btn-navy">Quero viver a Oceanoterapia</a><a href="contato.html?assunto=Parcerias%20e%20patroc%C3%ADnios" class="btn btn-line">Levar para a minha empresa</a>')

p_mata = pagina_projeto(PMAP["mata-quantica"], f"{IMG4}/mata/mata-04522.webp", "Onde a floresta encontra o mar.",
    """<p>A Mata Atlântica é o segundo bioma mais ameaçado do mundo, e o desmatamento dela já avançou mais rápido que o da Amazônia.</p>
                <p>Diante disso, destinamos <strong>100 hectares de floresta preservada</strong> às margens da Baía do Iguape, em processo para se tornar uma <strong>Reserva Particular do Patrimônio Natural (RPPN)</strong>. É aqui que funciona a sede do Instituto e onde acontecem retiros, vivências e encontros.</p>""",
    f"assets/images/v4/mata/mata-04522.webp", f"""
    <section class="sec">
        <div class="wrap grid2">
            <div data-rv="l">
                <span class="script">hospedagem com propósito</span>
                <h2 class="t-sec">Quem se hospeda também protege</h2>
                <p class="lead">A Mata Quântica recebe grupos, famílias e empresas para hospedagens e experiências na natureza. <strong>Parte do valor de cada hospedagem é destinada aos projetos do Instituto Gaia Soul.</strong></p>
                <div class="btns"><a href="{MATA_URL}" target="_blank" rel="noopener" class="btn btn-cta">Conheça a Mata Quântica <i class="fas fa-arrow-up-right-from-square"></i></a></div>
            </div>
            {galeria([(f"assets/images/v4/mata-casa.webp", "Casa na Mata Quântica"), (f"{IMG4}/mata/mata-05328.webp", "Piscina natural"), (f"assets/images/v2/baia-iguape-aerea.webp", "Encontros e retiros"), (f"{IMG4}/mata/mata-05167.webp", "Vivências ao ar livre")], "wide g2")}
        </div>
    </section>
    <section class="sec espuma">
        <div class="wrap">
            {sec_head("", "Veja onde fica", "Da Baía de Todos-os-Santos até a Mata Quântica.", script="no mapa")}
            <div class="grid2 grid-mapa">{mapa_html()}{MAPA_INFO}</div>
        </div>
    </section>""",
    btns=f'<a href="{MATA_URL}" target="_blank" rel="noopener" class="btn btn-navy">Site da Mata Quântica</a><a href="contato.html?assunto=Experiências" class="btn btn-line">Retiros e vivências</a>')

p_palestras = pagina_projeto(PMAP["palestras"], f"{IMG4}/bg-baleia.webp", "Educação e conscientização ambiental.",
    """<p>Marcelo Telles é oceanógrafo e passou boa parte da vida em alto mar. Das travessias, tempestades e encontros com a vida marinha nasceram palestras que <strong>emocionam, ensinam e mudam comportamentos</strong>.</p>
                <p>Ele já palestrou em congressos internacionais, eventos de grande público, escolas e empresas, levando a educação oceânica para ambientes corporativos e educacionais.</p>""",
    f"{IMG4}/palestra-4.webp", f"""
    <section class="sec"><div class="wrap">{galeria([g for g in GAL_PALESTRAS if "palestra-4" not in g[0]])}</div></section>
    <section class="sec espuma">
        <div class="wrap caixas">
            <div class="caixa" data-rv style="background:#fff"><h3>A conexão com o mar: um convite à reflexão</h3><p>As histórias vividas em alto mar viram fonte de inspiração. Entre os temas:</p><ul><li><strong>Oceano e ecossistemas costeiros:</strong> como o litoral e a saúde do planeta estão ligados.</li><li><strong>Mudanças climáticas:</strong> o que já está acontecendo e o que podemos fazer.</li><li><strong>Sustentabilidade no dia a dia:</strong> práticas simples para pessoas e empresas.</li></ul></div>
            <div class="caixa" data-rv style="background:#fff"><h3>Escolas: impacto que forma cidadãos</h3><p>Nas escolas, as palestras despertam curiosidade e responsabilidade nas novas gerações:</p><ul><li><strong>Dinâmicas e debates ecológicos.</strong></li><li><strong>Projetos escolares e comunitários.</strong></li><li><strong>Palestras imersivas com óculos de realidade virtual,</strong> para explorar recifes e ver de perto os impactos da poluição.</li></ul></div>
            <div class="caixa" data-rv style="background:#fff"><h3>Empresas: sustentabilidade como estratégia</h3><ul><li><strong>Responsabilidade social empresarial (ESG).</strong></li><li><strong>Redução da pegada de carbono.</strong></li><li><strong>Inovação verde e cultura de cuidado.</strong></li><li><strong>SIPAT e semanas de meio ambiente.</strong></li></ul></div>
            <div class="caixa navy" data-rv><h3>Impacto e objetivos</h3><p>Capacitar pessoas e empresas a adotarem comportamentos mais conscientes, criando um ciclo virtuoso de cuidado com o meio ambiente, com conhecimento prático, vivências reais e dados científicos.</p></div>
        </div>
    </section>""",
    btns='<a href="contato.html?assunto=Palestras" class="btn btn-navy">Quero uma palestra</a><a href="contato.html?assunto=Escolas" class="btn btn-line">Palestra na minha escola</a>')

# =====================================================================
# ATUAÇÃO & IMPACTO
# =====================================================================
EIXOS = [
    ("01", "Conhecer", "Cultura Oceânica e educação", "Traduzimos a ciência do oceano em experiências educativas acessíveis, que despertam curiosidade, consciência e pertencimento.",
     f"{IMG4}/imersao-sala.webp", [("projeto-imersao-azul.html", "Imersão Azul"), ("projeto-palestras.html", "Palestras")]),
    ("02", "Experimentar", "Tecnologia e experiências imersivas", "Realidade virtual, audiovisual e experiências sensoriais para que qualquer pessoa possa viver o universo oceânico.",
     f"{IMG4}/sub-familia.webp", [("projeto-mundo-submarino-360.html", "Mundo Submarino 360°"), ("projeto-submarino-imersivo.html", "Submarino Imersivo")]),
    ("03", "Conectar", "Oceanoterapia e bem-estar", "Experiências que estimulam a reconexão consciente com a água e com a natureza, promovendo presença e bem-estar.",
     f"{IMG4}/mata/mata-04739.webp", [("projeto-oceanoterapia.html", "Oceanoterapia"), ("projeto-mata-quantica.html", "Mata Quântica")]),
    ("04", "Transformar", "Territórios e regeneração", "Iniciativas ligadas à realidade social, ambiental e cultural dos territórios e das suas comunidades.",
     f"{IMG4}/iguape-4.webp", [("baia-do-iguape.html", "Ações na Baía do Iguape"), ("#quem-apoiamos", "Quem apoiamos")]),
]
eixos_html = "".join(f"""<div class="motivo" data-rv>
                    <div class="ph"><img src="{img}" alt="{v}" loading="lazy"></div>
                    <div class="bd"><span class="eyebrow">{n} · {sub}</span><h3 style="font-family:var(--f-hero);font-size:2.4rem;line-height:1">{v}</h3><p>{t}</p>
                        <p style="margin-top:.8rem">{" · ".join(f'<a class="more" href="{h}">{nm}</a>' for h, nm in links)}</p></div>
                </div>""" for n, v, sub, t, img, links in EIXOS)

atuacao = head("Atuação & Impacto | Instituto Gaia Soul",
               "Conhecer, experimentar, conectar e transformar: os quatro eixos do Instituto Gaia Soul, nossos números, o território na Baía do Iguape e quem apoiamos.",
               "atuacao-e-impacto.html") + ptop(
    f"{IMG4}/bg-pescador.webp", "Atuação & Impacto", "Do propósito ao impacto", "Conhecimento que vira consciência. Consciência que vira ação.",
    """<p>Nossa atuação conecta Cultura Oceânica, educação, tecnologia, bem-estar e território. São caminhos diferentes com um mesmo destino: aproximar as pessoas do oceano e transformar essa conexão em mudança real.</p>""",
    f"{IMG4}/iguape-1.webp", '<a href="seja-um-guardiao.html" class="btn btn-navy">Seja um Guardião</a><a href="baia-do-iguape.html" class="btn btn-line">Ações na Baía do Iguape</a>',
    alt="Comunidade reunida na Baía do Iguape") + f"""
    <section class="sec" id="eixos">
        <div class="wrap">
            {sec_head("", "Os quatro eixos da nossa atuação", "Conhecer, experimentar, conectar e transformar.", script="como transformamos")}
            {eixos_cards(["11 livros didáticos autorais, alinhados à BNCC e à Década do Oceano.", "Experiências levadas a escolas, aeroportos e shopping centers.", "Vivências no mar, práticas contemplativas e 100 hectares de Mata Atlântica.", "2 comunidades quilombolas e 803 famílias de pescadores e marisqueiras."])}
        </div>
    </section>

    <section class="manifesto" id="numeros" style="background-image:url('{IMG4}/baia-iguape.webp')">
        <div class="wrap">
            <h2 data-rv>Nosso impacto começa <span>nas pessoas.</span></h2>
            <div class="counters">
                <div class="counter" data-rv><b><span data-to="803">803</span></b><span>famílias de pescadores e marisqueiras apoiadas</span></div>
                <div class="counter" data-rv><b><span data-to="65">65</span></b><span>jovens atletas no Real São Francisco</span></div>
                <div class="counter" data-rv><b><span data-to="2">2</span></b><span>comunidades quilombolas na Baía do Iguape</span></div>
                <div class="counter" data-rv><b><span data-to="11">11</span></b><span>livros autorais de Cultura Oceânica</span></div>
            </div>
        </div>
        <div class="scallop"></div>
    </section>

    <section class="sec" id="territorio">
        <div class="wrap">
            {sec_head("", "Nosso território", "Atuamos dentro da APA da Baía de Todos-os-Santos, na Reserva Extrativista da Baía do Iguape, onde fica a nossa sede na Mata Quântica.", script="onde estamos")}
            <div class="grid2 grid-mapa">{mapa_html()}{MAPA_INFO}</div>
        </div>
    </section>

    <section class="sec espuma" id="indicadores">
        <div class="wrap">
            {sec_head("", "Por trás de cada número, existem pessoas", "", center=False, script="indicadores")}
            {indicadores()}
        </div>
    </section>

    <section class="sec areia" id="historias">
        <div class="wrap">
            {sec_head("", "Por trás de cada número, existem pessoas.", "", script="histórias de impacto")}
            {historias_html()}
            <div class="btns center" style="margin-top:2.4rem"><a href="baia-do-iguape.html" class="btn btn-navy">Ver as ações na Baía do Iguape <i class="fas fa-arrow-right"></i></a></div>
        </div>
    </section>

    <section class="sec" id="quem-apoiamos">
        <div class="wrap apoiamos">
            <div data-rv="l">
                <span class="script">esporte que transforma</span>
                <h2 class="t-sec">Quem apoiamos</h2>
                <p>Esporte e educação caminham juntos para formar não só atletas, mas cidadãos conscientes do papel do oceano na vida de todos.</p>
            </div>
            <div class="apoio-cards">
                <div class="apoio" data-rv><div class="ph"><img src="{LOGO}/real-sao-francisco.png" alt="Esporte Clube Real São Francisco" loading="lazy"></div><h3>Real São Francisco</h3><p>65 jovens de 12 a 17 anos, com treinador, uniformes, bolas e lanche. Vice-campeões em 2025.</p></div>
                <div class="apoio" data-rv><div class="ph"><img src="{IMG4}/jiujitsu-atletas.webp" alt="Atletas de jiu-jitsu de costas, com kimono azul" loading="lazy" style="height:150px;width:auto;object-fit:cover"></div><h3>Jiu-jitsu</h3><p>As irmãs gêmeas Larissa e Stella encontraram no esporte um caminho de disciplina e pertencimento e se tornaram campeãs baianas.</p></div>
                <div class="apoio" data-rv><div class="ph"><span class="ic"><i class="fas fa-sailboat"></i></span></div><h3>Vela e canoa</h3><p>Escolinha de vela e as regatas de canoa da Baía do Iguape, os bordejos.</p></div>
            </div>
        </div>
    </section>

    <section class="sec areia" id="utilidade-publica">
        <div class="wrap grid2">
            <div data-rv="l">
                <span class="script">reconhecimento</span>
                <h2 class="t-sec">Declarado de Utilidade Pública</h2>
                <p class="lead">O trabalho do Instituto junto às comunidades da Baía do Iguape foi reconhecido pela <strong>Prefeitura de Cachoeira (BA)</strong>, que declarou o Instituto Gaia Soul de Utilidade Pública.</p>
                <p>{RAZAO} · CNPJ {CNPJ} · Associação sem fins lucrativos fundada em 04/07/2019.</p>
            </div>
            <div data-rv="r"><div class="selo"><img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública"><div><small>Reconhecimento de</small><b>Utilidade Pública</b><small>Prefeitura de Cachoeira (BA)</small></div></div></div>
        </div>
    </section>
""" + CTA_GUARDIAO + FOOTER

# =====================================================================
# BAÍA DO IGUAPE (página antiga "Projeto Social Baía do Iguape")
# =====================================================================
def acao(titulo, texto, fotos, cls=""):
    return f"""
    <section class="sec{' espuma' if cls == 'alt' else ''}">
        <div class="wrap">
            <div class="head" data-rv><h2 class="t-sub" style="font-size:clamp(1.7rem,3vw,2.3rem)">{titulo}</h2>{f'<p class="lead">{texto}</p>' if texto else ''}</div>
            {galeria(fotos, "g3" if len(fotos) == 3 else "")}
        </div>
    </section>"""


iguape = head("Ações na Baía do Iguape | Instituto Gaia Soul",
              "Esporte, regatas de canoa, educação ambiental e apoio a 803 famílias de pescadores e marisqueiras na Reserva Extrativista da Baía do Iguape (BA).",
              "baia-do-iguape.html") + ptop(
    f"{IMG4}/bg-pescador.webp", '<a href="atuacao-e-impacto.html">Atuação & Impacto</a> / Baía do Iguape', "Ações na Baía do Iguape",
    "Marisqueiras e pescadores: resiliência e sustentabilidade.",
    """<p>Desde 2019, o Instituto Gaia Soul caminha ao lado das famílias de pescadores e marisqueiras e das comunidades quilombolas da <strong>Reserva Extrativista da Baía do Iguape</strong>.</p>
                <p>Apoiamos a <strong>Associação de Pescadores e Marisqueiras de Cachoeira, que reúne 803 famílias</strong>, com cestas, kits de higiene, brinquedos, esporte e educação ambiental. Mais do que suprir necessidades, queremos fortalecer um ciclo de dignidade e autonomia.</p>""",
    f"{IMG4}/iguape-1.webp", '<a href="seja-um-guardiao.html" class="btn btn-navy">Seja um Guardião</a><a href="contato.html" class="btn btn-line">Fale Conosco</a>',
    alt="Entrega de doações na comunidade") + acao(
    "Time Real São Francisco", "<strong>65 jovens de 12 a 17 anos</strong> em campo. Garantimos treinador, uniformes, bolas e lanche. Em 2025, o time chegou ao <strong>vice-campeonato</strong>.",
    [(f"{IMG}/rsf-1.webp", "Real São Francisco no Campeonato Cachoeirano"), (f"{IMG}/rsf-2.webp", "Time com a bandeira do Instituto"), (f"{IMG4}/iguape-3.webp", "Jovens reunidos antes do jogo"), (f"{IMG4}/iguape-4.webp", "Time perfilado")]) + acao(
    "Bordejos e regatas de canoa", "As tradicionais regatas de canoa a vela mantêm viva a cultura do mar e reúnem toda a comunidade.",
    [(f"{IMG}/bordejo-3.webp", "Canoas a vela na praia"), (f"{IMG}/bordejo-premiacao.webp", "Premiação do Grande Bordejo"), (f"{IMG}/bordejo-1.webp", "Regata de canoas"), (f"{IMG}/bordejo-2.webp", "Canoa a vela ao pôr do sol")], "alt") + acao(
    "Associação de Pescadores e Marisqueiras de Cachoeira", "Convênio de cooperação e presença nas datas que importam: Natal, Dia das Mães, Dia dos Pais e Dia das Crianças.",
    [(f"{IMG4}/iguape-2.webp", "Marisqueiras com as doações"), (f"{IMG4}/iguape-5.webp", "Entrega de kits na associação"), (f"{IMG}/pescadores-3.webp", "Confraternização na praia"), (f"{IMG}/maes-3.webp", "Dia das Mães"), (f"{IMG}/pescadores-1.webp", "Entrega na sede do sindicato"), (f"{IMG}/pescadores-2.webp", "Confraternização com as famílias"), (f"{IMG}/maes-1.webp", "Festa do Dia das Mães"), (f"{IMG}/maes-2.webp", "Presentes do Dia das Mães")]) + acao(
    "Educação ambiental e Dia das Crianças", "Nas escolas, levamos educação ambiental e alegria: brinquedos e chocolates para as crianças das comunidades.",
    [(f"{IMG}/escola-1.webp", "Educação ambiental na escola"), (f"{IMG}/escola-3.webp", "Crianças com a equipe do Instituto"), (f"{IMG}/brinquedos-1.webp", "Crianças com os brinquedos recebidos"), (f"{IMG}/brinquedos-2.webp", "Crianças escolhendo brinquedos")], "alt") + f"""
    <section class="sec areia">
        <div class="wrap grid2">
            <div data-rv="l"><h2 class="t-sec">Declarado de Utilidade Pública</h2><p class="lead">Reconhecimento da Prefeitura de Cachoeira (BA) ao trabalho do Instituto junto às comunidades do território.</p></div>
            <div data-rv="r"><div class="selo"><img src="{LOGO}/selo-utilidade-publica.png" alt="Selo de Utilidade Pública"><div><small>Reconhecimento de</small><b>Utilidade Pública</b><small>Prefeitura de Cachoeira (BA)</small></div></div></div>
        </div>
    </section>
""" + CTA_GUARDIAO + FOOTER

# =====================================================================
# SEJA UM GUARDIÃO (a página que mais precisa convencer)
# =====================================================================
if PIX_CHAVE:
    pix_html = f'<div class="dado"><div><small>Chave Pix ({PIX_TIPO})</small><b>{PIX_CHAVE}</b></div><button class="copy" data-copy="{PIX_CHAVE}">Copiar</button></div>'
else:
    pix_html = f'<div class="dado"><div><small>Chave Pix</small><b>Enviamos na hora pelo WhatsApp</b></div></div>'
banco_html = (f'<div class="dado"><div><small>{BANCO["banco"]}</small><b>Agência {BANCO["agencia"]} · Conta {BANCO["conta"]}</b></div></div>' if BANCO
              else '<div class="dado"><div><small>Transferência bancária</small><b>Enviamos os dados pelo WhatsApp</b></div></div>')
cnpj_html = f'<div class="dado"><div><small>Favorecido · CNPJ</small><b>{CNPJ}</b></div><button class="copy" data-copy="{CNPJ}">Copiar</button></div>'
_ON = ' class="on"'
FORM_GUARDIAO = stepper("guardiao", [
    ("Com quanto você quer contribuir por mês?", "Você pode mudar ou cancelar quando quiser.",
     opts("valor", [("30", "R$ 30", "fa-seedling", "por mês"), ("60", "R$ 60", "fa-water", "por mês"), ("120", "R$ 120", "fa-anchor", "por mês"), ("outro", "Outro valor", "fa-pen", "você escolhe")])
     + '<div class="outro" hidden>' + fld("outro", "Valor por mês (R$)", "text", req=False, extra=' inputmode="numeric"') + "</div>"),
    ("Quase lá! Como falamos com você?", "A nossa equipe te envia os próximos passos pelo WhatsApp.",
     '<div class="flds2">' + fld("nome", "Seu nome") + fld("telefone", "Seu WhatsApp", "tel") + "</div>" + LGPD),
], assunto="Quero ser Guardião (apoio mensal)", ok="Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar e a nossa equipe te passa os próximos passos.", enviar="Quero ser Guardião")
tiers = "".join(f'<button type="button"{_ON if v == 60 else ""} data-valor="{v}">R$ {v}/mês</button>' for v in (30, 60, 120)) + '<button type="button" data-valor="outro">Outro valor</button>'
loja_btn = (f'<a href="{LOJA_URL}" target="_blank" rel="noopener" class="btn btn-line">Quero a minha camiseta</a>' if LOJA_URL
            else '<a href="contato.html?assunto=Camiseta" class="btn btn-line">Quero a minha camiseta</a>')

WA_PIX = WA + "?text=" + "Olá! Quero fazer uma doação para o Instituto Gaia Soul. Pode me passar a chave Pix?".replace(" ", "%20")
WA_TED = WA + "?text=" + "Olá! Quero doar por transferência para o Instituto Gaia Soul.".replace(" ", "%20")

guardiao = head("Seja um Guardião | Instituto Gaia Soul",
                "Seja um Guardião do Instituto Gaia Soul: apoio mensal, doação por Pix ou transferência, Imposto de Renda, empresas (patrocínio, Lei Rouanet, ESG) e voluntariado.",
                "seja-um-guardiao.html") + ptop(
    f"{IMG4}/sub-recife.webp", "Seja um Guardião", "Seja um Guardião", "Faça parte dessa onda que transforma vidas.",
    """<p>Os Guardiões Gaia Soul são pessoas, empresas e organizações que escolheram navegar com a gente. Cada contribuição ajuda o Instituto a ampliar seus projetos, levar a Cultura Oceânica a mais gente e criar experiências que aproximam sociedade e oceano.</p>
                <p>Mais do que apoiar uma instituição, ser Guardião é embarcar num movimento de <strong>conexão, conhecimento e transformação</strong>. Não precisa ser oceanógrafo nem morar perto do mar: basta acreditar que o futuro do oceano também é o nosso.</p>""",
    f"{IMG4}/iguape-2.webp", '<a href="#embarque" class="btn btn-cta">Quero ser Guardião</a><a href="contato.html?assunto=Seja%20um%20Guardi%C3%A3o" class="btn btn-line">Fale com a gente</a>',
    alt="Marisqueiras da Baía do Iguape") + f"""
    <section class="sec">
        <div class="wrap">
            {sec_head("", "Sua contribuição nos leva mais longe.", "Faça parte da mudança que você quer ver no mundo. Quando você apoia o Gaia Soul, ajuda a:", script="por que apoiar")}
            <div class="formas">
                <div class="forma" data-rv><span class="ic"><i class="fas fa-child"></i></span><h3>Levar Cultura Oceânica a crianças e jovens</h3><p>Livros, realidade virtual e formação de professores para estudantes que nunca estudaram o mar.</p></div>
                <div class="forma teal" data-rv><span class="ic"><i class="fas fa-vr-cardboard"></i></span><h3>Criar experiências transformadoras</h3><p>Atividades educativas, culturais, imersivas e de sensibilização que ninguém esquece.</p></div>
                <div class="forma verde" data-rv><span class="ic"><i class="fas fa-people-roof"></i></span><h3>Fortalecer comunidades</h3><p>Esporte, educação ambiental e apoio às 803 famílias de pescadores e marisqueiras da Baía do Iguape.</p></div>
                <div class="forma cta" data-rv><span class="ic"><i class="fas fa-compass"></i></span><h3>Manter o Instituto navegando</h3><p>A estrutura que planeja, executa e acompanha cada projeto, o ano inteiro.</p></div>
            </div>
            <p class="center edit" style="font-size:1.4rem;color:var(--abissal);margin-top:2.4rem" data-rv>Cada contribuição movimenta essa maré.</p>
        </div>
    </section>

    <section class="apoie-sec guardioes" id="embarque">
        <div class="wrap">
            <div class="head center light" data-rv><span class="script" style="color:var(--piscina)">escolha o seu caminho</span><h2 class="t-sec" style="color:#fff">Como você quer embarcar?</h2></div>
            <div class="apoie-list" style="max-width:760px">
                <a class="apoie-it" href="#mensal" data-rv><span class="ic"><i class="fas fa-anchor"></i></span><div><h3>Quero ser um Guardião</h3><p>Contribua todo mês e faça parte da comunidade que mantém os projetos navegando.</p></div></a>
                <a class="apoie-it" href="#doacao" data-rv><span class="ic"><i class="fas fa-hand-holding-heart"></i></span><div><h3>Quero fazer uma doação</h3><p>Pix ou transferência. Uma contribuição pontual também faz muita diferença.</p></div></a>
                <a class="apoie-it" href="#empresas" data-rv><span class="ic"><i class="fas fa-building"></i></span><div><h3>Quero apoiar como empresa</h3><p>Patrocínio, Lei Rouanet, investimento social privado, ESG e parcerias institucionais.</p></div></a>
                <a class="apoie-it" href="#voluntariado" data-rv><span class="ic" style="background:var(--alga)"><i class="fas fa-hands-helping"></i></span><div><h3>Quero ser voluntário</h3><p>Conhecimento, experiência e disponibilidade também transformam.</p></div></a>
            </div>
        </div>
    </section>

    <section class="sec" id="mensal">
        <div class="wrap grid2">
            <div data-rv="l">
                <span class="script">guardião mensal</span>
                <h2 class="t-sec">Uma contribuição que mantém essa maré em movimento.</h2>
                <p class="lead">Ao se tornar Guardião, você passa a fazer parte de uma comunidade que acredita no poder do oceano para educar, conectar e transformar.</p>
                <p class="lead">Escolha um valor mensal e navegue com a gente.</p>
            </div>
            {FORM_GUARDIAO}
        </div>
    </section>

    <section class="sec espuma" id="acompanhe">
        <div class="wrap">
            {sec_head("", "O maior benefício é pertencer.", "Ser Guardião é acompanhar de perto o impacto que você ajudou a gerar.", script="quem é guardião acompanha a viagem")}
            <div class="formas">
                <div class="forma" data-rv><span class="ic"><i class="fas fa-bullhorn"></i></span><h3>Notícias de Bordo</h3><p>Novidades sobre projetos, conquistas e próximos destinos.</p></div>
                <div class="forma teal" data-rv><span class="ic"><i class="fas fa-book"></i></span><h3>Diário de Bordo</h3><p>Acompanhe o que estamos realizando e os impactos gerados.</p></div>
                <div class="forma verde" data-rv><span class="ic"><i class="fas fa-users"></i></span><h3>Encontros dos Guardiões</h3><p>Convites para experiências e atividades especiais do Instituto, quando disponíveis.</p></div>
                <div class="forma" data-rv><span class="ic"><i class="fas fa-fish"></i></span><h3>Conteúdos do oceano</h3><p>Histórias e conteúdos que aproximam você ainda mais do universo oceânico.</p></div>
            </div>
        </div>
    </section>

    <section class="sec" id="doacao">
        <div class="wrap">
            {sec_head("", "Quero contribuir agora.", "Uma contribuição pontual também pode fazer muita diferença. Escolha a forma mais fácil para você.", script="faça uma doação")}
            <div class="formas">
                <div class="forma cta" data-rv>
                    <span class="ic"><i class="fas fa-qrcode"></i></span>
                    <h3>Pix</h3>
                    <p>Rápido, simples e no valor que couber para você hoje.</p>
                    {pix_html}{cnpj_html}
                    <div class="btns"><a href="{WA_PIX}" target="_blank" rel="noopener" class="btn btn-cta"><i class="fab fa-whatsapp"></i> Quero doar agora</a></div>
                </div>
                <div class="forma teal" data-rv>
                    <span class="ic"><i class="fas fa-building-columns"></i></span>
                    <h3>Transferência bancária</h3>
                    <p>Prefere transferência ou precisa de recibo? A gente cuida disso para você.</p>
                    {banco_html}
                    <div class="dado"><div><small>Favorecido</small><b>{RAZAO}</b></div></div>
                    <div class="btns"><a href="{WA_TED}" target="_blank" rel="noopener" class="btn btn-line">Pedir os dados</a></div>
                </div>
                <div class="forma" data-rv>
                    <span class="ic"><i class="fas fa-file-invoice-dollar"></i></span>
                    <h3>Pelo Imposto de Renda</h3>
                    <p>Parte do imposto que você já pagaria pode ir para um projeto cultural aprovado na Lei Rouanet, como o <strong>Imersão Azul</strong>, sem custo extra para você.</p>
                    <div class="btns"><a href="contato.html?assunto=Imposto%20de%20Renda" class="btn btn-line">Quero saber como</a></div>
                </div>
            </div>
        </div>
    </section>

    <section class="sec navy" id="empresas">
        <div class="wrap">
            <div class="head center light" data-rv><span class="script" style="color:var(--piscina)">empresas a bordo</span><h2 class="t-sec" style="color:#fff">Sua empresa pode levar essa transformação ainda mais longe.</h2><p class="lead" style="color:#cfe0ea">Empresas e organizações são parte importante dos nossos Guardiões. Construímos parcerias que conectam os objetivos da sua organização à Cultura Oceânica, à educação, à inovação, ao bem-estar e ao desenvolvimento socioambiental.</p></div>
            <div class="modalidades">
                <div class="mod" data-rv><i class="fas fa-landmark"></i><h3>Lei de incentivo fiscal</h3><p>Apoie projetos aprovados na Lei Rouanet com parte do imposto devido.</p></div>
                <div class="mod" data-rv><i class="fas fa-award"></i><h3>Patrocínio</h3><p>Associe a sua marca a projetos e experiências com propósito.</p></div>
                <div class="mod" data-rv><i class="fas fa-hand-holding-heart"></i><h3>Investimento Social Privado</h3><p>Invista em iniciativas de impacto alinhadas às estratégias sociais e territoriais da sua organização.</p></div>
                <div class="mod" data-rv><i class="fas fa-leaf"></i><h3>ESG</h3><p>Projetos ligados a oceano, educação, comunidades e sustentabilidade.</p></div>
                <div class="mod" data-rv><i class="fas fa-briefcase"></i><h3>Programas corporativos</h3><p>Cultura Oceânica, experiências imersivas, Oceanoterapia e palestras para colaboradores e clientes.</p></div>
                <div class="mod" data-rv><i class="fas fa-handshake"></i><h3>Apoio institucional</h3><p>Contribua diretamente para fortalecer e expandir a atuação do Instituto.</p></div>
            </div>
            <div class="btns center" style="margin-top:2.4rem" data-rv><a href="#captacao" class="btn btn-white">Conheça os projetos em captação</a><a href="contato.html?assunto=Parcerias%20e%20patroc%C3%ADnios" class="btn btn-cta">Converse com o Gaia Soul</a></div>
        </div>
    </section>

    <section class="sec" id="captacao">
        <div class="wrap">
            {sec_head("", "Escolha onde você quer gerar impacto.", "", script="projetos esperando novos tripulantes")}
            {captacao_html()}
        </div>
    </section>

    <section class="sec espuma" id="voluntariado">
        <div class="wrap">
            {sec_head("", "Apoio não é só dinheiro.", "", script="outras formas de ser Guardião")}
            <div class="formas">
                <div class="forma verde" data-rv><span class="ic"><i class="fas fa-hands-helping"></i></span><h3>Seja voluntário</h3><p>Educadores, comunicadores, fotógrafos, profissionais de qualquer área: doe tempo e conhecimento.</p><div class="btns"><a href="contato.html?assunto=Voluntariado" class="btn btn-line">Quero ser voluntário</a></div></div>
                <div class="forma teal" id="imagens" data-rv><span class="ic"><i class="fas fa-camera"></i></span><h3>Doe suas imagens</h3><p>Fotógrafo ou mergulhador? Colabore com o <strong>Blue Bank</strong>, o nosso banco de imagens do oceano, e transforme suas fotos em material educativo.</p><div class="btns">{BLUE_BANK_BTN}</div></div>
                <div class="forma" data-rv><span class="ic"><i class="fas fa-share-nodes"></i></span><h3>Compartilhe nossa causa</h3><p>Siga, comente e compartilhe: ajude a Cultura Oceânica a chegar mais longe.</p><div class="btns"><a href="{IG}" target="_blank" rel="noopener" class="btn btn-line">@institutogaiasoul</a></div></div>
                <div class="forma cta" data-rv><span class="ic"><i class="fas fa-shirt"></i></span><h3>Compre com propósito</h3><p>A camiseta do Instituto ajuda a manter as atividades e leva a nossa mensagem para onde você for.</p><div class="btns">{loja_btn}</div></div>
                <div class="forma" data-rv><span class="ic"><i class="fas fa-school"></i></span><h3>Leve nossos projetos até você</h3><p>Escolas, empresas, eventos e instituições podem receber as nossas experiências.</p><div class="btns"><a href="contato.html?assunto=Experiências" class="btn btn-line">Quero receber</a></div></div>
            </div>
        </div>
    </section>
""" + PARCEIROS_HTML.replace("Quem navega com a gente", "Quem já está a bordo") + cta_final(
    "O oceano é grande.<br>Nossos Guardiões também podem ser.",
    "Cada pessoa que embarca fortalece a nossa capacidade de levar conhecimento, experiências e Cultura Oceânica cada vez mais longe. Vem com a gente?",
    f"{IMG4}/sub-recife.webp",
    '<a href="#mensal" class="btn btn-cta">Quero ser um Guardião</a><a href="#empresas" class="btn btn-line-white">Quero embarcar minha empresa</a>') + FOOTER

# =====================================================================
# DIÁRIO DE BORDO
# =====================================================================
diario = head("Diário de Bordo | Instituto Gaia Soul",
              "Projetos, notícias, ciência e oceano, bastidores e eventos do Instituto Gaia Soul.",
              "diario-de-bordo.html") + ptop(
    f"{IMG4}/bg-baleia.webp", "Diário de Bordo", "Diário de Bordo", "Acompanhe nossa jornada.",
    "<p>Projetos, bastidores, eventos, notícias e ciência do oceano. Tudo o que está acontecendo a bordo do Instituto Gaia Soul.</p>",
    f"{IMG}/bordejo-2.webp", f'<a href="{IG}" target="_blank" rel="noopener" class="btn btn-navy"><i class="fab fa-instagram"></i> Acompanhe no Instagram</a>',
    alt="Canoa a vela ao pôr do sol") + f"""
    <section class="sec"><div class="wrap">{diario_html(DIARIO)}</div></section>
""" + NEWSLETTER + FOOTER

# =====================================================================
# CONTATO
# =====================================================================
ASSUNTOS = [("Parcerias e patrocínios", "fa-handshake"), ("Projetos", "fa-water"), ("Escolas", "fa-school"), ("Palestras", "fa-microphone"),
            ("Experiências", "fa-vr-cardboard"), ("Seja um Guardião", "fa-anchor"), ("Voluntariado", "fa-hands-helping"), ("Imprensa", "fa-newspaper"), ("Outros assuntos", "fa-comment-dots")]
FORM_CONTATO = stepper("contato", [
    ("Sobre o que você quer falar?", "Escolha uma opção para começar.", opts("assunto", [(a, a, ic, "") for a, ic in ASSUNTOS])),
    ("Como podemos te chamar?", "Usamos o seu WhatsApp só para responder você.", '<div class="flds2">' + fld("nome", "Seu nome") + fld("telefone", "Seu WhatsApp", "tel") + "</div>" + fld("email", "Seu e-mail (opcional)", "email", req=False)),
    ("Conte um pouco mais.", "Quanto mais detalhes, mais rápido a gente te ajuda.", fld("mensagem", "Sua mensagem", req=False, area=True) + LGPD),
], ok="Abrimos o WhatsApp com a sua mensagem. É só tocar em enviar.")
contato = head("Contato | Instituto Gaia Soul",
               f"Fale com o Instituto Gaia Soul: parcerias, projetos, escolas, palestras, experiências e imprensa. WhatsApp {TEL}.",
               "contato.html") + ptop(
    f"{IMG4}/sub-mergulho.webp", "Contato", "Fale Conosco", "Entre em contato com a nossa equipe.",
    f"""<ul class="contatos">
                    <li><i class="fab fa-whatsapp"></i><a href="{WA}" target="_blank" rel="noopener">{TEL}</a></li>
                    <li><i class="far fa-envelope"></i><a href="mailto:{MAIL}">{MAIL}</a></li>
                    <li><i class="fab fa-instagram"></i><a href="{IG}" target="_blank" rel="noopener">@institutogaiasoul</a></li>
                    <li><i class="fas fa-location-dot"></i><span>Sede: Mata Quântica, Baía do Iguape (BA) · Escritório: {ESCRITORIO}</span></li>
                    <li><i class="fab fa-google"></i><a href="{GOOGLE_INSTITUTO}" target="_blank" rel="noopener">Veja e deixe a sua avaliação no Google</a></li>
                </ul>
                <div class="fsocial" style="margin-top:0">{"".join(f'<a class="{c}" href="{u}" target="_blank" rel="noopener" aria-label="{n}"><i class="{i}"></i></a>' for u, i, n, c in SOCIAL)}</div>""",
    f"{IMG4}/mergulho-coral.webp", alt="Mergulhador entre corais") + f"""
    <section class="sec espuma">
        <div class="wrap grid2" style="align-items:start">
            <div data-rv="l">
                <span class="script">vamos conversar?</span>
                <h2 class="t-sec">Conte pra gente como quer navegar com o Gaia Soul.</h2>
                <p class="lead">São só três passos. A sua mensagem chega direto no nosso WhatsApp e a equipe responde o quanto antes.</p>
                <ul class="contatos" style="margin-top:1.4rem">
                    <li><i class="fas fa-check"></i> Parcerias, patrocínio e Lei Rouanet</li>
                    <li><i class="fas fa-check"></i> Projetos em escolas, empresas e eventos</li>
                    <li><i class="fas fa-check"></i> Palestras, imprensa e voluntariado</li>
                </ul>
            </div>
            {FORM_CONTATO}
        </div>
    </section>
""" + FOOTER


# =====================================================================
# LEGAIS
# =====================================================================
def legal(fname, title, corpo):
    return head(f"{title} | Instituto Gaia Soul", f"{title} do Instituto Gaia Soul.", fname) + f"""
    <section class="ptop"><div class="faixa" style="background-image:url('{IMG4}/bg-baleia.webp')"></div></section>
    <section class="sec"><div class="wrap" style="max-width:820px">
        <h1 class="t-sec">{title}</h1>
{corpo}
        <p style="color:var(--golfinho);font-size:.9rem">Última atualização: setembro de 2026.</p>
    </div></section>
""" + FOOTER


privacidade = legal("politica-de-privacidade.html", "Política de Privacidade", f"""
        <p>Esta política explica como o <strong>{RAZAO}</strong> (CNPJ {CNPJ}), controlador dos dados, trata as informações pessoais de quem visita este site ou entra em contato conosco, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
        <h2 class="t-sub">Quais dados coletamos</h2><p>Somente os dados que você informa nos formulários: nome, telefone (WhatsApp), e-mail, valor ou forma de contribuição e a mensagem enviada.</p>
        <h2 class="t-sub">Para que usamos</h2><ul><li>Responder ao seu contato e dar andamento à sua contribuição, apoio ou voluntariado;</li><li>Enviar novidades do Instituto, quando você pedir;</li><li>Cumprir obrigações legais e de prestação de contas.</li></ul>
        <h2 class="t-sub">Com quem compartilhamos</h2><p>Não vendemos nem cedemos seus dados. Eles podem ser processados por ferramentas de comunicação (como WhatsApp e e-mail), apenas para as finalidades acima.</p>
        <h2 class="t-sub" id="cookies">Cookies</h2><p>Este site pode usar cookies técnicos e de medição de audiência para melhorar a sua experiência. Você pode bloqueá-los nas configurações do navegador.</p>
        <h2 class="t-sub">Seus direitos</h2><p>Você pode pedir acesso, correção, anonimização, portabilidade ou exclusão dos seus dados, e revogar o consentimento, escrevendo para <a href="mailto:{MAIL}">{MAIL}</a>.</p>""")

termos = legal("termos-de-uso.html", "Termos de Uso", f"""
        <p>Ao usar este site, você concorda com estes termos. O site é mantido pelo <strong>{RAZAO}</strong> (CNPJ {CNPJ}).</p>
        <h2 class="t-sub">Conteúdo</h2><p>Textos, imagens, vídeos e marcas pertencem ao Instituto Gaia Soul ou a seus parceiros e não podem ser reproduzidos para fins comerciais sem autorização. O compartilhamento com citação da fonte é bem-vindo.</p>
        <h2 class="t-sub">Contribuições</h2><p>As contribuições são destinadas às finalidades estatutárias do Instituto. Os dados para doação são sempre confirmados pelos canais oficiais listados neste site.</p>
        <h2 class="t-sub">Links externos</h2><p>Este site pode conter links para sites de terceiros, pelos quais o Instituto não se responsabiliza.</p>""")


def redirect(dest, titulo):
    return f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>{titulo} | Instituto Gaia Soul</title>
<meta http-equiv="refresh" content="0; url={dest}"><link rel="canonical" href="https://institutogaiasoul.ong.br/{dest}">
<meta name="robots" content="noindex"></head><body><p><a href="{dest}">{titulo}</a></p></body></html>
"""


PAGES = [
    ("index.html", index), ("o-instituto.html", instituto), ("projetos.html", projetos),
    ("projeto-imersao-azul.html", p_imersao), ("projeto-mundo-submarino-360.html", p_mundo),
    ("projeto-submarino-imersivo.html", p_sub), ("projeto-oceanoterapia.html", p_oceano),
    ("projeto-mata-quantica.html", p_mata), ("projeto-palestras.html", p_palestras),
    ("atuacao-e-impacto.html", atuacao), ("baia-do-iguape.html", iguape), ("seja-um-guardiao.html", guardiao),
    ("contato.html", contato), ("politica-de-privacidade.html", privacidade), ("termos-de-uso.html", termos),
    # páginas antigas (v3 e site WordPress) redirecionam para as novas
    ("marujada.html", redirect("seja-um-guardiao.html", "Seja um Guardião")),
    ("transparencia.html", redirect("atuacao-e-impacto.html#utilidade-publica", "Atuação & Impacto")),
    ("acoes-sociais.html", redirect("baia-do-iguape.html", "Ações na Baía do Iguape")),
    ("diario-de-bordo.html", diario),
    ("sobre.html", redirect("o-instituto.html", "O Instituto")),
]

if __name__ == "__main__":
    for nome, html in PAGES:
        for bad in ("—", "–"):
            assert bad not in html, f"travessão em {nome}"
        (ROOT / nome).write_text(html, encoding="utf-8")
        print("ok", nome, len(html))
