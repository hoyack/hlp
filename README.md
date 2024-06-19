# Project Structure
    hlp/
    │
    ├── main.py
    ├── templates/
    │ ├── agents_config.json
    │ ├── crews_config.json
    │ └── tasks_config.json
    └── src/
    ├── agents/
    │ ├── agent_factory.py
    │ ├── callback.py
    ├── tasks/
    │ └── task_factory.py
    ├── utils/
    │ ├── json_loader.py
    │ └── logger.py
    └── crew_factory.py
# Installation

1. Create and activate a new conda environment:
    ```sh
    conda create -n crew
    conda activate crew
    ```

2. Install Python:
    ```sh
    conda install python
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Copy the example environment file and configure your API keys:
    ```sh
    cp .env.example .env
    ```

# Configuration

1. Add your API keys to the `.env` file.
2. Examine the `/templates` folder and edit the `agents_config.json` and `tasks_config.json` files to suit your needs.
3. Assign the tools to the agents and tasks according to the `tools_config.json`.

# Run the Task

To run the project, execute the following command and enter your business idea when prompted:
```sh
python main.py
Enter your business idea when prompted.