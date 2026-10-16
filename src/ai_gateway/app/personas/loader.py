import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
PERSONA_DIR = Path(__file__).parent / "config"


def load_persona(persona_id : str) :
    path  = PERSONA_DIR / f"{persona_id}.json"
    if not path.is_file():
        logging.info(f"Persona not found with name {persona_id}.json")
        raise FileNotFoundError(
            f'file not found with persona {persona_id}'
        )
    logging.info(f"Persona found with name {persona_id}.json")
    with path.open('r', encoding='utf-8') as f:
        persona = json.load(f)

    return persona