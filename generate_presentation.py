"""
Script to generate a professional PowerPoint presentation for CampusWatt AI.
Configured with 16:9 widescreen, clean cards, modern typography, and sustainability theme.
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Theme Colors
DARK_GREEN = RGBColor(18, 64, 46)     # #12402E
PRIMARY_GREEN = RGBColor(27, 107, 74) # #1B6B4A
ACCENT_MINT = RGBColor(72, 187, 120)  # #48BB78
CARD_BG = RGBColor(245, 250, 247)     # #F5FAF7
CARD_BORDER = RGBColor(210, 235, 222) # #D2EBDE
TEXT_DARK = RGBColor(33, 37, 41)      # #212529
TEXT_MUTED = RGBColor(108, 117, 125)  # #6C757D
WHITE = RGBColor(255, 255, 255)
GOLD = RGBColor(217, 119, 6)          # #D97706


def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------
    # Helper: Add Header
    # -------------------------------------------------------------
    def add_header(slide, title_text, category_tag="1M1B & IBM SKILLSBUILD"):
        # Category Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8), Inches(0.4))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_tag.upper()
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = PRIMARY_GREEN

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = DARK_GREEN

    # -------------------------------------------------------------
    # Helper: Add Card Box
    # -------------------------------------------------------------
    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        return shape

    # =============================================================
    # SLIDE 1: TITLE SLIDE
    # =============================================================
    s1 = prs.slides.add_slide(blank_layout)

    # Full Background Banner on left
    banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    banner.fill.solid()
    banner.fill.fore_color.rgb = DARK_GREEN
    banner.line.fill.background()

    # Inner Card
    inner_card = add_card(s1, Inches(0.9), Inches(0.8), Inches(11.533), Inches(5.9), WHITE, CARD_BORDER)

    # Content
    tb1 = s1.shapes.add_textbox(Inches(1.4), Inches(1.2), Inches(10.5), Inches(5.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "1M1B AI FOR SUSTAINABILITY VIRTUAL INTERNSHIP"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = PRIMARY_GREEN
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "CampusWatt AI: Smart Energy Optimization & Audit Assistant"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = DARK_GREEN
    p1.space_after = Pt(12)

    p2 = tf1.add_paragraph()
    p2.text = "An AI-Driven Solution for Campus HVAC and Lighting Efficiency Aligned with UN SDGs"
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(28)

    # Details Section
    p3 = tf1.add_paragraph()
    p3.text = "Project Identity & Author Information:"
    p3.font.size = Pt(14)
    p3.font.bold = True
    p3.font.color.rgb = DARK_GREEN
    p3.space_after = Pt(8)

    details = [
        ("Candidate Name", "Senku Lokesh"),
        ("Institution", "The ICFAI University, Raipur"),
        ("Program Partner", "In collaboration with IBM SkillsBuild & AICTE"),
        ("Target SDGs", "SDG 7 (Affordable & Clean Energy) | SDG 11 (Sustainable Cities & Communities)"),
    ]
    for label, val in details:
        pd = tf1.add_paragraph()
        pd.text = f"•  {label}: {val}"
        pd.font.size = Pt(13)
        pd.font.color.rgb = TEXT_DARK
        pd.space_after = Pt(4)

    # =============================================================
    # SLIDE 2: PROBLEM STATEMENT & SDG ALIGNMENT
    # =============================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Problem Statement & SDG Alignment", "Slide 2 | Context & Purpose")

    # Left Column: The Problem & Stakeholders
    add_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
    tb2_left = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
    tf2_l = tb2_left.text_frame
    tf2_l.word_wrap = True

    p = tf2_l.paragraphs[0]
    p.text = "THE REAL-WORLD CHALLENGE"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(10)

    p = tf2_l.add_paragraph()
    p.text = "• Campus Energy Waste: Academic campuses operate extensive facilities (lecture halls, labs, libraries) where air conditioning and lighting frequently run continuously regardless of actual room occupancy."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(10)

    p = tf2_l.add_paragraph()
    p.text = "• Timetable vs. Reality Mismatch: Static class schedules do not reflect cancellations, early dismissals, or low student density, causing massive idle energy waste and high utility bills."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(14)

    p = tf2_l.add_paragraph()
    p.text = "TARGET STAKEHOLDERS"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(8)

    p = tf2_l.add_paragraph()
    p.text = "Campus facility managers, university estate officers, administrative heads, and student environmental societies."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK

    # Right Column: SDG Alignment
    add_card(s2, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
    tb2_right = s2.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf2_r = tb2_right.text_frame
    tf2_r.word_wrap = True

    p = tf2_r.paragraphs[0]
    p.text = "UNITED NATIONS SDG MAPPING"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(12)

    # SDG 7 Card Box
    p = tf2_r.add_paragraph()
    p.text = "SDG 7: Affordable and Clean Energy"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.space_after = Pt(4)

    p = tf2_r.add_paragraph()
    p.text = "• Target 7.3: Double the global rate of improvement in energy efficiency.\n• Role: Eliminates unnecessary grid draw via intelligent cooling algorithms and dynamic daylight harvesting."
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(16)

    # SDG 11 Card Box
    p = tf2_r.add_paragraph()
    p.text = "SDG 11: Sustainable Cities & Communities"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(4)

    p = tf2_r.add_paragraph()
    p.text = "• Target 11.6: Reduce environmental impact of educational and public infrastructure.\n• Role: Converts high-emission campus buildings into smart, decarbonized, eco-conscious learning facilities."
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_DARK

    # =============================================================
    # SLIDE 3: PROPOSED AI SOLUTION
    # =============================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Proposed AI Solution & Architecture", "Slide 3 | Solution Design")

    # 3 Pillars
    pillars = [
        ("1. Data Ingestion Layer", "Ingests lecture timetable schedules, room capacity, actual/expected headcounts, and live ambient weather temperature.", Inches(0.8)),
        ("2. AI Optimization Engine", "Evaluates ambient heat load vs. occupancy density to determine optimal HVAC setpoints (24°C–26°C dynamic regulation) and lighting zones.", Inches(4.8)),
        ("3. Automated Audit & Advisory", "Delivers actionable operational directives to facility teams and calculates projected kilowatt-hour (kWh) and CO2 reductions.", Inches(8.8)),
    ]

    for title, desc, left in pillars:
        add_card(s3, left, Inches(1.6), Inches(3.7), Inches(3.2))
        tb = s3.shapes.add_textbox(left + Inches(0.2), Inches(1.8), Inches(3.3), Inches(2.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_GREEN
        p.space_after = Pt(10)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK

    # Bottom Banner: Why AI is Needed
    add_card(s3, Inches(0.8), Inches(5.1), Inches(11.7), Inches(1.8))
    tb_why = s3.shapes.add_textbox(Inches(1.1), Inches(5.25), Inches(11.1), Inches(1.5))
    tf_why = tb_why.text_frame
    tf_why.word_wrap = True
    p = tf_why.paragraphs[0]
    p.text = "WHY TRADITIONAL TIMERS FAIL & WHY AI IS ESSENTIAL:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DARK_GREEN
    p.space_after = Pt(6)

    p = tf_why.add_paragraph()
    p.text = "Non-linear relationships between outdoor temperature, indoor thermal mass, occupancy density, and daylight availability make static timer switches inefficient. CampusWatt AI continuously recalculates the optimal comfort-to-consumption frontier, ensuring zero waste while maintaining ASHRAE-compliant student comfort."
    p.font.size = Pt(12.5)
    p.font.color.rgb = TEXT_DARK

    # =============================================================
    # SLIDE 4: PROTOTYPE & TECHNICAL WORKFLOW
    # =============================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Prototype & Technical Workflow", "Slide 4 | Implementation")

    # Pipeline Card
    add_card(s4, Inches(0.8), Inches(1.6), Inches(4.5), Inches(5.3))
    tb4_l = s4.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(4.1), Inches(4.9))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True

    p = tf4_l.paragraphs[0]
    p.text = "WORKFLOW PIPELINE"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(10)

    stages = [
        ("Input Layer", "Timetable data, outdoor weather API, classroom dimensions & capacity."),
        ("Processing Layer", "Thermal comfort estimation, HVAC setpoint logic, daylight harvesting rules."),
        ("Advisory Layer", "Natural-language operational schedule and anomaly alerts for facility staff."),
    ]
    for st, sdesc in stages:
        p = tf4_l.add_paragraph()
        p.text = f"• {st}:"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = DARK_GREEN
        p = tf4_l.add_paragraph()
        p.text = sdesc
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(8)

    # Demonstration Scenario Card
    add_card(s4, Inches(5.6), Inches(1.6), Inches(6.9), Inches(5.3))
    tb4_r = s4.shapes.add_textbox(Inches(5.8), Inches(1.8), Inches(6.5), Inches(4.9))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True

    p = tf4_r.paragraphs[0]
    p.text = "PROTOTYPE DEMONSTRATION & AUDIT TEST"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(10)

    p = tf4_r.add_paragraph()
    p.text = "Sample Input Test Case:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = DARK_GREEN
    p = tf4_r.add_paragraph()
    p.text = "Room: LH-102 (ICFAI) | Capacity: 60 | Scheduled Headcount: 35 | Ambient Temp: 33.5°C | Duration: 3 Hours"
    p.font.size = Pt(12)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(10)

    p = tf4_r.add_paragraph()
    p.text = "System Audit Output:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    outputs = [
        ("Operational Status", "ACTIVE OPTIMIZED"),
        ("HVAC Setpoint", "Adjusted to 25.0°C (Dynamic comfort mode)"),
        ("Lighting Policy", "Full On (Sufficient density across rows)"),
        ("Baseline Consumption", "15.00 kWh"),
        ("Optimized Consumption", "11.62 kWh"),
        ("Single-Session Savings", "3.38 kWh (22.5% Reduction) | 2.77 kg CO2e Avoided"),
        ("Campus Daily Savings", "~14.8 kWh/day per block (11.2 kg CO2e/day)"),
    ]
    for lbl, val in outputs:
        p = tf4_r.add_paragraph()
        p.text = f"• {lbl}: {val}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(2)

    # =============================================================
    # SLIDE 5: RESPONSIBLE AI CONSIDERATIONS
    # =============================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Responsible & Ethical AI Principles", "Slide 5 | Ethics & Governance")

    principles = [
        ("Fairness & Inclusivity",
         "Ensures uniform thermal comfort across all campus facilities (labs, general lecture halls, faculty blocks) without preferential treatment or biased cooling distribution.",
         Inches(0.8), Inches(1.6)),
        ("Transparency & Explainability",
         "Rather than operating as an inscrutable black box, the system provides explicit human-readable rationale (e.g., ambient heat surge, occupancy ratios) for every advisory.",
         Inches(6.8), Inches(1.6)),
        ("Privacy & Data Protection",
         "Relies strictly on aggregate headcount figures and academic timetables. Strictly zero biometric scanning, facial recognition, or video surveillance data is stored or collected.",
         Inches(0.8), Inches(4.3)),
        ("Human-in-the-Loop Governance",
         "Acts as a decision-support advisory system for facility engineers. Critical override controls remain with human operators to prevent accidental shutoffs during events.",
         Inches(6.8), Inches(4.3)),
    ]

    for title, desc, left, top in principles:
        add_card(s5, left, top, Inches(5.7), Inches(2.5))
        tb = s5.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(5.3), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_GREEN
        p.space_after = Pt(8)

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(12.5)
        p.font.color.rgb = TEXT_DARK

    # =============================================================
    # SLIDE 6: EXPECTED IMPACT & FUTURE SCOPE
    # =============================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Expected Impact & Future Roadmap", "Slide 6 | Vision & Scaling")

    # Left Card: Expected Impact
    add_card(s6, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.3))
    tb6_l = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.9))
    tf6_l = tb6_l.text_frame
    tf6_l.word_wrap = True

    p = tf6_l.paragraphs[0]
    p.text = "PROJECTED QUANTITATIVE IMPACT"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(10)

    p = tf6_l.add_paragraph()
    p.text = "• 15%–25% Reduction in Campus Electricity Usage:\nSignificant trimming of non-peak and idle power consumption in educational blocks."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(12)

    p = tf6_l.add_paragraph()
    p.text = "• Measurable Carbon Abatement:\nDirect reduction in institutional greenhouse gas emissions (approx. 0.82 kg CO2e per kWh saved), supporting university NAAC/NIRF green audit metrics."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(12)

    p = tf6_l.add_paragraph()
    p.text = "• Operational Cost Savings:\nDirect reduction in monthly commercial electricity utility bills for the university administration."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK

    # Right Card: Future Scope
    add_card(s6, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
    tb6_r = s6.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.9))
    tf6_r = tb6_r.text_frame
    tf6_r.word_wrap = True

    p = tf6_r.paragraphs[0]
    p.text = "FUTURE DEVELOPMENT ROADMAP"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_GREEN
    p.space_after = Pt(10)

    p = tf6_r.add_paragraph()
    p.text = "• IoT Smart Relay Integration:\nTransition from manual advisory notifications to automated Modbus/MQTT hardware relay actuation for contactless switching."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(12)

    p = tf6_r.add_paragraph()
    p.text = "• Campus Solar Balancing:\nSync AI scheduling with rooftop solar PV generation profiles to prioritize heavy loads during maximum renewable solar output."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK
    p.space_after = Pt(12)

    p = tf6_r.add_paragraph()
    p.text = "• Multi-Campus Expansion:\nCentralized multi-tenant dashboard monitoring energy telemetry across multiple institutional campuses."
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_DARK

    output_path = "e:/1m1b project/CampusWatt_AI_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")


if __name__ == "__main__":
    create_deck()
