import streamlit as st
import time

st.set_page_config(
    page_title="Дашборд поручений",
    layout="wide"
)

# === АВТООБНОВЛЕНИЕ КАЖДЫЕ 30 СЕКУНД ===
REFRESH_INTERVAL = 30  # секунд

if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

if time.time() - st.session_state.last_refresh >= REFRESH_INTERVAL:
    st.session_state.last_refresh = time.time()
    st.experimental_rerun()
# ================== НАСТРОЙКИ СТРАНИЦЫ ==================
st.set_page_config(
    page_title="Дашборд поручений",
    layout="wide"
)

# ================== СТИЛИ ==================
st.markdown("""
<style>
/* ===== ФОН ===== */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #F5F6F8 !important;
}

/* ===== ВЕСЬ ТЕКСТ ЧЁРНЫЙ ===== */
h1, h2, h3, p, div, span {
    color: #000000;
}

/* ===== ЗАГОЛОВКИ ===== */
h2, h3 {
    margin-bottom: 6px;
}

/* ===== ПОДПИСИ ===== */
.caption {
    font-size: 14px;
    color: #000000;
}

/* ===== ВЕРХНИЕ КАРТОЧКИ ===== */
.card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    height: 150px;
    position: relative;
}

.card-title {
    font-size: 15px;
    font-weight: 600;
}

.card-value {
    font-size: 38px;
    font-weight: 800;
    margin-top: 8px;
}

.card-desc {
    font-size: 14px;
}

.blue  { border-bottom: 6px solid #4F7DF3; }
.green { border-bottom: 6px solid #22C55E; }
.red   { border-bottom: 6px solid #8B1E3F; }

/* ===== ИКОНКИ ===== */
.icon {
    position: absolute;
    right: 20px;
    top: 38px;
    width: 52px;
    height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: #FFFFFF;
}

.icon-blue  { background: #4F7DF3; }
.icon-green { background: #22C55E; }
.icon-red   { background: #8B1E3F; }

/* ===== СЕКЦИИ ===== */
.section {
    background: #FFFFFF;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    height: 200px;
}

.section-title {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* ===== МЕТРИКИ ===== */
.metrics {
    display: flex;
    gap: 14px;
}

.metric {
    flex: 1;
    border-radius: 14px;
    padding: 14px;
    text-align: center;
}

.metric-value {
    font-size: 26px;
    font-weight: 800;
}

.metric-label {
    font-size: 13px;
}

/* ===== ЦВЕТА ===== */
.m-red    { color: #8B1E3F; }
.m-yellow { color: #D97706; }
.m-green  { color: #16A34A; }

.bg-red    { background: #FDECEF; }
.bg-yellow { background: #FFF4E5; }
.bg-green  { background: #ECFDF5; }

/* ===== ССЫЛКИ (ТОЛЬКО ЗАГОЛОВКИ) ===== */
a {
    color: #000000 !important;   /* чёрный как весь текст */
    text-decoration: none !important;
    font-weight: 700;
}

a:hover {
    color: #000000 !important;
    text-decoration: none !important;
}
</style>
""", unsafe_allow_html=True)

# ================== ЗАГОЛОВОК ==================
st.markdown("## 📊 Дашборд поручений")
st.markdown("<div class='caption'>Обзор состояния и нагрузки по управлениям</div>", unsafe_allow_html=True)

# ================== ВЕРХНИЕ КАРТОЧКИ ==================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card blue">
        <div class="card-title">Всего поручений</div>
        <div class="card-value">120</div>
        <div class="card-desc">Общее количество поручений</div>
        <div class="icon icon-blue">📊</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card green">
        <div class="card-title">В работе</div>
        <div class="card-value">99</div>
        <div class="card-desc">Активные поручения</div>
        <div class="icon icon-green">📈</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card red">
        <div class="card-title">Просрочено</div>
        <div class="card-value">52</div>
        <div class="card-desc">С нарушением срока</div>
        <div class="icon icon-red">⚠️</div>
    </div>
    """, unsafe_allow_html=True)

# ================== РАЗБИВКА ПО УПРАВЛЕНИЯМ ==================
st.markdown("### 📌 Разбивка по управлениям")

def management_block(title, link, r, y, g):
    st.markdown(f"""
    <div class="section blue">
        <div class="section-title">
            <a href="{link}" target="_blank">{title}</a>
        </div>
        <div class="metrics">
            <div class="metric bg-red">
                <div class="metric-value m-red">{r}</div>
                <div class="metric-label">Просрочено</div>
            </div>
            <div class="metric bg-yellow">
                <div class="metric-value m-yellow">{y}</div>
                <div class="metric-label">Сегодня</div>
            </div>
            <div class="metric bg-green">
                <div class="metric-value m-green">{g}</div>
                <div class="metric-label">В работе</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

u1, u2, u3 = st.columns(3)

with u1:
    management_block(
        "Управление СО",
        "https://docs.google.com/spreadsheets/d/1zCHKMi_0VFaZ5W1pPUeHXG1k7C8u8zmR60D1fJrKt_A/edit#gid=1562831922",
        11, 0, 20
    )

with u2:
    management_block(
        "Управление УСО",
        "https://docs.google.com/spreadsheets/d/1zCHKMi_0VFaZ5W1pPUeHXG1k7C8u8zmR60D1fJrKt_A/edit#gid=1484976844",
        15, 0, 28
    )

with u3:
    management_block(
        "Управление ЗОИ",
        "https://docs.google.com/spreadsheets/d/1zCHKMi_0VFaZ5W1pPUeHXG1k7C8u8zmR60D1fJrKt_A/edit#gid=0",
        26, 0, 51
    )

# ================== НАГРУЗКА ==================
st.markdown("### 📊 Нагрузка")

def load_block(title, value):
    st.markdown(f"""
    <div class="section green" style="height:160px;">
        <div class="section-title">{title}</div>
        <div style="font-size:36px; font-weight:800; margin-top:24px;">
            {value}%
        </div>
        <div class="caption">Текущая нагрузка</div>
    </div>
    """, unsafe_allow_html=True)

n1, n2, n3 = st.columns(3)

with n1:
    load_block("Управление СО", 20)
with n2:
    load_block("Управление УСО", 29)
with n3:
    load_block("Управление ЗОИ", 50)
