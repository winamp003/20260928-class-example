from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="김요한 | 전기·신재생에너지 교육",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');
    :root {
        --ink: #191f28;
        --muted: #788391;
        --paper: #ffffff;
        --surface: #f7f9fc;
        --accent: #3182f6;
        --accent-hover: #1769e0;
        --accent-soft: #f2f7ff;
        --accent-border: #e6efff;
        --upload-border: #b9d2fb;
        --note: #596574;
        --on-accent: #ffffff;
        --sun: #f2ce45;
        --line: #e8edf3;
    }
    [data-theme="dark"] {
        --ink: #eef3f9;
        --muted: #a5b0bf;
        --paper: #10151d;
        --surface: #1a222d;
        --accent: #78adff;
        --accent-hover: #9bc2ff;
        --accent-soft: #1d2b40;
        --accent-border: #2d405a;
        --upload-border: #506f9d;
        --note: #c3ccd8;
        --on-accent: #101722;
        --line: #303b49;
        color-scheme: dark;
    }
    .stApp { background: var(--paper); color: var(--ink); font-family: 'DM Sans', 'Noto Sans KR', sans-serif; }
    .block-container { max-width: 1080px; padding-top: 2rem; padding-bottom: 4rem; }
    h1, h2, h3, p, label { font-family: 'DM Sans', 'Noto Sans KR', sans-serif; }
    h1, h2, h3 { color: var(--ink); font-weight: 700; }
    h1 { font-size: 4rem; line-height: 1.08; }
    h2 { font-size: 1.7rem; }
    h3 { font-size: 1.2rem; }
    [data-testid="stHeader"] { background: var(--paper); border-bottom: 1px solid var(--line); }
    [data-testid="stSidebar"] { background: var(--surface); border-right: 1px solid var(--line); }
    [data-testid="stMetric"] { background: var(--accent-soft); border: 1px solid var(--accent-border);
                                border-radius: 8px; padding: 1rem 1.1rem; }
    [data-testid="stMetricLabel"] { color: var(--muted); }
    [data-testid="stMetricValue"] { color: var(--ink); font-size: 1.05rem; font-weight: 700;
                                      line-height: 1.3; white-space: normal; overflow-wrap: anywhere; }
    [data-testid="stMetricValue"] div { font-size: inherit; line-height: inherit;
                                         white-space: normal; overflow-wrap: anywhere; }
    [data-testid="stTabs"] [role="tab"] { color: var(--muted); font-weight: 600; }
    [data-testid="stTabs"] [aria-selected="true"] { color: var(--accent); }
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] { background-color: var(--accent); }
    [data-testid="stBaseButton-primary"] { background: var(--accent); color: var(--on-accent);
                                             border: 0; border-radius: 8px; }
    [data-testid="stBaseButton-primary"]:hover { background: var(--accent-hover); border: 0; }
    [data-testid="stBaseButton-secondary"] { border: 1px solid var(--line); border-radius: 8px; }
    [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
        background: var(--surface); color: var(--ink);
    }
    [data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent);
    }
    [data-testid="stFileUploader"] section { background: var(--accent-soft);
                                               border: 1px dashed var(--upload-border); border-radius: 8px; }
    [data-testid="stRadio"] [role="radiogroup"] { flex-wrap: wrap; column-gap: .7rem; row-gap: .2rem; }
    [data-testid="stRadio"] [role="radiogroup"] label p { font-size: .84rem; line-height: 1.35;
                                                              white-space: normal; overflow-wrap: anywhere; }
    .eyebrow { color: var(--accent); font: 700 .76rem 'DM Sans', sans-serif;
               letter-spacing: .09em; text-transform: uppercase; }
    .hero-title span { color: var(--sun); }
    .hero-note { color: var(--note); font-size: 1.05rem; line-height: 1.8; max-width: 38rem; }
    .initials { align-items: center; background: var(--accent); border-radius: 8px;
                color: var(--on-accent); display: flex; font: 700 5rem 'DM Sans', 'Noto Sans KR', sans-serif;
                justify-content: center; min-height: 330px; }
    [data-testid="stImage"] img { height: 330px; object-fit: cover; object-position: center 38%; border-radius: 8px; }
    .section-kicker { color: var(--accent); font: 700 .74rem 'DM Sans', sans-serif;
                      letter-spacing: .09em; text-transform: uppercase; }
    .profile-card { background: var(--surface); border: 1px solid var(--line); border-left: 4px solid var(--sun);
                    border-radius: 8px; margin: .45rem 0; padding: .9rem 1rem; }
    div[data-testid="stForm"] { background: var(--surface); border: 1px solid var(--line);
                                 border-radius: 8px; padding: 1.2rem; }
    hr { border-color: var(--line); }
    @media (max-width: 700px) {
        .block-container { padding-top: 1rem; }
        h1 { font-size: 3rem; }
        .initials { min-height: 220px; }
        [data-testid="stImage"] img { height: 260px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### 김요한")
    st.caption("전기 · 신재생에너지 · AI 융합교육")
    st.divider()
    st.markdown("서울공업고등학교")
    st.markdown("신재생에너지과 부장")
    st.markdown("숙명여자대학교 대학원 재학")
    st.divider()
    st.caption("프로필 사진은 아래 사진 영역에서 추가할 수 있습니다.")

intro_column, portrait_column = st.columns([1.35, 1], gap="large", vertical_alignment="center")
with intro_column:
    st.markdown('<div class="eyebrow">TEACHER · ENERGY · LEARNING</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">김요한<span>⚡</span></h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hero-note">서울공업고등학교에서 전기 교과를 가르치며, '
        '신재생에너지과를 이끌고 있습니다. AI 융합교육을 공부하며 '
        '기술과 배움이 만나는 지점을 탐구합니다.</p>',
        unsafe_allow_html=True,
    )
    st.markdown("**전기 교육**　/　**신재생에너지**　/　**AI 융합교육**")

with portrait_column:
    portrait_path = Path(__file__).resolve().parent / "images1" / "123.jpg"
    st.image(portrait_path, caption="김요한", width="stretch")

st.divider()
first_metric, second_metric, third_metric = st.columns(3)
first_metric.metric("가르치는 교과", "전기")
second_metric.metric("맡은 역할", "신재생에너지과 부장")
third_metric.metric("배움", "AI융합교육 대학원")

profile_tab, education_tab, contact_tab = st.tabs(["프로필", "교육과 관심", "연락하기"])

with profile_tab:
    st.markdown('<div class="section-kicker">ABOUT</div>', unsafe_allow_html=True)
    st.header("기술을 가르치고, 배움을 새롭게 고민합니다")
    teaching_column, study_column = st.columns(2, gap="large")
    with teaching_column:
        st.markdown("#### 학교에서")
        st.write("서울공업고등학교에서 전기 교과를 가르치고 있습니다.")
        st.markdown('<div class="profile-card"><b>현재 역할</b><br>신재생에너지과 부장</div>', unsafe_allow_html=True)
    with study_column:
        st.markdown("#### 대학원에서")
        st.write("숙명여자대학교 대학원 AI융합교육과에 재학 중입니다.")
        st.markdown('<div class="profile-card"><b>관심의 접점</b><br>전기·에너지 교육과 AI 융합교육</div>', unsafe_allow_html=True)
    with st.expander("조금 더 소개합니다"):
        st.write(
            "전기 교과와 신재생에너지 분야의 교육 경험을 바탕으로, "
            "AI 융합교육을 공부하고 있습니다. 수업과 배움에 대한 이야기를 나누고 싶습니다."
        )

    st.divider()
    st.markdown("#### 김요한 알아가기 퀴즈")
    st.caption("다섯 문제를 모두 맞히면 특별한 축하 메시지가 나와요.")
    quiz_questions = [
        {
            "question": "현재 근무하는 학교는 어디일까요?",
            "options": ["서울공업고등학교", "숙명여자대학교", "서울과학고등학교", "경기공업고등학교"],
            "answer": "서울공업고등학교",
        },
        {
            "question": "가르치는 교과는 무엇일까요?",
            "options": ["전기", "미술", "국어", "체육"],
            "answer": "전기",
        },
        {
            "question": "부장으로 맡고 있는 학과는 어디일까요?",
            "options": ["신재생에너지과", "기계과", "건축과", "조리과"],
            "answer": "신재생에너지과",
        },
        {
            "question": "대학원에서 공부하는 전공은 무엇일까요?",
            "options": ["AI융합교육", "경영학", "환경공학", "체육교육"],
            "answer": "AI융합교육",
        },
        {
            "question": "수업 밖에서 관심을 두고 있는 것은 무엇일까요?",
            "options": ["운동", "등산", "요리", "사진"],
            "answer": "운동",
        },
    ]

    with st.form("profile_quiz"):
        selected_answers = [
            st.radio(
                f"{index}. {item['question']}",
                item["options"],
                key=f"profile_quiz_{index}",
                horizontal=True,
            )
            for index, item in enumerate(quiz_questions, start=1)
        ]
        quiz_submitted = st.form_submit_button("정답 확인", type="primary")

    if quiz_submitted:
        correct_count = sum(
            selected == item["answer"]
            for selected, item in zip(selected_answers, quiz_questions)
        )
        st.progress(correct_count / len(quiz_questions), text=f"정답 {correct_count} / {len(quiz_questions)}")
        if correct_count == len(quiz_questions):
            st.success("축하드립니다. 김요한에 대해 많이 공부하셨군요!!")
            st.balloons()
        else:
            st.info(f"{len(quiz_questions)}문제 중 {correct_count}문제를 맞혔어요. 틀린 답을 확인해 보세요.")
            for index, (selected, item) in enumerate(zip(selected_answers, quiz_questions), start=1):
                if selected != item["answer"]:
                    st.caption(f"{index}번 정답: {item['answer']}")

with education_tab:
    st.markdown('<div class="section-kicker">TEACHING & INTERESTS</div>', unsafe_allow_html=True)
    st.header("관심을 두고 있는 분야")
    interest_columns = st.columns(3, gap="medium")
    with interest_columns[0]:
        st.markdown("#### 01 / 전기")
        st.write("서울공업고등학교 전기 교과")
    with interest_columns[1]:
        st.markdown("#### 02 / 에너지")
        st.write("신재생에너지과 부장으로 교육 현장에 함께합니다.")
    with interest_columns[2]:
        st.markdown("#### 03 / AI 교육")
        st.write("숙명여자대학교 대학원에서 AI융합교육을 공부합니다.")
    st.divider()
    st.markdown("#### 수업 밖의 관심")
    st.write("운동을 좋아하고, 꾸준히 몸을 움직이는 데 관심이 많습니다.")

with contact_tab:
    st.markdown('<div class="section-kicker">CONTACT</div>', unsafe_allow_html=True)
    st.header("편하게 연락 주세요")
    contact_column, guestbook_column = st.columns([0.85, 1.15], gap="large")
    with contact_column:
        st.markdown("#### 전화")
        st.link_button("010-0000-0000 전화하기", "tel:01000000000", icon="📞")
        st.caption("연락처를 누르면 기기의 전화 앱이 열립니다.")
        contact_card = "BEGIN:VCARD\nVERSION:3.0\nFN:김요한\nTEL:010-0000-0000\nORG:서울공업고등학교\nTITLE:신재생에너지과 부장\nEND:VCARD\n"
        st.download_button(
            "연락처 저장",
            data=contact_card,
            file_name="김요한.vcf",
            mime="text/vcard",
            icon="📥",
        )
    with guestbook_column:
        st.markdown("#### 방명록")
        with st.form("guestbook_form", clear_on_submit=True):
            visitor_name = st.text_input("이름", placeholder="이름을 입력해 주세요")
            visitor_message = st.text_area("메시지", placeholder="인사나 응원의 말을 남겨주세요")
            guestbook_submitted = st.form_submit_button("메시지 남기기", type="primary")

        if "guestbook" not in st.session_state:
            st.session_state.guestbook = []
        if guestbook_submitted:
            if visitor_name.strip() and visitor_message.strip():
                st.session_state.guestbook.insert(
                    0, {"name": visitor_name.strip(), "message": visitor_message.strip()}
                )
                st.toast("방명록에 메시지를 남겼습니다.", icon="✍️")
            else:
                st.warning("이름과 메시지를 모두 입력해 주세요.")

        if st.session_state.guestbook:
            for entry in st.session_state.guestbook[:3]:
                st.markdown(f"**{entry['name']}**　{entry['message']}")
        else:
            st.caption("첫 인사를 남겨주세요. 방명록은 현재 세션에서만 유지됩니다.")

st.divider()
st.caption("김요한 · 서울공업고등학교 · 전기 및 신재생에너지 교육")
