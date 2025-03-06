## Running the Script

To run the `top_performing_logos.py` script, follow these steps:

1. Open a terminal.
2. Navigate to the directory where the script is located:
    ```sh
    cd path/to/your/script
    ```
3. Ensure you have the necessary libraries installed:
    ```sh
    pip install pandas matplotlib
    ```
4. Run the script:
    ```sh
    python top_performing_logos.py
    ```

After running the script, you should see the top-performing brands printed in the terminal, a CSV file named `top_performing_brands.csv` saved in the same directory, and a bar chart displaying the top-performing brands by revenue.


# sales-performance-insights
## A python project that analyzes sales performance, conversion rates, and revenue trends to optimize sales strategies. It identifies top performing logos and generates automated insights. 
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data for different brands (logos)
data = {
    "Brand": ["Brand A", "Brand B", "Brand C", "Brand D", "Brand E"],
    "Deals Closed": [50, 75, 30, 100, 60],
    "Revenue ($)": [200000, 350000, 120000, 500000, 250000],
    "Conversion Rate (%)": [45, 50, 40, 55, 48]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Sort brands by highest revenue
top_brands = df.sort_values(by="Revenue ($)", ascending=False)

# Display top-performing brands
print("Top Performing Brands:")
print(top_brands)

# Save report
top_brands.to_csv("top_performing_brands.csv", index=False)
print("\nBrand performance report saved as 'top_performing_brands.csv'")

# Visualization - Top Brands by Revenue
plt.figure(figsize=(8, 5))
plt.bar(top_brands["Brand"], top_brands["Revenue ($)"], color='blue')
plt.xlabel("Brand")
plt.ylabel("Revenue ($)")
plt.title("Top Performing Brands by Revenue")
plt.xticks(rotation=45)
plt.show()




