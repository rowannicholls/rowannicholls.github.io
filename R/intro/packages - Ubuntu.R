# Install R and R packages on Ubuntu machines
# ===========================================
# - Ubuntu 20.04
# - R version 4.0.4
# 
# Install R
# ---------
# - Don't use `sudo apt install r-base-core` as it will install version 3.6.3
# - `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9`
# - `sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'`
# - `sudo apt update`
# - `sudo apt install r-base`
# - Run from the terminal with `R`
#
# Install packages
# ----------------
# The default library location (/usr/local/lib/R/site-library) is not writable.
# Instead, open R in a terminal and run install.packages() there. It will offer
# to create a personal library for you. Use that to install all your packages.
#
# Keyword arguments that may be needed:
# - lib = "~/R/x86_64-pc-linux-gnu-library/4.0"
# - repos = "http://cran.us.r-project.org"
#
# Needed by Debian:
# - sudo apt install libssl-dev
# - sudo apt install libxml2-dev
# - sudo apt install libcurl4-openssl-dev
# - sudo apt install libcairo2-dev
#
# Repo for Ubuntu:
# https://cloud.r-project.org/bin/linux/ubuntu

# install.packages("beeswarm")
# install.packages("BlandAltmanLeh")
# install.packages("brglm2")
# install.packages("Cairo")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("chron")
# install.packages("devtools")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("DiagrammeR")
# install.packages("dplyr")
# install.packages("emmeans")
# install.packages("epiR")
# install.packages("exact2x2")
# install.packages("extrafont")
# install.packages("forestplot")
# install.packages("formatR")
# install.packages("gapminder")
# install.packages("ggplot2")
# install.packages("ggpubr")
# install.packages("grDevices")
# install.packages("gtools")
# install.packages("Hmisc")
# install.packages("ini")
# install.packages("kableExtra")
# install.packages("knitr")
# install.packages("latex2exp")
# install.packages("lintr")
# install.packages("logging")
# install.packages("magick")
# install.packages("maps")
# install.packages("matrixStats")
# install.packages("mcr")
# install.packages("openxlsx")
# install.packages("pdftools")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("pROC")
# install.packages("psych")
# install.packages("readtext")  # Could not install on Ubuntu 20.04 with R 4.0.2
# install.packages("reshape")
# install.packages("reshape2")
# install.packages("Rmisc")
# install.packages("R.utils")
# install.packages("readr")
# install.packages("reticulate")
# install.packages("rmarkdown")
# install.packages("stringi")
# install.packages("stringr")
# install.packages("styler")
# install.packages("survminer")
# install.packages("tidyverse")
# install.packages("titanic")
# install.packages("utf8")
# install.packages("writexl")
# install.packages("WriteXLS")
# install.packages("xlsx")  # Could not install on Ubuntu 18.04 or 20.04 with R 4.0.2
# install.packages("Xmisc")
# install.packages("xtable")

library(beeswarm)
library(BlandAltmanLeh)
library(brglm2)
# library(Cairo)  # Could not install on Ubuntu 20.04 with R 4.0.2 or 4.0.4
library(chron)
library(devtools)  # Could not install on Ubuntu 20.04 with R 4.0.2
library(DiagrammeR)
library(dplyr)
library(emmeans)
library(epiR)
library(exact2x2)
library(extrafont)
library(forestplot)
library(formatR)
library(gapminder)
library(ggplot2)
library(ggpubr)
library(grDevices)
library(gtools)
library(Hmisc)
library(ini)
library(kableExtra)
library(knitr)
library(latex2exp)
library(lintr)
library(logging)
# library(magick)  # Could not install on Ubuntu 20.04 with R 4.0.4
library(maps)
library(matrixStats)
library(mcr)
library(openxlsx)
# library(pdftools)  # Could not install on Ubuntu 20.04 with R 4.0.2 or 4.0.4
library(pROC)
library(psych)
# library(readtext)  # Could not install on Ubuntu 20.04 with R 4.0.2 or 4.0.4
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
library(survminer)
library(tidyverse)
library(titanic)
library(utf8)
library(writexl)
library(WriteXLS)
# library(xlsx)  # Could not install on Ubuntu 18.04 or 20.04 with R 4.0.2
library(Xmisc)
library(xtable)
