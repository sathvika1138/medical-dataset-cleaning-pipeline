import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Setup the Dataset
# ---------------------------------------------------------
data = {
    'Patient ID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'Age': [28, 45, 60, 34, 50, 29],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Disease': ['Flu', 'Hypertension', 'Diabetes', 'Asthma', 'Arthritis', 'Flu'],
    'Medication': ['Paracetamol', 'Amlodipine', 'Metformin', 'Salbutamol', 'Ibuprofen', 'Paracetamol'],
    'Dosage (MG)': [500, 5, 500, 100, 400, 500]
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 2. Data Cleaning
# ---------------------------------------------------------
# Remove duplicates based on Patient ID
df = df.drop_duplicates(subset=['Patient ID'])

# Handle potential missing values (using medication group mean)
# Note: This step is robust even if your dataset grows larger later
df['Dosage (MG)'] = df.groupby('Medication')['Dosage (MG)'].transform(lambda x: x.fillna(x.mean()))

# ---------------------------------------------------------
# 3. Basic Analysis
# ---------------------------------------------------------
total_patients = df['Patient ID'].nunique()
avg_age = df['Age'].mean()
common_diseases = df['Disease'].value_counts()
avg_dosage = df.groupby('Medication')['Dosage (MG)'].mean()

# Print results to the console
print(f"--- Analysis Results ---")
print(f"Total Patients: {total_patients}")
print(f"Average Age: {avg_age:.2f}")
print(f"\nMost Common Diseases:\n{common_diseases.to_string()}")
print(f"\nAverage Dosage per Medication:\n{avg_dosage.to_string()}")

# ---------------------------------------------------------
# 4. Save Data
# ---------------------------------------------------------
# Save the cleaned dataset to a CSV file
df.to_csv('cleaned_patient_data.csv', index=False)
print("\nSuccess: Cleaned data saved to 'cleaned_patient_data.csv'")

# ---------------------------------------------------------
# 5. Visualization
# ---------------------------------------------------------
# Create a bar chart for disease distribution
plt.figure(figsize=(10, 6))
common_diseases.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Patient Distribution by Disease')
plt.xlabel('Disease')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image
plt.savefig('disease_distribution.png')
print("Success: Visualization saved as 'disease_distribution.png'")

# Display the plot
plt.show()