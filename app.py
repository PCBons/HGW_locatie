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

components.html(f"""
<div id="wrapper" style="
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    min-height:85vh; font-family:sans-serif; background:#fff;
">
    <!-- Countdown view -->
    <div id="countdown-view">
        <div style="font-size:1.6rem; color:#555; margin-bottom:24px; letter-spacing:0.05em; text-align:center;">
            De locatie wordt onthuld op woensdag 22 april om 17:00
        </div>
        <div id="clock" style="display:flex; gap:32px; align-items:flex-end; justify-content:center;"></div>
        <div style="
            display:flex; gap:32px; margin-top:12px; justify-content:center;
            font-size:1rem; color:#aaa; letter-spacing:0.05em;
        ">
            <span style="min-width:7rem;text-align:center;">dagen</span>
            <span style="min-width:1rem;"></span>
            <span style="min-width:7rem;text-align:center;">uren</span>
            <span style="min-width:1rem;"></span>
            <span style="min-width:7rem;text-align:center;">minuten</span>
            <span style="min-width:1rem;"></span>
            <span style="min-width:7rem;text-align:center;">seconden</span>
        </div>
    </div>

    <!-- Button view (hidden until live) -->
    <div id="button-view" style="display:none;">
        <a href="https://hgw2026.info/index.html?preview" target="_blank" style="
            display:inline-block;
            background-color:#00B050;
            color:white;
            font-size:2.5rem;
            font-weight:bold;
            padding:40px 80px;
            border-radius:20px;
            text-decoration:none;
            text-align:center;
            box-shadow:0 8px 30px rgba(0,0,0,0.2);
            transition:transform 0.1s;
        " onmouseover="this.style.transform='scale(1.04)'"
           onmouseout="this.style.transform='scale(1)'">
            Bekijk HGW 2026 &rarr;
        </a>
    </div>
</div>

<style>
  .unit {{
    display:flex; flex-direction:column; align-items:center;
    min-width:7rem;
  }}
  .num {{
    font-size:7rem;
    font-weight:900;
    line-height:1;
    color:#1a1a1a;
    text-align:center;
  }}
  .sep {{
    font-size:6rem;
    font-weight:900;
    color:#ccc;
    line-height:1;
    padding-bottom:4px;
  }}
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

    const clock = document.getElementById('clock');
    clock.innerHTML =
      `<div class="unit"><span class="num">${{pad(days)}}</span></div>` +
      `<div class="sep">:</div>` +
      `<div class="unit"><span class="num">${{pad(hours)}}</span></div>` +
      `<div class="sep">:</div>` +
      `<div class="unit"><span class="num">${{pad(minutes)}}</span></div>` +
      `<div class="sep">:</div>` +
      `<div class="unit"><span class="num">${{pad(seconds)}}</span></div>`;

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
