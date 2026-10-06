from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Create Bayesian Network structure (Fixed list syntax)
model = DiscreteBayesianNetwork([("Burglary", "Alarm"), ("Earthquake", "Alarm")])

# Step 2: Define probability of Burglary
cpd_burglary = TabularCPD(
    variable="Burglary", 
    variable_card=2, 
    values=[[0.999], [0.001]], 
    state_names={"Burglary": ["False", "True"]}
)

# Step 3: Define probability of Earthquake
cpd_earthquake = TabularCPD(
    variable="Earthquake", 
    variable_card=2, 
    values=[[0.998], [0.002]], 
    state_names={"Earthquake": ["False", "True"]}
)

# Step 4: Define probability of Alarm
cpd_alarm = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],  # Alarm = False
        [0.001, 0.29, 0.94, 0.95]   # Alarm = True
    ],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
    state_names={
        "Alarm": ["False", "True"],
        "Burglary": ["False", "True"],
        "Earthquake": ["False", "True"]
    }
)

# Step 5: Add CPDs to model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm)

# Step 6: Check whether model is correct
print("Is Bayesian Network valid?", model.check_model())

# Step 7: Perform inference
inference = VariableElimination(model)
result = inference.query(
    variables=["Burglary"], 
    evidence={"Alarm": "True"}
)

print("\nPosterior Probability:")
print("P(Burglary | Alarm = True)")
print(result)
