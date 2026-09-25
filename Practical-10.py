# Bayesian Network using pgmpy
# Example: Burglary-Alarm Network
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Create Bayesian Network structure
model = DiscreteBayesianNetwork([
    ("Burglary", "Alarm"), 
    ("Earthquake", "Alarm"), 
    ("Alarm", "JohnCalls"), 
    ("Alarm", "MaryCalls")
])

# Step 2: Define Conditional Probability Tables
# P(Burglary)
cpd_burglary = TabularCPD(
    variable="Burglary", 
    variable_card=2, 
    values=[[0.999], [0.001]], 
    state_names={"Burglary": ["False", "True"]}
)

# P(Earthquake)
cpd_earthquake = TabularCPD(
    variable="Earthquake", 
    variable_card=2, 
    values=[[0.998], [0.002]], 
    state_names={"Earthquake": ["False", "True"]}
)

# P(Alarm | Burglary, Earthquake)
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

# P(JohnCalls | Alarm)
cpd_john = TabularCPD(
    variable="JohnCalls", 
    variable_card=2, 
    values=[
        [0.95, 0.10],  # JohnCalls = False
        [0.05, 0.90]   # JohnCalls = True
    ],
    evidence=["Alarm"], 
    evidence_card=[2], 
    state_names={
        "JohnCalls": ["False", "True"], 
        "Alarm": ["False", "True"]
    }
)

# P(MaryCalls | Alarm)
cpd_mary = TabularCPD(
    variable="MaryCalls", 
    variable_card=2, 
    values=[
        [0.99, 0.30],  # MaryCalls = False
        [0.01, 0.70]   # MaryCalls = True
    ],
    evidence=["Alarm"], 
    evidence_card=[2], 
    state_names={
        "MaryCalls": ["False", "True"], 
        "Alarm": ["False", "True"]
    }
)

# Step 3: Add CPDs to model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# Step 4: Check model correctness
print("Is Bayesian Network valid?", model.check_model())

# Step 5: Perform inference
inference = VariableElimination(model)

# Query: Probability of Burglary when John and Mary both call
result = inference.query(
    variables=["Burglary"], 
    evidence={"JohnCalls": "True", "MaryCalls": "True"}
)

print("\nProbability of Burglary given JohnCalls=True and MaryCalls=True:")
print(result)
