import pandas as pd

rawData = pd.read_csv("autism_screening.csv")

# Begin new df, cloning numeric values
cleanData = rawData.select_dtypes(exclude="object")

# Deduce categorical variables
catCols = rawData.select_dtypes(include="object").columns.tolist()

# Encode binary data numerically
binCols = [c for c in catCols if len(rawData[c].unique()) == 2]

sex_coder = lambda x: 1 if str(x).strip().lower() == "m" else 0
ans_coder = lambda x: 1 if str(x).strip().lower() == "yes" else 0

cleanData["isMale"] = rawData["gender"].apply(sex_coder)
cleanData["jaundice"] = rawData["jundice"].apply(ans_coder)
cleanData["autistic_family_member"] = rawData["austim"].apply(ans_coder)
cleanData["used_app_before"] = rawData["used_app_before"].apply(ans_coder)
cleanData["diagnostic_status"] = rawData["Class/ASD"].apply(ans_coder)

# Export machine-readable data
cleanData.to_csv("autism_screening_MR.csv")

