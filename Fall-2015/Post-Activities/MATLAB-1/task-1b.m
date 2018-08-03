% Activity: MATLAB 1 Post Activity
% File: ML1_PA_Task1b_katherto.m
% Date: 16 November 2014
% By: Kathryn Atherton
% katherto
% Section: 04
% Team: 59
%
% ELECTRONIC SIGNATURE
% Kathryn Atherton
%
% The electronic signature above indicates that the script
% submitted for evaluation is my individual work. I
% have a general understanding of all aspects of its
% development and execution.
%
% A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
% This program computes the cross sectional area of any 
% I-beam, given its height, width, and thickness, assuming
% that the thickness is the same in the vertical segment
% as it is in the horizontal segments. The program then 
% outputs the height, width, thickness, and cross-sectional
% area. 

%create a function to define the inputs and outputs

function [Height, Width, Thickness, Cross_Sectional_Area] = ...
ML1_PA_Task1b_katherto(Height, Width, Thickness)
% Finds the cross-sectional area of an I-beam given the height, width,
% and thickness.
% Inputs are in feet, separated only by commas. Outputs are Height, 
% Width, Thickness, and Cross-Sectional Area
	
	Cross_Sectional_Area = (2 * (Width * Thickness)) ...
	+ ((Height - (2 * Thickness)) * Thickness);
	Height = Height;
	Width = Width;
	Thickness = Thickness;
	
	%print statements
	fprintf('Height = %.1f ft\n', Height)
	fprintf('Width = %.2f ft\n', Width)
	fprintf('Thickness = %.3f ft\n', Thickness)
	fprintf('Cross-Sectional area = %.2f sq. ft', Cross_Sectional_Area)

end


	
	