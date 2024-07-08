import os

# Help load and use the environmental variables.
env_vars = {}

def load_env():
    try:
        with open('.env') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        try:
                            key, value = line.split('=', 1)
                            env_vars[key] = value
                        except ValueError as e:
                            print(f"Error splitting line '{line}': {e}")
                    else:
                        print(f"Skipping malformed line: {line}")
    except OSError as e:
        print(".env file not found or another file error occurred: ", e)
    except Exception as e:
        print(f"An error occurred: {e}")
