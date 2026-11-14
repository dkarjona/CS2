‎Part 1 – Analyze the Logic
1. Input: What information does the program need?
‎The student's score from 0 to 100.
‎
‎2. Boundary: What is the minimum valid score?
‎0
‎
‎3. Boundary: What is the maximum valid score?
‎100
‎
‎4. Possible Outputs: What outcomes can the program produce?
‎–Invalid Score
‎
‎–Outstanding
‎
‎–Very Satisfactory
‎
‎–Satisfactory
‎
‎–Needs Improvement
‎
‎5. Selection Pattern: Which part uses a boundary condition?
‎When checking if the score is below 0 or above 100. If either condition is true, the program displays "Invalid Score"
‎
‎6. Selection Pattern: Which part uses multiple decision paths?
‎The if, elif, and else statements. 
‎
‎Part 2 — Create a Flowchart
*image here*
‎
‎Part 3 – Write the Pseudocode

‎START
‎
‎    INPUT score
‎
‎    IF score < 0 OR score > 100 THEN
‎        DISPLAY "Invalid Score."
‎
‎    ELSE IF score >= 90 THEN
‎        DISPLAY "Outstanding"
‎
‎    ELSE IF score >= 80 THEN
‎        DISPLAY "Very Satisfactory"
‎
‎    ELSE IF score >= 75 THEN
‎        DISPLAY "Satisfactory"
‎
‎    ELSE
‎        DISPLAY "Needs Improvement"
‎
‎END
‎
‎Part 4 — Implement the Code
‎*already in score_checker.py*
‎
‎Part 5 — Test the Program
‎*image here*
‎Testing Reflection
‎1. Why is it important to test the values 0 and 100?
‎Because they are the minimum and maximum valid scores and to ensure they are inclusive and not exclusive in the program. 

‎2. Why did you also test -1 and 101?
‎To make sure the program rejects values over and under the maximum and minimum values respectively. 
‎
‎3. Which test helped you understand boundary conditions the most?
‎Testing 0 and 100 because that's the limit. 
‎
‎4. Did any of your tests initially fail? If yes, what did you change in your program?
‎Surprisingly no. 
