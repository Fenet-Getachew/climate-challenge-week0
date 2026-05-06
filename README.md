# Climate Challenge - Week 0

## Development Setup
To reproduce the environment for this project, follow these steps:

1. **Clone the repository:**
   git clone https://github.com/Fenet-Getachew/climate-challenge-week0.git

2. **Create a virtual environment:**
   python -m venv .venv

3. **Activate the environment:**
   - Windows: .\.venv\Scripts\Activate.ps1
   - Mac/Linux: source .venv/bin/activate

4. **Install dependencies:**
   pip install -r requirements.txt



## Climate Dashboard (Streamlit)
A tool to visualize climate extremes and variability for 5 African nations.
### Usage:
1. Ensure your cleaned data is in `data/`.
2. Run `pip install streamlit plotly pandas`.
3. Launch via: `streamlit run app/main.py`.

### KPIs Met:
- **Interactive:** Year sliders and multi-country filters.
- **Dynamic:** Auto-calculates summary stats based on UI selection.