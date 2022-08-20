clear all;
N = 200;  %number of samples
n = 1 : N;      
order = 5;  %filter order
x = sin (2*pi*0.01* n);  %input signal
des= x;      % Desired singal

%parameters
a= rand(N,order);     %random a parameters

tic
for rep= 1:250       %Training
    [a , E(rep,:) ] = FIR_Filter (a ,x ,des);   %E(rep,:) row(error of each sample) column(error after repitions)
end
toc
rep = 1:250;

y =zeros( N, 1);

for i = order+1: N
    for p = 1:order
        y(i) = y(i) + a(i, p) * x( i - p);     %Summation process of the filter
    end
end

subplot(2,1,1)
plot(rep, E(:,6).^2) %plot error of column 6( sample 6) with reps.
title('Learning Curve');

subplot(2,1,2)
plot(n ,y , n , x)
title('Input and Output Signals')
%plot(n ,x)
%title('Input Signal')


d = E.^2;
%Note: when you change N, you must clear variables in memory to not mismatch
