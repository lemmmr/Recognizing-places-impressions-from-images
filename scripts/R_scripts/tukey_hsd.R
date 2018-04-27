setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems/")
###################
#Mturk annotations#
###################
df_labels_mturk <- read.csv("datasets/all-places-all-labels-median-medina.csv")

####################
#CECYTE annotations#
####################
df_labels_cecyte <- read.csv("datasets/cecyte_all_places_six_labels.csv")

#Getting the 6 labels to analyze
labels <- colnames(df_labels_cecyte[,!colnames(df_labels_cecyte) %in% c("imageName")])

#Initializing dataframe
df_tukey_hsd_summary <- data.frame()

for (label in labels){
  #Getting Ratings for each label
  df_mturk_temp <- data.frame("MT",df_labels_mturk[label])
  colnames(df_mturk_temp) <- c("Rater","Rating")
  df_cecyte_temp <- data.frame("LO",df_labels_cecyte[label])
  colnames(df_cecyte_temp) <- c("Rater","Rating")
  
  #Concatening the two dataframes
  df_mturk_cecyte <- rbind(df_mturk_temp,df_cecyte_temp)
  
  #Analysis of Variance
  aov.temp <- aov(Rating~Rater,df_mturk_cecyte)
  
  #Tukey HSD
  tukey.temp <- TukeyHSD(aov.temp,"Rater")
  
  df_tukey_hsd_summary <- rbind(df_tukey_hsd_summary, data.frame(label,tukey.temp$Rater))
}
saveRDS(df_tukey_hsd_summary, "r_results/tukey_hsd_results.rds")
