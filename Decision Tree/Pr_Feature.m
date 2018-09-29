function [ Pr_Z ] = Pr_Feature( Z, Z_col, Z_f )

    Pr_Z = zeros(1,Z_f); %initialization
    for i=1:Z_f
        Pr_Z(i) = sum(Z(:,Z_col) == (i-1))/size(Z,1);
    end
    
end

