# Installation
conda create -n crew\
conda activate crew\
conda install python\
pip install -r requirements.txt\
cp .env.example .env

# Configuration
Add your API keys to the .env\
Examine the `/templates` folder and edit the `agents_config.json` and `tasks_config.json`\
Assign the tools to the agents and task according to the `tools_config.json`

# Run the task
python src/main.py\
Enter your business idea: