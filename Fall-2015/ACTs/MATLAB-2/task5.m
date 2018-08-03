% Activity no.: Matlab 2, Task 5
% File: ML2_ACT_Task5_katherto.m
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
% The function takes an inpu, and then returns the pin related to that
% input

% clear the command window of all functions
clc
clear

function x = ML2_ACT_Task5_katherto
%Function takes th einput user, and then uses the indexing of the matrix
%"pin" to look for the pin related to the input
%   Inputs:
%       user -- Number of the pin that the user needs 
%   Outputs:
%       x -- Pin related to the user input

% Matrix pin with the 3 different pins (3 rows)
pin = ['LQFP100'; 'LQFP144';'LQFP176'];
% x is assigned to the row that contains the pin related to the number
% imputted, 1 corresponds to row 1, 2 to 2, etc.
x = pin(user, :);
% end the function
end 
