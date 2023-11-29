In the commit, I added the insert_row and update_row methods to the Table class in data_processing\
**insert_row(self, dict)**\
takes a dictionary which contains the information about the film as input and inserts the movie to the table.\
**def update_row(self, primary_attribute, primary_attribute_value, update_attribute, update_value):**\
Using the primary attribute and attribute value inputs, searches the table for a match and updates the value at location\
There appears to be no bugs.\
Test print functions tests the changes made to the table