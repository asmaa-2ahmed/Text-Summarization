import streamlit as st
from src.inference import text_summarizer
from src.schemas import SummarizationRequest
from pathlib import Path
import html

def load_css(file_name: str):
    css_path = Path(__file__).resolve().parent / file_name
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    # App Config
    st.set_page_config(
        page_title="📝 Text Summarizer Pro | BART", 
        page_icon="✂️",
        layout="wide"
    )

    # Load CSS
    load_css("styles.css")

    # Header
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e88e5 0%, #0d47a1 100%);
                padding: 1rem;
                border-radius: 8px;
                color: white;
                margin-bottom: 1.5rem;">
        <h1 style="color: white; margin: 0;">📝 Text Summarizer Pro</h1>
        <p style="color: #e3f2fd; margin: 0;">Summarize long articles using Facebook's BART-large-CNN model ✨</p>
    </div>
    """, unsafe_allow_html=True)

    # Session state handling
    if "clear_trigger" not in st.session_state:
        st.session_state.clear_trigger = False
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

    if st.session_state.clear_trigger:
        st.session_state.input_text = ""
        st.session_state.clear_trigger = False

    # Input Section
    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        input_text = st.text_area(
            "📋 **Paste your text here:**",
            height=300,
            placeholder="Paste your article, research paper, or report here...",
            key="input_text"
        )

    # Sidebar / Controls
    with col2:
        with st.expander("⚙️ **Summary Settings**", expanded=True):
            max_len = st.number_input(
                "**Max Length** 📏", 
                min_value=30, 
                max_value=200, 
                value=70,
                step=1,
                help="Maximum word count for the summary"
            )
            min_len = st.number_input(
                "**Min Length** 📌", 
                min_value=10, 
                max_value=100, 
                value=30,
                step=1,
                help="Minimum word count to ensure key details"
            )
            st.caption("💡 Tip: Use 30-70 words for concise summaries")

    # Buttons with spacing
    col1, col_spacer, col2 = st.columns([0.25, 0.1, 0.25])
    with col1:
        generate_btn = st.button("✨ **Generate Summary**", use_container_width=True)
    with col_spacer:
        st.write("")
    with col2:
        clear_btn = st.button("🗑️ **Clear Text**", use_container_width=True)

    # Handle Clear Button Click
    if clear_btn:
        st.session_state.clear_trigger = True
        st.rerun()


    # Generate Summary
    if generate_btn and input_text.strip():
        with st.spinner("🔍 Analyzing text..."):
            request = SummarizationRequest(
                text=input_text,
                max_length=max_len,
                min_length=min_len
            )

            response = text_summarizer.summarize(request)

            # Handle both object and dict responses
            status = getattr(response, "status", response.get("status") if isinstance(response, dict) else None)
            summary_text = getattr(response, "summary", response.get("summary") if isinstance(response, dict) else None)

            if status == "success" and summary_text:
                safe_summary = html.escape(summary_text)

                st.subheader("📌 Summary")
                st.markdown(f"""
                <div class="summary-box">
                    {safe_summary}
                </div>
                """, unsafe_allow_html=True)

                # Correct Stats
                words_in = len(input_text.split())
                words_out = len(summary_text.split())
                if words_in > 0:
                    retention = words_out / words_in
                    reduction = 1 - retention
                    st.caption(
                        f"📉 {words_out} / {words_in} words — "
                        f"compressed to {retention:.0%} of the original ({reduction:.0%} shorter)"
                    )
            else:
                st.error(f"⚠️ {summary_text if summary_text else 'Unknown error occurred'}")

    elif generate_btn and not input_text.strip():
        st.warning("⚠️ Please enter text to summarize")

if __name__ == "__main__":
    main()
