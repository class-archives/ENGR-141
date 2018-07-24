% Activity no.: Matlab 2, Task 4
% File: ML2_ACT_Task4_katherto.m
% Date: 22 November 2015
% By: Natalie Zimmermann
% Login ID: zimmermn
% Kathryn Atherton
% Login ID: katherto
% Ryan Hellyer
% Login ID: rhellyer
% Section: 04, 3:30 - 5:30, C111
% Team: 59
%
% ELECTRONIC SIGNATURE
% Natalie Zimmermann
% Kathryn Atherton
% Ryan Hellyer
%
% The electronic signatures above indicate that the program
% submitted for evaluation is the combined effort of all
% team members and that each member of the team was an
% equal participant in its creation. In addition, each
% member of the team has a general understanding of
% all aspects of the program development and execution.
%
% A BRIEF DESCRIPTION OF WHAT THE PROGRAM OR FUNCTION DOES
% The program simmulates the throwing of three dice 100 times, and saves
% the results in a matrix with the function randi, then creates a histogram
% with the results.

% clear the command window of previous functions and commands
clear
clc

%Throw first die 100 times
die_one = randi (6, [1, 100]);

%Throw second die 100 times
die_two = randi (6, [1, 100]);

%Throw third die 100 times
die_three = randi (6, [1, 100]);

%Concatenate the three dice
dice = [die_one; die_two; die_three];

%Declare the number of bins
m = 6; 

%Create the histogram
h = histogram (dice, m);