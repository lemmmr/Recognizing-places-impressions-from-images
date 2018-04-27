setwd("/Users/lemr/Documents/EPFL/Tercer_Semestre/COM-405_Optional_project_in_communication_systems/")
cat("\014")  
for (file in list.files("r_results")){
  print(paste0(file))
  cat("\n\n")
  print(readRDS(paste0("r_results/",file)))
  cat("\n\n")
}
