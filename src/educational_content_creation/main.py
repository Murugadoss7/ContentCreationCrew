#!/usr/bin/env python
import sys
import os
from dotenv import load_dotenv
from educational_content_creation.crew import ContentCreationCrew

# Load environment variables from .env file
load_dotenv()

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'Word_Count': '300',
        'Topic_Name': 'Water Life Cycle',
        'GRADE': '10',
        'Number_of_Questions': '5'
    }
    ContentCreationCrew().crew().kickoff(inputs=inputs)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    # elif command == "train":
    #     train()
    # elif command == "replay":
    #     replay()
    # # elif command == "test":
    # #     test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
