function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returs the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. You should return a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%

% Useful variables
[m n] = size(X);

% You need to return the following variables correctly.
centroids = zeros(K, n);


% ====================== YOUR CODE HERE ======================
% Instructions: Go over every centroid and compute mean of all points that
%               belong to it. Concretely, the row vector centroids(i, :)
%               should contain the mean of the data points assigned to
%               centroid i.
%
% Note: You can use a for-loop over the centroids to compute this.
%

% # centroids
idx_length = size(idx,1);

Csum = zeros(K,1);
x_sum = zeros(K,n);


for i = 1 : K                                   %loop over all centroids
  %fprintf (' loop/centroid number %d \n', i)
    for j = 1: idx_length                       % loop over all data points/all indices

        %simple = 0
        if idx(j) == i                          % perform if current index equal to current centroid
            Csum(i) = Csum(i) +1;

            for a = 1:n                         % sum seperately all columns n, of data X
                x_sum(i,a) = x_sum(i,a) + X(j,a);  %if j is the correct index sum up )
            end
        end

    end
end

for i = 1 : K
    for a = 1:n
        centroids(i,a) =   x_sum(i,a)/(Csum(i));  % find the new centroids but taking average
    end
end






% =============================================================


end

