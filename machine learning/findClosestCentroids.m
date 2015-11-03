function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Set K
K = size(centroids, 1);

%% DEBUG X = X(1:5,:)
% You need to return the following variables correctly.
idx = zeros(size(X,1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Go over every example, find its closest centroid, and store
%               the index inside idx at the appropriate location.
%               Concretely, idx(i) should contain the index of the centroid
%               closest to example i. Hence, it should be a value in the 
%               range 1..K
%
% Note: You can use a for-loop over the examples to compute this.
%


m = size(X,1);

for i = 1: m
    A_init = inf; %re-initialize A for each new data point X(i)

    for j = 1:K
        % calculate absolute distance
        A = (norm( X(i,:) - centroids(j,:))).^2;
    
        if (A <= A_init)
            A_init = A;
            idx(i) = j  ;       % this has to be idx(i) not j, because this is index for
                                % each training example X(i) AND equal to j,
                                % which runs through the space of all centroids
           %% fprintf( [' this is iteration: %d %d \n' ],i, j);
        end
    end
end

idx(1:3)

% =============================================================

end

