"""
Multi-Channel Alert Dispatcher Service
Formats localized Kannada and English emergency SMS / WhatsApp notifications
and dispatches them to Panchayat leaders and cooperative fish farmers.
"""

from typing import Dict, Any

class AlertDispatcher:
    @staticmethod
    def format_kannada_sms(tank_name: str, panchayat: str, predicted_do: float, days_left: int) -> str:
        return (
            f"⚠️ ಎಚ್ಚರಿಕೆ: {tank_name} ({panchayat} ಗ್ರಾ.ಪಂ)\n"
            f"ಉಪಗ್ರಹ ಪರಿಶೀಲನೆಯ ಪ್ರಕಾರ ಕೆರೆಯಲ್ಲಿ ಪಾಚಿ (Algal Bloom) ವೇಗವಾಗಿ ಬೆಳೆಯುತ್ತಿದೆ. "
            f"ಮುಂದಿನ {days_left} ದಿನಗಳಲ್ಲಿ ಆಮ್ಲಜನಕ {predicted_do} mg/L ಗೆ ಕುಸಿಯುವ ಸಾಧ್ಯತೆಯಿದೆ (< 4 mg/L ಮೀನುಗಳಿಗೆ ಅಪಾಯಕಾರಿ).\n"
            f"ತಕ್ಷಣ ಕ್ರಮಗಳು:\n"
            f"1. ನೀರನ್ನು ಡೀಸೆಲ್ ಪಂಪ್ ಅಥವಾ ಏರೇಟರ್ ಮೂಲಕ ಏರೇಟ್ ಮಾಡಿ.\n"
            f"2. ಚರಂಡಿ/ಗೊಬ್ಬರದ ನೀರು ಬರುವುದನ್ನು ತಕ್ಷಣ ನಿಲ್ಲಿಸಿ.\n"
            f"ಮೀನುಗಾರಿಕಾ ಇಲಾಖೆ ಸಹಾಯವಾಣಿ: 1800-425-1020"
        )

    @staticmethod
    def format_english_sms(tank_name: str, panchayat: str, predicted_do: float, days_left: int) -> str:
        return (
            f"⚠️ ALGAL BLOOM EARLY WARNING: {tank_name} ({panchayat} GP)\n"
            f"Satellite data detects rapid micro-algae surge. Dissolved Oxygen predicted to crash to "
            f"{predicted_do} mg/L in {days_left} days (Lethal limit is < 4.0 mg/L).\n"
            f"Immediate Actions:\n"
            f"1. Start mechanical aeration (tractor/diesel pump recycling) immediately.\n"
            f"2. Divert upstream agricultural/sewage runoff.\n"
            f"Inland Fisheries Dept Helpline: 1800-425-1020"
        )

    @classmethod
    def dispatch_alert(cls, tank_data: Dict[str, Any], risk_level: str) -> Dict[str, Any]:
        """
        Wireframe integration for Twilio, Gupshup, or Karnataka State SMS Gateway.
        """
        predicted_do = tank_data.get("predicted_do_48h", 3.2)
        days_left = 3 if risk_level == "HIGH_ALERT" else 1

        kannada_text = cls.format_kannada_sms(
            tank_name=tank_data.get("name_kannada", "ಗ್ರಾಮ ಕೆರೆ"),
            panchayat=tank_data.get("panchayat", "ಪಂಚಾಯತಿ"),
            predicted_do=predicted_do,
            days_left=days_left
        )

        english_text = cls.format_english_sms(
            tank_name=tank_data.get("name_english", "Village Tank"),
            panchayat=tank_data.get("panchayat", "Panchayat"),
            predicted_do=predicted_do,
            days_left=days_left
        )

        print(f"[AlertDispatcher] Sending SMS to {tank_data.get('phone')}...")
        return {
            "status": "QUEUED_FOR_DELIVERY",
            "channels": ["SMS", "WHATSAPP"],
            "recipient_phone": tank_data.get("phone"),
            "kannada_payload": kannada_text,
            "english_payload": english_text
        }
