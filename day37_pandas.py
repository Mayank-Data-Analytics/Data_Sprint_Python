# 1. We import the engine and give it a short alias 'pd' to save typing
import pandas as pd

# 2. We create raw data using a standard Python Dictionary
client_data = {
    "Client_Name": ["Apex Corp", "Zenith Media", "Nova Tech"],
    "Videos_Edited": [12, 5, 20],
    "Retainer_Active": [True, False, True]
}

# 3. We load the raw data into the Pandas Engine to create a DataFrame
df = pd.DataFrame(client_data)

# 4. Print the result
print("--- Raw Python Dictionary ---")
print(client_data)
print("\n--- Pandas DataFrame ---")
print(df)