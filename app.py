import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timedelta

st.set_page_config(page_title="HGW 2026", layout="wide")

st.markdown("""
<style>
  .block-container { padding-top: 2rem !important; }
  header[data-testid="stHeader"] { height: 1.2rem; }
  [data-testid="stSidebarNav"] { display: none; }
  [data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)

TARGET = datetime(2026, 4, 22, 17, 0, 0)
target_ms = int(TARGET.timestamp() * 1000)
preview_url = st.secrets["preview_url"]

components.html(f"""
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div id="wrapper" style="
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    min-height:85vh; font-family:sans-serif; background:#fff;
    padding: 16px; box-sizing:border-box;
">
    <!-- Countdown view -->
    <div id="countdown-view" style="width:100%; text-align:center;">
        <div class="subtitle">
            De locatie wordt onthuld op woensdag 22 april om 17:00
        </div>

        <div class="clock-row">
            <div class="unit">
                <span class="num" id="d">00</span>
                <span class="label">dagen</span>
            </div>
            <div class="sep">:</div>
            <div class="unit">
                <span class="num" id="h">00</span>
                <span class="label">uren</span>
            </div>
            <div class="sep">:</div>
            <div class="unit">
                <span class="num" id="m">00</span>
                <span class="label">minuten</span>
            </div>
            <div class="sep">:</div>
            <div class="unit">
                <span class="num" id="s">00</span>
                <span class="label">seconden</span>
            </div>
        </div>
    </div>

    <!-- Button view (hidden until live) -->
    <div id="button-view" style="display:none; text-align:center;">
        <a href="{preview_url}" target="_blank" class="big-btn">
            Bekijk HGW 2026 &rarr;
        </a>
    </div>
</div>

<style>
  * {{ box-sizing: border-box; }}

  .subtitle {{
    font-size: clamp(0.9rem, 3.5vw, 1.5rem);
    color: #555;
    margin-bottom: 32px;
    line-height: 1.4;
  }}

  .clock-row {{
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: clamp(4px, 2vw, 24px);
    flex-wrap: nowrap;
    width: 100%;
  }}

  .unit {{
    display: flex;
    flex-direction: column;
    align-items: center;
    flex: 1;
    min-width: 0;
  }}

  .num {{
    font-size: clamp(2.8rem, 16vw, 7rem);
    font-weight: 900;
    line-height: 1;
    color: #1a1a1a;
  }}

  .label {{
    font-size: clamp(0.6rem, 2.5vw, 1rem);
    color: #aaa;
    margin-top: 8px;
    letter-spacing: 0.03em;
  }}

  .sep {{
    font-size: clamp(2rem, 12vw, 5rem);
    font-weight: 900;
    color: #ccc;
    line-height: 1;
    padding-top: 4px;
    flex-shrink: 0;
  }}

  .big-btn {{
    display: inline-block;
    background-color: #00B050;
    color: white;
    font-size: clamp(1.4rem, 5vw, 2.5rem);
    font-weight: bold;
    padding: clamp(20px, 5vw, 40px) clamp(30px, 8vw, 80px);
    border-radius: 20px;
    text-decoration: none;
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
    transition: transform 0.1s;
  }}
  .big-btn:hover {{ transform: scale(1.04); }}
</style>

<script>
  const target = {target_ms};

  function pad(n) {{ return String(n).padStart(2, '0'); }}

  function tick() {{
    const now = Date.now();
    let diff = Math.max(0, target - now);

    const days    = Math.floor(diff / 86400000); diff -= days * 86400000;
    const hours   = Math.floor(diff /  3600000); diff -= hours * 3600000;
    const minutes = Math.floor(diff /    60000); diff -= minutes * 60000;
    const seconds = Math.floor(diff /     1000);

    document.getElementById('d').textContent = pad(days);
    document.getElementById('h').textContent = pad(hours);
    document.getElementById('m').textContent = pad(minutes);
    document.getElementById('s').textContent = pad(seconds);

    if (diff <= 0) {{
      clearInterval(timer);
      document.getElementById('countdown-view').style.display = 'none';
      document.getElementById('button-view').style.display = 'block';
    }}
  }}

  if (Date.now() >= target) {{
    document.getElementById('countdown-view').style.display = 'none';
    document.getElementById('button-view').style.display = 'block';
  }} else {{
    tick();
    const timer = setInterval(tick, 1000);
  }}
</script>
""", height=600)
