import os
import json
import pandas as pd
from typing import Dict, List


def get_crating_recipes(folder: str) -> List[Dict[str, str]]:
    """Return all recipes found in `folder` that are crafting related

    Args:
        folder (str): the folder to search

    Returns:
        List[Dict[str, str]]: the list of recipes
    """
    recipes = []
    for recipe_file in os.listdir('recipes'):
        with open(folder + '\\' + recipe_file) as file:
            recipe_json = json.loads(file.read())

            if 'crafting' not in recipe_json['type']:
                continue

            recipes.append(recipe_json)

    return recipes


def create_dataset(filename: str):
    """Create a dataset file with `filename`

    Args:
        filename (str): the filename to save the dataset
    """
    drop_columns = ['category', 'group', 'show_notification']

    df = pd.DataFrame.from_records(get_crating_recipes('recipes'))
    df = df.drop(drop_columns, axis=1)

    df.to_csv(filename, index=False)
