"""
CampusWatt AI - Energy Optimization & Audit Prototype
Author: Senku Lokesh (The ICFAI University, Raipur)
Internship: 1M1B AI for Sustainability Virtual Internship (in collaboration with IBM SkillsBuild & AICTE)
SDG Alignments: SDG 7 (Affordable & Clean Energy) & SDG 11 (Sustainable Cities & Communities)

Demonstrates AI-driven scheduling for campus lighting and HVAC efficiency.
"""

from typing import Dict, Any, List


def campuswatt_optimizer(
    room_id: str,
    capacity: int,
    scheduled_headcount: int,
    ambient_temp_c: float,
    duration_hours: float,
) -> Dict[str, Any]:
    """
    Evaluates ambient cooling load vs. occupancy density to determine optimal HVAC
    setpoints, lighting policies, and estimated energy/CO2 savings.
    """
    # Determine occupancy ratio
    occupancy_ratio = scheduled_headcount / max(capacity, 1)

    # Baseline power: Assume 1.5 kW per AC unit (1 unit per 20 capacity), 0.5 kW lighting
    ac_units = max(1, capacity // 20)
    baseline_kwh = (ac_units * 1.5 + 0.5) * duration_hours

    # Optimization Logic
    if scheduled_headcount == 0:
        recommended_state = "IDLE / SHUTOFF"
        recommended_temp = "N/A (Off)"
        lighting = "Off (Complete Shutoff)"
        optimized_kwh = 0.0
        recommendation_reason = (
            "Room has zero scheduled occupancy. Completely shut off HVAC and lighting."
        )
    else:
        # Dynamic HVAC setpoint based on thermal load and ambient temperature
        if ambient_temp_c >= 35:
            recommended_temp = "24.0°C"
            energy_factor = 0.85
            temp_reason = "High ambient heat load requires active cooling set to 24°C."
        elif ambient_temp_c >= 30:
            recommended_temp = "25.0°C"
            energy_factor = 0.75
            temp_reason = "Moderate ambient heat load allows comfort setting at 25°C."
        else:
            recommended_temp = "26.0°C (Eco Mode)"
            energy_factor = 0.65
            temp_reason = "Mild ambient conditions allow energy-saving Eco Mode at 26°C."

        # Lighting policy based on occupancy ratio (daylight harvesting)
        if occupancy_ratio < 0.5:
            lighting = "50% Natural Light Daylight Harvested"
            lighting_factor = 0.6
            light_reason = "Low occupancy density enables partial daylight harvesting zones."
        else:
            lighting = "Full On"
            lighting_factor = 1.0
            light_reason = "High occupancy density requires standard illumination across all rows."

        optimized_kwh = (
            (ac_units * 1.5 * energy_factor) + (0.5 * lighting_factor)
        ) * duration_hours
        recommended_state = "ACTIVE OPTIMIZED"
        recommendation_reason = f"{temp_reason} {light_reason}"

    saved_kwh = max(0.0, baseline_kwh - optimized_kwh)
    # Standard CEA grid emission factor (approx. 0.82 kg CO2e / kWh in India)
    co2_reduction_kg = saved_kwh * 0.82

    return {
        "room_id": room_id,
        "capacity": capacity,
        "scheduled_headcount": scheduled_headcount,
        "occupancy_rate": f"{round(occupancy_ratio * 100, 1)}%",
        "ambient_temp_c": f"{ambient_temp_c}°C",
        "duration_hours": duration_hours,
        "status": recommended_state,
        "recommended_hvac_temp": recommended_temp,
        "lighting_policy": lighting,
        "baseline_kwh": round(baseline_kwh, 2),
        "optimized_kwh": round(optimized_kwh, 2),
        "energy_saved_kwh": round(saved_kwh, 2),
        "co2_reduced_kg": round(co2_reduction_kg, 2),
        "advisory_notes": recommendation_reason,
    }


def print_audit_report(result: Dict[str, Any]) -> None:
    """Prints a cleanly formatted audit summary card."""
    print("=" * 60)
    print(f" CAMPUSWATT AI AUDIT REPORT : {result['room_id']}")
    print("=" * 60)
    for key, val in result.items():
        if key == "room_id":
            continue
        label = key.replace("_", " ").title()
        print(f"  • {label:<24}: {val}")
    print("=" * 60)
    print()


def run_multi_room_audit(scenarios: List[Dict[str, Any]]) -> None:
    """Executes audit across multiple rooms and compiles total impact."""
    total_baseline = 0.0
    total_optimized = 0.0
    total_saved = 0.0
    total_co2 = 0.0

    print("\n" + "#" * 60)
    print(" RUNNING CAMPUS-WIDE ENERGY OPTIMIZATION AUDIT")
    print("#" * 60 + "\n")

    for scenario in scenarios:
        res = campuswatt_optimizer(**scenario)
        print_audit_report(res)
        total_baseline += res["baseline_kwh"]
        total_optimized += res["optimized_kwh"]
        total_saved += res["energy_saved_kwh"]
        total_co2 += res["co2_reduced_kg"]

    print("=" * 60)
    print(" CAMPUS TOTALS & SDG IMPACT SUMMARY")
    print("=" * 60)
    print(f"  Total Baseline Consumption   : {total_baseline:.2f} kWh")
    print(f"  Total Optimized Consumption  : {total_optimized:.2f} kWh")
    print(f"  Total Energy Saved           : {total_saved:.2f} kWh ({round((total_saved / max(total_baseline, 1)) * 100, 1)}% reduction)")
    print(f"  Total CO2 Emissions Reduced  : {total_co2:.2f} kg CO2e")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Test Scenarios across typical campus facilities
    sample_scenarios = [
        {
            "room_id": "LH-102 (Lecture Hall, ICFAI Campus)",
            "capacity": 60,
            "scheduled_headcount": 35,
            "ambient_temp_c": 33.5,
            "duration_hours": 3.0,
        },
        {
            "room_id": "CS-LAB-01 (Computer Laboratory)",
            "capacity": 40,
            "scheduled_headcount": 38,
            "ambient_temp_c": 36.0,
            "duration_hours": 2.0,
        },
        {
            "room_id": "SEM-HALL-B (Seminar Hall - Vacant Period)",
            "capacity": 100,
            "scheduled_headcount": 0,
            "ambient_temp_c": 34.0,
            "duration_hours": 1.5,
        },
        {
            "room_id": "LIB-READING-02 (Library Study Area)",
            "capacity": 80,
            "scheduled_headcount": 22,
            "ambient_temp_c": 29.5,
            "duration_hours": 4.0,
        },
    ]

    run_multi_room_audit(sample_scenarios)
