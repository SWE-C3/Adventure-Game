# Contributing

## Setting up the environment

- Install Python 3.7.1 for your platform, see https://www.python.org/downloads/release/python-371/
- Install `virtualenv` for your python installation
  ```bash
  python -m pip install virtualenv
  ```
- Fork the repository to your own Github account
- Clone the repository
  ```bash
  git clone https://github.com/<your_user>/Adventure-Game
  ```
- Create a virtual environment inside the project directory
  ```bash
  cd Adventure-Game
  python -m virtualenv venv
  ```
- Activate the virtual environment
  - Windows
    ```bash
    venv\Scripts\activate
    ```
  - Linux
    ```bash
    . venv/bin/activate
    ```
- Install the project requirements
  ```bash
  pip install -r requirements.txt
  ```
- (Only on Windows systems) Install Windows-specific requirements
  - For 32-bit Python version
    ```bash
    pip install -r requirements-win32.txt
    ```
  - For 64-bit Python version
    ```bash
    pip install -r requirements-win64.txt
    ```
  
## Developing

After making any changes to the project that you want
to push to the main repository, do the following:

- make sure that your virtual environment is activated
- Run `autopep8` to automatically format you code
  ```bash
  autopep8 . --recursive --in-place --exclude venv
  ```
- create a pull request at the main repository

## Documentation

Documentation for the `curses` library can be found [at the
official website](https://docs.python.org/3/library/curses.html#module-curses),
as well as [a tutorial](https://docs.python.org/3/howto/curses.html)
on how to use it.