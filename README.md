# Grupp_6_Laboratory_Software
[![Pylint](https://github.com/Joppe17/Grupp_6_Laboratory_Software/actions/workflows/pylint.yml/badge.svg)](https://github.com/Joppe17/Grupp_6_Laboratory_Software/actions/workflows/pylint.yml)

[![CI](https://github.com/Joppe17/Grupp_6_Laboratory_Software/actions/workflows/parse.yml/badge.svg)](https://github.com/Joppe17/Grupp_6_Laboratory_Software/actions/workflows/parse.yml)

## Member Table
|Name                | Email                         | Github Handles    |
|--------------------|-------------------------------|-------------------|
|Elias Sjögren       | sjel24no@student.ju.se        | fleyvier          |
|Linus Jacobsson     | jali24qy@student.ju.se        | Joppe17           |
|Vilmer Levin        | vilmerlevin@gmail.com		 | KingVilmer        |
|Felix Gudmundsson   | felixgudmundsson@gmail.com    | FelixG11          |
|Knut Larsson        | knut.larsson@hotmail.se       | knutlarsson       |
|Oskar Ali           | oskarali03@hotmail.com        | oskarali          |



## Declaration:
I Elias Sjögren declare that I am the sole author of the content I add to this repository.  

I Vilmer Levin declare that I am the sole author of the content I add to this repository.    
   
I Linus Jacobsson declare that I am the sole author of the content I add to this repository.

I Felix Gudmundsson declare that I am the sole author of the content I add to this repository.

I Knut Larsson declare that I am the sole author of the content I add to this repository.

I Oskar Ali declare that I am the sole author of the content I add to this repository.


## Project Description

Our plan is to create a game based off the classic game cookie clicker. It will be implemented in python with pygame. The game is played by clicking the object on the screen and earning points. Features will be added as the project moves forward. Some of the features will be auto-clicker, multipliers and perhaps some easter eggs.              

Our workflow plan is that each student has a branch where they will create features to add to the main game. Every pull request will be reviewed by one student only and shall not be pushed before the review is finished.

Here you can check our progress on the [Kanban Board](https://github.com/users/Joppe17/projects/1/views/1).

## Running the game

To compile and run this project you first have to download pygame on your computer:
```
pip install pygame   
```

In command line write:  
``` 
python main.py
```  

or...

```
py main.py
```  

Or if you are using windows double click on run.bat
```
run
```
### Running unit tests
Running Unit Tests
Install pytest if you haven't already:
```
pip install pytest
```

Run all tests:
```
pytest unittest/
```

Run a specific test file:
```
pytest unittest/bananatest.py
```

### Code Coverage
Install pytest-cov if you haven't already:
```
pip install pytest-cov
```

Run tests with coverage report:
```
pytest unittest/ --cov=ui --cov=logic
```

To see exactly which lines are not covered:
```
pytest unittest/ --cov=ui --cov=logic --cov-report=term-missing
```

### Linter
Install flake8 if you haven't already:
```
pip install flake8
```

Run the linter on the entire project:
```
flake8 .
```

Or on a specific file:
```
flake8 ui/banana.py
```
