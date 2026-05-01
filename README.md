# Jorliveroo

# Table of Contents
-[Introduction](#introduction)
-[User Interactions](#user-interactions)
-[Database Design](#database-design)
-[User Stories](#user-stories)
  -[Item Selection](#item-selection)
  -[Total Money Box](#total-money-box)
  -[Category button and pop-up menu](#category-button-and-pop-up-menu)
  -[Proceed to checkout button](#proceed-to-checkout-button)
  -[Adding a new item to the database](#adding-a-new-item-to-the-database)
  -[Editing a current item in the database](#editing-a-current-item-in-the-database)
  -[Deleting an item from the database](#deleting-an-item-from-the-database)
  
  

## Introduction
Jorliveroo is a web application for users seeking a simplified food ordering experience. Have you been put off by ordering food simply because of the countless pages, tedious advertisements, and hidden fees? With Jorliveroo, I have simplified this experience, stripping away the tedious components that competitors offer. The main menu will host the twelve different categories, each with its own pop-up menu. From there, users will be able to select the items they want to add from that category. At the bottom of the main menu is the total fee including VAT. The application is designed to lower the anxiety challenges one could face when ordering food. Whether that be unsure of the total fee, or put off by the various pages and advertisements, Jorliveroo is here to lower that anxiety. The users will have a unique login so that they can gain access to the application. 
## Why my application is easy to use
My application is easy to use because I have simplified the food ordering system. Instead of multiple tabs, the menus are accessible under one page, with pop-up menus instead of a new page. This will make the application more efficient than its competitors due to its easy-to-use buttons, clear structure, and more. Not only will it be user-friendly through its clear structure, but the buttons will also be clear, color-blind friendly, with font-sizes that are readable on a variety of devices, and a color scheme that matches the core design of the application.
## User interactions 
Here is a full list of interactions that a user can have with my application:
* A user can enter their username and password to log into the application
* A user can click on one of the buttons to open up the respective pop-up menu
* A user can click the plus icon next to the respective item they wish to add to their basket
* A user can view the total price of their basket at the bottom of the main menu page
* A user can proceed to checkout
* A user can add another of the same item currently in their basket
* A user can also remove said item from the basket
* An admin can add items to the database
* An admin can edit the current item names and or price in the database
* An admin can remove one of the existing items from the database
## Database design 
My database will be easily manageable by any administrator who needs to step in at any given time. The database structure is as follows:
* id
* item category
* item name
* item price

## User Stories
The user stories for the Jorliveroo food delivery application were created with MoSCoW methodology in mind. These user stories helped with the application's design, clearly identifying the customer's journey, while also helping the admin team address any required adjustments.
## Login
* **As a user:** Customer
* **I want to be able to**: Login using my username and password.
* **So that**: I can access the food delivery application.
* **Acceptance Criteria**:
  * Simple login validation form that requires only a username and password box. 
  * Once the username and password are entered correctly, users are directed to the main menu.
  * If the password and or username is incorrect, an error message will appear.
## Item selection
* **As a user:** Customer
* **I want to be able to**: Choose from a variety of food items on one page.
* **So that**: I can proceed to checkout at a much quicker pace.
* **Acceptance Criteria**:
  * Button for each category: Pasta, Pizza, Burgers, Fish, Soup, Sides, Curry, Vegan, Gluten Free, Saver Menu, Desserts, and Kids Menu.
  *  The user can order from a variety of food choices.
  *  Button font must be Century Gothic (Body), white text colour, and bold.
## Total money box
* **As a user:** Customer
* **I want to be able to**: See the total number of their basket before proceeding to checkout.
* **So that**: Ensures the figure at the bottom of the page aligns with the budget I had in my head for ordering takeout.
* **Acceptance Criteria**:
     *  Total money box at the bottom of the page.
     *  The user can clearly see the total of their order.
     *  Text must be bold, black, Century Gothic, and 20px.
 ## Category button and pop-up menu  
 * **As a user:** Customer
 * **I want to be able to**: Click on a category button, and the respective menu appears.
 * **So that**: I can decide which of the respective items I want to add to my basket.
 * **Acceptance Criteria**:
    * Pop-up menu for each category.
    * The user can add items from the pop-up menu directly into their basket via the + button next to the item.
    * Menu colour must be blue, price figures box red, "add" box yellow, text size 20 px, and font Century Gothic.
 ## Proceed to checkout button 
 * **As a user:** Customer
 * **I want to be able to**: Proceed to checkout quickly without going through multiple menus to get to the end destination.
 * **So that**: I can proceed with payment and complete my purchase.
 * **Acceptance Criteria**:
    * Button that takes the user directly to the checkout page.
    * The customer's order, including items and their prices, appears on the checkout page, matching the figure displayed on the menu page.
    * Button must be red, the text colour white, font size 20 px, and Century Gothic font.
 ## Adding a new item to the database
 * **As a user:** Admin
 * **I want to be able to**: Add a new food item into one of the categories.
 * **So that**: The food menu is updated to the latest items for the online store.
 * **Acceptance Criteria**:
    * Item is saved in the database.
    * Item must be assigned a price.
    * Item must be assigned a category so that the database knows which category the item belongs to.
 ## Editing a current item in the database
  * **As a user:** Admin
  * **I want to be able to**: Edit one of the existing items in the database.
  * **So that**: The item is up to date with the latest requirements, for example, the price has changed.
  * **Acceptance Criteria**:
     * The edits are saved in the database.
     * The updates are saved and appear on the application.
  ## Deleting an item from the database
   * **As a user:** Admin
   * **I want to be able to**: Delete one of the existing items from the database.
   * **So that**: The item no longer appears in one of the respective menus in the application.
   * **Acceptance Criteria**:
      * The item is removed from the application.
      * The item is removed from the database.
      * The database is saved to reflect the new menu.
