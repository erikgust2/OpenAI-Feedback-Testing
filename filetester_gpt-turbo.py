import os
import openai
import time

# Measures the time taken to run the program
start_time = time.time()

# Name of the output file. Change this to whatever you want.
outputFileName = 'output_turbo.txt'

# Gets OpenAI API key from api.txt
# NOTE: YOU HAVE TO MANUALLY ADD THIS TEXTFILE WITH YOUR OWN KEY
f = open('apikey.txt')
API_KEY = f.read()
f.close()
openai.api_key = API_KEY

# Enter the language model you wish to use. Default is GPT-3.5 Turbo
model = 'gpt-3.5-turbo'

# Edit these to change the categories of the query
categories = ['AgeName', 'Average', 'BMI', 'Factorial', 'Fahrenheit', 'MergeSorted', 'Prime', 'Sorting', 'Sum', 'Triangle']

# Creates the output file
outputFile = open(outputFileName, 'w')

# Prompts OPENAI to generate a response for each python file in each category
for category in categories:

    # Writes the category name to the output file to signify a new category
    outputFile.write('Category: ' + category + '\n\n')

    # Writes the description of the prompt to the output file
    descriptionFile = open('dataset/' + category + '/' + category + '_description.txt')
    description = descriptionFile.read() + '\n\n'
    descriptionFile.close()

    # Iterates through each file in the category
    for file in os.listdir('dataset/' + category):

        # Ignores the description file
        if file.endswith('.py'):

            # Writes the file name to the output file to signify a new file
            outputFile.write(file + '\n\n')
            f = open('dataset/' + category + '/' + file)

            # Generates the prompt
            prompt = description + ' If you find any errors, explain why they inhibit correct functionality.' + f.read()
            f.close()

            # Generating a response from OpenAI
            response = openai.ChatCompletion.create(
                model = model,
                messages = [
                    {'role': 'system', 'content': 'You are a helpful programming instructor for beginners.'},
                    {'role': 'user', 'content': prompt}
                ]
            )

            # Writes the response to the output file
            for choice in response.choices:
                outputFile.write(choice.message.content + '\n\n' + '------------------------' + '\n\n')

outputFile.close()

print("Done! Output written to " + outputFileName + ".")

print("Time taken: " + str(time.time() - start_time) + " seconds")