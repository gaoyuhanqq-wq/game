import streamlit as st
import random  # 引入随机库，用来随机挑选表情和句子

# 1. 网页标题和说明
st.title("🥰小石宝宝你来啦！和我猜数字吧！")
st.write("在心里想一个三位数字哦宝宝，我要开始猜了！")
st.write("-" * 30)

# 2. 初始化你的候选列表和状态
if 'candidates' not in st.session_state:
    st.session_state.candidates = []
    for i in range(100, 1000):
        st.session_state.candidates.append(i)
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
# 新增：用来记住电脑被反馈后的“反应”
if 'reaction' not in st.session_state:
    st.session_state.reaction = ""


# === 核心逻辑函数（绝不改动你的原版循环逻辑！） ===
def process_guess():
    guess = st.session_state.candidates[0]
    feedback = st.session_state.feedback_input

    # 🌟 新增：根据反馈生成随机反应
    if feedback == 0:
        st.session_state.reaction = random.choice(["😭😭😭", "😢 全错啦", "💦 呜呜呜", "🌧️ 难过"])
    elif feedback == 1:
        st.session_state.reaction = random.choice(["嘿嘿", "如何", "好难", "有点希望！"])
    elif feedback == 2:
        st.session_state.reaction = random.choice(["😄", "🎉", "🥰", "马上就要猜对啦！"])
    else:
        st.session_state.reaction = ""  # 猜中3个的话就不在这里提示了

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
    st.session_state.reaction = ""  # 重新开始时清空反应


# ============================================================

# 3. 游戏界面展示
if st.session_state.game_over:
    guess = st.session_state.candidates[0]
    st.balloons()  # 🌟 新增：猜对时放个气球特效！
    st.success(f"🎉 我就知道是 {guess}！美丽小高赢啦")
    st.button("重新猜猜", on_click=restart_game)

elif len(st.session_state.candidates) > 0:
    guess = st.session_state.candidates[0]

    # 🌟 新增：如果电脑有反应，就展示在一个蓝色的提示框里
    if st.session_state.reaction:
        st.info(f" {st.session_state.reaction}")

    st.markdown(f"### 我猜是： **{guess}**")

    # 接收用户反馈
    st.number_input("猜对了几位数字呀？", min_value=0, max_value=3, step=1, key="feedback_input")

    # 按钮触发：点击时直接运行上面的 process_guess 函数
    st.button("确定", on_click=process_guess)

else:
    st.error("你是不是搞错了？我已经找不到符合条件的数字啦！")
    st.button("重新猜猜", on_click=restart_game)