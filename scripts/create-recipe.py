import sys
import os
import re
import argparse
import json
from openai import OpenAI
from datetime import datetime

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Ensure your OpenAI API key is set in your environment

def load_file_contents(file_path):
    absolute_path = os.path.abspath(file_path)
    try:
        with open(absolute_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {absolute_path}: {e}", file=sys.stderr)
        sys.exit(1)

def append_recipe_name(contents, recipe_name):
    return f"{contents}\n\n{recipe_name}"

def sanitize_filename(recipe_name):
    sanitized_name = re.sub(r'[^a-zA-Z0-9-]', '-', recipe_name.lower())
    return f"{sanitized_name}.json"

def write_to_file(output_directory, filename, content):
    absolute_output_directory = os.path.abspath(output_directory)
    if not os.path.exists(absolute_output_directory):
        os.makedirs(absolute_output_directory)

    output_path = os.path.join(absolute_output_directory, filename)

    try:
        with open(output_path, 'w') as file:
            json.dump(content, file, indent=4)
        print(f"Output written to {output_path}")
    except Exception as e:
        print(f"Error writing to file {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

def make_openai_request(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error making request to OpenAI: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Append recipe name to the contents of a markdown file and make a request to OpenAI.")
    parser.add_argument("file_path", help="The path to the markdown file.")
    parser.add_argument("recipe_name", help="The name of the recipe.")
    parser.add_argument("-o", "--output", help="The directory to save the output file.")
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print(f"The file {args.file_path} does not exist.", file=sys.stderr)
        sys.exit(1)

    contents = load_file_contents(args.file_path)
    prompt = append_recipe_name(contents, args.recipe_name)

    response_content = make_openai_request(prompt)
    json_content = json.loads(response_content)

    if args.output:
        filename = sanitize_filename(args.recipe_name)
        write_to_file(args.output, filename, json_content)
    else:
        print(json_content)
