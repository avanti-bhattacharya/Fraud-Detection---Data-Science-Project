import pandas as pd

def add_party_type_features(df):
    """Add sender/receiver classification (Customer or Merchant)."""
    df['orig_party_type'] = df['nameOrig'].str[0].map({'C': 'customer', 'M': 'merchant'})
    df['dest_party_type'] = df['nameDest'].str[0].map({'C': 'customer', 'M': 'merchant'})
    return df

def add_balance_features(df):
    """Calculate balance behavior risk patterns."""
    df['orig_balance_change'] = df['newbalanceOrig'] - df['oldbalanceOrg']
    df['dest_balance_change'] = df['newbalanceDest'] - df['oldbalanceDest']
    df['net_balance_change'] = df['orig_balance_change'] + df['dest_balance_change']
    return df

def encode_categoricals(df):
    """One-hot encode transaction & party-type columns."""
    categorical_cols = ['type', 'orig_party_type', 'dest_party_type']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def drop_leakage_columns(df):
    """Remove ID-like fields that leak information."""
    return df.drop(columns=['nameOrig', 'nameDest'], errors='ignore')
