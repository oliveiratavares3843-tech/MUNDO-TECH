import streamlit as st

st.set_page_config(
    page_title="Mundo Tech",
    page_icon="💻",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #f4f7fb;
}

.hero {
    padding: 2.4rem 2rem;
    border-radius: 22px;
    color: white;
    background:
        radial-gradient(circle at 85% 15%, #2861a8 0, transparent 35%),
        linear-gradient(120deg, #101d36, #173966);
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-size: clamp(2.3rem, 5vw, 4rem);
    line-height: 1.05;
    margin: 0;
}

.hero p {
    color: #d9e8fb;
    font-size: 1.12rem;
    max-width: 720px;
}

.eyebrow {
    color: #7dd3fc;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.tile {
    background: white;
    border: 1px solid #e3eaf3;
    border-radius: 18px;
    padding: 1.25rem;
    min-height: 190px;
    box-shadow: 0 8px 24px #10294a0b;
}

.tile .emoji {
    font-size: 2rem;
}

.tile h3 {
    margin: .5rem 0;
    color: #172033;
}

.tile p {
    color: #64748b;
}
</style>
""", unsafe_allow_html=True)


# MENU LATERAL
with st.sidebar:
    st.markdown("# 💻 Mundo Tech")
    st.caption("O futuro começa aqui.")

    page = st.radio(
        "Navegação",
        [
            "Início",
            "Programação",
            "Inteligência artificial",
            "Tecnologia",
            "Segurança digital",
            "Sobre"
        ]
    )

    st.divider()
    st.caption("Tecnologia, conhecimento e inovação para todos.")


# PÁGINA INICIAL
if page == "Início":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">Tecnologia para todos</div>
        <h1>O futuro começa aqui.</h1>
        <p>
            Aprenda sobre programação, inteligência artificial e inovação
            com explicações simples, dicas práticas e novidades do mundo digital.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # IMAGEM PRINCIPAL DO MUNDO TECH
    st.image(
        "mundo-tech-banner.png",
        use_container_width=True
    )

    st.subheader("Explore o Mundo Tech")

    cols = st.columns(3)

    items = [
        (
            "💻",
            "Programação",
            "Lógica, linguagens e ferramentas para criar seus primeiros projetos."
        ),
        (
            "🤖",
            "Inteligência artificial",
            "Entenda a IA e descubra maneiras úteis de aplicá-la no dia a dia."
        ),
        (
            "🌐",
            "Tecnologia",
            "Tendências, ferramentas digitais, segurança e inovação."
        ),
    ]

    for col, (emoji, title, desc) in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="tile">
                    <div class="emoji">{emoji}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    st.subheader("Comece por aqui")

    with st.expander("🧩 O que é programação?"):
        st.write(
            "Programação é a prática de dar instruções a um computador "
            "para resolver problemas e criar aplicações."
        )

    with st.expander("✨ O que é inteligência artificial?"):
        st.write(
            "É uma área da computação que desenvolve sistemas capazes "
            "de realizar tarefas que normalmente exigem inteligência humana."
        )

    with st.expander("🔐 Três hábitos para navegar com segurança"):
        st.write(
            "Use senhas fortes e únicas, ative a autenticação em duas etapas "
            "e desconfie de links inesperados."
        )


# PROGRAMAÇÃO
elif page == "Programação":

    st.title("💻 Programação")
    st.write("Aprenda a construir soluções digitais, começando do básico.")

    st.subheader("Primeiros passos")

    st.markdown("""
    1. **Lógica:** aprenda variáveis, condições e repetições.
    2. **Escolha uma linguagem:** Python é uma boa opção para começar.
    3. **Pratique:** crie calculadoras, listas e pequenos jogos.
    """)

    st.code(
        'nome = "Mundo Tech"\nprint(f"Olá, {nome}!")',
        language="python"
    )

    st.info("Dica: pratique um pouco todos os dias e avance no seu próprio ritmo.")


# INTELIGÊNCIA ARTIFICIAL
elif page == "Inteligência artificial":

    st.title("🤖 Inteligência artificial")

    st.write(
        "Entenda conceitos de IA e como usar essas ferramentas com responsabilidade."
    )

    st.subheader("O que é IA generativa?")

    st.write(
        "É uma tecnologia capaz de produzir textos, imagens, áudio, código "
        "e outros conteúdos a partir de instruções."
    )

    st.subheader("Boas práticas")

    st.markdown("""
    - Confira informações importantes em fontes confiáveis.
    - Não compartilhe dados pessoais ou senhas.
    - Use a IA como apoio, mantendo seu próprio julgamento.
    """)


# TECNOLOGIA
elif page == "Tecnologia":

    st.title("🌐 Tecnologia")

    st.write(
        "Um espaço para aprender sobre ferramentas, dispositivos e tendências digitais."
    )

    st.subheader("Temas para explorar")

    st.markdown("""
    - Computadores e dispositivos móveis
    - Aplicativos e serviços online
    - Internet e computação em nuvem
    - Inovação e novas tecnologias
    """)


# SEGURANÇA DIGITAL
elif page == "Segurança digital":

    st.title("🔐 Segurança digital")

    st.write(
        "Pequenos cuidados ajudam a proteger suas contas e seus dispositivos."
    )

    st.markdown("""
    - Crie senhas longas e diferentes para cada serviço.
    - Ative a autenticação em dois fatores.
    - Mantenha aplicativos e sistema atualizados.
    - Evite abrir anexos e links inesperados.
    - Faça cópias de segurança dos arquivos importantes.
    """)


# SOBRE
else:

    st.title("🌟 Sobre o Mundo Tech")

    st.write(
        "O Mundo Tech é um espaço para compartilhar conhecimento "
        "sobre programação, inteligência artificial e o universo digital."
    )

    st.write(
        "Nosso objetivo é tornar a tecnologia mais acessível, "
        "com conteúdo simples, útil e educativo."
    )

    st.success("Uma ideia de cada vez. O futuro começa aqui.")


# RODAPÉ
st.divider()

st.caption(
    "© 2026 Mundo Tech · Feito para aprender e compartilhar."
)


