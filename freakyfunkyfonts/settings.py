import os
import tomllib  # Python 3.11+; for older use `tomli`

DEFAULTS = {
    "fonts": {
        "pool": ["Arial", "Courier New", "Times New Roman", "Verdana", "Comic Sans MS"],
    },
    "inject": {
        "google_fonts_link": None,
    },
    "behaviour": {
        "skip_tags": ['head', 'title', 'meta', 'link', 'style', 'script'],
        "scope": ["body", "main", "article"]
    },
    "temporal_ranges": {
        "include": [],  # e.g. ["08:00-18:00"]
        "exclude": []  # e.g. ["23:00-01:00"]
    },
    "date_ranges": {
        "include": [],  # e.g. [{"range": "2025-10-01:2025-10-10", "temporal": ["08:00-18:00"]}]
        "exclude": []  # e.g. [{"range": "2025-12-24:2025-12-26", "temporal": ["00:00-23:59"]}]
    },
}

def load_config():
    path = os.path.join(os.getcwd(), "freakyfunkyfonts.toml")
    config = DEFAULTS.copy()
    if os.path.exists(path):
        with open(path, "rb") as f:
            user_conf = tomllib.load(f)
            # deep merge
            for section, values in user_conf.items():
                config[section].update(values)
    return config
