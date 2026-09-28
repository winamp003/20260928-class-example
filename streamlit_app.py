import csv
import io
import json

import streamlit as st


st.set_page_config(
    page_title="Streamlit Playground",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

accent_color = "#D45D3F"
with st.sidebar:
    st.markdown("### 🧪 STREAMLIT LAB")
    st.caption("기본 기능을 직접 만져보는 인터랙티브 쇼케이스")
    st.divider()
    show_hints = st.toggle("설명 표시", value=True)
    accent_color = st.color_picker("강조 색상", value=accent_color)
    st.selectbox("실행 모드", ["둘러보기", "직접 조작"], index=1)
    st.divider()
    st.caption("사이드바도 앱의 일부예요. 입력값은 즉시 반영됩니다.")

st.markdown(
    f"""
    <style>
    :root {{ --lab-accent: {accent_color}; }}
    .block-container {{ padding-top: 2.2rem; padding-bottom: 3rem; }}
    [data-testid="stSidebar"] {{ border-right: 1px solid rgba(128,128,128,.2); }}
    h1 {{ letter-spacing: -0.035em; }}
    .eyebrow {{ color: var(--lab-accent); font-size: .76rem; font-weight: 700;
                letter-spacing: .12em; text-transform: uppercase; }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">작은 앱을 빠르게, 풍부하게</div>', unsafe_allow_html=True)
st.title("Streamlit 기능 플레이그라운드")
st.write("입력부터 데이터 편집, 시각화, 파일 처리까지 한 화면에서 시험해 보세요.")

overview, widgets, data_lab, charts, files_lab = st.tabs(
    ["⌂ 개요", "◉ 입력 요소", "▦ 데이터", "▥ 시각화", "⇧ 파일·상태"]
)

with overview:
    st.subheader("앱의 현재 상태")
    metric_one, metric_two, metric_three, metric_four = st.columns(4)
    metric_one.metric("활성 세션", "1", "+1", help="현재 브라우저 세션 기준")
    metric_two.metric("렌더링", "실시간", "정상")
    metric_three.metric("구성 요소", "20+", "내장")
    metric_four.metric("실행 환경", "Python", "Streamlit")

    left, right = st.columns([1.35, 1], gap="large")
    with left:
        st.markdown("#### 한눈에 보는 사용량")
        st.area_chart(
            {"방문": [18, 24, 21, 32, 29, 43, 48], "가입": [4, 7, 6, 11, 9, 15, 19]},
            height=270,
        )
    with right:
        st.markdown("#### 상태 메시지")
        st.success("데이터 연결이 정상입니다.")
        st.info("위 탭을 이동해 기능을 직접 사용해 보세요.")
        st.warning("파일 업로드는 이 브라우저 세션에서만 처리됩니다.")
        if st.button("알림 띄우기", icon="🔔"):
            st.toast("버튼 이벤트가 정상적으로 전달됐어요.", icon="✅")
            st.balloons()

    with st.expander("이 페이지에 포함된 기능"):
        st.write(
            "사이드바 설정, 메트릭, 입력 위젯, 폼 제출, 데이터 에디터, 차트, "
            "파일 업로드와 다운로드, 진행 상태, 알림을 포함합니다."
        )

with widgets:
    st.subheader("입력 요소")
    st.caption("값을 바꾸면 Streamlit이 앱을 다시 실행해 결과를 갱신합니다.")
    first, second, third = st.columns(3)
    with first:
        name = st.text_input("이름", placeholder="예: 민지")
        quantity = st.number_input("수량", min_value=1, max_value=100, value=3)
        rating = st.slider("만족도", min_value=0, max_value=10, value=7)
    with second:
        category = st.selectbox("카테고리", ["디자인", "개발", "데이터", "기타"])
        tags = st.multiselect("관심 태그", ["Python", "시각화", "자동화", "AI"])
        priority = st.radio("우선순위", ["낮음", "보통", "높음"], horizontal=True)
    with third:
        due_date = st.date_input("날짜 선택")
        reminder = st.time_input("시간 선택")
        enabled = st.checkbox("알림 사용", value=True)
        st.toggle("미리보기 모드", value=False)

    if name:
        st.write(
            f"**{name}**님, {category} 항목 {quantity}개를 "
            f"{due_date}까지 준비합니다. 우선순위: {priority}, 만족도: {rating}/10."
        )
        st.caption(f"태그: {', '.join(tags) if tags else '선택 없음'} · 알림 시간: {reminder} · 사용 여부: {enabled}")

    st.divider()
    st.markdown("#### 폼으로 한 번에 제출")
    with st.form("feedback_form", clear_on_submit=False):
        feedback = st.text_area("의견", placeholder="개선 아이디어를 적어주세요.")
        score = st.select_slider("추천 점수", options=[1, 2, 3, 4, 5], value=4)
        submitted = st.form_submit_button("의견 제출", type="primary")
    if submitted:
        st.success(f"의견을 받았습니다. 추천 점수: {score}/5 · {feedback or '내용 없음'}")

with data_lab:
    st.subheader("표와 데이터 편집")
    st.caption("셀을 수정하거나 행을 추가·삭제한 뒤 아래 표에서 결과를 확인하세요.")
    sample_rows = [
        {"업무": "화면 설계", "담당자": "서연", "진행률": 80, "완료": False},
        {"업무": "API 연결", "담당자": "도윤", "진행률": 45, "완료": False},
        {"업무": "사용자 테스트", "담당자": "하린", "진행률": 100, "완료": True},
    ]
    edited_rows = st.data_editor(
        sample_rows,
        num_rows="dynamic",
        hide_index=True,
        width="stretch",
        key="editable_tasks",
    )
    st.markdown("#### 편집 결과")
    st.dataframe(edited_rows, hide_index=True, width="stretch")
    st.json({"행 수": len(edited_rows), "완료한 업무": sum(row["완료"] for row in edited_rows)})

with charts:
    st.subheader("데이터 시각화")
    period = st.select_slider("표시 기간", options=["1주", "2주", "1개월", "3개월"], value="1개월")
    chart_left, chart_right = st.columns(2, gap="large")
    with chart_left:
        st.markdown("#### 주간 추이")
        st.line_chart(
            {"방문자": [120, 155, 138, 190, 215, 202, 248], "주문": [18, 21, 17, 32, 35, 30, 42]},
            height=300,
        )
    with chart_right:
        st.markdown("#### 카테고리별 결과")
        st.bar_chart({"완료 항목": [32, 25, 19, 14], "대기 항목": [8, 12, 6, 10]}, height=300)
    st.caption(f"선택한 기간: {period} · 차트는 샘플 데이터로 표시됩니다.")

with files_lab:
    st.subheader("파일 업로드와 다운로드")
    uploaded_files = st.file_uploader(
        "CSV, JSON, 텍스트 또는 이미지를 선택하세요.",
        type=["csv", "json", "txt", "png", "jpg", "jpeg"],
        accept_multiple_files=True,
    )
    for uploaded_file in uploaded_files:
        st.markdown(f"**{uploaded_file.name}** · {uploaded_file.size:,} bytes")
        suffix = uploaded_file.name.rsplit(".", 1)[-1].lower()
        if suffix == "csv":
            text = uploaded_file.getvalue().decode("utf-8-sig")
            rows = list(csv.DictReader(io.StringIO(text)))
            st.dataframe(rows, width="stretch")
        elif suffix == "json":
            try:
                st.json(json.loads(uploaded_file.getvalue()))
            except (UnicodeDecodeError, json.JSONDecodeError):
                st.error("올바른 JSON 파일이 아닙니다.")
        elif suffix in {"png", "jpg", "jpeg"}:
            st.image(uploaded_file, caption=uploaded_file.name, width="stretch")
        else:
            st.text(uploaded_file.getvalue().decode("utf-8", errors="replace"))

    export_csv = "업무,진행률\n화면 설계,80\nAPI 연결,45\n사용자 테스트,100\n"
    st.download_button(
        "샘플 CSV 다운로드",
        data=export_csv.encode("utf-8-sig"),
        file_name="streamlit_sample.csv",
        mime="text/csv",
        icon="⬇️",
    )

    st.divider()
    st.markdown("#### 진행 상태와 알림")
    if st.button("작업 실행", type="primary", icon="▶️"):
        with st.status("샘플 작업을 실행하고 있습니다.", expanded=True) as status:
            progress = st.progress(0, text="준비 중")
            for step, label in enumerate(["데이터 읽기", "변환", "완료"], start=1):
                progress.progress(step / 3, text=label)
            status.update(label="작업이 완료됐습니다.", state="complete", expanded=False)
        st.toast("작업 완료", icon="✅")

if show_hints:
    st.divider()
    st.caption("더 알아보기: [Streamlit 문서](https://docs.streamlit.io/) · 위젯은 세션마다 독립적으로 동작합니다.")
