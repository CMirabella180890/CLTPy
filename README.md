# CLTPy - An analysis tool based on Classical Lamination Theory
## Introduction
It is often quite handy to have a fast-to-launch tool to make some preliminary calculation in many field of science and engineering. The purpose of this Python piece of code is to build such a tool concerning the design of a composite laminate, starting with composite ply material's data. The code is still far from being applicable in a straightforward manner to the preliminary design of composite material laminates, although it is able to perform all the basic calculations required. The use of an external .json file to store materials' properties provide a means to add new materials if the final user desires to do so.
## Current version of CLTpy
The current version of the program is capable to 
* accept as input a dictionary variable **t_ply** which contains the thickness of a single-ply with its unit of measure;
* accept as input the selected lamination sequence, stored inside a list variable **lam_seq** (it can be defined as a collection of integers or floats number);
* materials' database is loaded, stored inside object variable and converted to SI unit of measures, so that the program is fully capable to work in Engineering and SI unit of measures;
* **Classical Lamination Theory** is then applied to obtain stresses and strains inside every single-ply of the lamination sequence, evaluating also the **Margin of Safety** (not available at the moment but it will be very soon!).
## Criticism about current implementation 
At the moment, the program is too "heavy" and quite hard to read. Any possible improvements are related to
1. **increase the modularity level** and decompose the main program into several smaller parts;
2.  **building a package**, possibly following a high modularity logic; 
3.  **avoid misusing dictionary variables** and **correctly store all the materials' data**; 
4.  **improve the usability** with a better INPUT/OUTPUT or, even better, **building a GUI**; 
5.  **improve the readability of the code**, exploiting comments and **building proper documentation**.
## Long-term objectives 
The author of the code wants to build a free-of-charge tool to help preliminary design of composite laminates. Any help from other Python-enthusiast-engineers like the author will be greatly appreciated. Please, contact me if you want to collaborate.
