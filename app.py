import streamlit as st
from pathlib import Path
from datetime import datetime
import requests
from PIL import Image
import base64
from io import BytesIO

# ---------- Page Config ----------
st.set_page_config(page_title="Shiv Kumar Dubey | Portfolio", page_icon="📊", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
<style>
:root {
    --primary: #2563EB;
    --primary-light: #3B82F6;
    --secondary: #10B981;
    --accent: #F59E0B;
    --dark: #1F2937;
    --light: #F3F4F6;
    --text: #374151;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--text);
    line-height: 1.6;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

h1, h2, h3, h4 {
    color: var(--dark);
    margin-bottom: 1rem;
    font-weight: 700;
}

h1 {
    font-size: 2.5rem;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2 {
    font-size: 1.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--light);
    margin-top: 1.5rem;
}

.stButton>button {
    border-radius: 50px;
    padding: 0.7rem 1.5rem;
    font-weight: 600;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: white;
    border: none;
    transition: all 0.3s ease;
    width: 100%;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3);
}

.card {
    border-radius: 16px;
    padding: 1.5rem;
    background: white;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
    margin-bottom: 1.5rem;
    border: 1px solid rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 50px;
    background: var(--light);
    color: var(--dark);
    margin: 4px 8px 8px 0;
    font-size: 0.85rem;
    font-weight: 500;
    border: 1px solid #E5E7EB;
}

.highlight {
    background: linear-gradient(120deg, rgba(30, 64, 175, 0.1) 0%, rgba(59, 130, 246, 0.1) 100%);
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    font-weight: 600;
}

.profile-img {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    object-fit: cover;
    border: 5px solid white;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    margin: 0 auto 1.5rem;
    display: block;
}

.sidebar {
    background: linear-gradient(180deg, var(--primary) 0%, var(--primary-light) 100%);
    color: white;
    padding: 2rem 1.5rem;
}

.sidebar-content {
    color: white;
}

.sidebar-content a {
    color: white !important;
    text-decoration: none;
}

.sidebar-content a:hover {
    text-decoration: underline;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent);
    margin: 1.5rem 0;
}

.kpi-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 1.5rem 0;
}

.kpi-item {
    flex: 1;
    min-width: 200px;
    text-align: center;
    padding: 1.5rem 1rem;
    border-radius: 16px;
    background: white;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.kpi-value {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.kpi-label {
    font-size: 0.9rem;
    color: var(--text);
    opacity: 0.8;
}

.timeline {
    border-left: 3px solid var(--primary-light);
    padding-left: 2rem;
    margin-left: 1rem;
}

.timeline-item {
    position: relative;
    margin-bottom: 2rem;
}

.timeline-item:last-child {
    margin-bottom: 0;
}

.timeline-dot {
    position: absolute;
    left: -2.5rem;
    top: 0;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: var(--primary);
    border: 4px solid white;
    box-shadow: 0 0 0 3px var(--primary-light);
}

.timeline-date {
    font-size: 0.9rem;
    color: var(--primary);
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.contact-form {
    background: white;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
}

.social-icons {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--light);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--primary);
    transition: all 0.3s ease;
}

.social-icon:hover {
    background: var(--primary);
    color: white;
    transform: translateY(-3px);
}

.project-detail {
    background: var(--light);
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
}

.model-architecture {
    background: white;
    padding: 1rem;
    border-radius: 8px;
    border-left: 4px solid var(--primary);
    margin: 1rem 0;
}

.sidebar-name {
    color: ;
    text-align: center;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.sidebar-tagline {
    color: ;
    text-align: center;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

@media (max-width: 768px) {
    .kpi-item {
        min-width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- Telegram Function ----------
def send_telegram(name, email, message):
    token = "7963378403:AAHcDOL5FdL3tsrb0VLJnD7uHx7ayxdt0V0"   # Your bot token
    chat_id = "5430235789"                                     # Your chat ID
    text = f"📩 New Portfolio Message!\n\n👤 Name: {name}\n📧 Email: {email}\n💬 Message: {message}"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        r = requests.post(url, data=payload)
        return r.status_code == 200
    except Exception as e:
        print("Telegram error:", e)
        return False

# ---------- Helper Functions ----------
def img_to_bytes(img_path):
    try:
        img = Image.open(img_path)
        with BytesIO() as buffer:
            img.save(buffer, format='PNG')
            return base64.b64encode(buffer.getvalue()).decode()
    except:
        return None

# ---------- Data ----------
PROFILE = {
    "name": "Shiv Kumar Dubey",
    "tagline": "MBA (Business Analytics) |Transforming Business Potential into Data-Driven Growth",
    "location": "Greater Noida, India",
    "email": "shivkumardubey997@gmail.com",
    "phone": "+91-9151416459",
    "linkedin": "https://www.linkedin.com/in/shiv-dubey-6a975b203/",
    "github": "https://github.com/shiv915141",
    "image_path": "shiv.jpg",
    "resume_path": "shivkumardubey_Resume.pdf",
    "about": (
        "I am a Business Growth Strategist who transforms data into actionable plans for businesses ready to scale"
        "I specialize in partnering with companies that have strong operational capabilities but lack a clear strategic blueprint for expansion "
        "My expertise lies in conducting deep business diagnostics to identify bottlenecks, then architecting and executing end-to-end growth strategies "
        "This involves building a foundational digital presence, designing targeted sales funnels, and implementing data-informed campaigns that deliver measurable ROI and sustainable growth"
        "I am committed to turning business potential into tangible market share and revenue. "
        
        
    ),
    "highlights": [
        "MBA in Business Analytics, G. L. Bajaj Institute of Technology & Management (2024–2026)",
        "B.Tech in AI & ML, Sharda University (2020–2024)",
        "QA Engineer (TeleSys): automated 30+ scripts, reduced audit time from 4–6 days to <10 minutes",
        "Research: ICMCM 2025 (Handwritten Digit Recognition), ICDAM 2024 (Aerial Vehicle Monitoring)"
    ],
    "skills_core": [
        "Requirement Analysis", "KPI Tracking", "EDA", "A/B Testing", "Forecasting",
        "Clustering / Segmentation", "Time Series", "Stakeholder Communication"
    ],
    "skills_tools": [
        "SQL", "Python", "R", "Pandas", "Power BI", "Excel (Advanced)", "Google Analytics", "Oracle DB",
        "TensorFlow", "OpenCV", "PyTorch", "Scikit-learn", "Shell Scripting"
    ],
    "skills_pm": ["Agile & Scrum", "JIRA", "MS Project", "Test Automation", "QA & UAT"],
    "experience": [
        {
            "role": "QA Engineer",
            "company": "TeleSys Software Pvt. Ltd.",
            "location": "Noida (On-site)",
            "period": "Feb 2024 – Jun 2024",
            "bullets": [
                "Executed test cases for HLR modules; improved testing efficiency by 20%.",
                "Automated 30+ test scripts; coordinated 10+ defect reports to enhance reliability.",
                "Built shell-based audit tool for HLR configs; reduced manual audit from 4–6 days to <10 minutes.",
                "Collaborated with devs & QA to validate releases; reduced post-release issues by ~30%."
            ]
        }
    ],
    "projects": [
        {
            "title": "Handwritten Digit Recognition System",
            "year": "2023",
            "stack": ["Python", "TensorFlow", "Keras", "OpenCV", "CNN", "MLP"],
            "desc": "A comprehensive deep learning approach to recognize handwritten digits using multiple neural network architectures.",
            "detail": """
            Handwritten digit recognition has numerous applications in processing bank checks, identifying license plates, 
            sorting mail, and more. This project offers a thorough comparison of various machine learning and deep learning 
            techniques for handwritten digit recognition, addressing challenges arising from different writing styles.
            
            **Key Features:**
            - Implemented and compared MLP Classifier, LeNet, LeNet-5, ResNet, and CNN architectures
            - Evaluated models at 10, 50, and 100 epochs with batch size of 128
            - Used ReLU activation functions and Softmax for evaluation
            - Focused on training loss and accuracy metrics
            
            **Methodology:**
            The research involved extensive experimentation with:
            - Various activation functions and evaluation metrics
            - Different image sizes (28×28, 32×32, and 64×64 pixels)
            - Multiple neural network architectures:
            
            **MLP Architecture:**
            - Flatten(input_shape=(28, 28, 1))
            - Dense(128, activation='relu')
            - Dense(64, activation='relu')
            - Dense(10, activation='softmax')
            
            **CNN Architecture:**
            - Dense(64, activation='relu')
            - Dense(10, activation='softmax')
            
            **LeNet Architecture:**
            - Dense(120, activation='relu')
            - Dense(84, activation='relu')
            - Dense(10, activation='softmax')
            
            **ResNet Architecture:**
            - Dense(units=256, activation='relu')
            - Dense(units=128, activation='relu')
            
            **Results:**
            The project achieved high precision rates essential for real-world applications like automated bank check 
            processing systems where misinterpreting a digit could cause serious issues.
            """
        },
        {
            "title": "Aerial Vehicle Monitoring & Alert System",
            "year": "2024",
            "stack": ["TensorFlow", "OpenCV", "CUDA", "PyTorch", "Computer Vision"],
            "desc": "Computer-vision system to detect drones/mini choppers for security applications.",
            "detail": """
            This project developed a sophisticated computer vision system designed to detect and monitor aerial vehicles 
            such as drones and mini choppers for enhanced security applications. The system provides real-time monitoring 
            and alert capabilities for sensitive areas where unauthorized aerial access could pose security risks.
            
            **Key Features:**
            - Real-time detection of aerial vehicles using advanced computer vision techniques
            - Alert system for security personnel upon detection of unauthorized aerial vehicles
            - Capability to distinguish between different types of aerial vehicles
            - Integration with existing security infrastructure for comprehensive monitoring
            
            **Technical Implementation:**
            - Utilized TensorFlow and PyTorch for deep learning model development
            - Implemented OpenCV for image processing and computer vision tasks
            - Leveraged CUDA for GPU acceleration to ensure real-time performance
            - Developed custom datasets for training and validation purposes
            
            **Methodology:**
            The system employs a multi-stage approach:
            1. Frame capture from surveillance feeds
            2. Preprocessing and enhancement of captured images
            3. Feature extraction using convolutional neural networks
            4. Classification of aerial vehicles
            5. Alert generation and logging of detected vehicles
            
            **Applications:**
            - Security monitoring for sensitive facilities (government buildings, airports, etc.)
            - Event security for large public gatherings
            - Border surveillance and monitoring
            - Critical infrastructure protection
            
            **Challenges Addressed:**
            - Variable lighting conditions affecting detection accuracy
            - Different sizes and types of aerial vehicles
            - Real-time processing requirements
            - Minimizing false positives in complex environments
            """
        },
        {
            "title": "Local Food Wastage Management System",
            "year": "2025",
            "stack": ["Streamlit", "SQLite", "Pandas", "Python"],
            "desc": "Web-based platform to combat food waste by connecting food providers with receivers.",
            "detail": """
            This project is a web-based application built with Streamlit and SQLite to combat food waste and food insecurity. 
            It provides a platform for food providers to list surplus food and for receivers to find available donations, 
            creating a digital bridge for efficient food redistribution.
            
            **Key Features:**
            - Interactive Dashboard: Provides a quick, at-a-glance overview of key metrics
            - Detailed Analysis: Comprehensive data insights into providers, claims, and distribution patterns
            - Food Listings: Browse, filter, and search through available food listings
            - Provider Actions: CRUD functionality for food providers to manage listings
            - SQL Query Runner: Advanced feature for custom data exploration
            
            **Tech Stack:**
            - Framework: Streamlit
            - Database: SQLite3
            - Data Manipulation: Pandas
            
            **Impact:**
            The system helps reduce food waste while addressing food insecurity by creating an efficient platform 
            for redistributing surplus food to those in need.
            """
        }
    ],
    "leadership": [
        {
            "title": "President — Business Analytics Club",
            "bullets": [
                "Founded and led the club; promoted applied data thinking: 'Where Data Meets Decision'.",
                "Organized various management & analytics events; built evaluation rubrics and playbooks."
            ]
        },
        {
            "title": "GDSC — Event Organizer",
            "bullets": [
                "Coordinated technical & non-technical teams to run community tech events."
            ]
        }
    ],
    "publications": [
        "Handwritten Digit Recognition using Supervised Learning — ICMCM (Jan 2025)",
        "Aerial Vehicle Monitoring & Alert System — ICDAM 2024"
    ]
}

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    # Profile image
    img_bytes = img_to_bytes(PROFILE["image_path"])
    if img_bytes:
        st.markdown(f'<img src="data:image/png;base64,{img_bytes}" class="profile-img">', unsafe_allow_html=True)
    else:
        st.info("Add your image to the same folder and set 'image_path' in the PROFILE dictionary")
    
    # Fixed the name and tagline visibility with specific CSS classes
    st.markdown(f'<div class="sidebar-name">{PROFILE["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sidebar-tagline">{PROFILE["tagline"]}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown(f'<p>📍 {PROFILE["location"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p>📧 {PROFILE["email"]}</p>', unsafe_allow_html=True)
    st.markdown(f'<p>📱 {PROFILE["phone"]}</p>', unsafe_allow_html=True)
    
    st.markdown(f'<p>🔗 <a href="{PROFILE["linkedin"]}" target="_blank">LinkedIn Profile</a></p>', unsafe_allow_html=True)
    st.markdown(f'<p>💻 <a href="{PROFILE["github"]}" target="_blank">GitHub Profile</a></p>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Resume download
    resume_file = Path(PROFILE["resume_path"])
    if resume_file.exists():
        with open(resume_file, "rb") as f:
            st.download_button("📄 Download Resume", f, file_name=resume_file.name, mime="application/pdf", use_container_width=True)
    else:
        st.info("Upload your resume to assets/ and set 'resume_path' above.")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    nav_options = ["🏠 Home", "💼 Experience", "📊 Projects", "🧩 Skills", "🧭 Leadership", "📚 Publications", "✉️ Contact"]
    nav = st.radio("Navigate", nav_options, index=0)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Home ----------
if nav == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# Hi, I'm Shiv Kumar Dubey 👋")
        st.markdown(f'### {PROFILE["tagline"]}')
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### About Me")
        st.write(PROFILE["about"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Career Highlights")
        for h in PROFILE["highlights"]:
            st.markdown(f"- {h}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 📈 Key Achievements")
    
    st.markdown("""
    <div class="kpi-container">
        <div class="kpi-item">
            <div class="kpi-value">30+</div>
            <div class="kpi-label">Scripts Automated</div>
        </div>
        <div class="kpi-item">
            <div class="kpi-value">99%</div>
            <div class="kpi-label">Time Reduction</div>
        </div>
        <div class="kpi-item">
            <div class="kpi-value">20%</div>
            <div class="kpi-label">Efficiency Gain</div>
        </div>
        <div class="kpi-item">
            <div class="kpi-value">30%</div>
            <div class="kpi-label">Issues Reduced</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Experience ----------
elif nav == "💼 Experience":
    st.markdown("# 💼 Professional Experience")
    
    for exp in PROFILE["experience"]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"#### {exp['role']}")
        st.markdown(f"**{exp['company']}** | *{exp['location']}* | *{exp['period']}*")
        
        st.markdown("<ul>", unsafe_allow_html=True)
        for b in exp["bullets"]:
            st.markdown(f"<li>{b}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Projects ----------
elif nav == "📊 Projects":
    st.markdown("# 📊 Projects")
    
    for p in PROFILE["projects"]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"#### {p['title']} ({p['year']})")
        st.markdown("**Tech Stack:** " + ", ".join([f"<span class='badge'>{s}</span>" for s in p["stack"]]), unsafe_allow_html=True)
        st.markdown(p["desc"])
        
        with st.expander("View Project Details"):
            st.markdown(f'<div class="project-detail">{p["detail"]}</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Skills ----------
elif nav == "🧩 Skills":
    st.markdown("# 🧩 Skills & Expertise")
    
    st.markdown("### 🔍 Core Business Analytics")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(" ".join([f"<span class='badge'>{s}</span>" for s in PROFILE["skills_core"]]), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 🛠️ Tools & Technologies")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(" ".join([f"<span class='badge'>{s}</span>" for s in PROFILE["skills_tools"]]), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 📋 Project & Quality Management")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(" ".join([f"<span class='badge'>{s}</span>" for s in PROFILE["skills_pm"]]), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Leadership ----------
elif nav == "🧭 Leadership":
    st.markdown("# 🧭 Leadership & Activities")
    
    for l in PROFILE["leadership"]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"#### {l['title']}")
        
        st.markdown("<ul>", unsafe_allow_html=True)
        for b in l["bullets"]:
            st.markdown(f"<li>{b}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Publications ----------
elif nav == "📚 Publications":
    st.markdown("# 📚 Publications & Research")
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    for pub in PROFILE["publications"]:
        st.markdown(f"- {pub}")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Contact ----------
elif nav == "✉️ Contact":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("# ✉️ Get In Touch")
        st.markdown("### I'd love to hear from you!")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    if send_telegram(name, email, message):
                        st.success("✅ Message sent successfully! I'll get back to you soon.")
                    else:
                        st.error("❌ Failed to send message. Please try again later.")
                else:
                    st.warning("⚠️ Please fill in all fields.")
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📞 Contact Info")
        st.markdown(f"**Email:** {PROFILE['email']}")
        st.markdown(f"**Phone:** {PROFILE['phone']}")
        st.markdown(f"**Location:** {PROFILE['location']}")
        st.markdown(f"**LinkedIn:** [Shiv Kumar Dubey]({PROFILE['linkedin']})")
        st.markdown(f"**GitHub:** [shiv915141]({PROFILE['github']})")
        
        st.markdown("### 🌐 Socials")
        st.markdown("""
        <div class="social-icons">
            <a href="#" class="social-icon">📘</a>
            <a href="#" class="social-icon">🐦</a>
            <a href="#" class="social-icon">📸</a>
            <a href="#" class="social-icon">👨‍💻</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)