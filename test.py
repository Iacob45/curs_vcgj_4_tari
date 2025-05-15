import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime

# Inițializare listă pentru date
results = []

# Funcție pentru extragerea diferenței între locul 2 și locul 3
def fetch_difference():
    url = "https://prezenta.roaep.ro/prezidentiale04052025/pv/romania/results/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error {response.status_code} accessing the page")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Aici trebuie adaptat în funcție de structura actuală a paginii
    # Exemplu generic: presupunem că există un tabel cu clasament
    candidates = []

    # Exemplu fictiv – adaptare necesară!
    for row in soup.select("table tr")[1:]:
        cols = row.find_all("td")
        if len(cols) >= 3:
            name = cols[1].text.strip()
            votes = int(cols[2].text.strip().replace('.', '').replace(',', ''))
            candidates.append((name, votes))

    # Sortăm candidații după voturi
    candidates = sorted(candidates, key=lambda x: x[1], reverse=True)

    if len(candidates) >= 3:
        loc2 = candidates[1]
        loc3 = candidates[2]
        diff = loc2[1] - loc3[1]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        results.append({"time": timestamp, "loc2": loc2[0], "loc3": loc3[0], "difference": diff})
        print(f"{timestamp} - Diferență: {diff} ({loc2[0]} vs {loc3[0]})")
    else:
        print("Nu s-au găsit destui candidați.")


# Rulare loop la fiecare 2 minute
try:
    while True:
        fetch_difference()
        time.sleep(120)  # 2 minute
except KeyboardInterrupt:
    print("Oprire monitorizare. Salvare CSV...")
    df = pd.DataFrame(results)
    df.to_csv("diferente_loc2_loc3.csv", index=False)
    print("Salvat în 'diferente_loc2_loc3.csv'")
