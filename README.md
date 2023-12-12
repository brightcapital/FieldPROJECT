# Bloomberg Data Visualization and Management

## Overview

The script utilizes the Streamlit framework for the user interface and Bokeh for data visualization. The primary functionalities include:

- **Visualizing Data**: The script allows users to visualize historical price data for selected equities over different time frames.

- **Adding/Deleting Tickers**: Users can add new ticker symbols with corresponding equities and currencies to the CSV file. Additionally, existing ticker symbols can be deleted from the CSV file.

- **Automated Data Fetching**: The script can be set to run automatically at the first day of the month and every Monday, fetching data from Bloomberg and updating the CSV file.

## Requirements

- Python 3.x
- Pandas
- Xbbg
- Requests
- Streamlit

Install the required packages using:

```bash
pip install pandas xbbg requests streamlit
```

## Usage
1. **Clone the Repository:**

    ```bash
    git clone https://github.com/brightcapital/FieldPROJECT.git
    ```
   
2. **Run the Script:**

    ```bash
    cd FieldPROJECT
    ```
    ```bash
    streamlit run data_fetcher_streamlit.py
    ```


3. **Automated Execution:**

    The script is set to run automatically at the first day of the month and every Monday between 20:30 and 20:35. Adjust the scheduling parameters in the script if needed.

## Customization

Feel free to customize the script according to your specific requirements. You can modify the data visualization settings, update the input prompts, or extend the functionality as needed.

