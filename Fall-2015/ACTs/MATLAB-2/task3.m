% Activity: MATLAB 2 Bonus, Task 3
% File: ML2_ACT_Task3_katherto.m
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
% This function plots the function sin(x) with various 
% steps of x values. 

% clear the command window of previous variables and functions
clear
clc

% set the values for x
x = 0:2:10;

% set the function for y
y = sin(x);

% graph the function y vs x
plot(x, y)

%% new section

% plot on the same graph
hold on

% set the values for x
x = 0:1:10;

% set the function for y
y = sin(x);

% graph the function y vs x
plot(x,y)


%% new section

% set the values for x
x= 0:0.01:10;

% set the function for y
y = sin(x);

% graph the function y vs x
plot(x,y)

