# 1M1B Submission: Links, Prototype & Video Demo Guide

This document contains everything you need to answer the question:
> **"Any links to GitHub, videos, presentations or prototypes?"**

---

## 1. Ready-to-Paste Response for the Form

Copy and paste the block below directly into the Google Form response box:

```text
Project: CampusWatt AI - Campus Energy Optimization & Audit Assistant
Candidate: Senku Lokesh (The ICFAI University, Raipur)
Internship: 1M1B AI for Sustainability (with IBM SkillsBuild & AICTE)

1. GitHub Repository:
https://github.com/SENKULOKESH123/campuswatt-ai
(Contains the full source code, Python multi-room optimization engine, and interactive simulation dashboard)

2. Live Interactive Web Prototype (GitHub Pages):
https://senkulokesh123.github.io/campuswatt-ai/
(Interactive browser dashboard with real-time occupancy sliders, dynamic HVAC regulation, and CEA-compliant carbon reduction analytics)

3. Presentation Deck (16:9 Slides):
https://docs.google.com/presentation/d/1yGEIxFiQEy_XbmPe1mDXN4ayQkBoeKz0/edit?usp=sharing
(Complete 6-slide deck covering problem context, SDG 7 & 11 alignment, architecture, prototype test cases, responsible AI governance, and future scope)

4. Prototype Explainer Video (Demo):
https://1drv.ms/v/c/4245db17183b35f4/IQB-WeXIgXNDRIDxNXh-pwOuAYnczFlB_tMI5Xt-NVsf9ic?e=nsgg3m
(Full walkthrough demonstrating the campus energy waste challenge, real-time optimization algorithm, and kilowatt-hour / carbon reduction metrics)
```

*(Note: Replace `<your-github-username>` and the bracketed Google Drive links with your actual links before clicking Submit.)*

---

## 2. 60-Second Video Demo Script (Word-for-Word)

You can record your screen using **Loom**, **Windows Game Bar** (`Win + G`), or your phone camera facing your laptop screen:

> *"Hello everyone! My name is **Senku Lokesh** from **The ICFAI University, Raipur**, participating in the **1M1B AI for Sustainability Virtual Internship in collaboration with IBM SkillsBuild and AICTE**.*
>
> *Today, educational campuses waste significant electricity because air conditioning and lighting run continuously regardless of whether a classroom has 50 students or is completely empty. This causes massive peak energy waste.*
>
> *To solve this, I built **CampusWatt AI**, an intelligent energy optimization and audit assistant aligned with **SDG 7 (Affordable & Clean Energy)** and **SDG 11 (Sustainable Cities)**.*
>
> *Here in our prototype, the system ingests timetable schedules, room capacity, actual headcount, and ambient outdoor temperature. Instead of static cooling, it dynamically regulates HVAC setpoints between 24°C and 26°C and enables daylight harvesting.*
>
> *For example, in a 60-seat lecture hall at 33.5°C, CampusWatt AI reduces consumption by over 22%, saving 3.38 kWh and avoiding 2.77 kg of CO₂ in just a single lecture session.*
>
> *CampusWatt AI turns educational institutions into smart, low-carbon campuses. Thank you!"*

---

## 3. How to Get Your GitHub & Live Prototype Link (3 Steps)

The local git repository has already been initialized and committed on your machine!

1. Go to [github.com/new](https://github.com/new) and create a new public repository named:
   **`campuswatt-ai`**
2. In your PowerShell terminal in `E:\1m1b project`, run:
   ```powershell
   git remote add origin https://github.com/<your-username>/campuswatt-ai.git
   git branch -M main
   git push -u origin main
   ```
3. To enable the **Free Live Web Prototype**:
   - Go to your repository on GitHub -> **Settings** -> **Pages**.
   - Under **Branch**, select `main` and root `/`, then click **Save**.
   - Your live interactive web app will be live at:
     `https://<your-username>.github.io/campuswatt-ai/`

---

## 4. How to Get Your Presentation & Video Links (Google Drive)

1. Open [drive.google.com](https://drive.google.com).
2. Upload:
   - `CampusWatt_AI_Presentation.pptx` (from `E:\1m1b project\`)
   - Your short demo video recording (e.g., `CampusWatt_AI_Demo.mp4`).
3. Right-click each uploaded file -> **Share** -> Change General access to:
   **"Anyone with the link can view"**.
4. Click **Copy link** and paste it into the submission form.
