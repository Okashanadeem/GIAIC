# Prompt and Context Engineering

What is a Prompt?
it is the art of crafting instructionsthat that guides Ai language models to produce desired output.

Prompt Engineering & Context Engineering:
The instruction which you give the model are prompts and the context is the infprmation which model can see when following the instruction.

## Fundamentals of Prompting Techniques:

- Zero-Shot Prompting:
it is the simplest approach which is just asking or giving the task without any example.
- One-Shot Example:
it is where we provide a single example with our prompt which LLM will use while generating our output.
- Few-Shots Example:
as like the above we have more than one example which we give to the prompt.

We have 2 types of prompting. User prompt which user give to the LLM and next one is System prompt which is the instruction which we give to the Agent while we are making it. these instructions can e the oevr all context and the behavioral guidelines.

###  Role Prompting:
it is a type of prompt where we tell our agent that how it should act. 
etc
- Act as an Experienced Software Enginerr ...

### Contextual Prompting:
it is where we provide background information relevant to the task.


## Advanced Prompting Strategies.

### Chain of Thoughts (COT):
it is the procedure that LLM will implement while writing the output. this means that LLM will perform the task step by step 

- Self-Consistancy:
ask the same question continously and choose the most perfect output by comparing it with other responses
- Step-Back Prompting:
ask a general question first then use that as the context for the real task that you will ask after that general question.
- ReAct (Reasoning + Acting):
it is where the agent will reason about the task and then act on it or use a tool.

### Tree of Thoughts (TOT):
