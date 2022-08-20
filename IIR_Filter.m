% a, b is the IIR_filter parameters matrix (N*order)
clear;
alpha = 0.25 ;
order = 5 ;
N = 200 ;    %number of samples
n= 1: N ;
repitions = 250 ;
x = sin (2* pi* 0.01* n);  %input signal
des = x ;      % Desired singal
a= rand ( N , order );     %random a parameters
b= rand ( N , order );     %random b parameters
%Forward calculation
%y(n)= a(1)*x(n-1)+a(2)*x(n-2)+a(3)*x(n-3) - b(1)*y(n-1) -b(2)*y(n-2)-b(3)*y(n-3) ;      for example
tic
for rep = 1: repitions
    y = zeros( N , 1);
    for n = order + 1 : N
        for p = 1 : order
            y(n) = y(n) +  (a(n , p) * x( n - p)) - (b(n , p)* y( n - p ));     %Summation process of IIR filter
        end
       error( n ) =  y( n ) - des( n );        %Backward calcultion
    
       for p = 1 : order
           a( n , p ) = a( n , p )- (alpha * error( n ) * x( n - p )); %update filter parameters (a)
           %b( n , p ) = b( n , p )- (alpha * error( n ) * x( n - p )); %update filter parameters (b)
       end
        E(rep,n) = error(n);
    end
end
  toc  
rep = 1:repitions;
subplot(2,1,1)
plot(rep, E(:,6).^2) %plot error of column 6( sample 6) with reps.
title('Learning Curve');
n= 1: N;
subplot(2,1,2)
plot(n ,y , n , x)
title('Input and Output Signals')
%plot(n ,x)
%title('Input Signal')

    


