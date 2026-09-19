# CampusWatt AI: Campus Energy Optimization & Audit Assistant

[![SDG 7](https://img.shields.io/badge/SDG%207-Affordable%20and%20Clean%20Energy-gold)](https://sdgs.un.org/goals/goal7)
[![SDG 11](https://img.shields.io/badge/SDG%2011-Sustainable%20Cities%20and%20Communities-orange)](https://sdgs.un.org/goals/goal11)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

**CampusWatt AI** is an AI-driven energy optimization and audit assistant designed for university and college campuses. It bridges the gap between academic timetables, room occupancy, and ambient weather conditions to minimize idle HVAC and lighting consumption, slashing institutional carbon emissions.

---

## 1. Project Information
- **Project Title:** CampusWatt AI: Campus Energy Optimization & Audit Assistant
- **Candidate Name:** Senku Lokesh
- **Institution:** The ICFAI University, Raipur
- **Internship Program:** 1M1B AI for Sustainability Virtual Internship (in collaboration with IBM SkillsBuild & AICTE)
- **Primary SDG:** SDG 7 (Affordable & Clean Energy) — *Target 7.3: Double the global rate of improvement in energy efficiency*
- **Secondary SDG:** SDG 11 (Sustainable Cities & Communities) — *Target 11.6: Reduce environmental impact of public/educational infrastructure*

---

## 2. Problem Statement
Academic campuses operate extensive facilities (lecture halls, labs, libraries, seminar halls) where air conditioning and lighting often run continuously regardless of real occupancy. Mismatches between fixed timetable schedules and actual room usage lead to substantial energy wastage and high utility costs.

---

## 3. Project Structure
```text
1m1b project/
├── CampusWatt_AI_Presentation.pptx  # Ready-to-present PowerPoint slide deck (16:9 widescreen)
├── generate_presentation.py         # Python script that builds the PowerPoint presentation
├── campuswatt_optimizer.py          # Working Python prototype and multi-room simulation
├── presentation_slides.md           # Slide deck content ready to copy-paste into Google Slides
├── submission_form_answers.md       # Exact answers for the 1M1B Google Submission Form
└── README.md                        # Documentation & setup guide
```

---

## 4. How to Run the Prototype

### Prerequisites
- Python 3.10 or higher installed.

### Run Multi-Room Campus Audit Demo
```bash
python campuswatt_optimizer.py
```

### Sample Audit Output
```text
============================================================
 CAMPUSWATT AI AUDIT REPORT : LH-102 (Lecture Hall, ICFAI Campus)
============================================================
  - Capacity                : 60
  - Scheduled Headcount     : 35
  - Occupancy Rate          : 58.3%
  - Ambient Temp C          : 33.5°C
  - Duration Hours          : 3.0
  - Status                  : ACTIVE OPTIMIZED
  - Recommended Hvac Temp   : 25.0°C
  - Lighting Policy         : Full On
  - Baseline Kwh            : 15.0 kWh
  - Optimized Kwh           : 11.62 kWh
  - Energy Saved Kwh        : 3.38 kWh
  - Co2 Reduced Kg          : 2.77 kg CO2e
  - Advisory Notes          : Moderate ambient heat load allows comfort setting at 25°C. High occupancy density requires standard illumination across all rows.
============================================================
```

---

## 5. How to Regenerate or Customize Slides
If you want to regenerate or customize the PowerPoint file:
```bash
python -m pip install python-pptx
python generate_presentation.py
```
This produces `CampusWatt_AI_Presentation.pptx` in widescreen (16:9) with sustainability theme styling.

---

## 6. Submission Resources
- **Google Form Answers:** Check [`submission_form_answers.md`](./submission_form_answers.md) for direct copy-paste responses.
- **Slide Text:** Check [`presentation_slides.md`](./presentation_slides.md) for text corresponding to Slides 1–6.
- **Ready Presentation:** Open [`CampusWatt_AI_Presentation.pptx`](./CampusWatt_AI_Presentation.pptx) directly in PowerPoint, Google Slides, or LibreOffice.
