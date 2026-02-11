

"""
Returns a list of columns in df that are object/str type
and can be converted to datetime.
 Checks up to sample_size non-null values.
"""


def detect_datetime_columns(self, df, sample_size=100):
    import pandas as pd

    datetime_cols = []

    for col in df.columns:
        if df[col].dtype == 'object':  # only check string/object columns
            # Sample non-null values to avoid expensive full scan
            non_null_values = df[col].dropna().head(sample_size)
            if len(non_null_values) == 0:
                continue
            try:
                # Try converting the sample
                pd.to_datetime(non_null_values, errors='raise')
                datetime_cols.append(col)
            except Exception:
                pass  # Conversion failed, skip this column
    return datetime_cols
