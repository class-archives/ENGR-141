% Activity: MATLAB 2 Bonus, Task 1
% File: ML2_ACT_Task1_katherto.m
% Date: 22 November 2015
% By: Kathryn Atherton
% katherto
% Ryan Hellyer
% rhellyer
% Natalie Zimmermann
% zimmermn
% 
% Section: 04
% Team: 59
%
% ELECTRONIC SIGNATURE
% Kathryn Atherton
% Ryan Hellyer
% Natalie Zimmermann
%
% The electronic signatures above indicate that the script
% submitted for evaluation is the combined effort of all
% team members and that each member of the team was an
% equal participant in its creation. In addition, each
% member of the team has a general understanding of all
% aspects of the script development and execution.
%
% A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
% This program is used to plot the values of Y with respect
% to the values of X in the function approximating the 
% value of sine of X in radians.

clc
clear

X = -50:.1:50

Y = X - (X .^ 3) / 6 + (X .^ 5) / 120 - (X .^ 7) / 5040

plot(X, Y, 'bs')
title('sin(x) vs angle')
xlabel('angle (radians)')
ylabel('sin(x)')
