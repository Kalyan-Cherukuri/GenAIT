import streamlit as st

def classify_requirement(requirement):
    functional_keywords = [
        "allow", "enable", "provide", "support", "implement", "feature",
        "display", "execute", "calculate", "process", "authenticate",
        "validate", "manage", "create", "update", "delete", "retrieve",
        "search", "sort", "filter", "add", "remove", "access", "log in",
        "log out", "register", "notify", "alert", "upload", "download",
        "track", "monitor", "control", "view", "generate", "trigger",
        "edit", "store", "integrate", "sync", "automate", "print",
        "configure", "export", "import", "customize", "handle", "schedule",
        "reserve", "assign", "approve", "reject", "connect", "organize"
    ]
    non_functional_keywords = [
        "scalable", "secure", "reliable", "fast", "compliant", "performance",
    "responsive", "availability", "accessible", "efficiency", "maintainable",
    "scalability", "robust", "resilient", "fault-tolerant", "flexible",
    "recoverable", "encrypted", "safe", "stable", "portable", "adaptable",
    "usability", "user-friendly", "compatible", "integrity", "accuracy",
    "audit", "backup", "recovery", "latency", "throughput", "bandwidth",
    "optimization", "redundant", "redundancy", "lightweight", "overhead",
    "compliance", "logging", "traceability", "auditability", "availability",
    "downtime", "response time", "mean time to recovery", "load", "scaling",
    "privacy", "confidentiality", "durable", "localization", "globalization",
    "translation", "energy-efficient", "low power", "cost-effective",
    "eco-friendly", "reusability", "time-efficient", "data integrity",
    "error-tolerant", "minimum downtime", "high availability", "supportability"
    ]

    # Check for functional keywords
    if any(keyword in requirement.lower() for keyword in functional_keywords):
        return "Functional"
    # Check for non-functional keywords
    elif any(keyword in requirement.lower() for keyword in non_functional_keywords):
        return "Non-Functional"
    else:
        return "Uncategorized"

def explain_classification(requirement, category):
    if category == "Functional":
        return f"This describes what the system should do. For example, '{requirement}' specifies a feature or action the system enables."
    elif category == "Non-Functional":
        return f"This describes how the system should behave. For instance, '{requirement}' defines a quality attribute or constraint."
    else:
        return "This requirement is unclear or does not fall into functional or non-functional categories."

# Streamlit App
st.title("Requirements Separator and Explainator")

# Input Requirements
st.markdown("Enter your list of requirements, one per line:")
requirements_input = st.text_area("Requirements", placeholder="E.g., Allow users to log in securely\nEnsure the system is scalable")

if st.button("Process Requirements"):
    if requirements_input.strip():
        with st.spinner("Processing..."):
            # Split requirements into lines
            requirements = requirements_input.strip().split("\n")
            results = []

            for req in requirements:
                category = classify_requirement(req)
                explanation = explain_classification(req, category)
                results.append((req, category, explanation))

            # Display Results
            st.markdown("### Categorized and Explained Requirements")
            for req, category, explanation in results:
                st.markdown(f"**Requirement**: {req}")
                st.markdown(f"**Category**: {category}")
                st.markdown(f"**Explanation**: {explanation}")
                st.markdown("---")
    else:
        st.error("Please enter at least one requirement.")