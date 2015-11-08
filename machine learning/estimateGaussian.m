function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
% 

% Useful variables
[m, n] = size(X);

% You should return these values correctly
mu = zeros(n, 1);
sigma2 = zeros(n, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%


mu = (1/m).*sum(X);


%recall that bsxfun, defined as C = bsxfun(fun,A,B), is the element-wise binary operation
% specified by the function handle fun, to the arrays A and B.
% in this case use bsxfun(@minus ....) for the element-wise subtraction of the mean
% also, writing it like this avoids the annoying broadcasting message!

sigma2 = (1/m).* sum( bsxfun(@minus,X,mu).^2)




% =============================================================


end
