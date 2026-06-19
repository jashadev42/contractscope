import string

CANONICAL_COMPANIES = {
    "leidos": "Leidos",
    "booz": "Booz Allen Hamilton",
    "saic": "SAIC",
    "caci": "CACI",
    "mantech": "ManTech",
    "northrop": "Northrop Grumman",
    "parsons": "Parsons",
}

def canonical_recipient(name: str) -> str:
    cleaned = name.lower().translate(str.maketrans("", "", string.punctuation))
    words = cleaned.split()

    for keyword, canonical in CANONICAL_COMPANIES.items():
        if keyword in words:
            return canonical
    return "Other"
