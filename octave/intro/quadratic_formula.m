% quadratic_formula.m

% Quadratic root finder
% a*x^2 + b*x + c = 0
% https://en.wikipedia.org/wiki/Quadratic_formula

function [root1, root2] = quadratic_formula(a, b, c)
    discriminant = b^2 - 4 * a * c;
    root1 = (-b + sqrt(discriminant)) / (2 * a);
    root2 = (-b - sqrt(discriminant)) / (2 * a);
endfunction
