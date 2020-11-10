# Ubuntu 20.04
# ------------
# 
# Install R
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
# sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
# sudo apt update
# sudo apt install r-base
# Run with `R`
#
# Install packages
# The default library location (/usr/local/lib/R/site-library) is not writable.
# Instead, open R in a terminal and run install.packages() there. It will offer
# to create a personal library for you. Use that to install all your packages.

# Needed by Debian:
# sudo apt-get install libssl-dev
# sudo apt-get install libcurl4-openssl-dev
# REPO FOR UBUNTU
# https://cloud.r-project.org/bin/linux/ubuntu

# install.packages("BlandAltmanLeh", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("brglm2", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("chron", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("devtools", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("DiagrammeR", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("dplyr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("emmeans", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("epiR", repos = "http://cran.us.r-project.org")
# install.packages("exact2x2", repos = "http://cran.us.r-project.org")
# install.packages("forestplot", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("formatR", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("gapminder", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("ggplot2", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("ggpubr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("gtools", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("Hmisc", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 18.04 with R 4.0.2
# install.packages("ini", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("kableExtra", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 18.04 or 20.04 with R 4.0.2
# install.packages("knitr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("lintr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 18.04 with R 4.0.2
# install.packages("logging", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("maps", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("matrixStats", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on macOS Catalina or Ubuntu 18.04 with R 4.0.2
# install.packages("mcr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("openxlsx", repos = "http://cran.us.r-project.org")
# install.packages("pdftools", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("pROC", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("psych", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("readtext", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("reshape", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("reshape2", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 18.04 with R 4.0.2
# install.packages("Rmisc", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("R.utils", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("readr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("reticulate", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("rmarkdown", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("stringi", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("stringr", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("styler", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("tidyverse", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("titanic", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("utf8", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("writexl", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")
# install.packages("WriteXLS", repos = "http://cran.us.r-project.org")
# install.packages("xlsx", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")  # Could not install on Ubuntu 18.04 0r 20.04 with R 4.0.2
# install.packages("Xmisc", repos = "http://cran.us.r-project.org")
# install.packages("xtable", lib = "~/R/x86_64-pc-linux-gnu-library/4.0", repos = "http://cran.us.r-project.org")

library(BlandAltmanLeh)
library(brglm2)
library(chron)
# library(devtools)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(DiagrammeR)
library(dplyr)
library(emmeans)
library(epiR)
library(exact2x2)
library(forestplot)
library(formatR)
library(gapminder)
library(ggplot2)
# library(ggpubr)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(gtools)
library(Hmisc)
library(ini)
library(kableExtra)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(knitr)
# library(lintr)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(logging)
library(maps)
library(matrixStats)  # Could not install on macOS Catalina or Ubuntu 18.04 with R 4.0.2
library(mcr)
library(openxlsx)
# library(pdftools)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(pROC)
library(psych)
# library(readtext)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(reshape)
library(reshape2)
library(Rmisc)
library(R.utils)
library(readr)
library(reticulate)
library(rmarkdown)
library(stringi)
library(stringr)
library(styler)
# library(tidyverse)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(titanic)
library(utf8)
# library(writexl)
# library(WriteXLS)
# library(xlsx)  # Could not install on Ubuntu 18.04 0r 20.04 with R 4.0.2
library(Xmisc)
library(xtable)

# Couldn't install with R 4.x.x


# Full run
# [Finished in 384.6s]
