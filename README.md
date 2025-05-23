# py-bls-api

A Python wrapper for the Bureau of Labor Statistics (BLS) API, providing easy access to select surveys, metadata, data previews, series metadata, popular series IDs, and time series data.

## Features

- List available BLS surveys (`get_surveys`)
- Fetch survey metadata (`get_survey_metadata`)
- Preview data structure for a survey (`get_data_preview`)
- Retrieve series ID metadata as a DataFrame (`get_seriesid_metadata`)
- Get popular series IDs for a survey (`get_popular_seriesids`)
- Download time series data (`get_bls_data`)

## Installation

Install directly from PyPI:

```bash
pip install py-bls-api
```

Or install from GitHub (latest development version):

```bash
pip install git+https://github.com/coding-with-chris/py-bls-api.git
```

## Quick Start

First, import the package:

```python
from py_bls_api import (
    get_surveys,
    get_survey_metadata,
    get_data_preview,
    get_seriesid_metadata,
    get_popular_seriesids,
    get_bls_data
)
```

### 1. List all surveys

```python
surveys = get_surveys()
print(surveys)
# e.g., {'IP': 'Industrial Production', 'CU': 'Consumer Price Index', ...}
```

### 2. Fetch survey metadata

```python
meta = get_survey_metadata("CU")
print(meta.keys())
# e.g., ['survey_name', 'survey_abbreviation', 'series', 'data_preview']
```

### 3. Preview data for a survey

```python
df_preview = get_data_preview("IP")
print(df_preview.head())
```

### 4. Retrieve series metadata

```python
df_series_meta = get_seriesid_metadata("CU")
print(df_series_meta.head())
```

### 5. Get popular series IDs

```python
# Requires a BLS API registration key
api_key = "YOUR_API_KEY_HERE"
popular_ids = get_popular_seriesids("CU", api_key)
print(popular_ids)
```

### 6. Download time series data

```python
series_ids = ["CUUR0000SA0"]  # e.g., CPI-All Urban Consumers
start_year = 2020
end_year = 2024
api_key = "YOUR_API_KEY_HERE"

# Returns a tuple: (data_df, log_df)
data_df, log_df = get_bls_data(series_ids, start_year, end_year, api_key)
print(data_df.head())
print(log_df)
```

## Configuration

By default, metadata files are fetched from GitHub Pages:

```
https://coding-with-chris.github.io/py-bls-api/metadata/
```

## Requirements

- Python 3.6+
- pandas >= 1.3.0
- requests >= 2.25.0

## Contributing

Not looking for contributions at this time. However, feedback and suggestions are always welcome!  
Please feel free to open an issue if you find bugs or have ideas for improvements.

## License

This project is released under a Non-Commercial, No-Derivatives license. See [LICENSE](LICENSE) for details.

