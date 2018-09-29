function [ Entropy ] = entropyCalc( V )

%vectorzed implementation
V (V == 0) = 1; %for handling log(0) case
Entropy = - sum(V.*log2(V));

end

