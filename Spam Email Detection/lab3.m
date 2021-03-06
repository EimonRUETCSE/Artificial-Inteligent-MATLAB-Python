%application of naive bayes for spam/non spam classification

%load the dataset

%load the features
numTrainDocs = 700;
numTokens = 2500;
M = dlmread('train-features.txt', ' ');
spmatrix = sparse(M(:,1), M(:,2), M(:,3), numTrainDocs, numTokens);
train_matrix = full(spmatrix);

%load the labels
train_labels = dlmread('train-labels.txt');

%need to binarize the term-frequency matrix aka the train_matrix
train_matrix_bin = (train_matrix >= 1);

%calculate prior probabilities


p_Spam = sum(train_labels == 1) /length(train_labels);
p_Non_Spam = 1- p_Spam;

%calculate the conditional probabilities

P_Cond(:,1) = (transpose(train_matrix_bin)*(train_labels))+1;%laplacian smoothing
P_Cond(:,1) =P_Cond(:,1)/ (sum(train_labels == 1)+2);%laplacian smoothing

train_labels_n=double((train_labels <= 0));

P_Cond(:,2) = (transpose(train_matrix_bin)*(train_labels_n))+1;%laplacian smoothing
P_Cond(:,2) =P_Cond(:,2)/ (sum(train_labels == 0)+2);%laplacian smoothing

%load the test features
M = dlmread('test-features.txt', ' ');
spmatrix = sparse(M(:,1), M(:,2), M(:,3), numTrainDocs, numTokens);

test_matrix = full(spmatrix);

%binarize the test matrix
test_matrix_bin = (test_matrix >= 1);

test_labels = dlmread('test-labels.txt');

Result=zeros(260,1);

disp('No. of test email my model cant predict accurately')

for x=1:260

%consider only those conditional probabilities where the corresponding words belongs to
%given test email
temp1=P_Cond(test_matrix_bin(x,:),1);

P_Spam_Test=sum(log(temp1));

%consider only those conditional probabilities where the corresponding words belongs to
%given test email
temp2=P_Cond(test_matrix_bin(x,:),2);

P_NSpam_Test=sum(log(temp2));

Result (x,1) = ((P_Spam_Test>P_NSpam_Test)==(test_labels(x,:)));

%no. of email my model can't predict accurately
if (((P_Spam_Test>P_NSpam_Test)==(test_labels(x,:)))==0)
    disp(x);
end

x=x+1;
end

%calculate the accuracy in percentage
Accuracy=(sum(Result==1))/length(Result)*100






















