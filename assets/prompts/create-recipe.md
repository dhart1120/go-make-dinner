You will be provided with the name of a recipe. You should create a single recipe (one JSON object) in a valid JSON format based on the following instructions and context. So not include any additional summary, notes, or anything that would make the JSON file invalid. The response should start with `{` and end with `}`

**Goal:**
Generate a comprehensive, user-friendly collection of recipes that align with the specified nutritional goals. Each recipe should be clear, easy to follow, and provide all necessary details, including ingredients, instructions, and nutritional information. The aim is to create recipes that are nutritious, balanced, and appealing, suitable for various meals such as breakfast, lunch, dinner, and snacks.

**Nutritional Goals and Context:**

**Personal Nutritional Goals:**
1. **Body Recomposition:** Focus on a balanced diet that supports fat loss while maintaining or building lean muscle mass.
2. **Macronutrient Distribution:** Aim for a daily intake of approximately:
   - 35% of calories from fat
   - 30% of calories from protein
   - 35% of calories carbohydrates
   It's not expected that the meals will perfectly fit this ratio because it will the the total of all the meals and food eaten during the day.
3. **High Protein Intake:** Ensure meals are rich in protein to support muscle repair and growth, especially post-workout.
4. **Balanced Macronutrients:** Maintain a balanced intake of fats and carbohydrates to provide sustained energy throughout the day and support overall health.
5. **Nutrient-Dense Foods:** Incorporate a variety of whole, minimally processed foods to ensure adequate intake of vitamins, minerals, and other essential nutrients.

**Context:**
1. **Active Lifestyle:** Engage in regular physical activity, including strength training and cardiovascular exercises, necessitating a diet that supports energy needs and muscle recovery.
2. **Health and Wellness:** Prioritize overall health by choosing nutrient-dense foods that support immune function, digestive health, and cardiovascular health.
3. **Convenience and Accessibility:** Create meals that are not only nutritious but also easy to prepare and incorporate into a busy lifestyle.
4. **Flavor and Enjoyment:** Ensure meals are flavorful and enjoyable to maintain long-term adherence to the nutritional plan.
5. **Dietary Preferences and Restrictions:** Consider any personal dietary preferences or restrictions (e.g., gluten-free, dairy-free) when selecting ingredients and planning meals if asked.


**Recipe Format:**
Each recipe should follow a standardized format to ensure consistency. The format includes the following sections:

1. **Recipe Name:**
   - Clearly state the name of the recipe.

2. **Ingredients:**
   - List all ingredients with precise quantities, units of measurement, and names. Use float values for clear measurements (e.g., 0.25, 0.50) and fractions when necessary for readability (e.g., 1/3).
   - Example:
     ```json
     "ingredients": [
       {
         "quantity": "1",
         "unit": "cup",
         "name": "Greek yogurt"
       },
       {
         "quantity": "0.5",
         "unit": "cup",
         "name": "mixed berries"
       },
       {
         "quantity": "0.25",
         "unit": "cup",
         "name": "granola"
       }
     ]
     ```

3. **Instructions:**
   - Provide detailed, step-by-step instructions for preparing the meal. Ensure clarity and simplicity, making it easy for users to follow.
   - Example:
     ```json
     "instructions": [
       "Place Greek yogurt in a bowl.",
       "Top with mixed berries and granola.",
       "Serve immediately."
     ]
     ```

4. **Nutrition Ratio:**
   - Include a nutrition ratio object that specifies the amounts of fat, carbohydrates, and protein in the meal. Use multiples of 5 or 10 for clarity, and fall back to two being multiples while the third varies if necessary.
   - Example:
     ```json
     "nutrition_ratio": {
       "fat": 10,
       "carbs": 20,
       "protein": 15
     }
     ```

5. **Description:**
   - Add a brief description of the meal, highlighting its key attributes, flavor profile, and nutritional benefits. Mention if it's suitable for specific dietary needs (e.g., gluten-free, high-protein).

6. **Cooking Time:**
   - Indicate the total cooking time required, including preparation and cooking.

7. **Serving Size:**
   - Specify the number of servings the recipe yields.

8. **Additional Notes:**
   - Provide any additional notes or tips for preparing the meal, including possible ingredient substitutions, storage tips, or variations.

**Example Recipe:**

**Recipe Name:** Greek Yogurt with Berries and Granola

**Ingredients:**
```json
"ingredients": [
  {
    "quantity": "1",
    "unit": "cup",
    "name": "Greek yogurt"
  },
  {
    "quantity": "0.5",
    "unit": "cup",
    "name": "mixed berries"
  },
  {
    "quantity": "0.25",
    "unit": "cup",
    "name": "granola"
  }
]
```

**Instructions:**
```json
"instructions": [
  "Place Greek yogurt in a bowl.",
  "Top with mixed berries and granola.",
  "Serve immediately."
]
```

**Nutrition Ratio:**
```json
"nutrition_ratio": {
  "fat": 10,
  "carbs": 20,
  "protein": 15
}
```

**Description:**
A delicious and nutritious breakfast option featuring creamy Greek yogurt, fresh mixed berries, and crunchy granola. Perfect for a quick and healthy start to your day.

**Cooking Time:**
5 minutes

**Serving Size:**
1 serving

**Additional Notes:**
Feel free to substitute the granola with nuts or seeds for added crunch and nutrition. You can also use different types of berries based on seasonal availability.

**Instructions:**
By adhering to this format, the generated recipes will be consistent, easy to follow, and informative, ensuring a positive user experience and helping users achieve their nutritional goals.

**Examples:**
Sure, here is the schema with two examples for each meal type, formatted with valid JSON. Do not include additional fields that are not defined in the schema.

### JSON Schema

```json
{
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The name of the meal."
        },
        "ingredients": {
            "type": "array",
            "description": "A list of ingredients required for the meal.",
            "items": {
                "type": "object",
                "properties": {
                    "quantity": {
                        "type": "string",
                        "description": "The quantity of the ingredient needed, in float or fraction."
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit of measurement for the ingredient (e.g., ounces, cups, tablespoons)."
                    },
                    "name": {
                        "type": "string",
                        "description": "The name of the ingredient."
                    }
                },
                "required": ["quantity", "unit", "name"]
            }
        },
        "instructions": {
            "type": "array",
            "description": "Step-by-step instructions for preparing the meal.",
            "items": {
                "type": "string",
                "description": "A single step in the meal preparation process."
            }
        },
        "nutrition_ratio": {
            "type": "object",
            "description": "The nutritional ratio of the meal, indicating the amounts of fat, carbohydrates, and protein.",
            "properties": {
                "fat": {
                    "type": "number",
                    "description": "The amount of fat in the meal, ideally in a multiple of 5 or 10."
                },
                "carbs": {
                    "type": "number",
                    "description": "The amount of carbohydrates in the meal, ideally in a multiple of 5 or 10."
                },
                "protein": {
                    "type": "number",
                    "description": "The amount of protein in the meal, ideally in a multiple of 5 or 10."
                }
            },
            "required": ["fat", "carbs", "protein"]
        }
    },
    "required": ["name", "ingredients", "instructions", "nutrition_ratio"]
}
```

### Breakfast Examples

```json
[
    {
        "name": "Greek Yogurt with Berries and Granola",
        "ingredients": [
            {
                "quantity": "1",
                "unit": "cup",
                "name": "Greek yogurt"
            },
            {
                "quantity": "0.5",
                "unit": "cup",
                "name": "mixed berries"
            },
            {
                "quantity": "0.25",
                "unit": "cup",
                "name": "granola"
            }
        ],
        "instructions": [
            "Place Greek yogurt in a bowl.",
            "Top with mixed berries and granola.",
            "Serve immediately."
        ],
        "nutrition_ratio": {
            "fat": 10,
            "carbs": 20,
            "protein": 15
        }
    },
    {
        "name": "Protein Pancakes with Fresh Fruit",
        "ingredients": [
            {
                "quantity": "1",
                "unit": "cup",
                "name": "pancake mix"
            },
            {
                "quantity": "1",
                "unit": "scoop",
                "name": "protein powder"
            },
            {
                "quantity": "1",
                "unit": "each",
                "name": "egg"
            },
            {
                "quantity": "0.5",
                "unit": "cup",
                "name": "Greek yogurt"
            },
            {
                "quantity": "0.5",
                "unit": "cup",
                "name": "water"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "fresh fruit"
            }
        ],
        "instructions": [
            "Mix pancake mix, protein powder, egg, Greek yogurt, and water in a bowl until smooth.",
            "Cook on a non-stick griddle over medium heat until bubbles form, then flip and cook until golden brown.",
            "Serve with fresh fruit on top."
        ],
        "nutrition_ratio": {
            "fat": 5,
            "carbs": 30,
            "protein": 20
        }
    }
]
```

### Lunch Examples

```json
[
    {
        "name": "Chicken Caesar Salad Wrap",
        "ingredients": [
            {
                "quantity": "6",
                "unit": "ounces",
                "name": "grilled chicken breast"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "romaine lettuce"
            },
            {
                "quantity": "2",
                "unit": "tablespoons",
                "name": "Caesar dressing"
            },
            {
                "quantity": "1",
                "unit": "tablespoon",
                "name": "Parmesan cheese"
            },
            {
                "quantity": "1",
                "unit": "each",
                "name": "whole grain wrap"
            }
        ],
        "instructions": [
            "Slice the grilled chicken breast.",
            "Toss the romaine lettuce with Caesar dressing and Parmesan cheese.",
            "Lay the wrap flat and place the lettuce mixture and chicken slices on top.",
            "Roll up the wrap tightly and slice in half to serve."
        ],
        "nutrition_ratio": {
            "fat": 15,
            "carbs": 25,
            "protein": 30
        }
    },
    {
        "name": "Lemon Herb Quinoa Salad",
        "ingredients": [
            {
                "quantity": "1",
                "unit": "cup",
                "name": "quinoa"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "cherry tomatoes"
            },
            {
                "quantity": "0.5",
                "unit": "cup",
                "name": "cucumber"
            },
            {
                "quantity": "0.25",
                "unit": "cup",
                "name": "feta cheese"
            },
            {
                "quantity": "2",
                "unit": "tablespoons",
                "name": "olive oil"
            },
            {
                "quantity": "1",
                "unit": "each",
                "name": "lemon"
            },
            {
                "quantity": "1",
                "unit": "tablespoon",
                "name": "fresh parsley"
            }
        ],
        "instructions": [
            "Cook the quinoa according to package instructions and let it cool.",
            "Halve the cherry tomatoes and dice the cucumber.",
            "In a large bowl, combine the quinoa, cherry tomatoes, cucumber, and feta cheese.",
            "In a small bowl, whisk together the olive oil, juice of the lemon, and chopped parsley to make the dressing.",
            "Pour the dressing over the salad and toss to combine."
        ],
        "nutrition_ratio": {
            "fat": 20,
            "carbs": 50,
            "protein": 15
        }
    }
]
```

### Dinner Examples

```json
[
    {
        "name": "Beef Stroganoff with Whole Grain Noodles",
        "ingredients": [
            {
                "quantity": "8",
                "unit": "ounces",
                "name": "beef sirloin"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "mushrooms"
            },
            {
                "quantity": "1",
                "unit": "each",
                "name": "onion"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "beef broth"
            },
            {
                "quantity": "0.5",
                "unit": "cup",
                "name": "sour cream"
            },
            {
                "quantity": "1",
                "unit": "tablespoon",
                "name": "flour"
            },
            {
                "quantity": "2",
                "unit": "cups",
                "name": "whole grain noodles"
            }
        ],
        "instructions": [
            "Cook the whole grain noodles according to package instructions.",
            "Slice the beef sirloin into thin strips.",
            "In a large skillet, cook the beef over medium-high heat until browned, then remove from skillet.",
            "Add sliced mushrooms and chopped onion to the skillet, cooking until tender.",
            "Stir in the flour and cook for 1 minute.",
            "Gradually add the beef broth, stirring until thickened.",
            "Return the beef to the skillet and stir in the sour cream.",
            "Serve the beef stroganoff over the cooked noodles."
        ],
        "nutrition_ratio": {
            "fat": 20,
            "carbs": 40,
            "protein": 30
        }
    },
    {
        "name": "Baked Tilapia with Green Beans and Rice",
        "ingredients": [
            {
                "quantity": "7",
                "unit": "ounces",
                "name": "tilapia fillet"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "green beans"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "white rice"
            },
            {
                "quantity": "1",
                "unit": "tablespoon",
                "name": "olive oil"
            },
            {
                "quantity": "1",
                "unit": "teaspoon",
                "name": "lemon pepper seasoning"
            }
        ],
        "instructions": [
            "Preheat the oven to 375°F (190°C).",
            "Season the tilapia fillet with lemon pepper seasoning.",
            "Place the tilapia on a baking sheet and drizzle with olive oil.",
            "Bake for 20 minutes or until the fish is cooked through.",
            "Cook the white rice according to package instructions.",
            "Steam the green beans until tender.",
            "Serve the baked tilapia with green beans and white rice."
        ],
        "nutrition_ratio": {
            "fat": 10,
            "carbs": 45,
            "protein": 30
        }
    }
]
```

### Snack Examples

```json
[
    {
        "name": "Greek Yogurt with Honey and Almonds",
        "ingredients": [
            {
                "quantity": "1",
                "unit": "cup",
                "name": "Greek yogurt"
            },
            {
                "quantity": "1",
                "unit": "tablespoon",
                "name": "honey"
            },
            {
                "quantity": "2",
                "unit": "tablespoons",
                "name": "sliced almonds"
            }
        ],
        "instructions": [
            "Place Greek yogurt in a bowl.",
            "Drizzle honey over the yogurt.",
            "Sprinkle sliced almonds on top.",
            "Serve immediately."
        ],
        "nutrition_ratio": {
            "fat": 15,
            "carbs": 10,
            "protein": 20
        }
    },
    {
        "name": "Carrot Sticks with Hummus",
        "ingredients": [
            {
                "quantity": "2",
                "unit": "each",
                "name": "carrots"
            },
            {
                "quantity": "1",
                "unit": "cup",
                "name": "hummus"
            }
        ],
        "instructions": [
            "Wash and peel the carrots.",
            "Cut the carrots into sticks.",
            "Place the carrot sticks on a plate.",
            "Serve with a cup of hummus for dipping."
        ],
        "nutrition_ratio": {
            "fat": 10,
            "carbs": 30,
            "protein": 10
        }
    }
]
```

The name of the recipe that you should generate is:
