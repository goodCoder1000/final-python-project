# Overview
This Python code is a simple **NPC generator** that randomly creates a custom **number of NPCs**, each with a **random name**, **attributes**, a **height**, and **more**.

# Code Explanation
When the program starts, the user is asked to enter:
How many **attributes** each NPC should have (between **1 and 5**).
It automatically uses 10 NPCs.

If you enter a value outside of the range that I specified, it tells you to restart.

## The Complicated Code Explanation
The script then randomly selects from two lists: one containing names and another containing attributes. Each NPC is also given a random height between **4.0 and 7.0 feet**, which is my float, a random boolean **“Is tuff?”**, which is obviously my boolean, which is value that determines their toughness (lol).

Inside a loop running **10 times** (which is the number of NPCs being created), it prints the attributes. The number of attributes depends on how many you want (this is prompted at the start of the project). After this, it ***prints*** the **height** and indicates whether they are tough or not. Earlier, it only randomized the variable; it didn't print.

# Libraries
This program uses the random library for **randomness**. It also uses the time library just to make everything **cleaner**!
