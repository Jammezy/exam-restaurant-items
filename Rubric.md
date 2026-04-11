##### MAX SCORE: 100
##### YOUR SCORE:  
#### Grader's Notes:
- TAs: Put any notes on points lost here.
---
## Rubric

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>#</th>
      <th>Requirement</th>
      <th>Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Successfully creates SQLite Database through peewee with table and all required columns</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Creates menu that repeats after each option is chosen until exited</td>
      <td>5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Menu handles invalid input (something other than 1, 2, 3, or 4)</td>
      <td>5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Option 1: Can create new MenuItem row in database (or would if the .create() method wasn't overridden)</td>
      <td>10</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Option 1: Overriden create method validates price, doesn't create row/object if price isn't valid</td>
      <td>12</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Option 1: Overriden create method validates category, doesn't create row/object if category isn't valid</td>
      <td>12</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Option 1: Overriden create method saves correctly formatted category (all caps) when the category is spelled correctly but has other capitalization</td>
      <td>6</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Option 2: get_info method written correctly</td>
      <td>10</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Option 2: info printed out for all rows in the database</td>
      <td>8</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Option 3: Info printed out for the most expensive item of each category</td>
      <td>10</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Option 4: program ends when entering 4 </td>
      <td>2</td>
    </tr>
    <tr>
      <td colspan="2">Total</td>
      <td>100</td>
    </tr>
  </tbody>
</table>


## TA Guide

1. #### Successfully creates SQLite Database through peewee with table and all required columns
    - 10 points
        - -2 for each missing class variable
        - -2 if each class variable isn't assigned a reasonable Field type (e.g. making the price a CharField, etc.)
        - -10 if the syntax was attempted, but no database was actually created
        - -5 if the syntax was attempted, and the database was created, but the table with its columns wasn't actually created.

2. #### Creates menu that repeats after each option is chosen until exited
    - 5 points
        - -1 if it doesn't have all options listed
        - -3 if it doesn't correctly loop after each option is chosen (except exit)

3. #### Menu handles invalid input (something other than 1, 2, 3, or 4)
    - 5 points
        - -8 if it doesn't inherit from the Attendee class
        - -2 if missing instance variables

4. #### Option 1: Can create new MenuItem row in database (or would if the .create() method wasn't overridden)
    - 10 points
        - Note, if the .create function doesn't work because they made a mistake in overriding the function, don't mark down this. This is just if the regular .create() functionality would work otherwise.
        - -2 if it would work, but there are spelling errors (like of the column names)that prevent it from working
        - -2 each if the name, category or price is gathered and entered.
        
5. #### Option 1: Overriden create method validates price, doesn't create row/object if price isn't valid
    - 12 points
        - -6 if they do the correct logic for handling the price, but it isn't in an overriden version of the .create() method
        - -2 if it mostly works, there is just a small logic error (like the comparisons not being inclusive.)
        - -8 if it doesn't work, but there is some attempt (e.g. it doesn't end up creating the object correclty, but the logic is attempted. There can be some leeway here depending on the situation)

6. #### Option 1: Overriden create method validates category, doesn't create row/object if category isn't valid
    - 12 points
        - -6 if they do the correct logic for handling the category, but it isn't in an overriden version of the .create() method
        - -4 if it mostly works, but it doesn't create a new row when the category is spelled correctly but capitalized differently.
        - -8 if it doesn't work, but there is some attempt (e.g. it doesn't end up creating the object correclty, but the logic is attempted. There can be some leeway here depending on the situation)

7. #### Option 1: Overriden create method saves correctly formatted category (all caps) when the category is spelled correctly but has other capitalization
    - 6 points
        - -4 if an honest attempt was made, but it doesn't end up saving the uppercased version back into the database

8. #### Option 2: get_info method written correctly
    - 10 points
        - -2 for each variable not correctly returned in the string
        - -5 if it isn't a method in the MenuItem class

9. #### Option 2: info printed out for all rows in the database
    - 8 points
      - -6 if attempted, but it doesn't correctly print out all the information from the database using .get_info
      - -3 if the info is printed, but it doesn't use the .get_info method

10. #### Option 3: Info printed out for the most expensive item of each category
    - 10 points
        - -2 if it workds mostly, but breaks if there is a category that doesn't have any food in it
        - -8 if attempt is made that is close, but it doesn't work (e.g. it doesn't actually grab the most expensive of each category)

11. #### Option 4: program ends when entering 4 
    - 2 points
