#Task :# 

The aim is to develop a natural understanding module that uses LLMs to identify the intent of a user, extract entities from the utterance and link it to the entities in a given knowledge graph when possible. Then, generate SPARQL queries based on the extracted intent. A knowledge graph and example intents will be provided to be used as examples while prompting the LLM.

##Prerequisites:##

###Install Flask: pip install Flask


###NLU API Result:###

{
  "intent": "PersonInfo",
  "entities": ["John Doe"],
  "sparql_query": "SELECT ?property WHERE { John Doe ?property ?value }"
}


###Knowledge Graph API Result:###

{
  "John Doe": {
    "name": "John Doe",
    "age": 30,
    "occupation": "Engineer"
  }
}


###Final User Interaction Result:###

NLU Result: {'intent': 'PersonInfo', 'entities': ['John Doe'], 'sparql_query': 'SELECT ?property WHERE { John Doe ?property ?value }'}
Knowledge Graph Result: {'John Doe': {'name': 'John Doe', 'age': 30, 'occupation': 'Engineer'}}



