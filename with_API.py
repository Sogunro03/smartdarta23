from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge Graph
knowledge_graph = {
    "JohnDoe": {"name": "John Doe", "age": 30, "occupation": "Engineer"},
    "NewYork": {"name": "New York", "population": 8000000, "location": "USA"}
}

# intents and corresponding SPARQL query templates
intents = {
    "PersonInfo": "Tell me about <person>",
    "LocationInfo": "What is known about <location>"
}

sparql_templates = {
    "PersonInfo": "SELECT ?property WHERE { <person> ?property ?value }",
    "LocationInfo": "SELECT ?property WHERE { <location> ?property ?value }"
}

# NLU API endpoint
@app.route('/nlu', methods=['POST'])
def nlu():
    try:
        data = request.get_json()
        user_query = data.get('query')
        intent, entities = process_query(user_query)

        if intent:
            sparql_query = generate_sparql(intent, entities)
            return jsonify({"intent": intent, "entities": entities, "sparql_query": sparql_query})
        else:
            return jsonify({"error": "Intent identification failed."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Function to identify intent and extract entities
def process_query(user_query):
    for intent, pattern in intents.items():
        match = re.match(pattern.replace("<", "(.*)").replace(">", "(.*)"), user_query)
        if match:
            entities = [entity.strip() for entity in match.groups() if entity is not None]
            return intent, entities
    return None, []

# Function to generate SPARQL query
def generate_sparql(intent, entities):
    template = sparql_templates.get(intent)
    if template:
        sparql_query = template
        for entity in entities:
            sparql_query = sparql_query.replace(f"<{entity}>", entity)
        return sparql_query
    return None

if __name__ == '__main__':
    app.run(debug=True)
