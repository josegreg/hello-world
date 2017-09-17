library(dplyr)
library(Rcpp)


dir<-getwd()



subdir<-file.path(dir,"cleaninig data")
subdir
if (file.exists(subdir)){
  setwd(subdir)
} else {
  dir.create(subdir)
  setwd(subdir)
}


download.file(url="http://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip",destfile="./Dataset.zip", mode = 'wb' )
unzip("./Dataset.zip",exdir="../cleaninig data")
setwd("../cleaninig data/UCI HAR Dataset")


#Load the features file in  a data frame
feat <- read.table(file="features.txt",sep="\n",stringsAsFactors = FALSE)
View(feat)


#store it as an array#
LR<-feat$V1
LR



##load the activities for test and train data 
y_test <-read.table(file="./test/y_test.txt", sep="\n")
#View(y_test)

y_train <-read.table(file="./train/y_train.txt",sep="\n")
#View(y_train)

#Load the test measurements and add two columns
X_test<-read.table(file ="./test/X_test.txt")
#View(X_test)

X_test$desc <- "test"
X_test$meas <- y_test$V1

#Load the train measurements and add two additional info columns
X_train<-read.table(file="./train/X_train.txt")
X_train$desc<-"train"
X_train$meas <- y_train$V1


##Paste the tables
X_table <- rbind(X_train,X_test)

##Add the column names
colnames(X_table)<-c(as.character(LR),"desc","Activity")
View(X_table)


##Keep the mean and std and an identifier
tabla_0<-select(X_table, contains("mean"),contains("std"),"desc","Activity")
View(tabla_0)
act<-read.table(file="./activity_labels.txt")
colnames(act)<-c("Activity","Description_activity")

Table_1<-left_join(tabla_0, act, by = "Activity") %>% arrange(.,Activity) %>% select(.,"desc","Activity","Description_activity",contains("mean"),contains("std"))
View(Table_1)
colnames(Table_1)



Table_2<-select(Table_1,-contains("angle"))
name_col<-colnames(Table_2)
name_col<-gsub("BodyAcc","_Body_acceleration_",name_col)
name_col<-gsub("BodyGyro","_Body_angular_velocity_",name_col)
name_col<-gsub("GravityAcc","_Gravity_Acceleration_",name_col)
name_col<-gsub("Mag","_norm_2",name_col)
name_col<-stringr::str_split_fixed(name_col," ",2)[,2]


name_col[1]<-"desc"
name_col[2]<-"Activity"
name_col[3]<-"Description_Activity"

colnames(Table_2)<-c(name_col)

View(Table_2)
#######################################################################################
## From the data set in step 4, creates a second, independent tidy 
## data set with the average of each variable for each activity and each subject
########################################################################################
Table_3 <- select(Table_2,-desc) %>% group_by(.,Activity,Description_Activity) %>% summarise_all(.,mean) 
View(Table_3)
colnames(Table_3)

######################################################################################
saveRDS(Table_2,file="Dataset_1")
saveRDS(Table_3,file="Dataset_2")
write.table(Table_3,file="./Dataset_step5.txt", row.name = FALSE)
