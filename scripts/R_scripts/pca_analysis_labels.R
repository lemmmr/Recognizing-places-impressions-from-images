#PCA graphical analysis
#Note: From the PCA analysis we did in python, we know that the 2 principal components explain approx. 77% of the variance
#this analysis is only to get the graphical representation
setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems")
#Loading "ggbiplot2" modified
source("scripts/ggbiplot2.R")
#Loading the labels file
df_labels <- read.csv("datasets/all-places-all-labels-median-medina.csv",header=TRUE,sep=",")
df_labels <- df_labels[,!colnames(df_labels) %in% c("city","annotation")]
#Getting the PCA compoments
labels.pca <- princomp(df_labels)
#Plotting the components in a 2-D space
g <- ggbiplot2(labels.pca, obs.scale=1, var.scale=1, groups=NULL,ellipse=FALSE,circle=TRUE,choices=1:2,scale=1,alpha=0,varname.adjust=1,varname.size=4.5)
g <- g + theme_bw()+geom_vline(xintercept=c(0,0),linetype=2,colour="black")+geom_hline(yintercept = 0,linetype=2,colour="black")
g <- g + coord_cartesian(xlim = c(-1.15, 1.15),ylim = c(-1.15, 1.15)) + ggtitle("PCA analysis") + theme(plot.title = element_text(hjust = 0.5))
print(g)
ggsave("plots/2pcs.png",width=8,height=8)

