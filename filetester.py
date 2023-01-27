import openai

API_KEY = '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'
openai.api_key = API_KEY

model = 'text-davinci-003'

# User input of the query as well as attaching the file containing the code
prompt = input('Enter your query explaining the problem: ') + '\n'
filename = input('Enter the name of the file you wish to submit: ')

# Reading the specified file and adding the contents to the query
f = open(filename)
prompt += f.read()
f.close()

# Generating a response from OpenAI
response = openai.Completion.create(
    prompt = prompt,
    model = model,
    max_tokens=1000,
    temperature=0.7,
    n=1
) 

# Prints the response along with the used tokens to the terminal
for result in response.choices:
    print(result.text)
    print('\n\nEND OF RESPONSE\n\n')
print(response.usage)
