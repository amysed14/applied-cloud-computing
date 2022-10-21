/*Websites I used:*/
/*https://stackoverflow.com/questions/38803122/postgres-error-null-value-in-column-id-during-insert-operation*/
CREATE TABLE IF NOT EXISTS Meals (
  MealId SERIAL PRIMARY KEY,
  MealName VARCHAR(250) NOT NULL,
  MealPrice VARCHAR(250) NOT NULL
);

INSERT INTO Meals(MealName, MealPrice) VALUES ('Fiesta Lime Chicken','$17.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Hand-Battered Fish & Chips','$18.29');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Classic Burger','$8.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('8oz Top Sirloin','$25.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Cedar-Grilled Salmon','$23.59');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Double-Glazed Baby-Back Ribs','$17.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Grilled Shrimp Avocado & Grapefruit Salad','$18.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('3-Cheese Chicken Cavatappi','$11.99');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Tuscan Tomato Bisque','$9.25');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Santa Fe Salad','$19.75');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Jumbo Spaghetti and Meatballs','$20.45');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Mushroom Swiss Burger','$17.25');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Clam Chowder Soup','$9.25');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Vegetarian Pizza','$32.75');
INSERT INTO Meals(MealName, MealPrice) VALUES ('Buffalo Chicken Pizza','$33.75');
