# Base probabilities
PD = 0.01                  # Prior probability of having the disease
P_NotD = 1 - PD            # Probability of not having the disease (0.99)

# Conditional test probabilities
P_Pos_D = 0.99             # True Positive rate (Sensitivity)
P_Pos_NotD = 0.05          # False Positive rate (1 - Specificity)

# Bayes' Theorem Calculation
P_D_Pos = (P_Pos_D * PD) / ((P_Pos_D * PD) + (P_Pos_NotD * P_NotD))

print("Probability that person actually has disease:")
print(round(P_D_Pos * 100, 2), "%")

