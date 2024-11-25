import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print("Aperçu des premières lignes du dataset :")
print(df.head())

print("\nNettoyage des données...")

df["AskPrice"] = pd.to_numeric(df["AskPrice"].str.replace("₹", "").str.replace(",", ""), errors="coerce")

df["kmDriven"] = pd.to_numeric(df["kmDriven"].str.replace("km", "").str.replace(",", "").str.strip(), errors="coerce")

df = df.dropna()

print("\nRésumé des données après nettoyage :")
print(df.info())

print("\nAnalyse 1 : Distribution des prix des voitures...")
plt.figure(figsize=(10, 6))
sns.histplot(df["AskPrice"], kde=True, bins=20, color="skyblue")
plt.title("Distribution des prix des voitures")
plt.xlabel("Prix demandé (€)")
plt.ylabel("Nombre de voitures")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

print("\nAnalyse 2 : Prix moyen par marque...")
brand_prices = df.groupby("Brand")["AskPrice"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
brand_prices.plot(kind="bar", color="green")
plt.title("Prix moyen par marque")
plt.xlabel("Marque")
plt.ylabel("Prix moyen (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_price_by_brand.png")
plt.show()

print("\nAnalyse 3 : Impact du kilométrage sur le prix demandé...")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="kmDriven", y="AskPrice", data=df, hue="FuelType", palette="viridis")
plt.title("Relation entre kilométrage et prix demandé")
plt.xlabel("Kilométrage (km)")
plt.ylabel("Prix demandé (€)")
plt.tight_layout()
plt.savefig("mileage_vs_price.png")
plt.show()

print("\nAnalyse 4 : Répartition des types de transmission...")
transmission_counts = df["Transmission"].value_counts()

plt.figure(figsize=(8, 6))
transmission_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["skyblue", "orange"])
plt.title("Répartition des types de transmission")
plt.ylabel("")
plt.tight_layout()
plt.savefig("transmission_distribution.png")
plt.show()

print("\nAnalyse 5 : Prix moyen en fonction de l'âge de la voiture...")
age_prices = df.groupby("Age")["AskPrice"].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x=age_prices.index, y=age_prices.values, marker="o", color="blue")
plt.title("Prix moyen en fonction de l'âge de la voiture")
plt.xlabel("Âge de la voiture (années)")
plt.ylabel("Prix moyen (€)")
plt.tight_layout()
plt.savefig("price_by_age.png")
plt.show()

print("\nAnalyses terminées. Les graphiques sont enregistrés dans le dossier du projet.")
