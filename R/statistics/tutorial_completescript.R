# Set-Up
# ======
#
# Clear Environment Variables
# ---------------------------
# Remove any values you have stored from previous runs.
rm(list = ls())

# Change Your Working Directory
# -----------------------------
# By default, RStudio sets your working directory (ie the folder everything gets imported from, exported to and run from) to you home directory. This will be:
# - `/Users/<yourname>/` on macOS
# - `/home/<yourname>/` on Linux
# - `C:\Users\` on Windows
#
# Change this to be the same folder as the one your script is saved in:
setwd(dirname(parent.frame(2)$ofile))

# Packages
# ========
# For this tutorial you will need the 'titanic', 'knitr', 'ggplot2' and 'pROC' packages.
# The data will come from 'titanic'; see its documentation here: https://www.rdocumentation.org/packages/titanic/versions/0.1.0
#
# Install Packages
# ----------------
# When you want to use functionality that is part of a particular package, you need to import the package as a library in the script:
#
# ### RStudio
# - Packages → Install → search & install
# - Check that it appears in the list of packages
#
# ### Manually
# install.packages("titanic", repos = "http://cran.us.r-project.org")
# install.packages("knitr", repos = "http://cran.us.r-project.org")
# install.packages("ggplot2", repos = "http://cran.us.r-project.org")
# install.packages("pROC", repos = "http://cran.us.r-project.org")

# Import Libraries
# ----------------
library(titanic)
library(knitr)
library(ggplot2)
library(pROC)

# Preview the Data
# ================
# The titanic dataset is actually split into two: a 'training' subset and a 'test' subset. We're going to be working with the training subset, which is called `titanic_train`.
#
# When previewing the data, don't look at all of it at once because you don't know how much there is. If there is a massive amount it might crash RStudio! Instead, only look at the first few rows to get a general idea. This can be done by using the `head()` function:
#
# Print to Console
# ----------------
print(head(titanic_train))

# Print Using Kable
# -----------------
# Kable is a table generator which comes from the knitr package. It can automatically convert tables to HTML, Latex or Markdown format, making it easy to add them to a report or a webpage.
print(kable(head(titanic_train)))

# Export the Data
# ===============
# This step isn't actually necessary, but for the sake of this tutorial let's export the dataset to csv. You'll then be able to open it in Excel or Calc and share or save it.
write.csv(titanic_train, "titanic_train.csv")

# There should now be a file called "titanic_train.csv" in the same folder where this script is saved.
#
# Import the Data
# ===============
# Again, this step isn't necessary but for the sake of completeness let's import the csv we just exported:
df <- read.csv("titanic_train.csv")

# The data has been imported as a **data frame** and assigned to the variable **df**. A data frame is the fundamental data type in R; it's essentially a table of data where each column has a column heading and each row (usually) only has a number (ie there are no row names, only row numbers). Have a look at the column headings here:
print(colnames(df))

# ...and the number of rows here:
print(nrow(df))

# Data Manipulation
# =================
# We can chop and change the data frame to look exactly how we want it:
#
# Select Columns
# --------------
# Remove all columns except 'Name', 'Sex' and 'Age':
subset <- subset(df, select = c("Name", "Sex", "Age"))
print(head(subset))

# Search the Data
# ---------------
# Was there a Mr James Flynn onboard?
bool <- "Flynn, Mr. James" %in% df$"Name"
print(bool)

# Find Data
# ---------
# In which row is Miss Joan Wells?
idx <- match("Wells, Miss. Joan", df$"Name")
print(idx)

# Filter
# ------
# Let's look at only the passengers in third class:
subset <- subset(df, Pclass == "3")
print(head(subset))

# Now only the passengers between the ages of 20 and 30:
subset <- subset(df, Age >= 20 & Age < 30)
print(head(subset))

# How much was the cheapest, most expensive, average and median ticket?
min <- min(df$Fare)
max <- max(df$Fare)
mean <- mean(df$Fare)
median <- median(df$Fare)
print(min)
print(max)
print(mean)
print(median)

# Box Plot
# ========
# Let's ask the following question: were those people who paid more for their ticket more likely to survive? It's a bit hard to even guess at the answer just by scanning your eye down the table of numbers, so let's try visualising the data first. This can be done with a box plot (aka a box-and-whisker plot):
boxplot(Fare~Survived, data = df)

# The `boxplot()` function will create the graph for us, and the arguments we specified will tell it what to do:
# - The `data` keyword argument was set equal to `df` as that is the dataset we want to use
# - The two columns within the `df` data frame that we want to use are `Fare` on the y-axis and `Survived` on the x-axis. R uses the tilde symbol (~) - which means 'proportional to' in statistics - to specify which variable is being set proportional to another in the plot. Notice that the argument was `Fare~Survived`, ie the dependant variable was named first.
#
# This figure can be made more attractive by customising the function's settings, which won't be discussed here. However, a quick way to get a better-looking graph would be to re-do it with the `ggplot2` package:
df$"Survived"[df$"Survived" %in% 0] <- "Died"
df$"Survived"[df$"Survived" %in% 1] <- "Lived"
p <- ggplot(df, aes(Survived, Fare))
p <- p + geom_boxplot()
p <- p + ggtitle(
    "Were the passengers more likely to survive if they had paid more?"
)
p <- p + xlab("")
print(p)

# As you can see, this is more complicated but it arguably produces a nicer figure.

# Statistical Significance
# ========================
# Is this difference significant? We can't immediately assume that the data is Normally distributed, so let's use a non-parametric method such as the Wilcox test/Mann-Whitney U test to decide if one group is larger than the other (hint: in order to separate the two groups - Died and Survived - we will have to filter the data frame before performing the Wilcox test):
died <- subset(df, Survived == "Died")$Fare
lived <- subset(df, Survived == "Lived")$Fare
test <- wilcox.test(died, lived, alternative = "two.sided")
print(test$p.value)

# That's pretty convincing. Therefore, it's safe to conclude that a passenger who paid a higher fare would have been more likely to survive than one who paid a lower fare.

# Categorisation
# ==============
# Now let's ask a slightly different question: can a passenger's fare price be used to predict where or not they survived?
#
# Let's create a predictive test. Recall that the median ticket price paid by passengers was £14.45 (we calculated that using `median(df$Fare)`), so let's use that as a cut-off and make the follow predictions:
# - Any passenger who paid more than £14.45 survived
# - Any passenger who paid less than (or equal to) £14.45 died
# Is this prediction any good? Let's investigate. Create a new column called `Prediction` that predicts whether each passenger survived or died - ie it categorises them into 'predicted to survive' and 'predicted to die' groups (hint: if the fare was larger than 14.45, the prediction is that they lived, else it's that they died):
df$prediction <- ifelse(df$Fare > 14.45, "Lived", "Died")
print(head(df[c("Fare", "prediction")]))

# The next steps aren't strictly necessary, but they change the statistically 'positive' outcome of our test from 'Died' to 'Survived'. Try commenting out the following four lines and running the code that follows this. Then uncomment them and run it again to see what change they make.
df$prediction <- factor(df$prediction)
df$prediction <- relevel(df$prediction, ref = "Lived")
df$survived <- factor(df$Survived)
df$survived <- relevel(df$survived, ref = "Lived")

# Diagnostic Accuracy
# ===================
# We can investigate the accuracy of our test by creating a confusion matrix (https://en.wikipedia.org/wiki/Confusion_matrix) (hint: this is a table that compares a test with a 'ground truth' reference):
cm <- table(test = df$prediction, ref = df$survived)
print(cm)
print(nrow(df))

# Some of our 'positive' predictions (that the passenger survived) came true while some were false. Some of our 'negative' predictions (that the passenger died) came true while some were false. Extract the number of true positives, false positives, false negatives and true negatives from the confusion matrix (hint: this will require 2-dimensional indexing because a confusion matrix has two dimensions):
tp <- cm[1, 1]
fp <- cm[1, 2]
fn <- cm[2, 1]
tn <- cm[2, 2]
print(tp)
print(fp)
print(fn)
print(tn)

# We have all the information we need to calculate the four most important results of a confusion matrix investigation:
# - Sensitivity: how good is our test at predicting who survived?
# - Specificity: how good is our prediction at picking up who died?
# - Positive predictive value: if our test predicted that a passenger survived, how much value does that information have to us?
# - Negative predictive value: if our test predicted that a passenger died, how much value does that information have to us?
sens <- tp / (tp + fn)
spec <- tn / (tn + fp)
ppv <- tp / (tp + fp)
npv <- tn / (tn + fn)
print(sens)
print(spec)
print(ppv)
print(npv)

# Unfortunately these values aren't very good! Maybe it's because the cut-off we chose (14.45) wasn't good? We'll have to investigate how the sensitivity and specificity change when we use different cut-offs.

# Receiver Operating Characteristic Curve
# =======================================
# A ROC curve illustrates how the diagnostic accuracy (ie the sensitivity and specificity) of a binary classification test (eg predicting whether a passenger survived or died) changes as its threshold changes. Fortunately for us, there is a function that can do most of the work for us (hint: this function calculates the receiver operating characteristic):
r <- roc(Survived~Fare, data = df)

# Have a look at some of the thresholds (ie values for fare that will be taken as cut-offs) that this function produced:
print(head(r$thresholds))

# Plot Using Base R
# -----------------
plot(r, type = "S")

# Get the area under the curve and the 95% confidence interval of this area (which should be rounded off to 2 decimal places):
auc <- auc(r)
ci <- ci.auc(r)
ci_l <- round(ci[1], 2)
ci_u <- round(ci[3], 2)

# Add this information to the graph:
legend_text <- paste0(
    "AUC = ", round(auc, 2), " (95% CI = ", ci_l, " - ", ci_u, ")"
)
legend("bottomright", legend = legend_text, pch = 15)

# Plot Using ggplot2
# ------------------
p <- ggroc(r)
p <- p + ggtitle("Receiver Operating Characteristic Curve")
p <- p + geom_segment(
    aes(x = 1, xend = 0, y = 0, yend = 1), color = "grey", linetype = "dashed"
)
p <- p + scale_y_continuous(expand = c(0, 0))
p <- p + scale_x_reverse(expand = c(0, 0))
print(p)

# The area under the curve is 0.69; not particularly high! It seems that - despite the fact that the Mann-Whitney U test was highly significant - fare can't be used as an accurate predictor of passenger survival!
