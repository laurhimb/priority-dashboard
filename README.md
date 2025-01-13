# Priority Dashboard

A Streamlit dashboard for tracking strategic priorities.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/laurhimb/priority-dashboard.git
   cd priority-dashboard
   ```

2. Create a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the dashboard:
   ```bash
   streamlit run priorities_dashboard.py
   ```

The dashboard will open in your default web browser automatically.

## Features

- Visual display of strategic priorities
- Progress tracking
- Priority level indicators
- Real-time updates

## Adding Your Data

Currently using sample data. To add your own priorities, modify the `sample_data` dictionary in `priorities_dashboard.py`.

## Getting Help

If you encounter any issues, please check the [Streamlit documentation](https://docs.streamlit.io) or open an issue in this repository.