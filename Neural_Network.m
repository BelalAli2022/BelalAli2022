%NN has one hidden network and 8 Coefficients
% w is the parameters matrix (N*8)
clear;
alpha = 0.25 ;
coef = 8 ;  % no. of coefficients
N = 200 ;    %number of samples
n= 1: N ;
x = sin (2* pi* 0.01* n);  %input signal
des = x ;      % Desired signal
w= rand ( N , coef );     %random w coefficients
repitions = 250 ;
tic
for rep = 1: repitions
    for n = 1 : N-2
         % Forward Calculation
        u1(n)=( x(n) * w(n,1 ))+( x(n+1)* w(n,3) ) + ( x(n+2) * w(n,5 ));
        u2(n)=( x(n) * w(n,2))+( x(n+1) * w(n,4) )+( x(n+2) * w(n,6) );
        y1(n)= tanh( u1 ( n ) );       %output of hidden layer y1 
        y2(n)= tanh( u2 ( n )  );        %output of hidden layer y2
        u(n)=( y1(n) * w(n,7)) + ( y2(n) * w(n,8) );  %output u
        y(n)= tanh( u( n ) ) ;              %output sample y
        % Backward calcultion
        error ( n ) = y ( n ) - des ( n );
        %update wheights of the output neuron
        w(n,7) = w(n,7) - (alpha * error ( n ) * y1 ( n )); 
        w(n,8) = w(n,8) - (alpha * error ( n ) * y2 ( n ));
       %error at hidden layer
        segma1(n)= y1(n) * ( y1(n) -1 )* error( n ) * w(n,7);
        segma2(n)= y2(n) * ( y2(n) -1 ) * error( n )* w(n,8);
       %update wheights of hidden layer
       w( n ,1 ) = w ( n , 1 ) - alpha *segma1 (n) * x( n );
       w( n ,3 ) = w ( n , 3 ) - alpha *segma1 (n) * x( n + 1 );
       w( n ,5 ) = w ( n , 5 ) - alpha *segma1 (n) * x( n + 2 );
       w( n ,2 ) = w ( n , 2 ) + alpha *segma2 (n) * x( n );
       w( n ,4 ) = w ( n , 4 ) + alpha *segma2 (n) * x( n + 1 );
       w( n ,6 ) = w ( n , 6 ) + alpha *segma2 (n) * x( n + 2 );
     
       E(rep,n) = error(n);
    end
end
toc
rep = 1:repitions;
subplot(2,1,1)
plot(rep, E(:,6).^2) %plot error of column 6( sample 6) with reps.
title('Learning Curve');
n= 1: N-2;
m = 1 : N;
subplot(2,1,2)
plot(n ,y , m , x)
title('Input and Output Signal')



    


