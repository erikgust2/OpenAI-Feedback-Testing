# OpenAI-Feedback-Testing
This repository contains all data and scripts related to our bachelor's thesis in Computer Science at Stockholm University

## Dataset
This folder contains all manually written python scripts that comprises the dataset used in the experiment. Each subfolder contains all scripts related to one assignment.

## Results
- Results.xlsx contains the tables for each model, showing a comprehensive overview of each variant's results.
- ResultsTwo.xlsx contains tables for each category of error split between the models, showing how they compare.

## Filetester
These three files contain python scripts that construct prompts and send them to OpenAI. To be able to use them, you need to have the OpenAI package installed. Instructions for how to do that can be found [here](https://pypi.org/project/openai/).
- filetester_automatic.py tests the entire dataset using GPT-3 and sends the results to output.txt.
- filetester_commandline.py lets you send a single prompt with the file of your choice.
- filetester_gpt-turbo.py tests the entire dataset using GPT-3.5 and sends the results to output_turbo.txt.

## Output
- output.txt shows the replies from GPT-3 for each prompt, separated with a line of dashes.
- output_turbo.txt shows the replies from GPT-3.5 in the same way.

## Solutions
- solutions.txt contains a list of the errors intentionally added to the files in the dataset.
