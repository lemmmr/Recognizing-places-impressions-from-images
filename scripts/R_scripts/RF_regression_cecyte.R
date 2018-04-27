library(randomForest)
library(caret)

setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems/")

#Reading features csv files:
#Note: just uncomment the lines of the dataset you want to use and comment for the other datasets

############################################
##CECYTE - All semantic descriptors - Mode##
############################################
df_features <- read.csv("datasets/cecyte_all_places_descriptors_mode.csv",header=TRUE,sep=",")
#Adding new headers
colnames(df_features) <- c("annotation",paste0("feat_", seq(1:(ncol(df_features)-1))))

############################################
##CECYTE - All semantic descriptors - Mean##
############################################
#df_features <- read.csv("datasets/cecyte_all_places_descriptors_mean.csv",header=TRUE,sep=",")
#Adding new headers
#colnames(df_features) <- c("annotation",paste0("feat_", seq(1:(ncol(df_features)-1))))

############################################################################
#Reading the csv file with the labels

#####################
##CECYTE - 6 labels##
#####################
df_labels <- read.csv("datasets/cecyte_all_places_six_labels.csv")
labels <- colnames(df_labels[,!colnames(df_labels) %in% c("imageName")])
#Adding new headers
colnames(df_labels) <- c("annotation",labels)

###########################
##MTurk - all (12) labels##
###########################
#df_labels <- read.csv("datasets/all-places-all-labels-median-medina.csv")
#df_labels <- df_labels[,!colnames(df_labels) %in% c("city")]
#labels <- colnames(df_labels[,!(colnames(df_labels) %in% c("annotation"))])

#Merging everything
df_merge <- merge(df_features, df_labels, by.x=c("annotation"), by.y=c("annotation"))

#Initializing Data Frames
df.fit <- list()
df.fit.summary <- data.frame(stringsAsFactors=FALSE)
df.fit.summary <- rbind(df.fit.summary, c(0,0,0,0))

#Training the Random Forest for each of the labels.
for (label in labels){
  print(paste0("Processing label: ", label))
  
  #Defining a temporary data frame for analyzing each label.
  df_temp <-df_merge[, c(label, grep("feat",colnames(df_merge),value=TRUE))]
  
  #Training the model
  df.fit[[label]] <- train(x=df_temp[,grep("feat",colnames(df_temp),value=TRUE)], y=df_temp[,label], method="rf", ntree=1000, importance=FALSE, preProcess=NULL, trControl=trainControl(method = "repeatedcv",repeats=1, returnResamp="none",savePredictions = FALSE,verboseIter = TRUE),tuneGrid=expand.grid(mtry= floor(ncol(df_temp[, grep("feat", colnames(df_temp), value=TRUE)])/3)))
  
  #Getting RMSE
  baseline.rmse <- sqrt(mean( (df_temp[, label] - mean(df_temp[, label]))^2 )) # Baseline RMSE
  df.fit.summary <- rbind(df.fit.summary, c(label, baseline.rmse, df.fit[[label]]$results$RMSE, df.fit[[label]]$results$Rsquared))
}
df.fit.summary <- df.fit.summary[-1,]
colnames(df.fit.summary) <- c("feature", "baselineRMS", "rfRMSE", "rsquared")
saveRDS(df.fit.summary, "regression_cecyte_mode_descriptors_6_labels_results.rds")