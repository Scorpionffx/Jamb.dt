import streamlit as st
import random

st.set_page_config(page_title="JAMB AGGREGATOR PRO", page_icon="🎓", layout="wide")

if 'coins' not in st.session_state:
    st.session_state.coins = 50
if 'premium' not in st.session_state:
    st.session_state.premium = False

# ===== SIDEBAR - MONEY =====
with st.sidebar:
    st.title("🎓 JAMB PRO")
    st.metric("Your Coins", st.session_state.coins)
    
    st.write("### 💰 Earn Coins (Watch Ad = Money for you)")
    if st.button("📺 Watch Ad +10 Coins"):
        st.session_state.coins += 10
        st.success("You earned +10 Coins! (Ad viewed - you made money)")
    
    if st.button("🎰 Spin & Win"):
        win = random.choice([5,10,20,50,100])
        st.session_state.coins += win
        st.success(f"You won {win} Coins!")
    
    st.divider()
    st.write("### 🔥 Premium - Main Income")
    st.link_button("Buy Premium ₦1,500 - Unlock All", "https://paystack.com", use_container_width=True)
    st.link_button("Remove Ads ₦700", "https://paystack.com", use_container_width=True)
    st.link_button("Buy 350 Coins ₦1,500", "https://paystack.com", use_container_width=True)
    
    if st.checkbox("I have paid - Unlock"):
        st.session_state.premium = True
        st.success("Premium Unlocked!")

# ===== MAIN APP =====
st.markdown("""
<div style='background:linear-gradient(135deg,#5B3DF6,#EC4899);padding:30px;border-radius:20px;color:white'>
<h1>Score 350+ in JAMB<br>Without Stress</h1>
<p>15 Years Past Questions + Explanations + Predicted Questions</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# SPONSORED BANNERS - YOUR ₦20k/MONTH EACH
st.write("### 🔥 Sponsored CBT Centers (₦20k/month per center - Your Income)")
c1, c2, c3 = st.columns(3)
c1.warning("📍 DE-BOAT CBT, Ikeja - 08064353000")
c2.info("🎓 Lead City Uni Nursing - 08034356220")
c3.success("💼 Your Ad Here - ₦20k/mo")

# ADS - YOU EARN WHEN USER SEES IT
if not st.session_state.premium:
    st.markdown("<div style='background:#5B3DF6;padding:12px;border-radius:10px;color:white;text-align:center'>📢 META AD - Pays when user sees it (View = $0.002) | Replace with real Meta code after approval</div>", unsafe_allow_html=True)

st.divider()

# QUIZ
st.subheader("📚 JAMB Past Questions")
subject = st.selectbox("Choose Subject", ["English (FREE)", "Mathematics (50 Coins)", "Physics (Premium ₦1,500)", "Chemistry (Premium)"])

questions = {
    "English (FREE)": {"q": "Choose synonym for 'abundant'", "o": ["Scarce", "Plentiful", "Small"], "a": "Plentiful", "exp": "Abundant = Plentiful"},
    "Mathematics (50 Coins)": {"q": "Solve 2x + 3 = 7", "o": ["1", "2", "3"], "a": "2", "exp": "2x=4, x=2"},
    "Physics (Premium ₦1,500)": {"q": "Unit of Force?", "o": ["Joule", "Newton", "Watt"], "a": "Newton", "exp": "Force unit is Newton"},
    "Chemistry (Premium)": {"q": "Symbol for Sodium?", "o": ["So", "Na", "Sd"], "a": "Na", "exp": "Na from Latin Natrium"},
}

q = questions[subject]

if "Premium" in subject and not st.session_state.premium:
    st.error("🔒 Premium Only! Buy Premium in sidebar to unlock.")
else:
    if "50 Coins" in subject and st.session_state.coins < 50 and not st.session_state.premium:
        st.error("Not enough coins! Watch ads in sidebar to earn.")
    else:
        st.write(f"**Q: {q['q']}**")
        ans = st.radio("Pick answer", q['o'])
        if st.button("Submit Answer"):
            if not st.session_state.premium:
                st.info("📢 Interstitial Ad Shown (5 sec view) - You earned $0.002")
            if ans == q['a']:
                st.success("Correct! +10 Coins")
                st.session_state.coins += 10
            else:
                st.error(f"Wrong! Answer is {q['a']}")
            
            st.write("---")
            st.write("#### 🔒 Explanation Locked - Watch Ad to Unlock (Pays Highest)")
            col1, col2 = st.columns(2)
            if col1.button("📺 Watch 20s Ad to Unlock"):
                st.success(f"✅ Explanation: {q['exp']} - You earned $0.005 (Rewarded Ad - Highest Payer)")
            if col2.button("Use 20 Coins"):
                if st.session_state.coins >= 20:
                    st.session_state.coins -= 20
                    st.success(f"✅ Explanation: {q['exp']}")
                else:
                    st.error("Not enough coins")

st.divider()

# STORE
st.subheader("🛒 E-Book Store - Sell PDFs (₦1k-₦3k each)")
s1, s2, s3 = st.columns(3)
s1.button("Physics + Chemistry 2010-2024\n₦2,000")
s2.button("English Likely Qs 2025\n₦1,000")
s3.button("Post-UTME Past Qs\n₦3,000")

st.divider()

# SPONSOR CONTRACT
st.header("💼 Sponsor Dashboard - Make ₦20k Per CBT Center")
center = st.text_input("CBT Center Name", "DE-BOAT CBT Center, Ikeja")

contract = f"""
Hello {center} 👋,

I own JAMB AGGREGATOR PRO - We have 5,000+ JAMB students in Lagos daily.

I want to put your CBT Center at the TOP of our app.

WHAT YOU GET:
✅ Banner shown to 5,000+ students daily (150k views/month)
✅ Direct call button
✅ Top position on Home Screen
✅ 1 WhatsApp broadcast per month

COST: ₦20,000/month (or ₦50k for 3 months)

We already have 2 centers in Ikeja & Yaba paying.

Can I add {center} this week? 1 slot left.

- JAMB Aggregator Team
Live App: https://YOUR_APP.streamlit.app

PAYMENT: Opay - 1234567890 - Your Name
After payment, send Center Name, Address & Phone.
"""

st.code(contract)

st.write("### 📞 10 Lagos CBT Centers With Phone Numbers")
st.table([
    ["Living Seed Info Systems", "08064353000", "Okota"],
    ["Muslim Kids & Teens College", "08034356220", "Ikotun"],
    ["Davmir Enterprises", "08089771480", "Egbeda"],
    ["Majorstride Enterprise", "08105677330", "Lagos"],
    ["Sequential Tech", "09022840544", "Abule Egba"],
    ["Bachel Model College", "08036721541", "Ogba"],
    ["Bafuto Computer", "08023624940", "Egbe"],
    ["Brainpoint College", "08060217706", "Ebute-Metta"],
    ["Audax Solutions", "08038847295", "Lekki"],
    ["AOCOED CBT", "08034546199", "Ijanikin"],
])

st.caption("Income: Meta Ads (view=money) + Premium ₦1,500 + E-books + Sponsors ₦20k/mo = ₦15k-₦30k/day")
