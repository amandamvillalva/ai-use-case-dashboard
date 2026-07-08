import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from datetime import datetime

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Use Case Review Dashboard",
    page_icon="🤖",
    layout="wide",
)

# ── Moody's brand colors ──────────────────────────────────────────────────────
NAVY   = "#0a0a2e"
BLUE   = "#005EFF"
ORANGE = "#F26B43"

STATUS_COLORS = {
    "Live":                             "#00875A",
    "Approved":                         "#005EFF",
    "Build In Progress":                "#0052CC",
    "Pending Chapter Lead Approval":    "#F26B43",
    "Pending PLT Approval":             "#FF8B00",
    "Sent Back to Requestor":           "#6554C0",
    "On Hold":                          "#97A0AF",
    "New":                              "#00B8D9",
    "To be deleted with Navi launch":   "#FF5630",
    "Declined":                         "#BF2600",
    "Deleted":                          "#BF2600",
}

CHART_LAYOUT = dict(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#ffffff",
    font=dict(family="Arial", size=14, color=NAVY),
    margin=dict(t=50, b=20, l=10, r=80),
)

# ── Helper: clean nan values ──────────────────────────────────────────────────
def clean(val, fallback="Not provided"):
    if val is None:
        return fallback
    if isinstance(val, float) and pd.isna(val):
        return fallback
    s = str(val).strip()
    return s if s and s.lower() not in ("nan", "none", "") else fallback

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
  .stApp {{ background-color: #edf0f7; }}

  .section-card {{
    background: #ffffff;
    border-radius: 16px;
    padding: 32px 36px;
    margin-bottom: 36px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
  }}

  html, body,
  [class*="css"],
  p, span, div, label, h1, h2, h3, h4, h5, h6, li, a,
  .stMarkdown, .stText, .stCaption,
  [data-testid="stMarkdownContainer"] *,
  [data-testid="stText"] *,
  [data-testid="stCaptionContainer"] *,
  [data-testid="stExpander"] *,
  [data-testid="stExpanderDetails"] *,
  [data-testid="stHorizontalBlock"] *,
  [data-testid="column"] *,
  .streamlit-expanderHeader,
  .streamlit-expanderContent *,
  button, button *,
  .stButton *, .stDownloadButton *,
  [role="tab"], [role="tabpanel"] *
  {{ color: {NAVY} !important; }}

  .badge {{ color: #ffffff !important; }}
  .submit-btn, .submit-btn * {{ color: #ffffff !important; }}
  .card-num  {{ color: #ffffff !important; }}
  .card-lbl  {{ color: #ffffff !important; }}
  .section-title {{ color: #ffffff !important; }}

  [data-testid="stSidebar"] {{
    background-color: {NAVY} !important;
  }}
  [data-testid="stSidebar"] *,
  [data-testid="stSidebar"] p,
  [data-testid="stSidebar"] label,
  [data-testid="stSidebar"] span,
  [data-testid="stSidebar"] div {{
    color: #ffffff !important;
  }}
  [data-testid="stSidebar"] [data-baseweb="select"] div,
  [data-testid="stSidebar"] [data-baseweb="select"] input,
  [data-testid="stSidebar"] [data-baseweb="select"] span {{
    background-color: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    border-color: rgba(255,255,255,0.3) !important;
  }}
  [data-testid="stSidebar"] input[type="text"] {{
    background-color: rgba(255,255,255,0.12) !important;
    color: #ffffff !important;
    border-color: rgba(255,255,255,0.3) !important;
  }}
  [data-testid="stSidebar"] input[type="text"]::placeholder {{
    color: rgba(255,255,255,0.5) !important;
  }}
  [data-baseweb="popover"] ul li,
  [data-baseweb="popover"] ul li span,
  [data-baseweb="popover"] ul li div,
  [data-baseweb="menu"] li,
  [data-baseweb="menu"] li span {{
    color: #0a0a2e !important;
    background-color: #ffffff !important;
  }}
  [data-baseweb="popover"] ul li:hover,
  [data-baseweb="menu"] li:hover {{
    background-color: #e8eeff !important;
  }}
  [data-testid="stSidebar"] span[data-baseweb="tag"] {{
    background-color: {BLUE} !important;
  }}
  [data-testid="stSidebar"] span[data-baseweb="tag"] span {{
    color: #ffffff !important;
  }}
  [data-testid="stMultiSelect"] span[data-baseweb="tag"] {{ background-color: {BLUE} !important; }}
  [data-testid="stMultiSelect"] span[data-baseweb="tag"] span {{ color: #ffffff !important; }}

  .dash-header {{ text-align: center; padding: 10px 0 6px 0; }}
  .dash-title  {{ font-size: 1.9rem; font-weight: 800; color: {NAVY} !important; margin-top: 8px; }}
  .dash-sub    {{ font-size: 0.85rem; color: #555 !important; margin-top: 2px; }}

  .submit-btn {{
    display: inline-block;
    background-color: {NAVY};
    color: #ffffff !important;
    padding: 10px 24px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.95rem;
    text-decoration: none;
    margin: 12px auto 0 auto;
  }}
  .submit-btn:hover {{ background-color: {BLUE}; color: #ffffff !important; }}
  .btn-center {{ text-align: center; margin-bottom: 20px; }}

  .uc-card {{
    border-left: 5px solid {ORANGE};
    background-color: #eef2ff;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin-bottom: 12px;
  }}
  .uc-title {{ font-size: 1.05rem; font-weight: 700; margin-bottom: 6px; color: {NAVY} !important; }}
  .uc-meta  {{ font-size: 0.88rem; line-height: 1.7; color: #1a1a2e !important; }}
  .badge {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 8px;
  }}

  [data-testid="stMetricLabel"] p {{ color: {NAVY} !important; }}
  [data-testid="stMetricValue"]   {{ color: {BLUE} !important; }}
  [data-testid="stExpander"] summary p {{ color: {NAVY} !important; font-weight: 600; }}
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent / "data"

def load_latest_file():
    files = sorted(DATA_DIR.glob("*.xlsx"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not files:
        st.error("No Excel file found in the data/ folder.")
        st.stop()
    return files[0]

@st.cache_data(ttl=300)
def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    df.columns = df.columns.str.strip()
    for col in ["Total Score", "Band"]:
        if col in df.columns:
            df[col] = df[col].replace("#INVALID VALUE", pd.NA)
    df["Department/Team"] = df["Department/Team"].fillna("Unknown").str.strip()
    df["Status"] = df["Status"].fillna("Unknown").str.strip()
    return df

latest_file = load_latest_file()
df = load_data(str(latest_file))
df = df[~df["Status"].isin(["Deleted", "Declined"])].reset_index(drop=True)

file_modified = datetime.fromtimestamp(latest_file.stat().st_mtime).strftime("%B %d, %Y at %I:%M %p")

# ── Header ────────────────────────────────────────────────────────────────────
logo_path = Path(__file__).parent / "assets" / "mdy_logo_rgb_MoodysBlue.jpg"

st.markdown(f"""
<div style="text-align:center; padding: 20px 0 10px 0;">
    <img src="data:image/jpeg;base64,{__import__('base64').b64encode(open(str(logo_path),'rb').read()).decode()}"
         style="width:420px; margin-bottom:16px; mix-blend-mode:multiply;"><br>
    <span style="font-size:2rem; font-weight:800; color:{NAVY};">AI Use Case Review Dashboard</span><br>
    <span style="font-size:0.85rem; color:#555;">Moody's People Team</span><br>
    <span style="font-size:0.78rem; color:#888; margin-top:4px; display:inline-block;">
      📁 {latest_file.name} &nbsp;·&nbsp; 🕒 Last updated: {file_modified}
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="max-width:780px; margin:16px auto 32px auto; text-align:center;
            background:#ffffff; border-radius:12px; padding:18px 28px;
            box-shadow:0 2px 10px rgba(0,0,0,0.07); border-left:4px solid {BLUE}; text-align:left;">
  <span style="font-size:0.92rem; color:{NAVY}; line-height:1.7;">
    This dashboard provides the Moody's People team with a real-time view of all AI use case
    submissions under review by the AI Use Case Review Committee. Use it to track pipeline
    status, see which departments are most active, and explore individual use case details.
    Data is refreshed 1–2 times per week from the committee's Smartsheet export.
    <br><br>
    <b>Read-only.</b> To submit a new idea, use the form in the sidebar. ➡️
  </span>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image(str(logo_path), use_container_width=True)
    st.markdown("""
<div style="background-color:rgba(255,255,255,0.1); border-radius:10px; padding:14px 12px; text-align:center; margin-bottom:12px;">
    <div style="font-size:1rem; font-weight:700; color:#ffffff; margin-bottom:6px;">💡 Have a New AI Idea?</div>
    <div style="font-size:0.78rem; color:rgba(255,255,255,0.85); margin-bottom:12px; line-height:1.5;">
        If you have an idea for an AI use case, we want to hear it! Submit your idea for review by the committee.
    </div>
    <a href="https://app.smartsheet.com/b/form/019e46b887db7c1daebcc0c306b509f4" target="_blank"
       style="display:block; background-color:#F26B43; color:#ffffff; font-weight:700;
              padding:10px 0; border-radius:8px; text-decoration:none; font-size:0.88rem;">
        ➕ Submit a Use Case
    </a>
</div>
""", unsafe_allow_html=True)

    st.markdown("## 🔍 Filter Use Cases")
    st.markdown("---")

    search_query = st.text_input("🔎 Search by name or keyword", placeholder="e.g. onboarding, payroll...")

    all_statuses = sorted(df["Status"].unique().tolist())
    all_depts    = sorted(df["Department/Team"].unique().tolist())
    all_bands    = ["P1", "P2", "P3", "P4", "P5"]

    selected_statuses = st.multiselect("Status", options=all_statuses, default=[], placeholder="All statuses")
    st.markdown(" ")
    selected_depts = st.multiselect("Department", options=all_depts, default=[], placeholder="All departments")
    st.markdown(" ")
    selected_bands = st.multiselect("Score Band", options=all_bands, default=[], placeholder="All bands")

    filters_active = bool(selected_statuses or selected_depts or selected_bands or search_query)
    if filters_active:
        if st.button("✕ Clear all filters"):
            st.rerun()

    st.markdown("---")
    st.markdown("**📊 Score Band Reference**")
    st.markdown(f"""
<div style="display:flex; flex-direction:column; gap:6px; margin-bottom:12px;">
  <div style="background:rgba(255,255,255,0.08); border-left:3px solid #00875A; border-radius:6px; padding:7px 10px;">
    <span style="font-weight:800; color:#ffffff; class="section-title"">P1</span>
    <span style="color:rgba(255,255,255,0.85); font-size:0.78rem; margin-left:6px;">Approve &amp; expedite assignment.</span>
  </div>
  <div style="background:rgba(255,255,255,0.08); border-left:3px solid #4C9FEB; border-radius:6px; padding:7px 10px;">
    <span style="font-weight:800; color:#ffffff;">P2</span>
    <span style="color:rgba(255,255,255,0.85); font-size:0.78rem; margin-left:6px;">Approve &amp; high priority, normal queue.</span>
  </div>
  <div style="background:rgba(255,255,255,0.08); border-left:3px solid #F5A623; border-radius:6px; padding:7px 10px;">
    <span style="font-weight:800; color:#ffffff;">P3</span>
    <span style="color:rgba(255,255,255,0.85); font-size:0.78rem; margin-left:6px;">Approve or approve with conditions.</span>
  </div>
  <div style="background:rgba(255,255,255,0.08); border-left:3px solid #F26B43; border-radius:6px; padding:7px 10px;">
    <span style="font-weight:800; color:#ffffff;">P4</span>
    <span style="color:rgba(255,255,255,0.85); font-size:0.78rem; margin-left:6px;">Return for review: address gaps before re-submission.</span>
  </div>
  <div style="background:rgba(255,255,255,0.08); border-left:3px solid #DE350B; border-radius:6px; padding:7px 10px;">
    <span style="font-weight:800; color:#ffffff;">P5</span>
    <span style="color:rgba(255,255,255,0.85); font-size:0.78rem; margin-left:6px;">Decline or significant rework required.</span>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # Apply filters
    filtered_df = df.copy()
    if selected_statuses:
        filtered_df = filtered_df[filtered_df["Status"].isin(selected_statuses)]
    if selected_depts:
        filtered_df = filtered_df[filtered_df["Department/Team"].isin(selected_depts)]
    if selected_bands:
        filtered_df = filtered_df[filtered_df["Band"].isin(selected_bands)]
    if search_query:
        q = search_query.lower()
        mask = (
            filtered_df["Use Case Name"].fillna("").str.lower().str.contains(q) |
            filtered_df.get("Description", pd.Series(dtype=str)).fillna("").str.lower().str.contains(q)
        )
        filtered_df = filtered_df[mask]

    if filters_active:
        st.caption(f"Showing **{len(filtered_df)}** of {len(df)} use cases")
    else:
        st.caption(f"Showing all **{len(df)}** use cases")


# ── Helper: render a use case card ────────────────────────────────────────────
def uc_card(row, border_color=None):
    status      = str(row.get("Status", "Unknown"))
    badge_color = STATUS_COLORS.get(status, "#AAAAAA")
    top_color   = border_color or badge_color
    name        = clean(row.get("Use Case Name"), "Unnamed")
    description = clean(row.get("Description") or row.get("What do you want to build?"))
    savings     = clean(row.get("Time Savings"))
    rec         = clean(row.get("Recommendation"))
    go_live     = clean(row.get("Target Go-Live Date"))
    band        = row.get("Band")
    score       = row.get("Total Score")
    score_line  = (f"<br><span style='font-size:0.78rem;'><b>Score:</b> {score} &nbsp;|&nbsp; "
                   f"<b>Band:</b> {band}</span>") if pd.notna(band) and pd.notna(score) else ""
    go_live_line = f"<br><b>Target Go-Live:</b> {go_live}" if go_live != "Not provided" else ""
    return f"""
<div style="background:#ffffff; border-radius:12px; padding:18px 16px; margin-bottom:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08); border-top:4px solid {top_color};
            height:100%; display:flex; flex-direction:column; gap:8px;">
  <div style="font-weight:800; color:{NAVY}; font-size:0.95rem; line-height:1.3;">{name}</div>
  <div>
    <span style="background:{badge_color}; color:#fff; border-radius:20px;
                 padding:3px 10px; font-size:0.72rem; font-weight:700;">{status}</span>
  </div>
  <div style="color:#444; font-size:0.82rem; line-height:1.5; flex:1;">{description}</div>
  <div style="border-top:1px solid #eee; padding-top:8px; font-size:0.78rem; color:{NAVY};">
    <b>Time Savings:</b> {savings}<br>
    <b>Recommendation:</b> {rec}{go_live_line}{score_line}
  </div>
</div>"""


# ── Section 1: Pipeline Overview ─────────────────────────────────────────────
st.subheader("📊 Pipeline Overview")

total     = len(filtered_df)
live      = (filtered_df["Status"] == "Live").sum()
approved  = filtered_df["Status"].isin(["Approved", "Build In Progress"]).sum()
in_review = filtered_df["Status"].isin(["New", "Pending Chapter Lead Approval", "Pending PLT Approval"]).sum()
navi      = filtered_df["Status"].str.contains("Navi", case=False, na=False).sum()
on_hold   = (filtered_df["Status"] == "On Hold").sum()

# P1/P2 summary
reviewed_df  = filtered_df[filtered_df["Band"].notna()]
high_pri     = reviewed_df["Band"].isin(["P1", "P2"]).sum()
reviewed_cnt = len(reviewed_df)

def stat_card(label, value, bg_color, anchor):
    return f"""
    <a href="#{anchor}" style="text-decoration:none;">
    <div style="background-color:{bg_color}; border-radius:10px; padding:14px 10px;
                text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.12);
                cursor:pointer; transition: opacity 0.2s;"
         onmouseover="this.style.opacity='0.85'" onmouseout="this.style.opacity='1'">
        <div class="card-num" style="font-size:1.7rem; font-weight:800;">{value}</div>
        <div class="card-lbl" style="font-size:0.78rem; font-weight:600; margin-top:4px;">{label}</div>
        <div class="card-lbl" style="font-size:0.68rem; margin-top:4px; opacity:0.8;">click to view ↓</div>
    </div></a>"""

c1, c2, c3, c4, c5 = st.columns(5)
c1.markdown(stat_card("Total Submissions",    total,     "#0a0a2e", "status-breakdown"), unsafe_allow_html=True)
c2.markdown(stat_card("Live",                live,      "#00875A", "cases-live"),       unsafe_allow_html=True)
c3.markdown(stat_card("Approved / In Build", approved,  "#005EFF", "status-breakdown"), unsafe_allow_html=True)
c4.markdown(stat_card("Pending Review",      in_review, "#F26B43", "pending-review"),   unsafe_allow_html=True)
c5.markdown(stat_card("Flagged for Navi",    navi,      "#BF2600", "navi-impact"),      unsafe_allow_html=True)

# P1/P2 highlight + pipeline funnel
st.markdown("<br>", unsafe_allow_html=True)
col_insight, col_funnel = st.columns([1, 2])

with col_insight:
    st.markdown(
        f'<div style="background:{BLUE}; border-radius:12px; padding:20px 24px; text-align:center; '
        f'box-shadow:0 2px 10px rgba(0,94,255,0.2);">'
        f'<div style="font-size:2.6rem; font-weight:800; color:#ffffff;">  {high_pri}</div>'
        f'<div style="font-size:0.88rem; color:rgba(255,255,255,0.9); margin-top:6px; font-weight:600;">'
        f'High-Priority Cases (P1 or P2)</div>'
        f'<div style="font-size:0.75rem; color:rgba(255,255,255,0.7); margin-top:4px;">'
        f'out of {reviewed_cnt} reviewed cases</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

with col_funnel:
    pct_approved = f"{int(approved/total*100)}%" if total else "0%"
    pct_live     = f"{int(live/total*100)}%" if total else "0%"
    st.markdown(f"""
<div style="display:flex; align-items:center; justify-content:center; gap:0; height:100%; padding:12px 0;">

  <div style="background:{ORANGE}; border-radius:12px; padding:18px 20px; text-align:center;
              min-width:140px; box-shadow:0 2px 10px rgba(242,107,67,0.3);">
    <div style="font-size:2rem; font-weight:800; color:#ffffff;">{int(in_review)}</div>
    <div style="font-size:0.78rem; font-weight:700; color:rgba(255,255,255,0.9); margin-top:4px;">In Review</div>
  </div>

  <div style="display:flex; flex-direction:column; align-items:center; padding:0 6px;">
    <div style="font-size:1.4rem; color:#aaa;">→</div>
    <div style="font-size:0.68rem; color:#888; margin-top:2px;">{pct_approved} of total</div>
  </div>

  <div style="background:{BLUE}; border-radius:12px; padding:18px 20px; text-align:center;
              min-width:140px; box-shadow:0 2px 10px rgba(0,94,255,0.3);">
    <div style="font-size:2rem; font-weight:800; color:#ffffff;">{int(approved)}</div>
    <div style="font-size:0.78rem; font-weight:700; color:rgba(255,255,255,0.9); margin-top:4px;">Approved / In Build</div>
  </div>

  <div style="display:flex; flex-direction:column; align-items:center; padding:0 6px;">
    <div style="font-size:1.4rem; color:#aaa;">→</div>
    <div style="font-size:0.68rem; color:#888; margin-top:2px;">{pct_live} of total</div>
  </div>

  <div style="background:#00875A; border-radius:12px; padding:18px 20px; text-align:center;
              min-width:140px; box-shadow:0 2px 10px rgba(0,135,90,0.3);">
    <div style="font-size:2rem; font-weight:800; color:#ffffff;">{int(live)}</div>
    <div style="font-size:0.78rem; font-weight:700; color:rgba(255,255,255,0.9); margin-top:4px;">Live</div>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown('<div id="status-breakdown"></div>', unsafe_allow_html=True)
st.markdown(
    f'<div style="background-color:{BLUE}; border-radius:10px; padding:16px 24px; '
    f'margin:8px 0 4px 0; box-shadow:0 3px 10px rgba(0,0,0,0.15);">'
    f'<span style="color:#ffffff; font-size:1.2rem; font-weight:800; letter-spacing:0.5px;" class="section-title">'
    f'📊 Status Breakdown</span></div>',
    unsafe_allow_html=True,
)
status_counts = filtered_df["Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]
status_counts = status_counts.sort_values("Count", ascending=True)
color_map = {s: STATUS_COLORS.get(s, "#AAAAAA") for s in status_counts["Status"]}

fig_status = px.bar(
    status_counts, x="Count", y="Status", orientation="h",
    color="Status", color_discrete_map=color_map, text="Count",
    title="All Submissions by Status",
    labels={"Status": "", "Count": "Number of Use Cases"},
)
fig_status.update_traces(
    textposition="outside",
    textfont=dict(color=NAVY, size=14, family="Arial"),
    marker_line_width=0,
)
fig_status.update_layout(
    **CHART_LAYOUT,
    showlegend=False,
    height=520,
    xaxis=dict(showgrid=True, gridcolor="#e0e0e0",
               title=dict(text="Number of Use Cases", font=dict(color=NAVY)),
               tickfont=dict(color=NAVY)),
    yaxis=dict(tickfont=dict(color=NAVY, size=13)),
)
st.caption("💡 Click a bar to filter the department chart below. Click again to clear.")
sel_status = st.plotly_chart(fig_status, use_container_width=True, on_select="rerun",
                             selection_mode="points", key="plot_status")

clicked_status = None
if sel_status and sel_status.selection and sel_status.selection.points:
    clicked_status = sel_status.selection.points[0].get("y")

st.markdown('<div style="margin-top:8px;"></div>', unsafe_allow_html=True)

# ── Submissions by Department chart ──────────────────────────────────────────
st.markdown(
    f'<div style="background-color:{BLUE}; border-radius:10px; padding:16px 24px; '
    f'margin:8px 0 4px 0; box-shadow:0 3px 10px rgba(0,0,0,0.15);">'
    f'<span style="color:#ffffff; font-size:1.2rem; font-weight:800; letter-spacing:0.5px;" class="section-title">'
    f'🏢 Submissions by Department</span></div>',
    unsafe_allow_html=True,
)
if clicked_status:
    st.caption(f"Filtered to status: **{clicked_status}** — click the bar again to clear")
    _dept_source = filtered_df[filtered_df["Status"] == clicked_status]
else:
    _dept_source = filtered_df
dept_counts = (
    _dept_source.groupby("Department/Team").size()
    .reset_index(name="Count")
    .sort_values("Count", ascending=True)
)
fig_dept = px.bar(
    dept_counts, x="Count", y="Department/Team", orientation="h",
    color_discrete_sequence=[BLUE], text="Count",
    labels={"Department/Team": "", "Count": "Submissions"},
    title="Number of Use Cases per Department",
)
fig_dept.update_traces(
    textposition="outside",
    textfont=dict(color=NAVY, size=14, family="Arial"),
    marker_line_width=0,
)
fig_dept.update_layout(
    **CHART_LAYOUT,
    height=500,
    xaxis=dict(showgrid=True, gridcolor="#e0e0e0",
               title=dict(text="Number of Submissions", font=dict(color=NAVY)),
               tickfont=dict(color=NAVY)),
    yaxis=dict(tickfont=dict(color=NAVY, size=13)),
)
st.plotly_chart(fig_dept, use_container_width=True, key="plot_dept")

st.markdown('<div style="margin-top:8px;"></div>', unsafe_allow_html=True)

# ── Three spotlight charts ────────────────────────────────────────────────────
def spotlight_chart(subset_df, title, subtitle, color, chart_key):
    st.markdown(
        f'<div style="background-color:{color}; border-radius:10px; padding:16px 24px; '
        f'margin:8px 0 4px 0; box-shadow:0 3px 10px rgba(0,0,0,0.15);">'
        f'<span style="color:#ffffff; font-size:1.2rem; font-weight:800; '
        f'letter-spacing:0.5px;" class="section-title">{title}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
    if subset_df.empty:
        st.info("No cases currently match this status.")
        return

    counts = (
        subset_df.groupby("Department/Team").size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=True)
    )
    bar_height = max(300, len(counts) * 55 + 80)
    fig = px.bar(
        counts, x="Count", y="Department/Team", orientation="h",
        color_discrete_sequence=[color], text="Count",
        labels={"Department/Team": "", "Count": "Number of Cases"},
    )
    fig.update_traces(
        textposition="outside",
        textfont=dict(color=NAVY, size=14, family="Arial"),
        marker_line_width=0,
    )
    fig.update_layout(
        paper_bgcolor="#ffffff", plot_bgcolor="#ffffff",
        font=dict(family="Arial", size=14, color=NAVY),
        margin=dict(t=20, b=20, l=10, r=80),
        height=bar_height,
        xaxis=dict(showgrid=True, gridcolor="#e0e0e0",
                   title=dict(text="Number of Cases", font=dict(color=NAVY)),
                   tickfont=dict(color=NAVY), dtick=1),
        yaxis=dict(tickfont=dict(color=NAVY, size=13)),
    )
    st.caption("💡 Click a bar to filter the details below. Click again to clear.")
    sel = st.plotly_chart(fig, use_container_width=True, on_select="rerun",
                          selection_mode="points", key=f"plot_{chart_key}")

    selected_dept = None
    if sel and sel.selection and sel.selection.points:
        selected_dept = sel.selection.points[0].get("y")

    st.markdown("**Case details:**")
    if selected_dept:
        st.caption(f"Filtered to: **{selected_dept}**")
        detail_df = subset_df[subset_df["Department/Team"] == selected_dept]
    else:
        detail_df = subset_df

    departments = (
        detail_df.groupby("Department/Team").size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=False)["Department/Team"]
        .tolist()
    )
    for dept in departments:
        dept_df = detail_df[detail_df["Department/Team"] == dept].reset_index(drop=True)
        with st.expander(f"🏢 {dept}  —  {len(dept_df)} case(s)", expanded=selected_dept is not None):
            cols = st.columns(3)
            for i, (_, row) in enumerate(dept_df.iterrows()):
                with cols[i % 3]:
                    st.markdown(uc_card(row, border_color=color), unsafe_allow_html=True)

pending_df = filtered_df[filtered_df["Status"].isin([
    "Pending Chapter Lead Approval", "Pending PLT Approval"
])]
on_hold_df = filtered_df[filtered_df["Status"] == "On Hold"]
live_df    = filtered_df[filtered_df["Status"] == "Live"]

st.markdown('<div id="pending-review"></div>', unsafe_allow_html=True)
spotlight_chart(pending_df, "⏳ Pending Review", "", "#F26B43", "pending")
st.markdown("<br>", unsafe_allow_html=True)
spotlight_chart(on_hold_df, "⏸️ Cases On Hold", "", "#6554C0", "onhold")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div id="cases-live"></div>', unsafe_allow_html=True)
spotlight_chart(live_df, "✅ Cases Live", "", "#00875A", "live")

st.markdown('<div style="margin-top:8px;"></div>', unsafe_allow_html=True)

# ── Section 3: Enterprise Navigator Impact ────────────────────────────────────
st.markdown('<div id="navi-impact"></div>', unsafe_allow_html=True)
st.markdown(
    f'<div style="background-color:#FF5630; border-radius:10px; padding:16px 24px; '
    f'margin:8px 0 4px 0; box-shadow:0 3px 10px rgba(0,0,0,0.15);">'
    f'<span style="color:#ffffff; font-size:1.2rem; font-weight:800; letter-spacing:0.5px;" class="section-title">'
    f'🔄 Enterprise Navigator Impact</span></div>',
    unsafe_allow_html=True,
)
navi_df = filtered_df[filtered_df["Status"].str.contains("Navi", case=False, na=False)].reset_index(drop=True)

st.metric("Use Cases to Be Replaced", int(navi))
st.caption("These use cases are expected to sunset when Enterprise Navigator launches.")

if len(navi_df) > 0:
    cols = st.columns(3)
    for i, (_, row) in enumerate(navi_df.iterrows()):
        with cols[i % 3]:
            st.markdown(uc_card(row, border_color="#FF5630"), unsafe_allow_html=True)

st.markdown('<div style="margin-top:8px;"></div>', unsafe_allow_html=True)

# ── Section 4: Use Case Breakdown by Department ───────────────────────────────
st.markdown(
    f'<div style="background-color:{NAVY}; border-radius:10px; padding:16px 24px; '
    f'margin:8px 0 4px 0; box-shadow:0 3px 10px rgba(0,0,0,0.15);">'
    f'<span style="color:#ffffff; font-size:1.2rem; font-weight:800; letter-spacing:0.5px;" class="section-title">'
    f'📋 Use Case Breakdown by Department</span></div>',
    unsafe_allow_html=True,
)
departments = (
    filtered_df.groupby("Department/Team").size()
    .reset_index(name="Count")
    .sort_values("Count", ascending=False)["Department/Team"]
    .tolist()
)

for dept in departments:
    dept_df = filtered_df[filtered_df["Department/Team"] == dept].reset_index(drop=True)
    with st.expander(f"🏢 {dept}  —  {len(dept_df)} use case(s)"):
        cols = st.columns(3)
        for i, (_, row) in enumerate(dept_df.iterrows()):
            with cols[i % 3]:
                st.markdown(uc_card(row), unsafe_allow_html=True)
