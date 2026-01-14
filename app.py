import streamlit as st
import time

# =====================================================
# НАСТРОЙКИ СТРАНИЦЫ (ТОЛЬКО ОДИН РАЗ!)
# =====================================================
st.set_page_config(
    page_title="Дашборд поручений",
    layout="wide"
)

# =====================================================
# АВТООБНОВЛЕНИЕ КАЖДЫЕ 30 СЕКУНД
# =====================================================
REFRESH_INTERVAL = 30  # секунд

if "last_refresh" not in st.session_state:
    st.session_state.last_refresh = time.time()

if time.time() - st.session_state.last_refresh >= REFRESH_INTERVAL:
    st.session_state.last_refresh = time.time()
    st.experimental_rerun()

# =====================================================
# СТИЛИ
# =====================================================
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #F5F6F8 !important;
}

/* ВЕСЬ ТЕКСТ ЧЁРНЫЙ */
h1, h2, h3, p, div, span {
    color: #000000 !important;
}

/* КАРТОЧКИ */
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

.blue { border-bottom: 6px solid #4F7DF3; }
.green { border-bottom: 6px solid #22C55E; }
.red { border-bottom: 6px solid #8B1E3F; }

/* ИКОНКИ */
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
    color: white;
    font-size: 24px;
}

.icon-blue { background: #4F7DF3; }
.icon-green { background: #22C55E; }
.icon-red { background: #8B1E3F; }

/* БЛОКИ УПРАВЛЕНИЙ */
.section {
    background: #FFFFFF;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
    height: 210px;
}

.section-title {
    font-size: 15px;
    font-weight: 700;
}

.metrics {
    display: flex;
    gap: 14px;
    margin-top: 18px;
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

.bg-red { background: #FDECEF; }
.bg-yellow { background: #FFF4E5; }
.bg-green { background: #ECFDF5; }

.m-red { color: #8B1E3F; }
.m-yellow { color: #D97706; }
.m-green { color: #16A34A; }

/* УБИРАЕМ ПОДЧЕРКИВАНИЯ ССЫЛОК */
a {
    text-decoration: none !important;
    color: inherit !important;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# ЗАГОЛОВОК
# =====================================================
st.markdown("## 📊 Дашборд поручений")
st.markdown("<div style='font-size:14px;'>Обзор состояния по управлениям (автообновление каждые 30 сек)</div>", unsafe_allow_html=True)

# =====================================================
# ВЕРХНИЕ КАРТОЧКИ
# =====================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card blue">
        <div class="card-title">Всего поручений</div>
        <div class="card-value">120</div>
        <div class="card-desc">Общее количество</div>
        <div class="icon icon-blue">📂</div>
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

# =====================================================
# РАЗБИВКА ПО УПРАВЛЕНИЯМ (БЕЗ "НАГРУЗКИ")
# =====================================================
st.markdown("### 📌 Разбивка по управлениям")

def management_block(title, overdue, today, in_work):
    st.markdown(f"""
    <div class="section">
        <div class="section-title">{title}</div>
        <div class="metrics">
            <div class="metric bg-red">
                <div class="metric-value m-red">{overdue}</div>
                <div class="metric-label">Просрочено</div>
            </div>
            <div class="metric bg-yellow">
                <div class="metric-value m-yellow">{today}</div>
                <div class="metric-label">Сегодня</div>
            </div>
            <div class="metric bg-green">
                <div class="metric-value m-green">{in_work}</div>
                <div class="metric-label">В работе</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

u1, u2, u3 = st.columns(3)

with u1:
    management_block("Управление СО", 11, 0, 20)

with u2:
    management_block("Управление УСО", 15, 0, 28)

with u3:
    management_block("Управление ЗОИ", 26, 0, 51)
