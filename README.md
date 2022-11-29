:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Text Adventure With Graphical Output
## CS 110 Final Project
### Fall, 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

 [https://replit.com/join/fnrltzzdwg-ericpan7](#) 

<< [link to demo presentation slides](#) >>

### Team:  Eric & Ivan 
#### Ivan Yun, Eric Pan

***

## Project Description

An adventure game with multiple outputs depending on the decisions of the player. The input mechanism will mainly be text-driven, with graphical output to depict the player's decisions as well as graphics to display the player's next options.

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
* Class Interface Design
    1. < Scene Interface > 
    * __init__
        * < Instance Variables : screen_width screen_height bg_color >
        * < Methods : returns the width height and bgcolor to draw the scene >
        * < Dependencies : Relies on Sprite Class >
    2. < Player Interface > 
    * __init__
        * < Instance Variables : players x position players y position lives and speed>
        * < Methods : returns players position x and y coordinate >
        * < Dependencies : Relies on Sprite Class >
    3. < Item Interface > 
    * __init__
        * < Instance Variables : items x and y position and item size>
        * < Methods : return randomized x and y position of item >
        * < Dependencies : Relies on Sprite Class >                 
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * << You should have a list of each of your classes with a description. >>
    * << Scene Class: Sets color and height and width of the screen >>
    * << Player Class: x and y position of player and the amount of lives >>
    * << Item Class: Sets the image of item x and y position and size of item >>

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
