function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));
[m, n] = size(X);
% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

reg_cost_mult=ones(1,n)
reg_cost_mult(1)=0

J=((ones(1, m)*((-1.*y).*log(sigmoid(([theta]' * [X]')')) - (1.-y).*log(1.-(sigmoid(([theta]' * [X]')')))))/m) + ((lambda/(2*m))*(reg_cost_mult*(theta.^2)))

reg_grad_add=((lambda/m)*theta)
reg_grad_add(1)=0

grad=((((( ones(1,2) *([sigmoid(([theta]' * [X]')'), -1*y]') ) * X )')/m)) + reg_grad_add


% =============================================================

end
