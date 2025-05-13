# DevOps Individuell – CI/CD med GitHub Actions

Detta projekt är en del av kursen i DevOps, där jag har implementerat ett komplett CI/CD-arbetsflöde med hjälp av GitHub Actions. Projektet består av datagenerering, CSV-till-JSON-konvertering, testautomation och deployment till GitHub Pages.

---

## 🚀 Funktioner

### ✅ CI/CD-pipeline innehåller:
- **generate.py** – genererar `profiles1.csv`
- **csvtojson.py** – konverterar `profiles1.csv` till `data.json`
- **test_csvtojson.py** – verifierar att CSV och JSON har rätt struktur
- **GitHub Pages-deployment** – publicerar `index.html`, `script.js` och `data.json`

---

## 🔄 Workflow

Workflow-filen (`main.yml`) körs automatiskt vid varje `push` eller pull request till `main`-branchen.

### Steg-för-steg:
1. 🔄 Checkout av koden
2. 🐍 Python sätts upp
3. 🏗️ `generate.py` körs – skapar `profiles1.csv`
4. 🔁 `csvtojson.py` körs – skapar `data.json`
5. ✅ Tester körs med `unittest`
6. 📦 Filen `index.html`, `script.js`, `data.json` kopieras till `dist/`
7. 🚀 Deployment till GitHub Pages

---

## 📊 Tester

I `test_csvtojson.py` testas följande:

- CSV-filen innehåller exakt **12 kolumner**
- CSV-filen har **minst 900 rader**
- JSON-filen innehåller alla förväntade fält
- JSON-filen innehåller **minst 900 objekt**

Tester körs via:

```bash
python -m unittest discover -s . -p '*Test.py'
