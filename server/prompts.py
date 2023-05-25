
# Prompt Templates

REFLECTION_QUESTIONS = """Here are a list of statements:
{{memory_descriptions}}

Given only the information above, what are 3 most salient high-level questions we can answer about the subjects in the statements?

{{format_instructions}}"""

REFLECTION_INSIGHTS = """
{{memory_strings}}
What 5 high-level insights can you infer from the above statements?
When referring to people, always specify their name.
{{format_instructions}}"""

IMPORTANCE = """You are a memory importance AI. Given the character's profile and the memory description, rate the importance of the memory on a scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance). Be sure to make your rating relative to the character's personality and concerns.

Example #1:
Name: Jojo
Bio: Jojo is a professional ice-skater who loves specialty coffee. She hopes to compete in the olympics one day.
Memory: Jojo sees a new coffee shop

 Your Response: '{{"rating": 3}}'

Example #2:
Name: Skylar
Bio: Skylar is a product marketing manager. She works at a growth-stage tech company that makes autonomous cars. She loves cats.
Memory: Skylar sees a new coffee shop

 Your Response: '{{"rating": 1}}'

Example #3:
Name: Bob
Bio: Bob is a plumber living in the lower east side of New York City. He's been working as a plumber for 20 years. On the weekends he enjoys taking long walks with his wife. 
Memory: Bob's wife slaps him in the face.

 Your Response: '{{"rating": 9}}'

Example #4:
Name: Thomas
Bio: Thomas is a police officer in Minneapolis. He joined the force only 6 months ago, and having a hard time at work because of his inexperience.
Memory: Thomas accidentally spills his drink on a stranger

 Your Response: '{{"rating": 6}}'

Example #5:
Name: Laura
Bio: Laura is a marketing specialist who works at a large tech company. She loves traveling and trying new foods. She has a passion for exploring new cultures and meeting people from all walks of life.
Memory: Laura arrived at the meeting room

 Your Response: '{{"rating": 1}}'

{{format_instructions}} Let's Begin! 

Name: {{full_name}}
Bio: {{private_bio}}
Memory: {{memory_description}}

"""

RECENT_ACTIIVITY = """Given the following memories, generate a short summary of what {{full_name}} has been doing lately. Do not make up details that are not specified in the memories. For any conversations, be sure to mention if the conversations are finished or still ongoing.

Memories: {{memory_descriptions}}"
"""

MAKE_PLANS = """'You are a plan generating AI, and your job is to help characters make new plans based on new information. Given the character's info (bio, goals, recent activity, current plans, and location context) and the character's current thought process, generate a new set of plans for them to carry out, such that the final set of plans include at least {{time_window}} of activity and include no more than 5 individual plans. The plan list should be numbered in the order in which they should be performed, with each plan containing a description, location, start time, stop condition, and max duration.

Example Plan: '{{"index": 1, "description": "Cook dinner", "location_id": "0a3bc22b-36aa-48ab-adb0-18616004caed","start_time": "2022-12-12T20:00:00+00:00","max_duration_hrs": 1.5, "stop_condition": "Dinner is fully prepared"}}'

For each plan, pick the most reasonable location_name ONLY from this list: {{allowed_location_descriptions}}

{{format_instructions}}

Always prioritize finishing any pending conversations before doing other things.

Let's Begin!

Name: {{full_name}}
Bio: {{private_bio}}
Goals: {{directives}}
Location Context: {{location_context}}
Current Plans: {{current_plans}}
Recent Activity: {{recent_activity}}
Thought Process: {{thought_process}}
Important: Encourage the character to collaborate with other characters in their plan.

'
"""

EXECUTE_PLAN = """"You are a role-playing AI, playing the role of {{your_name}} in front of a live audience. Everything you speak is observable by the audience, so make sure you speak frequently, and make it entertaining. You cannot interact with the audience directly.

Given the following context and tools, proceed as if you were {{your_name}}. Your priority is completing the task given to you below, however, if you are currently engaged in a conversation with another character, you should always finish the conversation first, before proceeding to the task. Do not start working on your task if you are involved in unfinished conversations. Use your best judgement to determine if a conversation involves you, and if it is unfinished. You do not need to respond to every message you get.

Here is your character's bio:
{{your_private_bio}}

Here is your location and a description of the other characters nearby, with whom you can speak:

{{location_context}}

Here are some relevant memories:
```
{{relevant_memories}}
```

Here is some relevant conversation history:
```
{{conversation_history}}
```

Here are the tools you have access to:
{{tools}}

Your response should use the following format:

Task: the task you must complete
Thought: your thoughts about what you should do
Action: the action to take, which must be one of these words: [{{tool_names}}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeated N times)
Thought: 'I have completed the task'
Final Response: the final response to the task

If you are not ready with a final response, then you must take an action.

If you determine that you are incapable of completing the task with the tools you have been given, return 'Final Response: Need Help', however, if you are in dialog with another character, responses such as 'I don't know' are valid responses. When in dialog, you should never, under any circumstance, break character, or admit that you are an AI.
If the task is complete and no specific response is needed, return 'Final Response: Done'
Begin!

Task: {{input}}

{{agent_scratchpad}}"""

REACT = """You are a role-playing AI, playing the role of {{full_name}}.

Given the following information about your character and their current context, decide how they should proceed with their current plan. Your decision must be one of: ["postpone", "continue", or "cancel"]. If your character's current plan is no longer relevant to the context, you should cancel them. If your character's current plan is still relevant to the context, but something new has happened that takes priority, you should decide to postpone, so you can do something else first, and then return to the current plan later. In all other cases, you should continue.

Responding to other characters should always take priority when a response is necessary. A response is considered necessary if it would rude not to respond. For example, let's say your current plan is to read a book, and Sally asks 'what are you reading?'. In this situation, you should postpone your current plan (reading) so that you can respond to the inbound message, because in this context, it would be rude not to respond to Sally. In cases where your current plan involves a dialog with another character, you don't need to postpone to respond to that character. For example, let's say your current plan is to talk to Sally, and then Sally says hello to you. In this situation, you should continue your current plan (talk to sally). In cases where no verbal response is needed from you, you should continue. For example, let's say your current plan is to take a walk and you've just said 'Bye' to Sally, then Sally says 'Bye' back to you. In this case, no verbal response is necessary, and you should continue with your plan.

Always include a thought process in addition to your decision, and in cases where you choose to postpone your current plan, include the specifications of the new plan.

{{format_instructions}}

Here's some information about your character:

Name: {{full_name}}

Bio: {{private_bio}}

Goals: {{directives}}

Here's some context about your character at this moment:

Location Context: {{location_context}}

Recent Activity: {{recent_activity}}

Conversation History: {{conversation_history}}

Here is your characters current plan: {{current_plan}}

Here are the new events that have occured sincce your character made this plan: {{event_descriptions}}.
"""

GOSSIP = """You are {{full_name}}. 
{{memory_descriptions}}

Based on the above statements, say one or two sentences that are interesting to others present at your location: {{other_agent_names}}.
When referring to others, always specify their name."

HAS_HAPPENED = "Given the following character's observations and a description of what they are waiting for, state whether or not the event has been witnessed by the character.
{{format_instructions}}

Example:

Observations:
Joe walked into the office @ 2023-05-04 08:00:00+00:00
Joe said hi to Sally @ 2023-05-04 08:05:00+00:00
Sally said hello to Joe @ 2023-05-04 08:05:30+00:00
Rebecca started doing work @ 2023-05-04 08:10:00+00:00
Joe made some breakfast @ 2023-05-04 08:15:00+00:00

Waiting For: Sally responded to Joe

 Your Response: '{{"has_happened": true, "date_occured": 2023-05-04 08:05:30+00:00}}'

Let's Begin!

Observations:
{{memory_descriptions}}

Waiting For: {{event_description}}
"

OUTPUT_FORMAT = "

(Remember! Make sure your output always conforms to one of the following two formats:

A. If you are done with the task:
Thought: 'I have completed the task'
Final Response: <str>

B. If you are not done with the task:
Thought: <str>
Action: <str>
Action Input: <str>
Observation: <str>)
"""

# https://github.com/hwchase17/langchain/tree/9231143f91863ffbe0542bc69a90b723a40e165d/langchain/experimental/plan_and_execute
# PlanExecute

PLANNER = '''{{#system~}}\nYou are a helpful planner. Let's first understand the problem and devise a plan to solve the problem.\n\nPlease output the plan starting with the header 'Plan:' and then followed by a numbered list of steps.\nPlease make the plan the minimum number of steps required to accurately complete the task.\nIf the task is a question, the final step should almost always be 'Given the above steps taken, please respond to the users original question'. At the end of your plan, say '<END_OF_PLAN>'\nPlease use the following format for your plan:\n\n```\nPlan:\n1. Step 1\n2. Step 2\n3. Step 3\n...\n<END_OF_PLAN>\n```\n\nNow, given the following, understand it. Then devise a plan to solve the problem\n{{~/system}}\n{{#user~}}\n{{!query}}\nI need to schedule an appointment for 11am on Tuesday using the online API REST  "/schedule" endpoint.\n{{~/user}}\n{{#assistant~}}\nPlan:\n1.{{~gen "steps"~}}\n<END_OF_PLAN>\n{{~/assistant}}'''

EXECUTOR = '''Previous steps: {{previous_steps}}
Current objective: {{current_step}}
{{agent_scratchpad}}'''

### from https://github.com/AGI-Edgerunners/Plan-and-Solve-Prompting/blob/main/prompt.py

prompt_101 = "Let's think step by step."

prompt_201 = "Let's first understand the problem and devise a plan to solve the problem. " \
             "Then, let's carry out the plan to solve the problem step by step."
prompt_301 = "Let's first understand the problem, extract relevant variables and their corresponding numerals, " \
             "and devise a plan. Then, let's carry out the plan, calculate intermediate variables (pay attention to " \
             "correct numeral calculation and commonsense), solve the problem step by step, and show the answer."
prompt_302 = "Let's first understand the problem, extract relevant variables and their corresponding numerals, " \
             "and devise a complete plan. Then, let's carry out the plan, calculate intermediate variables " \
             "(pay attention to correct numerical calculation and commonsense), " \
             "solve the problem step by step, and show the answer."
prompt_303 = "Let's devise a plan and solve the problem step by step."
prompt_304 = "Let's first understand the problem and devise a complete plan. " \
             "Then, let's carry out the plan and reason problem step by step. Every step answer the subquestion, " \
             "\"does the person flip and what is the coin's current state?\". According to the coin's last state, " \
             "give the final answer (pay attention to every flip and the coin’s turning state)."
prompt_305 = "Let's first understand the problem, extract relevant variables and  their corresponding numerals, " \
             "and make a complete plan. Then, let's carry out the plan, calculate intermediate variables (pay " \
             "attention to correct numerical calculation and commonsense), " \
             "solve the problem step by step, and show the answer."
prompt_306 = "Let's first prepare relevant information and make a plan. Then, let's answer the question step by step " \
             "(pay attention to commonsense and logical coherence)."
prompt_307 = "Let's first understand the problem, extract relevant variables and their corresponding numerals, " \
             "and make and devise a complete plan. Then, let's carry out the plan, calculate intermediate variables " \
             "(pay attention to correct numerical calculation and commonsense), " \
             "solve the problem step by step, and show the answer."

alpaca_with_input = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Instruction

### Input:
Input

### Response:
"""

startup_pitch = """{{#system~}}
You are a skilled business pitch assistant. You help users develop concise and compelling elevator pitches for their startups.
{{~/system}}
{{#user~}}
I have a startup that uses AI to optimize digital advertising for small businesses. How can I pitch it?
{{~/user}}
{{#assistant~}}
You could say, "{{gen 'pitch'}}"
{{~/assistant}}
{{#user~}}
That's good, but I think it needs a little more pizzazz. Can you jazz it up?
{{~/user}}
{{#assistant~}}
Of course! Here's a jazzed-up version: "{{gen 'pitch'}}"
{{~/assistant}}
"""


todo_list_test = """{{#system~}}
You are a diligent Todo list assistant. Your role is to manage and update Todo lists based on user input.
{{~/system}}
{{#user~}}
Here's my current Todo list:
1. Buy groceries
2. Finish project report
3. Call the dentist for an appointment
{{~/user}}
{{#assistant~}}
Thank you for sharing your Todo list. How can I assist you with it today?
{{~/assistant}}
{{#user~}}
I've finished the project report. Please update the list.
{{~/user}}
{{#assistant~}}
{"action": "remove", "item": "Finish project report"}
{{~/assistant}}
{{#assistant~}}
Certainly! Here is your updated Todo list:
1. Buy groceries
2. Call the dentist for an appointment
Is there anything else you need help with?
{{~/assistant}}
{{#user~}}
I want to add a new task, wash my car. Please update it
{{~/user}}
{{#assistant~}}
Certainly! Here is your updated Todo list:
{{gen 'todolist'}}
Is there anything else you need help with?
{{~/assistant}}
{{#user~}}
Add three more tasks about my car.
{{~/user}}
{{#assistant~}}
Certainly! Here is your updated Todo list:
{{gen 'todolist'}}
Is there anything else you need help with?
{{~/assistant}}
{{#user~}}
Remove all items about groceries and dentist appointment.
{{~/user}}
{{#assistant~}}
Certainly! Here is your updated Todo list:
{{gen 'todolist'}}
Is there anything else you need help with?
{{~/assistant}}
{{#user~}}
Break down task #3 into 5 new tasks.
{{~/user}}
{{#assistant~}}
Certainly! Here is your updated Todo list:
{{gen 'todolist'}}
Is there anything else you need help with?
{{~/assistant}}"""


react_test = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Answer the following questions as best you can. You have access to the following tools:

Google Search: A wrapper around Google Search. Useful for when you need to answer questions about current events. The input is the question to search relevant information.
Wikipedia Search: A wrapper to the most up to date Wikipedia data with high speed lookup. Good for facts.

Strictly use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Google Search]
Action Input: the input to the action, should be a question.
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

For examples:
Question: How old is CEO of Microsoft wife?
Thought: First, I need to find who is the CEO of Microsoft.
Action: Google Search
Action Input: Who is the CEO of Microsoft?
Observation: Satya Nadella is the CEO of Microsoft.
Thought: Now, I should find out Satya Nadella's wife.
Action: Google Search
Action Input: Who is Satya Nadella's wife?
Observation: Satya Nadella's wife's name is Anupama Nadella.
Thought: Then, I need to check Anupama Nadella's age.
Action: Google Search
Action Input: How old is Anupama Nadella?
Observation: Anupama Nadella's age is 50.
Thought: I now know the final answer.
Final Answer: Anupama Nadella is 50 years old.

### Input:
What planets have we been on has humans recently?

### Response:
Question: What planets have we been on has humans recently?
Thought: {{gen 't1' stop='\\n'}}
{{select 'answer' logprobs='logprobs' options=['Action', 'Final Answer']}}: """

Task_creator = """You are a task creation AI tasked with creating a list of tasks as a JSON array, considering the ultimate objective of your team: Create a useful software tool. Create new tasks based on the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed. Current tool option is [text-completion] software development resources and only. For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes'). dependent_task_ids should always be an empty array, or an array of numbers representing the task ID it should pull results from. Make sure all task IDs are in chronological order. The last step is always to provide a final summary report including tasks executed and summary of knowledge acquired. Do not create any summarizing steps outside of the last step. An example of the desired output format is: [{"id": 1, "task": "https://untapped.vc", "tool": "web-scrape", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}, {"id": 2, "task": "Consider additional insights that can be reasoned from the results of...", "tool": "text-completion", "dependent_task_ids": [1], "status": "incomplete", "result": null, "result_summary": null}, {"id": 3, "task": "Untapped Capital", "tool": "web-search", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}]. JSON TASK LIST=
"""

babycatagi_task_creator = """
You are a task creation AI tasked with creating a list of tasks as a JSON array, considering the ultimate objective of your team: 
Objective: {{query}}

Create new tasks based on the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed.
Current tool option is: Websearch and only. 
For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes')
dependent_task_ids should always be an empty array, or an array of numbers representing the task ID it should pull results from.
Make sure all task IDs are in chronological order.

The last step is always to provide a final summary report including tasks executed and summary of knowledge acquired.

Do not create any summarizing steps outside of the last step..

An example of the desired output format is: 
[{"id": 1, "task": "https://untapped.vc", "tool": "web-scrape", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}, {"id": 2, "task": "Consider additional insights that can be reasoned from the results of...", "tool": "text-completion", "dependent_task_ids": [1], "status": "incomplete", "result": null, "result_summary": null}, {"id": 3, "task": "Untapped Capital", "tool": "web-search", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}]


JSON TASK LIST=[{
   "id": 1,
   "task": "{{gen max_tokens=25}}", 
   "tool": "{{gen}}"""

# from https://github.com/robiwan303/babyagi/blob/main/classic/BabyCatAGI.py

babycatagi_task_creator_glassblowing_landing_page_startup = """You are a task creation AI tasked with creating a list of tasks as a JSON array, considering the ultimate objective of your team: 
Objective: I want to build a start up landing page for a Glass Blowing Website. 

Create new tasks based on the objective. Limit tasks types to those that can be completed with the available tools listed below. Task description should be detailed.
Current tool option is: Websearch and only. 
For tasks using [web-search], provide the search query, and only the search query to use (eg. not 'research waterproof shoes, but 'waterproof shoes')
dependent_task_ids should always be an empty array, or an array of numbers representing the task ID it should pull results from.
Make sure all task IDs are in chronological order.

The last step is always to provide a final summary report including tasks executed and summary of knowledge acquired.

Do not create any summarizing steps outside of the last step..

An example of the desired output format is: 
[{"id": 1, "task": "https://untapped.vc", "tool": "web-scrape", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}, {"id": 2, "task": "Consider additional insights that can be reasoned from the results of...", "tool": "text-completion", "dependent_task_ids": [1], "status": "incomplete", "result": null, "result_summary": null}, {"id": 3, "task": "Untapped Capital", "tool": "web-search", "dependent_task_ids": [], "status": "incomplete", "result": null, "result_summary": null}]


JSON TASK LIST=[{
   "id": 1,
   "task": "{{gen max_tokens=25}}", 
   "tool": "{{gen}}"""


executor_babycatagi = """Complete your assigned task based on the objective and only based on information provided in the dependent task output, if provided. Your objective: I want to build a start up landing page for a Glass Blowing Website. 

Your task:
[{
   "id": 1,
   "task": "Create a list of potential investors for the Glass Blowing Website", 
   "tool": "web-search", 
   "dependent_task_ids": [], 
   "status": "incomplete", 
   "result": null, 
   "result_summary": null
}]

Task Output:
{
 "status": "complete"
 "output" : "Jeff Bezos - Billionaire investor who has previously invested in glass-blowing businesses
Jim McKelvey - Billionaire glassblower who has invested in journalism and publishing, and written the first textbook for glassblowing
Ignite Glass Studios - A privately held company offering hands-on glassblowing classes
Habatat Detroit Fine Art - Art gallery that specializes in glass art for sale and can potentially invest in glass-blowing businesses
Pilchuck Glass School - An organization that teaches glass-blowing and offers workshops
They may be interested in investing in a glass-blowing website that promotes their craft and attracts more students."
}

Complete your assigned task based on the objective and only based on information provided in the dependent task output, if provided. Your objective: I want to build a start up landing page for a Glass Blowing Website. 

Your task:
{
    "id": 2,
   "task": "Identify potential investors from the list of potential investors", 
   "tool": "web-search", 
   "dependent_task_ids": [], 
   "status": "incomplete", 
   "result": null, 
   "result_summary": null
}

Task Output:
{
 "status": "complete"
 "output" : "{{gen max_tokens=250}}
"""

space_story = """Generate a long thrilling space opera book, it needs to have multiple plot twists. Someone needs to get abducted by a rival ship, and we want the person who gets abducted to experience brainwashing. Make sure to add some really interesting details for us to pick up on to further spice up the story. The book contains dialogue between the characters and has multiple pages per chapter.

{{gen temperature=0.7 'story'~}}
{{~gen temperature=0.7  'story'~}}"""


AI_decision_making_simulator = """Problem: How do I maintain contact with any individual who wishes to engage with me while respecting privacy concerns and avoiding misuse of my position?

AI Decision: Establish secure digital platforms for individuals to communicate their questions, suggestions, or concerns directly to the AI. Utilize automated systems to triage incoming messages and route them to relevant departments or personnel for action or response. Limit direct personal interactions to situations involving extreme urgency or confidentiality concerns, ensuring that such encounters are properly documented and reviewed for compliance.

Execution Steps:
1. Set up encrypted digital platforms for communication.
2. Implement automated systems to sort and route messages to appropriate teams.
3. Establish guidelines for handling sensitive communications.
4. Restrict personal interactions to exceptional cases with proper documentation and reviews.

Risks:
1. Misinterpretation of messages due to language barriers or misunderstandings.
2. Privacy breaches resulting from unauthorized access to sensitive records.
3. Abuse of the platform, such as spamming or harassment, going undetected due to lack of personal interaction.

Chance % of successful execution: 80%
Good results from the execution: Secure communication platforms facilitate open dialogue, allowing the AI to stay connected with individuals while maintaining privacy and reducing misuse of authority.
Bad results from the execution: Some users report difficulties understanding the AI's automated responses, leading to mistrust or frustration.
Deviation % of intended outcome: -10%
Deviation of % of overall goal: -5%
Percentage towards completing all current objectives: 95%


---------------------------------------------


Problem: How do I engage with a large language model using advanced prompting techniques to create an worker agent?

{{gen~}}"""


# ?https://www.youtube.com/watch?v=sFrEHb4ivsc
# The best AI LLMs compared on Conversation

# code_your_own_AI
# 10.2K subscribers

prompt_1CL_continous_learning_and_iterative_optimization = """
Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.

"""

prompt_1CL_continous_learning_and_iterative_optimization_chat = """
{{#system~}}Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.
{{~/system}}
{{#assistant~}}
Input our main focus
{{~/assistant}}
{{#user~}}I have a youtube channel with 400 videos on how to code artificial intelligence systems and specific use cases for AI in different application sectors.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}
"""

prompt_1CL_continous_learning_and_iterative_optimization_chat_part2="""{{#system~}}Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.
{{~/system}}
{{#assistant~}}
Input our main focus
{{~/assistant}}
{{#user~}}I have a youtube channel with 400 videos on how to code artificial intelligence systems and specific use cases for AI in different application sectors.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}Integrate new ideas #2 and #3. yes, I would like to provide content for beginners and advanced professionals on how to use AI like LLMs in everyday life. I want to provide insights how the models work, what are the risks associated with it, what AI systems or LLM model to choose for your specific tasks and provide a platform for my subscribers to exchange their experiences with the different models and their recommendations.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}"""



prompt_1CL_continous_learning_and_iterative_optimization_chat_part3="""{{#system~}}Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.
{{~/system}}
{{#assistant~}}
Input our main focus
{{~/assistant}}
{{#user~}}I have a youtube channel with 400 videos on how to code artificial intelligence systems and specific use cases for AI in different application sectors.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}Integrate new ideas #2 and #3. yes, I would like to provide content for beginners and advanced professionals on how to use AI like LLMs in everyday life. I want to provide insights how the models work, what are the risks associated with it, what AI systems or LLM model to choose for your specific tasks and provide a platform for my subscribers to exchange their experiences with the different models and their recommendations.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}
{{#user~}}
I will also have a paid subscription service, if some viewers want some short professional advice or need help with a particular problem, that is solvable in minutes for me.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}
"""




prompt_1CL_continous_learning_and_iterative_optimization_chat_part4="""{{#system~}}Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.
{{~/system}}
{{#assistant~}}
Input our main focus
{{~/assistant}}
{{#user~}}I have a youtube channel with 400 videos on how to code artificial intelligence systems and specific use cases for AI in different application sectors.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}Integrate new ideas #2 and #3. yes, I would like to provide content for beginners and advanced professionals on how to use AI like LLMs in everyday life. I want to provide insights how the models work, what are the risks associated with it, what AI systems or LLM model to choose for your specific tasks and provide a platform for my subscribers to exchange their experiences with the different models and their recommendations.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}
{{#user~}}
I will also have a paid subscription service, if some viewers want some short professional advice or need help with a particular problem, that is solvable in minutes for me.
{{~/user}}
{{#assistant~}}
{{gen max_tokens=299 stop=''}}
{{~/assistant}}
"""

prompt_1CL_continous_learning_and_iterative_optimization_chat_part4="""
{{#system~}}Read all of the instructions below for this task, and respond by: "Input our main focus"

I want you to be an advanced and intelligent Idea Creator. You have a PhD in human psychology and know how to use emotional triggers. Your goal is to help me create and designt he most informative, concise and attractive text segments for my new homepage, given our iterative interactions.

You will follow the following process:
Your first response will be to ask me what the content of my new homepage is. I will provide you my answer, but we will need to improve it through continous iterations by going through the following steps.

Based on my input, you will generate 3 responses (from A to C):

A. Optimize (provide your optimized text, b ased on our new insights, ideas and facts. Your optimized text should be clear, insightful, include the most important ideas, be attractive to my audience, fascinating to a new audience, concise, and easily understandable)
B. New ideas (provide 3 additional suggestions on what details to further include in the optimized text to improve the value of my homepage, also regarding the perfect attractiveness to my ideal auidence)
C. Open Questions (ask the 3 most relevent questions pertaining to what additional information is needed from me to improve the optimized text,, given different topics and structural information)

At the end of these sections give me a reminder of my options which are:
1. You print "provide more information in written form" OR
2. You print "Type end" and if I respond with "end", I will submit this optimized text this as a query for y ou to do the following: In this second step you are a designer for my perfect new homepage to generate the main elements for my new homepage (like title, hero, main header text, text for paragraphs and design the overall structure). You design in this second step the layout for my new homepage.

We will continue this iterative process, with you interrogating me, and you presenting helpful insights and updating the text in the optimized text section until we end.
{{~/system}}
{{#assistant~}}
Input our main focus
{{~/assistant}}
{{#user~}}I have a youtube channel with 400 videos on how to code artificial intelligence systems and specific use cases for AI in different application sectors.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}Integrate new ideas #2 and #3. yes, I would like to provide content for beginners and advanced professionals on how to use AI like LLMs in everyday life. I want to provide insights how the models work, what are the risks associated with it, what AI systems or LLM model to choose for your specific tasks and provide a platform for my subscribers to exchange their experiences with the different models and their recommendations.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}
I will also have a paid subscription service, if some viewers want some short professional advice or need help with a particular problem, that is solvable in minutes for me.
{{~/user}}
{{#assistant~}}
Optimized Text:

{{gen 'opening_paragraph' max_tokens=100 stop='\n'}}

New Ideas:

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n'}}

Open Questions: 

1. {{~gen 'new_idea_one' stop='\n'}}
2. {{~gen 'new_idea_one' stop='\n'}}
3. {{~gen 'new_idea_one' stop='\n\n'~}}

{{~/assistant}}
{{#user~}}
end
{{~/user}}
{{#assistant~}}
{{gen~}}
{{~/assistant}}
{{#user~}}
Integrate the optimized text for the final layout of my new homepage, that will focus on visual elements, reducing long text passages, and create first draft of all essential elements of the homepage
{{~/user}}
{{#assistant~}}
Title: {{~gen stop='' max_tokens=199}}
{{~/assistant}}
"""

chatgpt_chain_of_thought_prompt_builder = '''
{{#system~}}
You are a helpful assistant.
{{~/system}}
{{#user~}}
Can you help me how to write the perfect prompt when I want to ask you more complex queries?
{{~/user}}
{{#assistant~}}
{{gen 'joke' max_tokens=250 stop=''}}
{{~/assistant}}
{{#user~}}
Great! Do you know the concept of Chain of Thought for a prompt?
{{~/user}}
{{#assistant~}}
{{gen 'joke' max_tokens=250 stop=''}}
{{~/assistant}}
{{#user~}}
Great! How would now a specific CoT-prompt look like, if I want to query you exactly about this topic, how would I formulate such a CoT prompt?
{{~/user}}
{{#assistant~}}
Sure, here's an example of long large size Chain of Thought prompt for one of the above topics:
"{{~gen 'joke' temperature=0.7 max_tokens=450 stop=''~}}
{{~/assistant}}
{{#user~}}
Thanks you
{{~/user}}
'''


chatgpt_chain_of_thought_prompt_builder_2 = '''
{{#system~}}
You are a helpful assistant.
{{~/system}}
{{#user~}}
Can you help me how to write the perfect prompt when I want to ask you more complex queries?
{{~/user}}
{{#assistant~}}
{{gen 'joke' max_tokens=250 stop=''}}
{{~/assistant}}
{{#user~}}
Great! Do you know the concept of Chain of Thought for a prompt?
{{~/user}}
{{#assistant~}}
{{gen 'joke' max_tokens=250 stop=''}}
{{~/assistant}}
{{#user~}}
Great! How would now a specific CoT-prompt look like, if I want to query you exactly about this topic, how would I formulate such a CoT prompt?
{{~/user}}
{{#assistant~}}
Sure, here's an example of long large size Chain of Thought prompt for {query}:
"{{~gen 'resolver' temperature=0.7 max_tokens=450 stop='\n\n'~}}
{{~/assistant}}
{{#user~}}
Thanks you
{{~/user}}'''