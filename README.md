# 🛰️ Algal Bloom & Fish Hypoxia Early Warning System
### Satellite-Powered Monitoring & Early Intervention Framework for Karnataka Village Fish Tanks

---

## 📌 Problem Statement

Village fish tanks across Karnataka experience recurring mass fish deaths caused by severe algal blooms. 

* **The Mechanism:** High-nutrient influx from agricultural runoff and domestic wastewater triggers rapid micro-algal growth in shallow inland tanks. Over a **7 to 14-day window**, the bloom multiplies exponentially, exhausts available nutrients, and dies. Aerobic bacteria rapidly decompose the biomass, consuming dissolved oxygen in the water column. Once Dissolved Oxygen (DO) plummets below **4.0 mg/L**, fish cannot survive and mass asphyxiation occurs.
* **The Monitoring Gap:** No water quality monitoring currently exists at the Gram Panchayat village tank level. The first notification a farmer or cooperative society receives is floating dead fish — at which stage the economic loss is total and irreversible.
* **Scale & Impact:**
  * A 6-state Central Pollution Control Board (CPCB) survey of 215 water bodies found none with safe dissolved oxygen levels for fish. Karnataka and Telangana were identified as the worst-affected states (DO in the 0–4 mg/L range).
  * Bengaluru recorded 16 mass fish-kill events in 2023 alone.
  * Karnataka has **3,407 Gram Panchayat tanks** stocked with fish annually; zero possess continuous water quality monitoring.
  * A single fish-kill event in a typical 10-hectare tank causes a catastrophic direct loss of **₹1.5 to ₹3 Lakh** for the local cooperative society.

---

## 💡 Solution Overview

An end-to-end remote sensing and early warning framework utilizing freely accessible **Sentinel-2 MSI satellite imagery** to detect bloom formation during **Days 1 to 4** of growth. By identifying spectral signatures 7 to 10 days before oxygen depletion occurs, automated alerts and Standard Operating Procedure (SOP) advisories are dispatched to fish farmers and Panchayat officers in **Kannada and English**, enabling preventative aeration and chemical buffering before fish mortality occurs.

```
+---------------------------------------------------------------------------------------+
|                                3-TIER SYSTEM ARCHITECTURE                              |
+---------------------------------------------------------------------------------------+
|                                                                                       |
|  [TIER 1: SATELLITE & SENSING]                                                        |
|   • Copernicus Sentinel-2 MSI Multi-Spectral Imagery (Level-2A BOA)                   |
|   • Spectral Bands: Band 4 (Red 665nm), Band 5 (Red Edge 705nm), Band 8 (NIR 842nm)   |
|   • 5-Day Revisit Cadence over Karnataka (Free & Open Access)                         |
|                                     │                                                 |
|                                     ▼                                                 |
|  [TIER 2: ANALYTICAL & RISK SCORING]                                                  |
|   • SCL Band Cloud & Water Masking                                                    |
|   • NDCI (Normalized Difference Chlorophyll Index) Computation                        |
|   • 14-Day Growth Velocity & Dissolved Oxygen Crash Prediction Model                  |
|                                     │                                                 |
|                                     ▼                                                 |
|  [TIER 3: DISSEMINATION & ACTION]                                                     |
|   • Automated Kannada & English SMS / WhatsApp Alerts                                 |
|   • Gram Panchayat & Taluk Fisheries Officer GIS Dashboard                            |
|   • Mitigation SOP (Night Aeration Hours, Quicklime Dosage, Inflow Diversion)         |
|                                                                                       |
+---------------------------------------------------------------------------------------+
```

---

## ⏱️ 14-Day Detection & Intervention Lifecycle

| Stage | Timeline | Satellite Signature | Dissolved Oxygen | System Status | Field Action Protocol |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline** | Day 0 | $	ext{NDCI} < 0.15$ | $7.5 - 8.5	ext{ mg/L}$ | 🟢 **NORMAL** | Routine automated 5-day satellite monitoring. |
| **Nutrient Influx** | Day 1 – 3 | $	ext{NDCI: } 0.18 - 0.25$ | $7.5	ext{ mg/L}$ | 🟡 **WATCH** | Flagged on Gram Panchayat watch list; verify water clarity. |
| **Rapid Bloom** | **Day 4 – 6** | **$	ext{NDCI: } 0.26 - 0.38$** | **$6.5 - 7.5	ext{ mg/L}$** | 🟠 **HIGH ALERT** | **CRUCIAL INTERVENTION WINDOW**: Automated SMS/WhatsApp alert dispatched to cooperative. Block incoming runoff. |
| **Bloom Peak & Die-off** | Day 7 – 10 | $	ext{NDCI: } 0.40 - 0.55$ | $4.2 - 5.5	ext{ mg/L}$ | 🔴 **CRITICAL** | Emergency night aeration (02:00 AM – 07:00 AM); apply 150 kg/ha quicklime. |
| **Hypoxia Collapse** | Day 11 – 14 | $	ext{NDCI drops}$ | **$< 4.0	ext{ mg/L}$ (Lethal)** | ☠️ **MASS KILL** | *Prevented if early intervention taken during Days 4–7.* |

---

## 📁 Repository Directory Structure

This repository contains pure structural specifications, data dictionaries, API blueprints, and UI/alert wireframes:

```text
algal-bloom-early-warning/
├── README.md                                   # Comprehensive project overview & blueprints
│
├── architecture/
│   ├── 01_system_overview.txt                  # Full 3-tier architectural breakdown
│   └── 02_dataflow_lifecycle.txt               # End-to-end 14-day lifecycle from orbit to farmer
│
├── pipeline_spec/
│   ├── 01_satellite_ingestion_structure.txt    # Sentinel-2 MSI band selection & cloud filtering
│   ├── 02_algal_bloom_detection_logic.txt      # NDCI, NDVI, and NDTI formula specifications
│   └── 03_dissolved_oxygen_prediction_model.txt# Multi-factor DO crash & hypoxia prediction rules
│
├── data_dictionary/
│   ├── 01_tank_registry_structure.txt          # Entity attributes for 3,407 Karnataka GP tanks
│   └── 02_14day_bloom_telemetry_schema.txt     # Observation records & spectral parameter schemas
│
├── api_spec/
│   └── 01_rest_endpoints_structure.txt         # REST API route tree for tanks, telemetry & alerts
│
└── wireframes/
    ├── 01_dashboard_layout_wireframe.txt       # ASCII layout for Panchayat & Fisheries GIS dashboard
    ├── 02_alert_and_advisory_templates.txt     # Bilingual Kannada & English SMS/WhatsApp templates
    └── 03_escalation_protocol_matrix.txt       # Green / Yellow / Orange / Red escalation matrix
```

---

## 📱 Alert & Notification Wireframes

### Kannada SMS / WhatsApp Notification (Local Gram Panchayat Dialect)
```text
⚠️ ಎಚ್ಚರಿಕೆ: ಹೊಸಹಳ್ಳಿ ಗ್ರಾಮ ಪಂಚಾಯತಿ ಕೆರೆ (ಮದ್ದೂರು ತಾಲ್ಲೂಕು, ಮಂಡ್ಯ)
ಉಪಗ್ರಹ ಪರಿಶೀಲನೆಯ ಪ್ರಕಾರ ನಿಮ್ಮ ಕೆರೆಯಲ್ಲಿ ಪಾಚಿ (Algal Bloom) ಅಪಾಯಕಾರಿ ಮಟ್ಟಕ್ಕೆ ಬೆಳೆಯುತ್ತಿದೆ.
ಮುಂದಿನ 48 ರಿಂದ 72 ಗಂಟೆಗಳಲ್ಲಿ ನೀರಿನಲ್ಲಿ ಕರಗಿದ ಆಮ್ಲಜನಕ 3.2 mg/L ಗೆ ಕುಸಿಯುವ ಸಾಧ್ಯತೆಯಿದೆ
(4.0 mg/L ಗಿಂತ ಕಡಿಮೆ ಆದಲ್ಲಿ ಮೀನುಗಳು ಉಸಿರುಗಟ್ಟಿ ಸಾಯುತ್ತವೆ).

ತುರ್ತು ರಕ್ಷಣಾ ಕ್ರಮಗಳು:
1. ತಕ್ಷಣ ರಾತ್ರಿ 2 ರಿಂದ ಬೆಳಿಗ್ಗೆ 7 ರವರೆಗೆ ಡೀಸೆಲ್ ಪಂಪ್ ಅಥವಾ ಏರೇಟರ್ ಮೂಲಕ ನೀರನ್ನು ಏರೇಟ್ ಮಾಡಿ.
2. ಹೊಲಗಳಿಂದ ಬರುವ ಗೊಬ್ಬರ ಅಥವಾ ಚರಂಡಿ ನೀರಿನ ಒಳಹರಿವನ್ನು ತಕ್ಷಣ ನಿಲ್ಲಿಸಿ.
3. ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ 150 ಕೆಜಿ ಸುಣ್ಣವನ್ನು ನೀರಿನಲ್ಲಿ ಕರಗಿಸಿ ಕೆರೆಗೆ ಸಿಂಪಡಿಸಿ.

ಸಹಾಯಕ್ಕಾಗಿ ಸಂಪರ್ಕಿಸಿ:
ಕರ್ನಾಟಕ ಒಳನಾಡು ಮೀನುಗಾರಿಕಾ ಇಲಾಖೆ ಸಹಾಯವಾಣಿ: 1800-425-1020
```

### English SMS / WhatsApp Notification
```text
⚠️ EARLY WARNING: Hosahalli Gram Panchayat Tank (Maddur, Mandya)
Sentinel-2 satellite monitoring indicates accelerated micro-algal growth.
Dissolved Oxygen is forecasted to crash to 3.2 mg/L within 48-72 hours.
Critical lethal threshold is < 4.0 mg/L; mass mortality risk is HIGH without intervention.

Actionable SOP:
1. Run mechanical surface aerators / diesel pump recycling nightly (02:00 AM - 07:00 AM).
2. Cut off upstream agricultural fertilizer and wastewater inflows.
3. Apply agricultural quicklime (CaO) at 150 kg/hectare to strip excess phosphates.

Inland Fisheries Dept Helpline: 1800-425-1020
```

---

## 🖥️ Dashboard UI ASCII Wireframe

```text
+-------------------------------------------------------------------------------------------------------+
| [LOGO] MATSYA-WATCH: Karnataka Village Fish Tank Early Warning Portal           [District: Mandya v]  |
+-------------------------------------------------------------------------------------------------------+
| KPI CARDS:                                                                                            |
|  +---------------------+ +--------------------+ +---------------------+ +--------------------------+  |
|  | Monitored Tanks     | | Watch List (D1-4)  | | High Alert (D5-8)   | | Critical Hypoxia (<4mg/L)|  |
|  | 3,407 Tanks         | | 42 Tanks           | | 11 Tanks            | | 3 Tanks                  |  |
|  +---------------------+ +--------------------+ +---------------------+ +--------------------------+  |
+-------------------------------------------------------------------------------------------------------+
| MAIN WORKSPACE:                                                                                       |
|                                                                                                       |
|  +------------------------------------------------------+  +---------------------------------------+  |
|  | GIS MAP VIEW (Sentinel-2 Live Revisit Layer)         |  | SELECTED TANK DETAILS:                |  |
|  |                                                      |  | Name: Hosahalli Gram Panchayat Kere   |  |
|  |      [G] Normal Tank (Kolar)                         |  | District: Mandya | Taluk: Maddur      |  |
|  |                                                      |  | Area: 12.0 Hectares (~30 Acres)       |  |
|  |                [O] High Alert (Hosahalli, Mandya)    |  | Status: [ HIGH ALERT (Day 7 Bloom) ]  |  |
|  |                                                      |  | Current NDCI: 0.46 (Hyper-eutrophic)  |  |
|  |         [Y] Watch Tank (Ramanagara)                  |  | Predicted DO: 3.2 mg/L in 48 Hours    |  |
|  |                                                      |  | At-Risk Value: Rs. 2,40,000 INR       |  |
|  |  Map Layers: [x] Satellite  [ ] Algae Heatmap        |  +---------------------------------------+  |
|  +------------------------------------------------------+  | 14-DAY NDCI VS DISSOLVED OXYGEN:      |  |
|                                                            | 1.0|          /---\ (Bloom Peak)      |  |
|  +------------------------------------------------------+  | 0.5|   /-----/      \                |  |
|  | ADVISORY & MITIGATION SOP (Auto-Calculated):          |  | 0.0+---+-----+-----+-----+-----+----   |  |
|  | • Aerator Hours: 8 Hours/Night (02:00 AM - 07:00 AM)  |  |   DO: 7.6mg/L ---------> [3.2mg/L CRASH]|  |
|  | • Quicklime (CaO) Dosage: 1,800 kg total (150 kg/ha)  |  +---------------------------------------+  |
|  | • Inflow: Stop agricultural runoff channel diversion  |  | [ 📲 Resend Kannada Alert (SMS/WA) ]  |  |
|  | • Emergency Contact: R. Kumar (+91-98450-XXXXX)      |  | [ 📄 Download Official Advisory PDF ] |  |
|  +------------------------------------------------------+  +---------------------------------------+  |
+-------------------------------------------------------------------------------------------------------+
```

---

## 📜 Incident Escalation Matrix

| Risk Level | Lead Time | Trigger Condition | Primary Recipient | Automated Action |
| :--- | :--- | :--- | :--- | :--- |
| **🟢 Normal** | $> 14	ext{ Days}$ | $	ext{NDCI} < 0.20$ | District Portal | Baseline 5-day revisit monitoring. |
| **🟡 Watch** | $7 - 10	ext{ Days}$ | $0.20 \le 	ext{NDCI} < 0.35$ | Cooperative Secretary | WhatsApp advisory; inspect tank inlets. |
| **🟠 High Alert** | $3 - 5	ext{ Days}$ | $0.35 \le 	ext{NDCI} < 0.50$ | Cooperative President & PDO | SMS, WhatsApp & IVR voice call; start nightly aeration. |
| **🔴 Critical** | $< 48	ext{ Hours}$ | $	ext{DO} < 4.0	ext{ mg/L}$ | Taluk Fisheries Assistant Director | Continuous emergency aeration; initiate partial emergency harvest. |

---

## 🏛️ Alignment with Government Initiatives
- **PMMSY (Pradhan Mantri Matsya Sampada Yojana):** Fulfills quality monitoring, loss reduction, and aqua-tech adoption mandates.
- **KSRSAC (Karnataka State Remote Sensing Applications Centre):** Integrates with state geo-spatial water body inventories.
- **Gram Panchayat Asset Management:** Protects public auction revenue and community cooperative livelihood.
