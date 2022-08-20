function [a , error ] = FIR_Filter( a, x, des)
% a is the adp_filter parameter matrix (n*order)
alpha = 0.25;
order = 5;
N = 200;    %number of samples
%Forward calculation
y = zeros( N , 1);

%y(n)=a(1)*x(n-1)+a(2)*x(n-2)+a(3)*x(n-3);      for example
for n = order + 1 : N
    for p = 1 : order
        y(n) = y(n) + a(n , p) * x( n - p);     %Summation process of the filter
    end
    
    error( n ) =  y( n ) - des( n );        %Backward calcultion
    
    for p = 1 : order
        a( n , p ) = a( n , p )- (alpha * error( n ) * x( n - p )); %update filter parameters (a)
    end
end


    


