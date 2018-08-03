% Activity: MATLAB 2 Bonus, Task 2
% File: ML2_ACT_Task2_katherto.m
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
% This progam plots two functions in various plots and 
% subplots, in separate graphs or on the same graph. 

% clear the command window of previous commands and functions
clear
clc
% Create vector X
X = -50:0.5:50;

% Calculate e^x
ex = 1 + (X / 1) + ((X .^ 2) / 2) + ((X .^ 3) / 6) + ((X .^ 4) / 24);

% Plot value of A = 2, two plots on same figure
A = 2;

% Calculate e'^x
e_x = A * (ex);

% Plotting
figure(1)
plot(X,ex,'b'),title('Equation 1 (blue) and Equation 2 (red)'),xlabel('X'),ylabel('e^x (blue), e''^x (red)')
hold on; 
plot(X,e_x,'r')
hold off;

% Plot value of A = 5, two subplots on same figure
A = 5;

% Calculate e'^x
e_x = A * (ex);

% Plotting
figure(2)
subplot(2,1,1),plot(X,ex),title('Equation 1'),xlabel('X'),ylabel('e^x')
subplot(2,1,2),plot(X,e_x),title('Equation 2'),xlabel('X'),ylabel('e''^x')
hold off;

% Plot value of A = 10, dotted lines in Equation 1, Red 
% Circular Markers in Equation 2
A = 10;

% Calculate e'^x
e_x = A * (ex);

% Plotting
figure(3)
plot(X,ex,':'),title('Equation 1 (dotted) and Equation 2 (red circles)'),xlabel('X'),ylabel('e^x (dotted), e''^x (red circles)')
hold on;
plot(X,e_x,'ro')
hold off;

% Plot value of A = 3, 4 subplots
A = 3;

% Calculate e'^x
e_x = A * (ex);

% Plotting
figure(4)
subplot(2,2,1),plot(X,ex,'b'),title('Equation 1 (blue) and Equation 2 (red)'),xlabel('X'),ylabel('e^x (blue), e''^x (red)')
hold on;
subplot(2,2,1),plot(X,e_x,'r')
hold off;
subplot(2,2,2),plot(X,ex,'b^'),title('Equation 1 (blue) and Equation 2(red)'),xlabel('X'),ylabel('e^x (blue), e''^x (red)')
hold on;
subplot(2,2,2),plot(X,e_x,'ro')
hold off;
subplot(2,2,3),plot(X,ex),title('Equation 1'),xlabel('X'),ylabel('e^x')
subplot(2,2,4),plot(X,e_x),title('Equation 2'),xlabel('X'),ylabel('e''^x')