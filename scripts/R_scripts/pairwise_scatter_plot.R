require(lattice)
require(ggplot2)
setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems/")

#Reading CECYTE's annotations
df_labels_cecyte <- read.csv("datasets/cecyte_all_places_six_labels.csv")
labels <- colnames(df_labels_cecyte[,!colnames(df_labels_cecyte) %in% c("imageName")])

#Reading MTurk's annotations
df_labels_mturk <- read.csv("datasets/all-places-all-labels-median-medina.csv")
df_labels_mturk <- df_labels_mturk[,c("annotation",labels)]

#Merging both dataframes
df_merge <- merge(df_labels_cecyte,df_labels_mturk,by.x="imageName",by.y="annotation")

#Pair-wise scatterplot
#Dangerous
p <- ggplot(df_merge, aes(x=Dangerous.x, y=Dangerous.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/dangerous.jpg"),width=4,height=4)
dev.off()

#Dirty
p <- ggplot(df_merge, aes(x=Dirty.x, y=Dirty.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/dirty.jpg"),width=4,height=4)
dev.off()

#Pretty
p <- ggplot(df_merge, aes(x=Pretty.x, y=Pretty.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/pretty.jpg"),width=4,height=4)
dev.off()

#Interesting
p <- ggplot(df_merge, aes(x=Interesting.x, y=Interesting.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/interesting.jpg"),width=4,height=4)
dev.off()

#Polluted
p <- ggplot(df_merge, aes(x=Polluted.x, y=Polluted.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/polluted.jpg"),width=4,height=4)
dev.off()

#Pleasant
p <- ggplot(df_merge, aes(x=Pleasant.x, y=Pleasant.y)) 
p <- p + geom_count(shape=1) + scale_size_area(max_size = 15) + geom_abline(linetype="dashed")
p <- p + theme_bw() + scale_x_continuous("CECYTE",breaks = c(1,2,3,4,5,6,7))
p <- p + scale_y_continuous("MTurkers",breaks = c(1,2,3,4,5,6,7))
p <- p + coord_cartesian(ylim=c(1, 7), xlim=c(1,7))
p <- p +theme(
  legend.position="none",
  panel.grid.minor.y = element_blank(),
  panel.grid.minor.x = element_blank()
)
p
ggsave(paste0("plots/pairwise_analysis/pleasant.jpg"),width=4,height=4)
dev.off()

