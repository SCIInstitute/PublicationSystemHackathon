# ORCID Publications Fetcher

## IMPORTANT: Notes

This experiment was unsuccessful due to the incompatibility of tabular data with the non-tabulated nature of our data source. Key details are outlined below:

- Decision to Avoid Tabular Data:
- The data source is inherently non-tabulated, making it impractical to use tabular data structures.

- Polars Limitation: - While Polars efficiently processes data into hierarchical, strictly-typed structures, this approach requires recursive flattening. - Although technically feasible, the effort involved does not justify the potential benefits.

  - Recommendation:

    - Use a document database like MongoDB to handle non-tabulated data more effectively.

  - ORCID Public API:
    - The script successfully fetches data from the ORCID Public API v3.0.
    - However, consider using Academic Tracker, which integrates ORCID data and may better suit the project's needs.

To install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with one or more ORCID IDs as arguments:

```bash
python fetch_publications.py ORCID_ID1 ORCID_ID2 ...
```

Example:

```bash
python fetch_publications.py 0000-0002-1825-0097 0000-0001-5109-3700
```

## Features

- Fetches publication data from ORCID's Public API v3.0
- Processes JSON response data using Polars DataFrame
- Saves output in both Parquet and CSV formats with timestamp
- Handles multiple ORCID IDs in a single run
- Error handling for failed API requests
- Debug output of JSON responses and DataFrame schema

## Output

The script generates two output files for each run:

1. `publications_YYYYMMDD_HHMMSS.parquet`
2. `publications_YYYYMMDD_HHMMSS.csv`

The timestamp in the filename ensures unique output files for each run.

## API Details

- Base URL: https://pub.orcid.org/v3.0
- Uses JSON format for API responses
- No authentication required (uses public API)
