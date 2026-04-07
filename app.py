import streamlit as st
import time

st.set_page_config(page_title="ParametiQ: Powered by ADI", page_icon="🛡️", layout="centered")

st.title("🛡️ ParametiQ: Smart Income Protection")
st.write("Powered by the **AI Disruption Index (ADI)** to protect gig workers from severe environmental and API-driven disruptions.")

tab1, tab2 = st.tabs(["Worker Portal", "Oracle Trigger Simulator"])

with tab1:
    st.header("Worker Portal")
    st.write("Onboard and manage your parametric insurance policy.")
    worker_name = st.text_input("Name", placeholder="e.g. Rahul Kumar")
    worker_zone = st.selectbox("Operating Zone", ["Delhi NCR", "Mumbai", "Bangalore", "Chennai"])
    
    premium = 15
    if worker_zone == "Delhi NCR":
        premium = 25 # Higher rate due to AQI risk
        st.info("Note: Premium is slightly higher in Delhi NCR due to elevated AQI risks.")
    
    st.markdown(f"**Weekly Premium:** ₹{premium}")
    st.markdown("**Coverage:** Instant ₹500 compensation triggered automatically when the **AI Disruption Index (ADI) exceeds 60/100**.")
    
    if st.button("Pay Premium & Activate Cover"):
        if worker_name:
            with st.spinner("Activating policy..."):
                time.sleep(1)
            st.success(f"Policy activated for {worker_name} in {worker_zone}. You are now covered!")
        else:
            st.error("Please enter your name.")

with tab2:
    st.header("Oracle Trigger Simulator")
    st.write("Simulate environmental conditions to trigger automated claims evaluation.")
    
    aqi_level = st.slider("Air Quality Index (AQI)", min_value=0, max_value=500, value=150)
    rainfall_mm = st.slider("Rainfall (mm in last 24h)", min_value=0, max_value=200, value=10)
    temp_celsius = st.slider("Temperature (°C)", min_value=20, max_value=55, value=30)
    
    if st.button("Trigger System Evaluation"):
        st.write("---")
        st.subheader("Automated Claims Engine")
        
        # ADI Calculation logic based on Phase 1 design
        adi_score = 0
        
        if aqi_level > 300: adi_score += 40
        elif aqi_level > 200: adi_score += 20
            
        if rainfall_mm > 60: adi_score += 40
        elif rainfall_mm > 30: adi_score += 20
            
        if temp_celsius >= 45: adi_score += 30
        elif temp_celsius >= 40: adi_score += 15
        
        # Simulate Traffic & Demand drops from Phase 1 Architecture
        simulated_traffic_risk = 15
        adi_score += simulated_traffic_risk
        
        # Cap at 100
        adi_score = min(adi_score, 100)
        
        st.metric(label="Calculated AI Disruption Index (ADI)", value=f"{adi_score} / 100", delta="Severe Disruption" if adi_score >= 60 else "Normal")
        
        is_triggered = adi_score >= 60
        
        # UI for process
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.write("Oracle Node: Fetching data from CPCB and IMD APIs...")
        time.sleep(1)
        progress_bar.progress(25)
        
        status_text.write(f"Evaluating Risk - AQI: {aqi_level}, Rainfall: {rainfall_mm}mm, Temp: {temp_celsius}°C...")
        time.sleep(1)
        progress_bar.progress(50)
        
        if is_triggered:
            status_text.write("Trigger condition met! Cross-checking worker eligibility and GPS limits...")
            time.sleep(1.5)
            progress_bar.progress(75)
            
            status_text.write("Eligibility Verified. Issuing smart contract payout...")
            time.sleep(1)
            progress_bar.progress(100)
            
            reasons = []
            if aqi_level > 300: reasons.append("Severe Pollution (AQI > 300)")
            if rainfall_mm > 60: reasons.append("Extreme Rainfall (>60mm)")
            if temp_celsius >= 45: reasons.append("Extreme Heat (>= 45°C)")
            trigger_reason = " & ".join(reasons)
                
            st.success(f"✅ Immediate UPI Payment of ₹500 initiated! Reason: {trigger_reason}.")
            st.balloons()
        else:
            status_text.write("Conditions normal. Policy active, no payout triggered.")
            progress_bar.progress(100)
            st.info("ADI Score is below 60. Conditions are stable; no payout triggered.")
