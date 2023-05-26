# Guidance Agent Eval 

This is a fork of https://github.com/QuangBK/localLLM_guidance/ with added models and example agents.

Standard prompt is a blank guidance prompt so you can design your own agent.
Once you are satisified, you can create an agent file in the 'server' folder. 
You can start by copying the UniversalMarkdown agent and adding your prompt.

Generally speaking the input variables are "query" (the input box) and "resolver" (the output box) if your agent has a guidance resolver variable.

How to run
- Download the models. For now, they are hard coded in ./app.py and you will need to change them to your local path.
- Set your models home directory in app.py
```
MODEL_DIRECTORY = "/home/shazam"
```
- Run the server

Optionally: Install GPTQ-for-LLaMA following the Oobabooga instructions
https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md
At this time, they are using a forked version of GPTQ-for-LLaMA. Please pay special attention to the instructions above.


## Run 

`python3 app.py`

Goto http://localhost:7860/

## Example agents

"StandardPrompt", "COTpromptBuilder", "COTpromptBuilder2PromptResponse", "AIDecisionMakerSimulator", "SearchToolAgentPOC", "AgentGuidanceSmartGPT", "ChatGPTAgentGuidance", "AgentGuidanceFlowGPT", "UniversalAnythingToJSON", "UniversalAnythingToMarkdown"]

- StandardPrompt is a blank guidance prompt so you can design your own agent.
- COTpromptBuilder is based on Connect multiple ChatGPT sessions w/ dynamic ChatGPT prompts https://www.youtube.com/watch?v=8PbpFxPibJM
- COTpromptBuilder2PromptResponse is the above, but the resolver is the result.
- AIDecisionMakerSimulator is an experimental simple agent that uses a decision tree to make a decision.  Based on Henky!! from KoboaldAI and crew. 
- SearchToolAgentPOC is an experimental agent that uses a search tool to find the answer.  NOTE: GoogleSerp is disabled and instead I am using SearX.  It must be installed. I use the docker version. https://python.langchain.com/en/latest/reference/modules/searx_search.html?highlight=searx
- AgentGuidanceSmartGPT is based on another youtube video by code4AI https://www.youtube.com/@code4AI
- ChatGPTAgentGuidance is just an example of using ChatML with guidance
- AgentGuidanceFlowGPT is an attempt to use FlowGPT Proteus
- UniversalAnythingToJSON converts anything (!) to JSON
- UniversalAnythingToMarkdown converts anything (including JSON) to Markdown



-----


Original readme:

# Makea simple agent with Guidance and local LLMs
The [Guidance](https://github.com/microsoft/guidance) is a tool for controlling LLM. It provides a good concept to build prompt templates. This repository shows you how to make a agent with Guidance. You can combine it with various LLMs in Huggingface. My [medium article](https://medium.com/@gartist/a-simple-agent-with-guidance-and-local-llm-c0865c97eaa9) for more explanation.

UPDATE: Added gradio UI.

# Install
Python packages:
- [guidance](https://github.com/microsoft/guidance)
- [GPTQ-for-LLaMa](https://github.com/oobabooga/GPTQ-for-LLaMa.git)
- [langchain](https://github.com/hwchase17/langchain)
- [gradio](https://github.com/gradio-app/gradio) (Only for web UI)

Note: we only use langchain for build the `GoogleSerper` tool. The agent itself is built only by Guidance. Feel free to change/add/modify the tools with your goal.
The GPTQ-for-LLaMa I used is the oobabooga's fork. You can install it with [this command](https://github.com/oobabooga/text-generation-webui/blob/main/docs/GPTQ-models-(4-bit-mode).md#step-1-install-gptq-for-llama).

# Run
There are two options: run a Gradio server with UI and run the notebook file.

## Gradio server
Please modify the `SERPER_API_KEY`, `MODEL_PATH`, `CHECKPOINT_PATH` in the app.py and run:
```sh
gradio app.py
```

## Notebook
Please check the [notebook file]((https://github.com/QuangBK/localLLM_guidance/blob/main/demo_ReAct.ipynb)). You should have a free SERPER API KEY and a LLM model to run this.
I use the [wizard-mega-13B-GPTQ](https://huggingface.co/TheBloke/wizard-mega-13B-GPTQ) model. Feel free to try others.

# Example
![alt text](https://github.com/QuangBK/localLLM_guidance/blob/main/gradio.png?raw=true)


TODO 
https://github.com/hwchase17/langchain/tree/9231143f91863ffbe0542bc69a90b723a40e165d/langchain/experimental/plan_and_execute

