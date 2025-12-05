RAW_DATA_PATH = "../data/raw/onlinefraud.csv"
PROCESSED_DATA_PATH = "../data/processed/onlinefraud_clean.csv"

def print_shape(df, label="Data"):
    print(f"{label} shape: {df.shape}")
