# CampusWatt AI: Presentation Slides Content
**1M1B AI for Sustainability Virtual Internship** (in collaboration with IBM SkillsBuild & AICTE)

---

## Slide 1: Title Slide
- **Title:** CampusWatt AI: Smart Energy Optimization & Audit Assistant
- **Subtitle:** An AI-Driven Solution for Campus HVAC and Lighting Efficiency Aligned with UN SDGs
- **Author / Candidate:** Senku Lokesh
- **Institution:** The ICFAI University, Raipur
- **Internship Program:** 1M1B AI for Sustainability Virtual Internship (in collaboration with IBM SkillsBuild & AICTE)
- **Primary SDG:** SDG 7: Affordable and Clean Energy (Target 7.3)
- **Secondary SDG:** SDG 11: Sustainable Cities and Communities (Target 11.6)

---

## Slide 2: Problem Statement & SDG Alignment

### The Real-World Problem:
- Academic campuses operate extensive facilities (lecture halls, labs, libraries, seminar halls) where air conditioning and lighting often run continuously regardless of real occupancy.
- Mismatches between fixed timetable schedules and actual room usage lead to substantial energy wastage and high utility costs.
- **Target Stakeholders:** Campus facility managers, estate offices, university administrations, and student communities.

### SDG Mapping:
- **SDG 7 (Affordable & Clean Energy - Target 7.3):** Double the global rate of improvement in energy efficiency through data-driven appliance scheduling.
- **SDG 11 (Sustainable Cities & Communities - Target 11.6):** Reduce environmental impact of educational infrastructure, converting campus buildings into low-carbon, smart learning environments.

---

## Slide 3: Proposed AI Solution

### Solution Architecture:
1. **Data Ingestion:** Captures room capacity, real-time or scheduled occupancy, lecture timetable hours, and local ambient temperature.
2. **AI Optimization Engine:** Evaluates ambient cooling load vs. occupancy density to determine optimal HVAC setpoints (e.g., dynamic 24°C–26°C regulation instead of static low cooling) and lighting zones.
3. **Automated Audit & Recommendation:** Delivers an actionable schedule for facility staff and calculates estimated kilowatt-hour (kWh) and carbon savings.

### Why AI is Needed:
- Non-linear relationships between outdoor temperature, indoor thermal mass, and occupancy make static timer switches inefficient.
- AI dynamically models optimal comfort-to-consumption trade-offs while maintaining ASHRAE thermal comfort standards.

---

## Slide 4: Prototype & Technical Workflow

### Workflow Pipeline:
- **Input Layer:** Academic schedule + weather API data + room dimensions/capacity.
- **Processing Layer:** Thermal comfort estimation and dynamic scheduling algorithm.
- **Generative / Advisory Layer:** Generates natural-language operational directives and facility anomaly alerts.

### Prototype Demonstration Example:
- **Input Scenario:**
  - Room: `LH-102 (ICFAI Campus)`
  - Capacity: `60 seats`
  - Schedule: `10:00 AM – 12:00 PM` (Occupancy: 35–45 students)
  - Outdoor Temp: `33.5°C – 34.0°C`
- **Output Action:**
  - Pre-cool at 24°C starting 10 minutes prior to session.
  - Adjust to eco-mode (25.0°C–25.5°C) during active session.
  - Daylight harvesting enabled for perimeter zones if occupancy < 50%.
  - Automatic shutoff command triggered upon session dismissal.
- **Projected Daily Savings:** 14.8 kWh/day per block (11.2 kg CO₂e avoided daily).

---

## Slide 5: Responsible AI Considerations

- **Fairness & Inclusivity:** Ensures standard thermal comfort across all campus buildings (laboratories, lecture halls, and faculty rooms) without favoring specific blocks.
- **Transparency & Explainability:** The system provides explicit reasoning for every recommendation (e.g., citing outdoor temperature surge and occupancy thresholds) rather than acting as a black box.
- **Privacy & Security:** Uses aggregate headcount data and academic schedules; no biometric identification or personal camera feeds are collected or stored.
- **Human-in-the-Loop:** Acts as a decision-support advisory system for facility managers rather than initiating unmonitored hard shutoffs.

---

## Slide 6: Expected Impact & Future Scope

### Projected Quantitative Impact:
- **15%–25% reduction** in non-peak campus electricity consumption.
- Measurable carbon footprint reduction aligned with institutional green audit standards (approx. 0.82 kg CO₂e per kWh saved).
- Significant financial reduction in monthly university utility bills.

### Future Scope:
- **IoT Smart Relay Integration:** Direct integration with Modbus/MQTT relays for automated contactless appliance switching.
- **Rooftop Solar Integration:** Balancing grid draw with on-campus renewable generation by scheduling energy-intensive activities during peak solar hours.
- **Multi-Campus Fleet Dashboard:** Centralized telemetry across multiple university buildings and branches.
