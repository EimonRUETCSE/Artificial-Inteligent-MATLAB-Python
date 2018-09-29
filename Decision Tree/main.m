%load surveyDataSet
load surveyDataSet.txt

%feature set
X = surveyDataSet(:,1:4);

%output
Y = surveyDataSet(:,5);

%Probability of Purchase
Pr_P = Pr_Feature( Y, 1, 2 );

%Entropy of Purchase
H_P = entropyCalc(Pr_P);

%Specific Conditional entopy --> H(Purchase|Age = a)
H_P_given_Age = cEntropy(1, 5, 4, X, surveyDataSet);

%Information Gain => IG(Purchase,Age)
IG_P_Age = H_P - H_P_given_Age;

%Specific Conditional entopy --> H(Purchase|Marital Status = a)
H_P_given_Marital = cEntropy(4, 5, 2, X, surveyDataSet);

%Information Gain --> IG(Purchase;Marital Status)
IG_P_Marital = H_P - H_P_given_Marital;

%Specific Conditional entopy --> H(Purchase|Income = a)
H_P_given_Income = cEntropy(3, 5, 2, X, surveyDataSet);

%Information Gain --> IG(Purchase,Income)
IG_P_Income = H_P - H_P_given_Income;

%Specific Conditional entopy --> H(Purchase|Education = a)
H_P_given_Education = cEntropy(2, 5, 3, X, surveyDataSet);

%Information Gain --> IG(Purchase,Education)
IG_P_Education = H_P - H_P_given_Education;

