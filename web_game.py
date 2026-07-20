import streamlit as st

# 1. 网页标题和说明
st.title("🤖 电脑猜数字游戏")
st.write("请在心里想一个三位数字（100-999），我要开始猜了！")
st.write("-" * 30)

# 2. 初始化你的候选列表
if 'candidates' not in st.session_state:
    st.session_state.candidates = []
    for i in range(100, 1000):
        st.session_state.candidates.append(i)
if 'game_over' not in st.session_state:
    st.session_state.game_over = False


# === 核心逻辑函数（完全保留你手写的原版逻辑，绝不改动！） ===
def process_guess():
    guess = st.session_state.candidates[0]
    feedback = st.session_state.feedback_input

    if feedback == 3:
        st.session_state.game_over = True
    else:
        # ⬇️ 以下为你原本编写的循环判断代码，原封不动保留 ⬇️
        new_candidates = []
        for number in st.session_state.candidates:
            guess_str = str(guess)
            num_str = str(number)

            match_count = 0

            if guess_str[0] == num_str[0]:
                match_count += 1
            if guess_str[1] == num_str[1]:
                match_count += 1
            if guess_str[2] == num_str[2]:
                match_count += 1

            if match_count == feedback:
                new_candidates.append(number)

        st.session_state.candidates = new_candidates
        # ⬆️ 原版逻辑结束 ⬆️


def restart_game():
    st.session_state.candidates = []
    for i in range(100, 1000):
        st.session_state.candidates.append(i)
    st.session_state.game_over = False


# ============================================================

# 3. 游戏界面展示
if st.session_state.game_over:
    guess = st.session_state.candidates[0]
    st.success(f"我就知道答案是 {guess}！游戏结束！")
    st.button("重新开始游戏", on_click=restart_game)

elif len(st.session_state.candidates) > 0:
    guess = st.session_state.candidates[0]

    st.markdown(f"### 我猜是： **{guess}**")

    # 接收用户反馈
    st.number_input("请问猜对了几位数字？", min_value=0, max_value=3, step=1, key="feedback_input")

    # 按钮触发：点击时直接运行上面的 process_guess 函数
    st.button("提交反馈", on_click=process_guess)

else:
    st.error("哎呀，你是不是给错提示了？我已经找不到符合条件的数字啦！")
    st.button("重新开始游戏", on_click=restart_game)