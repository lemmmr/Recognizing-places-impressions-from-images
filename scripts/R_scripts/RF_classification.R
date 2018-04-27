library(randomForest)
library(caret)
library(reshape2)
setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems/")

#Reading features csv files:
#Note: just uncomment the lines of the dataset you want to use and comment for the other datasets

####################################
##DilatedNet Semantic Segmentation##
####################################
#df_features <- read.csv("datasets/dilatednet_segmentation150-class_summary.csv",header=FALSE,sep=",")
#colnames(df_features) <- c("annotation",paste0("feat_", seq(1:(ncol(df_features)-1))))

#######################
##GoogLeNet places205##
#######################
df_features <- read.csv("datasets/googlenet_places205-class-prob-summary.csv",header=FALSE,sep=",")
#Adding new headers
colnames(df_features) <- c("annotation","most_prob_feat","prob",paste0("feat_", seq(1:(ncol(df_features)-3))))
#Removing "most_prob_feat" and "prob" columns
df_features <- df_features[,!colnames(df_features) %in% c("most_prob_feat","prob")]
#Renaming the images (in case of using the dataset "googlenet_places205-class-prob-summary.csv")
df_features$annotation <- gsub("GC_", "", df_features$annotation)
df_features$annotation <- gsub("SC_", "", df_features$annotation)
df_features$annotation <- gsub("LC_", "", df_features$annotation)

#######################
##GoogLeNet places365##
#######################
#df_features <- read.csv("datasets/googlenet_places365-class-prob-summary.csv",header=FALSE,sep=",")
#Adding new headers
#colnames(df_features) <- c("annotation","most_prob_feat","prob",paste0("feat_", seq(1:(ncol(df_features)-3))))
#Removing "most_prob_feat" and "prob" columns
#df_features <- df_features[,!colnames(df_features) %in% c("most_prob_feat","prob")]

############################################################################
#Reading labels csv file:
#Note: just uncomment the lines of the dataset you want to use and comment for the other datasets

##########################
##Mturk labels binarized##
##########################
df_labels <- read.csv("datasets/labels_bin.csv")
labels <- colnames(df_labels)[!colnames(df_labels) %in% c("annotation")]

############################################################################
#Merging everything
df_merge <- merge(df_features,df_labels, by.x=c("annotation"), by.y=c("annotation"))

#Initializing Data Frame for the results
df.fit <- list()
df.fit.summary <- data.frame(stringsAsFactors=FALSE)
df.fit.summary <- rbind(df.fit.summary, c(0,0,0,0))

#Training the Random Forests for each label
for (label in labels){
  print(paste0("Processing label: ", label))

  #Defining a temporary data frame for analyzing each label.
  df_temp <-df_merge[, c(label, grep("feat",colnames(df_merge),value=TRUE))]
  
  #Training the model
  df.fit[[label]] <- train(x=df_temp[,grep("feat",colnames(df_temp),value=TRUE)], y=factor(df_temp[,label]), method="rf", ntree=1000, importance=FALSE, preProcess=NULL, trControl=trainControl(method = "repeatedcv",repeats=4, returnResamp="all",savePredictions = FALSE,verboseIter = TRUE,sampling = "down"),tuneGrid=expand.grid(mtry= floor(ncol(df_temp[, grep("feat", colnames(df_temp), value=TRUE)])/3)))

  #Getting RMSE
  baseline.rmse <- sqrt(mean( (df_temp[, label] - mean(df_temp[, label]))^2 )) # Baseline RMSE
  df.fit.summary <- rbind(df.fit.summary, c(label, baseline.rmse, df.fit[[label]]$results$Accuracy, df.fit[[label]]$results$Kappa))
}
df.fit.summary <- df.fit.summary[-1,]
colnames(df.fit.summary) <- c("feature", "baselineRMS", "rfAccuracy", "kappa")
saveRDS(df.fit.summary, "r_results/classification_places205_results.rds")
