from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

print("=" * 60)
print("BAYESIAN NETWORK FOR DISEASE DIAGNOSIS")
print("=" * 60)

# Network Structure
model = DiscreteBayesianNetwork([
    ("COVID", "Fever"),
    ("COVID", "Cough"),
    ("COVID", "Fatigue"),
    ("COVID", "LossOfSmell")
])

# Prior Probability of COVID
cpd_covid = TabularCPD(
    variable="COVID",
    variable_card=2,
    values=[
        [0.9],
        [0.1]
    ]
)

# Fever
cpd_fever = TabularCPD(
    variable="Fever",
    variable_card=2,
    values=[
        [0.85, 0.20],
        [0.15, 0.80]
    ],
    evidence=["COVID"],
    evidence_card=[2]
)

# Cough
cpd_cough = TabularCPD(
    variable="Cough",
    variable_card=2,
    values=[
        [0.75, 0.25],
        [0.25, 0.75]
    ],
    evidence=["COVID"],
    evidence_card=[2]
)

# Fatigue
cpd_fatigue = TabularCPD(
    variable="Fatigue",
    variable_card=2,
    values=[
        [0.80, 0.30],
        [0.20, 0.70]
    ],
    evidence=["COVID"],
    evidence_card=[2]
)

# Loss Of Smell
cpd_smell = TabularCPD(
    variable="LossOfSmell",
    variable_card=2,
    values=[
        [0.95, 0.10],
        [0.05, 0.90]
    ],
    evidence=["COVID"],
    evidence_card=[2]
)

# Add CPDs
model.add_cpds(
    cpd_covid,
    cpd_fever,
    cpd_cough,
    cpd_fatigue,
    cpd_smell
)

# Validate Model
print("\nChecking Model...")
print("Model Valid:", model.check_model())

# Inference
inference = VariableElimination(model)

result = inference.query(
    variables=["COVID"],
    evidence={
        "Fever": 1,
        "Cough": 1,
        "Fatigue": 1,
        "LossOfSmell": 1
    }
)

print("\nEvidence Provided:")
print("Fever = True")
print("Cough = True")
print("Fatigue = True")
print("LossOfSmell = True")

print("\nPosterior Probability:")
print(result)

print("\nInference Completed Successfully")