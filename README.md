# 🐸 Single Player Freckers

This project is Part A of the COMP30024 Artificial Intelligence course at the University of Melbourne (March 2025). It involves building a Python program to solve a simplified single-player version of the **Freckers** board game.

## 🧠 Project Overview

In Single Player Freckers, the player controls one **Red frog**, which must reach the final row (r = 7) of an 8×8 board. The board also contains static **Blue frogs** and **lily pads**. The goal is to compute the **shortest possible sequence of legal MOVE actions** to reach the final row, or determine that no path exists.

## 🎯 Objectives

- Solve a deterministic, single-agent search problem using informed search techniques.
- Return the **minimum-cost** action sequence to win the game.
- Reinforce concepts from AI lectures, including:
  - Optimal pathfinding using A* search
  - Heuristic design and evaluation
  - State-space modeling and board representation in Python

## 🚀 Algorithm: A*

We implemented the **A\*** search algorithm to find the optimal solution.  
To guide the search, we used the **Euclidean distance** from the current position to the nearest cell in the final row (r = 7) as our heuristic function.  

This heuristic is:
- **Admissible**, because it never overestimates the true cost.
- **Consistent**, as the estimated cost always decreases as the frog moves closer to the goal.

By using A* with this heuristic, we efficiently find the shortest valid sequence of jumps or moves to reach the other side, or correctly determine when no such path exists.

## 👥 Team Contributions

This project was completed collaboratively by two team members.

- **[Yurim CHO]** was primarily responsible for implementing the A* search algorithm, designing the Euclidean distance heuristic, and developing the core logic of the program.
- **[Chuanmiao YU]** contributed by discussing and planning the algorithmic approach together before implementation, and later wrote the report (`report.pdf`) that analyzes our chosen strategy, heuristic design, and time/space complexity.

We regularly communicated to align on design choices and ensured both members fully understood the overall solution.
