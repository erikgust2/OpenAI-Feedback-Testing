import os
import openai

outputFileName = 'output.txt'

# Gets OpenAI API key from api.txt
# NOTE: YOU HAVE TO MANUALLY ADD THIS TEXTFILE WITH YOUR OWN KEY
f = open('apikey.txt')
API_KEY = f.read()
f.close()
openai.api_key = API_KEY

# Enter the language model you wish to use. Default is the latest and most complicated model - DaVinci
model = 'text-davinci-003'

# Edit these to change the categories of the query
categories = ['BMI', 'Fahrenheit', 'Sorting']

outputFile = open(outputFileName, 'w')

# Iterates through each category
for category in categories:

    outputFile.write('Category: ' + category + '\n\n')

    descriptionFile = open('dataset/' + category + '/' + category + '_description.txt')
    description = descriptionFile.read() + '\n\n'
    descriptionFile.close()

    for file in os.listdir('dataset/' + category):

        if file.endswith('.py'):
            outputFile.write(file + '\n\n')
            f = open('dataset/' + category + '/' + file)
            prompt = description + f.read()
            f.close()

            # Generating a response from OpenAI
            response = openai.Completion.create(
                prompt = prompt,
                model = model,
                max_tokens=1000,
                temperature=0.7,
                n=1
            )
            
            # outputFile.write(prompt + '\n\n' + '------------------------' + '\n\n')

            for choice in response.choices:
                outputFile.write(choice.text + '\n\n' + '------------------------' + '\n\n')

outputFile.close()

print("Done! Output written to " + outputFileName + ".")