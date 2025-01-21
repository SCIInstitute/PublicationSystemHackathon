#!/usr/bin/env python3

import requests
import polars as pl
from typing import List, Dict
import sys
from datetime import datetime
from pprint import pprint
from io import StringIO
import json
from flatten_json import flatten

class ORCIDPublicationsFetcher:
    BASE_URL = "https://pub.orcid.org/v3.0"
    HEADERS = {
        "Accept": "application/json"
    }

    def __init__(self, orcid_ids: List[str]):
        self.orcid_ids = orcid_ids
        self.publications_data = []

    def fetch_researcher_publications(self, orcid_id: str) -> pl.DataFrame:
        """Fetch publications for a single researcher."""
        url = f"{self.BASE_URL}/{orcid_id}/works"
        response = requests.get(url, headers=self.HEADERS)
        
        if response.status_code != 200:
            print(f"Error fetching data for ORCID {orcid_id}: {response.status_code}")
            return pl.DataFrame()

        data = response.json()

        # Write the data json to a file
        with open(f"{orcid_id}_data.json", "w") as f:
            json.dump(data, f, indent=2)

        
        # Convert dictionary to JSON string for Polars
        data_str = json.dumps(data)

        print(json.dumps(data, indent=2)) # Print the JSON data
        
        # Read JSON string into Polars DataFrame
        df = pl.read_json(StringIO(data_str))
        print("DataFrame Schema:")
        pprint(dict(df.schema))
        print("\nFirst few rows:")
        print(df)
        sys.exit()
        
        return df

    def fetch_all_publications(self) -> pl.DataFrame:
        """Fetch publications for all researchers and return as a Polars DataFrame."""
        # Create list to store DataFrames for each researcher
        dfs = []
        
        for orcid_id in self.orcid_ids:
            df = self.fetch_researcher_publications(orcid_id)
            if not df.is_empty():
                dfs.append(df)
                print(f"Fetched {len(df)} publications for ORCID: {orcid_id}")

        # Concatenate all DataFrames
        if dfs:
            return pl.concat(dfs)
        return pl.DataFrame()

    def save_to_parquet(self, df: pl.DataFrame, output_file: str):
        """Save the DataFrame to a parquet file."""
        df.write_parquet(output_file)
        print(f"Saved publications data to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_publications.py <orcid_id1> <orcid_id2> ...")
        sys.exit(1)

    orcid_ids = sys.argv[1:]
    fetcher = ORCIDPublicationsFetcher(orcid_ids)
    
    # Fetch publications and create DataFrame
    df = fetcher.fetch_all_publications()
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"publications_{timestamp}"
    
    # Save to parquet
    fetcher.save_to_parquet(df, f"{output_filename}.parquet")
    df.write_csv(f"{output_filename}.csv")

if __name__ == "__main__":
    main()
