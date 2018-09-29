function [ H_P_given_X ] = cEntropy( X_col, Y_col, X_f, X, surveyDataSet )
  
    Pr_X = Pr_Feature( X, X_col, X_f );

    %H(Y_col|X_col = a)
    temp = surveyDataSet(:, [X_col Y_col]);
    Pr_P_given_X = zeros(X_f, 2);
    H_P_given_X = 0;

    for j=1:X_f %j=X_col
        for i=1:2 %i = Purchase
            Pr_1_2 = sum(temp(:, 1) == (j-1) & temp(:, 2) == (i-1))/size(temp, 1);
            Pr_P_given_X(j, i) = Pr_1_2/Pr_X(j);
        end
        H_P_given_X = H_P_given_X + Pr_X(j)*entropyCalc(Pr_P_given_X(j, :));
    end
end

