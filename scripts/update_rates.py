import json
from datetime import datetime

# Static data — to be replaced later with live scraping/API
data = {
    "updated": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
    "gold": {
        "24k": "Rs. 14,300/g",
        "22k": "Rs. 13,200/g",
        "change": "+1.2%"
    },
    "forex": {
        "interbank": "Rs. 278.50",
        "open_market": "Rs. 283.90",
        "change": "-0.45%"
    },
    "crypto": {
        "btc": "$62,150",
        "eth": "$3,120",
        "xrp": "$0.72"
    },
    "petrol": {
        "petrol": "Rs. 265.00/ltr",
        "diesel": "Rs. 275.00/ltr",
        "change": "+0.35%"
    }
}

# Save JSON
with open('../auto/latest_rates.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

# Build HTML
html = f"""
<div style="font-family:sans-serif; color:#fff;">
  <h2 style="text-align:center;">💹 Pakistan Ka Rates</h2>
  <p style="text-align:center;">Updated: {data['updated']}</p>

  <h3>🥇 GOLD RATES</h3>
  <ul>
    <li>24K: {data['gold']['24k']}</li>
    <li>22K: {data['gold']['22k']}</li>
    <li>Change: {data['gold']['change']}</li>
  </ul>

  <h3>💱 USD/PKR FOREX</h3>
  <ul>
    <li>Interbank: {data['forex']['interbank']}</li>
    <li>Open Market: {data['forex']['open_market']}</li>
    <li>Change: {data['forex']['change']}</li>
  </ul>

  <h3>🪙 CRYPTO</h3>
  <ul>
    <li>BTC: {data['crypto']['btc']}</li>
    <li>ETH: {data['crypto']['eth']}</li>
    <li>XRP: {data['crypto']['xrp']}</li>
  </ul>

  <h3>⛽ PETROL / DIESEL</h3>
  <ul>
    <li>Petrol: {data['petrol']['petrol']}</li>
    <li>Diesel: {data['petrol']['diesel']}</li>
    <li>Change: {data['petrol']['change']}</li>
  </ul>
</div>
"""

# Save HTML
with open('../auto/latest_rates.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ latest_rates.json & latest_rates.html updated successfully.")
