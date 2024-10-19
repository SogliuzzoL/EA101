import matplotlib.pyplot as plt
import numpy as np
import random

# Définir les coefficients pour le modèle linéaire
alpha = 100  # Constante initiale
beta_1 = 0.5  # Coefficient de la demande
beta_2 = -0.3  # Coefficient de l'offre
beta_3 = 2.0  # Coefficient de l'inflation
beta_4 = 0.01  # Coefficient de la masse monétaire
beta_5 = -1.5  # Coefficient du taux directeur

# Fonction prix linéaire
def prix_lineaire(Q, S, I, M, T):
    return (alpha + 
            beta_1 * Q + 
            beta_2 * S + 
            beta_3 * I + 
            beta_4 * M + 
            beta_5 * T)

# Simulation de Monte Carlo
def monte_carlo_simulation(n_simulations=10000):
    prix_simules = []
    
    for _ in range(n_simulations):
        # Générer des paramètres aléatoires pour chaque simulation
        Q = random.uniform(0, 100)  # Demande aléatoire
        S = random.uniform(20, 50)  # Offre aléatoire
        I = random.uniform(1.0, 5.0)  # Inflation aléatoire entre 1% et 5%
        M = random.uniform(900, 1100)  # Masse monétaire aléatoire entre 900 et 1100 milliards
        T = random.uniform(0.25, 1.5)  # Taux directeur aléatoire entre 0.25% et 1.5%
        
        # Calculer le prix pour cette combinaison
        prix = prix_lineaire(Q, S, I, M, T)
        prix_simules.append(prix)
    
    return prix_simules

# Fonction pour simuler le prix en fonction du temps avec des tendances
def prix_en_fonction_du_temps(n_temps=50):
    temps = np.arange(n_temps)  # Création d'un tableau de temps
    prix_temps = []

    # Initialiser les valeurs des paramètres
    base_Q = 50  # Demande de base
    base_S = 35  # Offre de base
    base_I = 3.0  # Inflation de base
    base_M = 1000  # Masse monétaire de base
    base_T = 0.75  # Taux directeur de base

    for t in temps:
        # Appliquer des tendances avec un bruit aléatoire
        Q = base_Q + 0.5 * t + random.uniform(-5, 5)  # Demande qui augmente avec le temps
        S = base_S + random.uniform(-1, 1)  # Offre stable
        I = base_I + 0.02 * t + random.uniform(-0.1, 0.1)  # Inflation qui augmente lentement
        M = base_M + random.uniform(-10, 10)  # Masse monétaire avec peu de fluctuations
        T = base_T + random.uniform(-0.05, 0.05)  # Taux directeur avec fluctuations

        # Calculer le prix pour cette combinaison
        prix = prix_lineaire(Q, S, I, M, T)
        prix_temps.append(prix)

    return temps, prix_temps

# Calculer le prix de Monte Carlo
n_simulations = 10000
prix_simules = monte_carlo_simulation(n_simulations)

# Calculer le prix en fonction du temps
n_temps = 50
temps, prix_temps = prix_en_fonction_du_temps(n_temps)

# Affichage des graphiques
fig, axs = plt.subplots(2, 1, figsize=(12, 12))

# Graphique de Monte Carlo
axs[0].hist(prix_simules, bins=50, color='lightblue', edgecolor='black')
axs[0].set_title(f"Distribution des prix simulés (Monte Carlo - {n_simulations} simulations)")
axs[0].set_xlabel("Prix")
axs[0].set_ylabel("Fréquence")
axs[0].grid(True)

# Graphique du prix en fonction du temps
axs[1].plot(temps, prix_temps, marker='o', linestyle='-', color='orange')
axs[1].set_title("Évolution du prix linéaire en fonction du temps")
axs[1].set_xlabel("Temps")
axs[1].set_ylabel("Prix")
axs[1].grid(True)
axs[1].set_xticks(temps)  # Afficher les valeurs de temps sur l'axe x

plt.tight_layout()  # Ajuster l'espacement entre les graphiques
plt.show()
